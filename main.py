def get_impossible_games_list(max_red: int, max_green: int, max_blue: int):
    games_list = []
    with open("input", "r") as file:
        for line in file:
            game_line = line.strip().split(":")[1]
            rounds = game_line.split(";")
            print(rounds)

    return games_list


if __name__ == '__main__':
    get_impossible_games_list(20, 20, 20)