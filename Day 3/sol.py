def get_number_indices(data: str):
    indices = list()
    for index, char in enumerate(data):
        if char.isdigit():
            indices.append(index) 
    
    return indices

def get_symbol_indices(data: str):
    indices = list()
    for index, char in enumerate(data):
        if (not char.isdigit() and char != "."):
            indices.append(index) 
    
    return indices

def extract_number(string, c):
    number = ""
    counter = c
    for char in string:
        if char.isdigit():
            number += char
            counter += 1
        else:
            break

    return number, counter

def check_adjacent(symbols, numbers, line):
    res_numbers = []

    if not symbols:
        return []
    c = 0
    for s_index in symbols:
        for n_index in numbers:
            if s_index == n_index or \
            s_index + 1 == n_index or \
            s_index - 1 == n_index:
                n, c = extract_number(line[c:], c)
                print(c)
                res_numbers.append(n)
    
    return res_numbers


with open("Day 3\input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()
    total = 0

    for index, line in enumerate(lines):
        current_line_number_indices = get_number_indices(line)
        # next_line_number_indices = get_number_indices(lines[index + 1])
        # prev_line_number_indices = get_number_indices(lines[index - 1])
        current_line_symbol_indices = get_symbol_indices(line)
        try:
            next_line_symbol_indices = get_symbol_indices(lines[index + 1])
        except IndexError:
            next_line_symbol_indices = [] 

        try:     
            prev_line_symbol_indices = get_symbol_indices(lines[index - 1])
        except IndexError:
            prev_line_symbol_indices = []


        # print("number index : ", current_line_number_indices)
        # print("current symbol index : ", current_line_symbol_indices)
        # print("next symbol index : ", next_line_symbol_indices)
        # print("prev symbol index : ", prev_line_symbol_indices)

        # if check_adjacent(current_line_symbol_indices, current_line_number_indices) or \
        #     check_adjacent(next_line_symbol_indices, current_line_number_indices) or \
        #     check_adjacent(prev_line_symbol_indices, current_line_number_indices):

        res = check_adjacent(current_line_symbol_indices, current_line_number_indices, line)
        res.append(check_adjacent(next_line_symbol_indices, current_line_number_indices, line))
        res.append(check_adjacent(prev_line_symbol_indices, current_line_number_indices, line))

        for number in res:
            total += int(number)

print(total)
