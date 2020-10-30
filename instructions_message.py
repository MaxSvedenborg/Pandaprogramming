import time
import random
import sys


def instructions_message():

    guide_main_goal_message = (
        "\n\nWelcome to Panda programming, lets make programming fun!\n"
        "Down below the instructions of the game are listed:\n"
        "1. Complete various programming tasks, one for the moment.\n"
        "2. If you don't succeed the task, you will be teleported to the starting room.\n"
        "3. You can retry the tasks as many times as you want.\n"
        "If you would like to see the instructions again,"
        "Type 'instructions' in chat while being in the starting room.\n"
        "If you would like to exit the game, type exit in chat at any time.\n"
        "\nif not, type 'adventure' to start your journey!\n")

    for char in guide_main_goal_message:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)




