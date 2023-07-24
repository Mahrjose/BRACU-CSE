# Problem -03

import random


def musical_chair(players):
    player_num = len(players)

    while player_num > 1:

        print(f"Current Players: {players}")
        var = random.randint(0, 3)

        if var == 1:
            position = int(player_num / 2)
            print(
                f"\nThe music stopped!!!\nPlayer Name: {players[position]} in Position: {position} is out of the Game!\n"
            )
            players.pop(position)

        # Circulate items
        players.insert(0, players[len(players) - 1])
        players.pop(len(players) - 1)
        player_num = len(players)
    print(f"We've got the Winner!!!\nAaand the winner is: {players[0]}")


def main():
    players = ["Guts", "Eren", "Kaneki", "Araragi", "Hachiman", "Itachi", "Lelouch"]
    musical_chair(players)


if __name__ == "__main__":
    main()
