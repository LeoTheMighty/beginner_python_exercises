def find_yes_or_no(bool_string):
    s = bool_string.lower()
    if s == "no" or s == "nah" or s == "n":
        return False
    elif s == "yes" or s == "yeah" or s == "y":
        return True
    else:
        return -1


def find_r_p_s(rps_string):
    s = rps_string.lower()
    # Consider using a dictionary map
    if s == "rock" or s == "r":
        return 'r'
    elif s == "paper" or s == "p":
        return 'p'
    elif s == "scissors" or s == "scissor" or s == "s":
        return 's'


def curr_player_str(curr_player):
    return "Player " + str(curr_player)


def switch_1_and_2(num):
    return (num % 2) + 1


isPlaying = True
# maybe implement a best out of solution
while isPlaying:
    current_player = 1
    current_player_str = curr_player_str(current_player)
    playingGame = True
    best_of = int(input("What do you want this game to be the best of?\n"))
    wins = [0, 0]
    while playingGame:
        moves = ["", ""]
        for i in range(0, 2):
            moves[i] = find_r_p_s(input(current_player_str + ": it is your move...\n"))
            current_player = switch_1_and_2(current_player)
            current_player_str = curr_player_str(current_player)
        if moves[0] == "r":
            if moves[1] == "p":
                wins[1] += 1
            elif moves[1] == "s":
                wins[0] += 1
        elif moves[0] == "p":
            if moves[1] == "r":
                wins[0] += 1
            elif moves[1] == "s":
                wins[1] += 1
        elif moves[0] == "s":
            if moves[1] == "r":
                wins[1] += 1
            elif moves[1] == "p":
                wins[0] += 1
        print(str(wins[0]) + " - " + str(wins[1]))
        if wins[0] + wins[1] >= best_of and wins[0] != wins[1]:
            if wins[0] > wins[1]:
                current_player = 1
            else:
                current_player = 2
            current_player_str = curr_player_str(current_player)
            print(current_player_str + ", you win!")
            playingGame = False
    isPlaying = find_yes_or_no(input("Would you like to play again?\n"))
print("Have a lovely day!")
