
import time
import sys
import random


def main():

    #lägg in user_name +1 så man aldrig automatiskt får detta meddelande två gånger. lägg in !help för commandon - dvs köra om välkomstscriptet.
    starting_message = "Hello, and welcome to Panda programming! "
    for char in starting_message:
        timer_value1 = random.uniform(0.01, 0.1)
        sys.stdout.write(char)
        time.sleep(timer_value1)

    time.sleep(2)

    ask_user_name = "\nBefore we start, please enter your name in the textbox below.\n"
    for char in ask_user_name:
        timer_value2 = random.uniform(0.01, 0.1)
        sys.stdout.write(char)
        time.sleep(timer_value2)

    user_name = input()

    while not user_name.isalpha():
        error_message_1 = "Please enter your name in the textbox below, with only alphabetic characters."
        for char in error_message_1:
            timer_value4 = random.uniform(0.01, 0.1)
            sys.stdout.write(char)
            time.sleep(timer_value4)
    user_name = input()

    if user_name.isalpha:
        welcome_message = (f"\nHello, {user_name}, it is nice to have you here!")

        for char in welcome_message:
            timer_value3 = random.uniform(0.01, 0.1)
            sys.stdout.write(char)
            time.sleep(timer_value3)

#fyll på med guide-linjer


if __name__ == "__main__":
    main()
