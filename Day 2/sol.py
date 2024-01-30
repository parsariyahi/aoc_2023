MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBSE = 14

RULES = {
    "red": MAX_RED_CUBES,
    "green": MAX_GREEN_CUBES,
    "blue": MAX_BLUE_CUBSE,
}

with open("Day 2\input.txt", "r") as file:
    data = file.read()
    games = data.splitlines()
    total = 0

    for game in games:
        game_info = game.split(":")
        game_id = game_info[0].split(" ")[1]
        rounds = game_info[1].split(";")
        possible = False
        
        for round_ in rounds:
            cubes = round_.split(",")
            for cube in cubes:
                cube_info = cube.split(" ")
                cube_count = cube_info[1]
                cube_color = cube_info[2]
                rule = RULES.get(cube_color)
                if int(cube_count) > rule:
                    break
            else:
                continue

            break

        else:
            total += int(game_id)

print(total)