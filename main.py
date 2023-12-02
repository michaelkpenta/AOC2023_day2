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
        game_number = 1
        for line in file:
            game_line = line.strip().split(":")[1]
            rounds = game_line.split(";")
            game_is_ok = True
            for game_round in rounds:
                round_colors = get_colors_in_round(game_round)
                if round_colors["red"] > max_red:
                    game_is_ok = False
                if round_colors["green"] > max_green:
                    game_is_ok = False
                if round_colors["blue"] > max_blue:
                    game_is_ok = False
            if game_is_ok:
                games_list.append(game_number)
            game_number += 1
    return games_list


if __name__ == '__main__':
    print(sum(get_impossible_games_list(12, 13, 14)))
