#Create a program that will play the “cows and bulls” game with the user.
#The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
#For every digit that the user guessed correctly in the correct place, they have
#a “cow”. For every digit the user guessed correctly in the wrong place is a
#“bull.” Every time the user makes a guess, tell them how many “cows” and “bulls”
#they have. Once the user guesses the correct number, the game is over. Keep
#track of the number of guesses the user makes throughout teh game and tell the
#user at the end.


import random


# defining funtion to take user input
def user_input():
    return list(input("Enter a four digit number:"))


#defining function to generate a random 4 digit number
def randnum():
    return random.sample(range(10),4)


def cow_bull():
    cow = bull = 0
    winning_num = randnum()
    user_num = user_input()
    attempt = 1

    while attempt <= 5:
 
        # converting the user input into integers
        comparable_list = []
        for elements in user_num:
            num = int(elements)
            comparable_list.append(num)
        
        
        if comparable_list == winning_num:
            print("HURRAY!! YOU HAVE GOT IT RIGHT")
            print("YOU TOOK", attempt, "TO GET IT RIGHT")
        
        else:
            for (digit1, digit2) in zip(winning_num, comparable_list):
                if digit1 == digit2:
                    cow += 1
                elif digit1 != digit2 and digit2 in winning_num:
                    bull += 1
            print("Cows:", cow)
            print("Bulls:", bull)
            print("ATTEMPTS:", attempt)
            
        user_num = user_input()
        attempt += 1
    print("The number is", winning_num)
           

cow_bull()
        
