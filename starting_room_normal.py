import time
import random
import sys


def starting_room_normal():

    first_reply = ("You are now in the starting room.\n"
                   "Available commands are:\n"
                   "'instructions', 'exit', 'adventure'\n")
    for char in first_reply:
        timer_value6 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value6)

    while True:

        user_starting_room_choice = input().lower()
        if user_starting_room_choice == "instructions":
            instructions_message()
        elif user_starting_room_choice == "continue":
            adventure_choice()
        elif user_starting_room_choice == "exit":
            print("Are you sure you want to exit the game? Type yes/no")
            user_choice_exit2 = input().lower()
            if user_choice_exit2 == "yes":
                exit()
