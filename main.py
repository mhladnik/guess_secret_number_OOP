from functions import play_game, get_top_scores

while True:
    choose = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")
    if choose.upper() == "A":
        play_game()
    elif choose.upper() == "B":
        for score_dict in get_top_scores():
            print(score_dict)
    else:
        break