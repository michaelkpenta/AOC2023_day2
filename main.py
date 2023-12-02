def get_colors_in_round(round_string: str):
    color_list = round_string.strip().split(",")
    colors = {"red": 0, "green": 0, "blue": 0}
    for col in color_list:
        [count, color] = col.split()
        colors[color] = int(count)
    return colors


def get_impossible_games_list(max_red: int, max_green: int, max_blue: int):
    games_list = []
    min_set_for_games = []
    with open("input", "r") as file:
        game_number = 1
        for line in file:
            game_line = line.strip().split(":")[1]
            rounds = game_line.split(";")
            game_is_ok = True
            min_set = {}
            for game_round in rounds:
                round_colors = get_colors_in_round(game_round)
                if round_colors["red"] > max_red:
                    game_is_ok = False
                if round_colors["green"] > max_green:
                    game_is_ok = False
                if round_colors["blue"] > max_blue:
                    game_is_ok = False
                # min set
                color_keys = ["red", "green", "blue"]
                for c in color_keys:
                    if c not in min_set or round_colors[c] > min_set[c]:
                        min_set[c] = round_colors[c]
            min_set_for_games.append(min_set)
            if game_is_ok:
                games_list.append(game_number)
            game_number += 1
    return games_list, min_set_for_games


def get_power_of_sets(min_sets: list):
    powers = []
    for ms in min_sets:
        product = 1
        for color in ms:
            product *= ms[color]
        powers.append(product)
    return powers


if __name__ == '__main__':
    imp, min_set = get_impossible_games_list(12, 13, 14)
    print(sum(imp))
    print(get_power_of_sets(min_set))
