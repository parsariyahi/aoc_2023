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
    adjacent = [0]
    if other_line:
        numbers = find_number(line)
        line_symbols = find_symbols(line)
        other_line_symbols = find_symbols(other_line)
        # print(line_symbols)
        # print(other_line_symbols)
        for number, number_indices in numbers:
            for num_index in number_indices:
                if (num_index in line_symbols or num_index-1 in line_symbols or num_index+1 in line_symbols) \
                    or (num_index in other_line_symbols or num_index-1 in other_line_symbols or num_index+1 in other_line_symbols):
                    if adjacent[-1] == number:
                        continue
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
            print("res with prev: ", res_with_prev, "\n")
            print("res with next: ", res_with_next, "\n")
            total += sum(res_with_prev) if res_with_prev else 0
            total += sum(res_with_next) if res_with_next else 0

    print(total)


main()


# a = "......470.............*...............160...........560.......962.....*.....431.909..*..*...712.........852....838.........64.614..........."
# b = " ....................762................*........211.......164.........27............817.286.....@493..............*............@..422.837..."
# c = " ........*........404...406.=561....98........@........-.195.....*...320..........*..922.777..*.............%.&.........530.................."

# print(b)
# print(a)
# print(c)
# print(find_adjacent_number(c, a))
# # print(find_adjacent_number(a, c))