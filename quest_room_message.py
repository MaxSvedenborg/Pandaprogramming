import random
import sys
import time
from starting_room_normal import starting_room_normal


def quest_room_welcome():

    quest_room_message = (
        "\n\nYou enter a room containing various tasks.\n" 
        "Choose the task you want to do by typing it's name in chat. " 
        "Current task's available: 'if'. \n\n"
        "If you want to back to the starting room, type 'back',\n"
        "or if you want to exit, type 'exit'.\n\n")

    for char in quest_room_message:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)

    in_choice = True
    while in_choice:
        user_quest_room_choice = input().lower()
        if user_quest_room_choice == "if":
            print("if-sats task metoden initating")
        elif user_quest_room_choice == "back":
            print("You turn around and head back to the starting room.\n\n")
            time.sleep(2)
            starting_room_normal()
            in_choice = False
        elif user_quest_room_choice == "exit":
            print("Are you sure you want to exit the game? Type yes/no")
            user_choice_exit2 = input().lower()
            if user_choice_exit2 == "yes":
                exit()
            elif user_choice_exit2 == "no":
                print("Available commands are: 'if' to initiate the if-task, 'back' to"
                      " return to starting room, or 'exit' to exit the game.")
