def get_colors_in_round(round_string: str):
    color_list = round_string.strip().split(",")
    colors = {"red": 0, "green": 0, "blue": 0}
    for col in color_list:
        [count, color] = col.split()
        colors[color] = int(count)
    return colors



def get_impossible_games_list(max_red: int, max_green: int, max_blue: int):
    games_list = []
    with open("input", "r") as file:
        for line in file:
            game_line = line.strip().split(":")[1]
            rounds = game_line.split(";")
            get_colors_in_round(rounds[0])

    return games_list


if __name__ == '__main__':
    get_impossible_games_list(20, 20, 20)