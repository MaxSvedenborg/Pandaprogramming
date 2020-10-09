
import time
import sys
import random

flagga1 = 0

def main():

    def first_message():
        if flagga == 0:


            starting_message = "Hello, and welcome to Panda programming!"
            for char in starting_message:
                timer_value1 = random.uniform(0.01, 0.1)
                sys.stdout.write(char)
                time.sleep(timer_value1)

            time.sleep(2)

            ask_user_name = "\nBefore we start,\n"
            for char in ask_user_name:
                timer_value2 = random.uniform(0.01, 0.1)
                sys.stdout.write(char)
                time.sleep(timer_value2)

            time.sleep(1)

            while True:
                error_message_1 = "Please enter your name in the textbox below, with only alphabetic characters.\n"
                for char in error_message_1:
                    timer_value4 = random.uniform(0.01, 0.1)
                    sys.stdout.write(char)
                    time.sleep(timer_value4)
                user_name = input()

                if user_name.isalpha():
                    welcome_message = (f"\nHello, {user_name}, it is nice to have you here!")
                    for char in welcome_message:
                        timer_value3 = random.uniform(0.01, 0.1)
                        sys.stdout.write(char)
                        time.sleep(timer_value3)
                    break
flagga1 == 1
time.sleep(1)


    def instructions_message():
        guide_main_goal_message = ("\n\nYour main goal is to collect enough PandaCash to buy your freedom. Who doesn't like freedom?\n" 
                                  "Down below the instructions of the game are listed:\n"  
                                  "1. Complete various programming tasks flawless to gain PandaCash.\n" 
                                  "2. If you don't succeed the task, your health will go down.\n" 
                                  "3. More health can be purchased with earned PandaCash at the starting room.\n" 
                                  "4. Navigate to each rooms by looking at the map to the left and entering them with textcommands.\n" 
                                  "5. If your health drops below 1, the game will end and you will have to start over.\n" 
                                  "6. You win by gaining 10 PandaCash as that is the price for freedom.\n\n" 
                                  "if you would like to see the instructions again, TYPE 'instructions' in chat while being in the startingroom.\n" 
                                  "if not, TYPE 'continue' to start your journey!\n")

        for char in guide_main_goal_message:
            timer_value1 = random.uniform(0.01, 0.1)
            sys.stdout.write(char)
            time.sleep(timer_value1)

        while True:

            user_instructions_choice = input().lower()
            if user_instructions_choice == "instructions":
                for char in guide_main_goal_message:
                    timer_value1 = random.uniform(0.01, 0.1)
                    sys.stdout.write(char)
                    time.sleep(timer_value1)
            elif user_instructions_choice == "continue":
                break

if __name__ == "__main__":
    main()
