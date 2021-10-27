import random
import json

class Result():
    def __init__(self, name, attempts, wrong_attempts):
        self.name = name
        self.attempts = attempts
        self.wrong_attempts = wrong_attempts

def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = list()
    score_list = get_score_list()
    name = input("What is your name? ")
    level = input("Choose your level (easy/hard): ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        if guess == secret:
            results = Result(name=name, attempts=attempts, wrong_attempts=wrong_guesses)
            score_list.append(results.__dict__)
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print(f"You've guessed it - congratulations {name}! It's number {secret}. You needed {attempts}")
            break
        else:
            if level.upper() == "EASY":
                if guess > secret:
                    print("Your guess is not correct... try something smaller")
                    wrong_guesses.append(guess)
                else:
                    print("Your guess is not correct... try something bigger")
                    wrong_guesses.append(guess)
            elif level.upper() == "HARD":
                print("Wrong, try again.")
                wrong_guesses.append(guess)
            else:
                break

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    return (sorted(score_list, key=lambda name: int(name["attempts"])))[:3]

