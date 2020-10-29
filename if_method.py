import time
import random
import sys
from starting_room_normal import starting_room_normal
from health_info import health_info


def if_method_quest():

    if_method_message = (
        "\n\nThe goal here is to understand the if-statement.\n"
        "If you succeed, you will be granted 10 points, "
        "but if you don't you will loose 1 heart per try.\n" 
        "An if-statement is built up starting with an "
        "if-statement followed by an condition between two values followed by a ':'" 
        " followed by an intended code on the next line. \n"
        "Here is an example:\n"
        "if 1 < 2:\n"
        "    print('hi')\n"
        "If you want to back to the starting room, type 'back',\n"
        "or if you want to exit, type 'exit'.\n")

    for char in if_method_message:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)

    time.sleep(1)

    if_method_task = (
        "\nType in chat the final value of X, as an integer.\n"
        "If you succeed, you will be granted 10 points.\n\n"
        "x, y = 3, 20 \n"
        "if y > x:\n"
        "   x = 5\n"
        "else:\n"
        "   x = 3\n"
        "X = ")

    for char in if_method_task:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)

    in_choice = True
    while in_choice:
        user_if_method_choice = input().lower()
        if user_if_method_choice == "5":
            print("wincondition för tasken")
        elif user_if_method_choice == "back":
            print("You turn around and head back to the starting room.\n\n")
            time.sleep(2)
            starting_room_normal()
            in_choice = False
        elif user_if_method_choice == "exit":
            print("Are you sure you want to exit the game? Type yes/no")
            user_choice_exit2 = input().lower()
            if user_choice_exit2 == "yes":
                exit()
            elif user_choice_exit2 == "no":
                print("Available commands are: 'back' to"
                      " return to starting room, or 'exit' to exit the game.")
        while user_if_method_choice not in ("5", "back", "exit"):
            print("you lost a life")
            lives -= 1
            health_info(lives)
            break

