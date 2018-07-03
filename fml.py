import re

NUM_SCREENS = 8
STARTING_BUDGET = 1000
MAX_INDEX_CHARACTERS = 4
GLOBAL_DEFAULT_SEPARATOR = "|"
EMPTY_MOVIE_COST = -2000000

class Movie:
    """A Movie has a name and a week_id,since some Movies may appear in multiple weeks.
    """
    def __init__(self, name, week_id):
        self.name = name
        self.week_id = week_id

    def __repr__(self):
        return "{0}: {1}".format(type(self).__name__, repr(self.name)[1:-1])

EMPTY_MOVIE = Movie('', 0)

class Bracket:
    """A Bracket contains Movies.
    """
    def __init__(self,lst=[], week_id=0, id_string="Bracket"):
        for item in lst:
            assert type(item) is Movie, "Must input a list of Movies."
        self.movies = lst
        self.week_id = week_id
        self.id_string = id_string

    def __repr__(self, separator=GLOBAL_DEFAULT_SEPARATOR):
        lines = ["Bracket - Week {0} {1}".format(self.week_id, self.id_string)] + make_lines(self, "movies", separator)
        return "\n".join(lines)

    def __getitem__(self, index):
        return self.movies[index]

    def __setitem__(self, index, item):
        assert type(item) is Movie, "Must input a Movie."
        self.movies[index] = item

    def __add__(self, other):
        self.movies.extend(other.movies)
        return self

    def __len__(self):
        return len(self.movies)

    def list(self):
        return self.movies

class Projection:
    """Projections store names of movies and their corresponding box-office
    projections.
    """
    MAX_REPR_NUM_CHARS = 20
    MAX_REPR_NAME_CHARS = 50

    def __init__(self, name, projection):
        self.name = name
        self.projection = projection

    def __repr__(self, separator=GLOBAL_DEFAULT_SEPARATOR):
        name = repr(self.name)
        while len(name) <= self.MAX_REPR_NAME_CHARS:
            name += " "
        projection = '${:,.2f}'.format(self.projection)
        while len(projection) <= self.MAX_REPR_NUM_CHARS:
            projection += " "
        return separator.join([name, projection])

class ProjectionSet:
    """A ProjectionSet stores Projections.
    """
    proj_type = ""
    def __init__(self, week_id, string=""):
        self.week_id = week_id
        self.projections = []
        self.process_raw(string)

    def __repr__(self, separator=GLOBAL_DEFAULT_SEPARATOR):
        lines = ["Projections - Week {0} {1}".format(self.week_id, self.proj_type)] + \
            make_lines(self, "projections", separator)
        return "\n".join(lines)

    def process_raw(self, string):
        self.process(self.parse(string))

    def process(self, pair_list):
        for pair in pair_list:
            self.projections.append(Projection(pair[0], pair[1]))

    def __getitem__(self, movie):
        if movie is EMPTY_MOVIE:
            return EMPTY_MOVIE_COST
        if type(movie) is int:
            return self.projections[movie]
        if type(movie) is Movie:
            movie = movie.name
        for proj in self.projections:
            if proj.name == movie:
                return proj.projection
        raise KeyError('Movie "{0}" not in this ProjectionSet'.format(movie))

