# the rules:

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1. (it will count as 1 when the total is over 21)
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
#-----------------------------------------------------------------------------------------------------

# How the program will work:

# the program will ask you if you want to play the game? y or n
# if y you enter the game
# the logo will be printed 
# it will show you your card in a list [X, Y], current score is (X + Y)
# Computer first card: X  >>>>> probably the first element from the computer list

# it askes you if you get another card or pass y or n 
# if you want to pass (n) it will show you your final hand which is your list and the sum the number in it
# then prints the computer's final hand which is the computer list and the sum of the numbers
# if the sum of the computer's list is less than 17 it adds another card and check again
# tells you if you win or not and why (with emoji ;) )_
# then ask you if you want to play the game? (while loop)
# if you chose to take another card 
# if your cards sum is over 21 you lose and the program prints the whle results as before
# if the sum is still not over 21 it shows you the sum of your card and the first card from the computer's list and ask again
#------------------------------------------------------------------------------------------------------------------------------

from enum import Flag
import random
from tkinter import Y
from replit import clear
from art import logo_blackjack

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def add_random_card(the_list):
    random_card = random.choice(cards)
    the_list.append(random_card)


def win_the_game(user_list, user_list_sum, computer_list, computer_list_sum):
    print(f"Your final hand: {user_list} final score: {user_list_sum}")
    print(f"Computer's final hand is : {computer_list} final score: {computer_list_sum}")
    print("You won :) ")





def lose_the_game(user_list, user_list_sum, computer_list, computer_list_sum):
    print(f"Your final hand: {user_list} final score: {user_list_sum}")
    print(f"Computer's final hand is : {computer_list} final score: {computer_list_sum}")
    print("You went over. You lost :( ")


def draw(user_list, user_list_sum, computer_list, computer_list_sum):
    print(f"Your final hand: {user_list} final score: {user_list_sum}")
    print(f"Computer's final hand is : {computer_list} final score: {computer_list_sum}")
    print("it is a Draw ")





def print_results(user_list, user_list_sum, computer_list):
    print(f"your cards are: {user_list} current score: {user_list_sum}")
    print(f"Computer's first card is: {computer_list[0]}")




def ace_to_one(a_list):
    sum_of_the_list = sum(a_list)
    for num in a_list:
        if num == 11 and sum_of_the_list > 21:
            a_list[a_list.index(num)] = 1



def play_or_not():
    
    user_cards = []
    computer_cards = []
    want_to_play = input("Do you want to play the game Blackjack ? Type 'y' or 'n': ").lower()

    if want_to_play == "y":
        clear()
        print(logo_blackjack)
        # Giving two card to the user and to thwe computer 
        for i in range(0,2):
            add_random_card(user_cards)
            add_random_card(computer_cards)

            ace_to_one(user_cards)
            ace_to_one(computer_cards)

        # Calculating the sum of the cards for the user and the computer 
        sum_of_user = sum(user_cards)
        sum_of_computer = sum(computer_cards)
        
        print_results(user_cards, sum_of_user, computer_cards)

        winning = True
        while winning:

            another_card = input("Do you want another card or pass ? Type 'y' or 'n': ")

            if another_card == "y":
                add_random_card(user_cards)
                ace_to_one(user_cards)
                sum_of_user = sum(user_cards)
                print_results(user_cards, sum_of_user, computer_cards)

                if sum_of_user > 21:
                    lose_the_game(user_cards, sum_of_user, computer_cards, sum_of_computer)
                    winning = False
                    play_or_not()
                
            else:
                
                while sum_of_computer < 17:
                    add_random_card(computer_cards)
                    ace_to_one(computer_cards)
                    sum_of_computer = sum(computer_cards)

                if sum_of_user > sum_of_computer or sum_of_computer > 21:
                   win_the_game(user_cards, sum_of_user, computer_cards, sum_of_computer) 
                   play_or_not()
                   
                elif sum_of_computer > sum_of_user and sum_of_computer < 21:
                    lose_the_game(user_cards, sum_of_user, computer_cards, sum_of_computer)
                    play_or_not()
                elif sum_of_computer == sum_of_user:
                    draw(user_cards, sum_of_user, computer_cards, sum_of_computer)
                    play_or_not()
                winning = False   



    else:
        print("GoodBye")
        return









play_or_not()









