with open("Day 1\input.txt", "r") as file:
    data = file.read()
    data = data.splitlines()
    total = 0

    for item in data:
        numbers = [char for char in item if char.isdigit()]
        number = ""
        if len(numbers) > 1:
            numbers = [numbers[0], numbers[-1]]
            number = "".join(numbers)
        else:
            number = "".join(numbers)
            number = number + number

        total += int(number)


print(total)
