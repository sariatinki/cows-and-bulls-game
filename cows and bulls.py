import random


def no_generator_4digit():
    return random.sample(range(10), 4)


def num_input(number="Enter a 4 digit number:"):
    return list(input(number))


def play_cows_bulls():
    cows = 0
    bulls = 0
    attempts = 0

    while True:
        player = num_input()
        wining_num = no_generator_4digit()

        attempts += 1

        for (digit1, digit2) in zip(player, wining_num):
            num = int(digit1)
            if num == digit2:
                cows += 1
            elif num in wining_num:
                bulls += 1

        print(wining_num)
        print("COWS:", cows)
        print("BULLS:", bulls)
        print("ATTEMPTS:", attempts)

        if attempts == 5:
            print("GAME OVER!")
            break


if __name__ == "__main__":
    play_cows_bulls()