class BOR_Projections(ProjectionSet):
    """BOR_Projections is a ProjectionSet of Projections made from Box Office
    Report. It has a specific parse method used during intitiation, and a unique
    method intersect_w_fml for use when movie predictions are split up into
    three days.
    """
    proj_type = "BOR"
    def intersect_w_fml(self, fml_projections):
        """Takes a set of fml_projeections and, if it exists, takes the movie that
        was split up into three days and emulates it in self.prections by splitting
        up the movie but with the same ratio distribution as in fml_projections.
        Assumes 3 days are at the beggining of fml_projections and day to triple
        (if necessary) is the first element in self.projections
        """
        if "(Friday)" in fml_projections.projections[0].name:
            key = fml_projections.projections[0].name.replace(" (Friday)", "")
            print(key)
            days = [p for p in fml_projections.projections if key in p.name]
            bor = self.projections.pop(0).projection
            fml = sum([p.projection for p in days])
            ratio = bor / fml
            for p in days:
                self.projections.append(Projection(p.name, (p.projection * ratio)))
        for name in [proj.name for proj in fml_projections.projections]:
            if name not in [proj.name for proj in self.projections]:
                self.projections.append(Projection(name, fml_projections[name]))

    def parse(self, string):
        """For parse methods, I chose to avoid using built-in Python string methods
        in order to handle new errors that arise as the structures of the input
        string change with each week and as I work with new websites.
        """
        #remove up to "#"
        curr = ""
        while curr != "#":
            curr = string[0]
            string = string[1:]
        #parse into individual elements
        elems = []
        while len(string) > 0:
            elem = ""
            string = string[1:]
            while len(string) > 0 and string[0] != "\n" and string[0] != "\t":
                elem += string[0]
                string = string[1:]
            elems.append(elem)
        #parse into (movie title, projected earning) pairs
        movies = []
        while len(elems) > 1:
            elems.pop(0)
            movie = []
            while "$" not in elems[0]:
                movie.append(elems.pop(0))
            movie.append(elems.pop(0))
            for _ in range(3):
                elems.pop(0)
            movies.append(movie)
        #join separate title strings together if existent
        for movie in movies:
            if len(movie) > 2:
                end = movie.pop()
                while len(movie) > 1:
                    movie[0] = movie.pop(0) + " " + movie[0]
                movie.append(end)
        #remove studio titles
        for movie in movies:
            title = movie[0]
            start = title.find("(")
            end = title.find(")")
            title = title[:start-1] + title[end+1:]
            movie[0] = title
        #remove number formatting
        for movie in movies:
            movie[1] = float(movie[1][1:-2])*1000000
        #Ensure title case
        movies = [[movie[0].title(), movie[1]] for movie in movies]
        return movies

class FML_Projections(ProjectionSet):
    """FML_Projections is a ProjectionSet of Projections made from Fantasy
    Movie League Insider. It has a unique parse method used during intitiation.
    """
    proj_type = "FML"
    def parse(self, string):
        """For parse methods, I chose to avoid using built-in Python string methods
        in order to handle new errors that arise as the structures of the input
        string change with each week and as I work with new websites.
        """
        #Parse into individual elements
        lines = []
        while len(string) > 0:
            line = ""
            while len(string) > 0 and string[0] != "\n":
                line += string[0]
                string = string[1:]
            string = string[1:]
            lines.append(line)
        #Remove empty lines
        index = 0
        while index < len(lines):
            if lines[index] == "":
                lines.pop(index)
            else:
                index += 1
        #make pairs from lines
        pairs = []
        for line in lines:
            index = line.find(" - ")
            pairs.append([line[:index], line[index+3:]])
        #format
        for pair in pairs:
            pair[0] = pair[0].replace('\"', '')
            if "million" in pair[1]:
                pair[1] = float(pair[1].replace(" million", "").replace("$", "").replace(",", "")) * 1000000
            else:
                pair[1] = float(pair[1].replace("$", "").replace(",", ""))
        #ensure title case
        pairs = [[pair[0].title(), pair[1]] for pair in pairs]
        return pairs

class Price:
    """A Price links a movie name with it's corresponding FML price.
    """
    MAX_REPR_NUM_CHARS = 4
    MAX_REPR_NAME_CHARS = 50

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self, separator=GLOBAL_DEFAULT_SEPARATOR):
        name = repr(self.name)
        while len(name) <= self.MAX_REPR_NAME_CHARS:
            name += " "
        price = repr(self.price)
        while len(price) <= self.MAX_REPR_NUM_CHARS:
            price += " "
        return "{0}{2}{1}".format(name, price, separator)

