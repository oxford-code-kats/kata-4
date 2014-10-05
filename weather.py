import re

def clean_data(input):
    input = input.replace("*","")
    return input

def tokenize(input):
    tokens = input.split()
    return tokens

def is_valid(tokens):
    if len(tokens) < 3:
        return False
    for token in tokens[:3]:
        try:
            int(token)
        except ValueError:
            return False
    return True

def min_range_day(token_list):
    current_day = None
    min_range = None
    for tokens in token_list:
        low_tmp = int(tokens[2])
        high_tmp = int(tokens[1])
        if not min_range:
            min_range = high_tmp - low_tmp
        if high_tmp - low_tmp < min_range:
            min_range = high_tmp - low_tmp
            current_day = int(tokens[0])
    return current_day

def get_min_diurnal(file_name):
    with open(file_name, 'r') as file:
        cleaned_data = [clean_data(line) for line in file]
        tokens_list = [tokenize(line) for line in cleaned_data]
        valid_data = []
        for tokens in tokens_list:
            if is_valid(tokens):
                valid_data.append(tokens)
        day = min_range_day(valid_data)
    return day