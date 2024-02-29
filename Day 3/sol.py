from copy import deepcopy


def check_symbol(char: str):
    if not (char.isalnum()) and char != ".":
        #print("current char: ", char, "\n")
        return True
    return False


def find_symbols(line: str):
    result = []
    for index, char in enumerate(line):
        if check_symbol(char):
            result.append(index) 

    return result


def find_number(line: str):
    result = []
    number = ""
    indices = []
    for index, char in enumerate(line):
        if char.isnumeric():
            number += char
            indices.append(index)
            continue

        if number:
            result.append([int(number), deepcopy(indices)])
            number = ""
            indices.clear()

    return result


def find_adjacent_number(line: str, other_line):
    adjacent = []
    if other_line:
        numbers = find_number(line)
        line_symbols = find_symbols(line)
        other_line_symbols = find_symbols(other_line)
        for number, number_indices in numbers:
            for num_index in number_indices:
                if num_index in line_symbols or num_index in other_line_symbols:
                    adjacent.append(number)

    return adjacent


def main():
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.splitlines()
        total = 0
        max_index = len(lines) - 1
        min_index = 0

        for index, line in enumerate(lines):
            current_line = line
            prev_line = lines[index-1] if index != min_index else None
            next_line = lines[index+1] if index != max_index else None
            print("current line: \n", current_line)
            print("prev line: \n", prev_line)
            print("next line: \n", next_line)
            res_with_prev = find_adjacent_number(current_line, prev_line)
            res_with_next = find_adjacent_number(current_line, next_line)
            total += sum(res_with_prev) if res_with_prev else 0
            total += sum(res_with_next) if res_with_next else 0

    print(total)


main()
