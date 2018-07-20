import re
import pandas as pd
import csv
from math import isnan
import models.metascraping as ms

def print_status(*args):
    print('\r' + " ".join(args), end='')

def split_list(iterable, splitters):
    """Splits the input iterable into a list of lists at each occurrence of anything in splitters.
    :param iterable: An iterable to split
    :param splitters: An iterable of elements to split the iterable by
    :return: A list of lists - the original iterable split by splitters.
    """
    splitters = set(splitters)
    lists = []
    this_list = []
    for elem in iterable:
        if elem in splitters:
            if len(this_list) > 0:
                lists.append(this_list)
                this_list = []
            continue
        else:
            this_list.append(elem)
    return lists


def writeTable(table, filename):
    """Writes table to csv.
    :param table: The table to write (should be indexed by rows then columns)
    :param filename: The directory to write the csv to
    :return: None
    """
    with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(table)


def parse_digit(string, caster):
    """Parses the digits of a string, and casts them using input caster.
    :param string: Input string to parse for digits
    :param caster: Input function used to cast parsed string (e.g. int, float, or str). Defaults to float.
    :return: The casted, parsed value.
    """
    return caster(re.sub("[^0-9.-]", "", string)) if isinstance(string, str) else string


def replace_list(iterable, mappings):
    """Returns a new list where all instances of any key in mappings are replaced with their corresponding replacement.
    :param iterable: Iterable to replace values in.
    :param mappings: A dictionary having each value we want to replace as a key with it's corresponding replacement
    as its value.
    :return: New list with replacements
    """
    return [(mappings[k] if (k in mappings) else k) for k in iterable]


def function_results_to_df(iterable, f, input_name="", sep="_"):
    df = pd.DataFrame()
    for counter, elem in enumerate(iterable):
        print_status("Processing Row {0} out of {1}".format(counter, len(iterable)))
        if input_name:
            df.loc[counter, input_name] = elem
        results = f(elem)
        for key in results:
            df.loc[counter, input_name + sep + key] = results[key]
    return df


def one_hot_encode(str, sep=", "):
    return {} if pd.isnull(str) else {k: 1 for k in str.split(sep)}

def apply_to_df(df, f, columns = None):
    if not columns:
        columns = df.columns
    for column in columns:
        df[column] = [f(e) for e in df[column]]
