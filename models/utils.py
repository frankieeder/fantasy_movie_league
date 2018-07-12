import re

def parse_digit(string):
    return float(re.sub("[^0-9.-]", "", string)) if isinstance(string, str) else string

def replace_list(list, val, replacement):
    return [(replacement if i == val else i) for i in list]