import time
from starting_room_normal import starting_room_normal
from quest_room_message import quest_room_welcome


def door_choice():

    in_choice = True
    while in_choice:

        user_adventure_choice = input().lower()
        if user_adventure_choice == "yes":
            quest_room_welcome()
            in_choice = False
        elif user_adventure_choice == "no":
            print("You back away from the door.\n\n")
            time.sleep(2)
            starting_room_normal()
            in_choice = False
        elif user_adventure_choice == "exit":
            print("Are you sure you want to exit the game? Type yes/no")
            user_choice_exit2 = input().lower()
            if user_choice_exit2 == "yes":
                exit()
            elif user_choice_exit2 == "no":
                print("Available commands are: 'yes' - enter the door, 'no' - "
                      "back away from the door, or 'exit' to exit the game")