class Prices:
    """A Prices object has a week_id and a list of Prices.
    """
    def __init__(self, week_id, string="", id_string=""):
        self.week_id = week_id
        self.prices = self.process_raw(string)
        self.string = string
        self.id_string = id_string

    def process_raw(self, string):
        """Takes in a raw price string and returns a list of Prices.
        """
        return self.process(self.parse(string))

    def process(self, pairs):
        """Takes in a list of (name, price) pairs and returns a list of
        corresponding Price objects.
        """
        return [Price(*pair) for pair in pairs]

    def __getitem__(self, movie):
        if movie is EMPTY_MOVIE:
            return 0
        for price in self.prices:
            if movie.name == price.name:
                return price.price
        raise KeyError("Movie '{0}' not in these Week {1} prices.".format(movie, self.week_id))

    def __repr__(self, separator=GLOBAL_DEFAULT_SEPARATOR):
        return "\n".join(["Prices - Week {0} {1}".format(self.week_id, self.id_string)] + make_lines(self, "prices", separator))

    def make_options(self):
        return Bracket([Movie(price.name, self.week_id) for price in self.prices], self.week_id, "Options")

    def parse(self, string):
        """For parse methods, I chose to avoid using built-in Python string methods
        in order to handle new errors that arise as the structures of the input
        string change with each week and as I work with new websites.
        """
        #parse lines
        lines = re.split("\n|\t", string)
        #remove extra lines
        index = 0
        while index < len(lines):
            if lines[index] == "+" or lines[index] == "UNAVAILABLESCREENS LOCKED"\
                or lines[index] == "SCREENS LOCKED" or lines[index] == "UNAVAILABLE"\
                or lines[index] == "\n" or lines[index] == "":
                lines.pop(index)
            else:
                index += 1
        #make pairs
        pairs = []
        while lines:
            pair = [lines.pop(0),lines.pop(0)]
            pairs.append(pair)
        #format text
        for pair in pairs:
            #first
            #old set
            if pair[0][:5] == "FRI: ":
                str = pair[0].replace(" - FRI ONLY", "").replace("FRI: ", "")
                pair[0] = str + " (Friday)"
            if pair[0][:5] == "SAT: ":
                str = pair[0].replace(" - SAT ONLY", "").replace("SAT: ", "")
                pair[0] = str + " (Saturday)"
            if pair[0][:5] == "SUN: ":
                str = pair[0].replace(" - SUN ONLY", "").replace("SUN: ", "")
                pair[0] = str + " (Sunday)"
            if pair[0][:5] == "MON: ":
                str = pair[0].replace(" - MON ONLY", "").replace("MON: ", "")
                pair[0] = str + " (Monday)"

            #new set
            if pair[0][:6] == "FRI - ":
                end = pair[0].find(" - FRI ONLY")
                pair[0] = pair[0][6:end] + " (Friday)"
            if pair[0][:6] == "SAT - ":
                end = pair[0].find(" - SAT ONLY")
                pair[0] = pair[0][6:end] + " (Saturday)"
            if pair[0][:6] == "SUN - ":
                end = pair[0].find(" - SUN ONLY")
                pair[0] = pair[0][6:end] + " (Sunday)"
            if pair[0][:6] == "MON - ":
                end = pair[0].find(" - MON ONLY")
                pair[0] = pair[0][6:end] + " (Monday)"
            #second
            pair[1] = int(pair[1][pair[1].find("$")+1:])
        #convert to title case
        pairs = [[pair[0].title(), pair[1]] for pair in pairs]
        return pairs

def best_bracket(prices, projections, budget=STARTING_BUDGET, available_slots=NUM_SCREENS):
    """Returns the bracket of size available_slots with the highest projected weekend earnings.
    >>> best_bracket(week_2017_q3_w8.PRICES, week_2017_q3_w8.ACTUAL_FML_EARNINGS)
    Bracket - Week 8 FML
    0   |Movie: Geostorm
    1   |Movie: Geostorm
    2   |Movie: Geostorm
    3   |Movie: Geostorm
    4   |Movie: Geostorm
    5   |Movie: Victoria And Abdul
    6   |Movie: Victoria And Abdul
    7   |Movie:
    >>> best_bracket(week_2017_q4_w6.PRICES, week_2017_q4_w6.FML_PROJECTIONS)
    Bracket - Week 6 FML
    0   |Movie: Jumanji: Welcome To The Jungle
    1   |Movie: Jumanji: Welcome To The Jungle
    2   |Movie: Coco
    3   |Movie: Coco
    4   |Movie: Coco
    5   |Movie: Coco
    6   |Movie: Downsizing
    7   |Movie: Downsizing
    >>> best_bracket(week_2017_q4_w6.PRICES, week_2017_q4_w6.BOR_PROJECTIONS)
    Bracket - Week 6 BOR
    0   |Movie: Jumanji: Welcome To The Jungle
    1   |Movie: Jumanji: Welcome To The Jungle
    2   |Movie: Darkest Hour
    3   |Movie: Darkest Hour
    4   |Movie: Darkest Hour
    5   |Movie: Darkest Hour
    6   |Movie: Wonder
    7   |Movie: Wonder
    """
    cache = {}
    options = prices.make_options().list()
    def best_helper(options, budget, available_slots):
        if available_slots == 0:
            return Bracket()
        i_d = str(budget) + " " + str(available_slots)
        if i_d in cache:
            return cache[i_d]
        filtered_options = [option for option in options if prices[option] <= budget]
        if not filtered_options:
            return Bracket()
        brackets = [Bracket([movie]) + best_helper(filtered_options, (budget - prices[movie]), available_slots - 1) for movie in filtered_options]
        best = max(brackets, key = lambda x: calc_total(x, projections, available_slots))
        cache[i_d] = best
        return best
    return Bracket(best_helper(options, budget, available_slots), projections.week_id, projections.proj_type)

