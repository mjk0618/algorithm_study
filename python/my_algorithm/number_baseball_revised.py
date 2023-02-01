# chatGPT version

import random

def get_input(n):
    while True:
        reply = input("Enter a {}-digit number: ".format(n))
        if reply.isdigit() and len(reply) == n:
            return [int(d) for d in reply]
        else:
            print("Invalid input. Try again.")

def get_score(answer, guess):
    score = {"strike": 0, "ball": 0}
    for i, d in enumerate(guess):
        if d in answer:
            if answer[i] == d:
                score["strike"] += 1
            else:
                score["ball"] += 1
    return score

def play_game(n):
    answer = random.sample(range(10), n)
    cnt = 0
    while True:
        guess = get_input(n)
        cnt += 1
        score = get_score(answer, guess)
        print("Strike: {}\nBall: {}".format(score["strike"], score["ball"]))
        if score["strike"] == n:
            print("You win!")
            print("Attempts: {}".format(cnt))
            return

num_digits = int(input("How many digits do you want to use? "))
play_game(num_digits)