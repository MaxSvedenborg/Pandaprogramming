import time
import random
import sys

from starting_room_normal import starting_room_normal


def adventure_choice():

    adventure_start_message = (
        "\n\nVery well, off we go!\n\n" 
        ". . . . . . . . . . . . . . . . .\n\n" 
        "A door appears in front of you, do you wish to enter? type 'yes'/'no' in chat.\n")

    for char in adventure_start_message:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)

    while True:

        user_adventure_choice = input().lower()
        if user_adventure_choice == "yes":
            print("questroom method insert here")
        elif user_adventure_choice == "no":
            print("You back away from the door.\n\n")
            time.sleep(2)
            starting_room_normal()
        elif user_adventure_choice == "exit":
            print("Are you sure you want to exit the game? Type yes/no")
            user_choice_exit2 = input().lower()
            if user_choice_exit2 == "yes":
                exit()