def calc_total(bracket, projections, available_slots=NUM_SCREENS):
    """Calculates the total value of bracket given projections and with
    available_slots number of remaining slots in the Bracket (Cineplex). Accounts
    for empty slot earning deduction.
    >>> calc_total(week_2017_q3_w8.REAL_BRACKET, week_2017_q3_w8.ACTUAL_FML_EARNINGS)
    70789110.0
    >>> calc_total(week_2017_q3_w8.FML_BRACKET, week_2017_q3_w8.FML_PROJECTIONS)
    67700000.0
    >>> calc_total(week_2017_q4_w1.FML_BRACKET, week_2017_q4_w1.FML_PROJECTIONS)
    61601000.0
    """
    bracket = bracket.list()
    while len(bracket) < available_slots:
        bracket.append(EMPTY_MOVIE)
    total = sum([projections[movie] for movie in bracket])
    return total

def calc_price(bracket, prices):
    """Calculates the total price of bracket given corresponding prices.
    >>> calc_price(week_2017_q3_w8.FML_BRACKET, week_2017_q3_w8.PRICES)
    1000
    >>> calc_price(week_2017_q3_w8.REAL_BRACKET, week_2017_q3_w8.PRICES)
    992
    >>> calc_price(week_2017_q4_w6.FML_BRACKET, week_2017_q4_w6.PRICES)
    998
    """
    return sum((prices[movie] for movie in bracket))

def make_lines(obj, iterable_name, separator=GLOBAL_DEFAULT_SEPARATOR):
    """Make_lines takes in an Object obj, a String iterable_name, and String
    separator (optional) and returns a list of strings. Each string is a
    representations of an the objects in object.iterable_name, but with an
    index concatenated to the beggining.
    """
    strings = []
    i = 0
    for item in getattr(obj, iterable_name):
        num = (str(i) + "".join([" " for _ in range(MAX_INDEX_CHARACTERS)]))[:MAX_INDEX_CHARACTERS]
        strings += [num + separator + repr(item)]
        i += 1
    return strings

def exec_raw(week, raw_prices, raw_bor_projections, raw_fml_projections, prnt=True):
    """Takes a week (an int representing the week), raw_prices, bor_projections,
    and fml_projects and runs and prints the results of the projections.
    """
    print("#############################################################")
    prices = Prices(week, raw_prices)
    print(prices)
    print()

    fml_projections = FML_Projections(week, raw_fml_projections)
    bor_projections = BOR_Projections(week, raw_bor_projections)
    bor_projections.intersect_w_fml(fml_projections)

    print(fml_projections)
    print()
    fml_bracket = best_bracket(prices, fml_projections)
    print(fml_bracket)
    fml_total = calc_total(fml_bracket.list(), fml_projections)
    print("FML TOTAL:", fml_total)
    fml_total_bor = calc_total(fml_bracket.list(), bor_projections)
    print("BOR TOTAL:", fml_total_bor)
    print()


    print(bor_projections)
    print()
    bor_bracket = best_bracket(prices, bor_projections)
    print(bor_bracket)
    bor_total = calc_total(bor_bracket.list(), bor_projections)
    print("BOR TOTAL:", bor_total)
    bor_total_fml = calc_total(bor_bracket.list(), fml_projections)
    print("FML TOTAL:", bor_total_fml)

    print("#############################################################")
    return prices, fml_projections, fml_bracket, bor_projections, bor_bracket
