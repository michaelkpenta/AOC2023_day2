def parse_file():
    with open("input", "r") as file:
        game_number = 1
        games = []
        for line in file:
            game_line = line.strip().split(":")[1]
            rounds = game_line.split(";")
            games.append((game_number, rounds))
            game_number += 1
    return games


def get_colors_in_round(round_string: str):
    color_list = round_string.strip().split(",")
    colors = {"red": 0, "green": 0, "blue": 0}
    for col in color_list:
        [count, color] = col.split()
        colors[color] = int(count)
    return colors


def get_impossible_games_list(games: list, max_red: int, max_green: int, max_blue: int):
    games_list = []
    for game in games:
        game_is_ok = True
        for game_round in game[1]:
            round_colors = get_colors_in_round(game_round)
            if round_colors["red"] > max_red:
                game_is_ok = False
            if round_colors["green"] > max_green:
                game_is_ok = False
            if round_colors["blue"] > max_blue:
                game_is_ok = False
        if game_is_ok:
            games_list.append(game[0])
    return games_list


def get_minimum_set_list(games: list):
    min_set_for_games = []
    color_keys = ["red", "green", "blue"]
    for game in games:
        minimum_set = {}
        for game_round in game[1]:
            round_colors = get_colors_in_round(game_round)
            for c in color_keys:
                if c not in minimum_set or round_colors[c] > minimum_set[c]:
                    minimum_set[c] = round_colors[c]
        min_set_for_games.append(minimum_set)
    return min_set_for_games


def get_power_of_sets(min_sets: list):
    powers = []
    for ms in min_sets:
        product = 1
        for color in ms:
            product *= ms[color]
        powers.append(product)
    return powers


if __name__ == '__main__':
    all_games = parse_file()
    imp = get_impossible_games_list(all_games, 12, 13, 14)
    print(sum(imp))
    min_set = get_minimum_set_list(all_games)
    print(sum(get_power_of_sets(min_set)))
