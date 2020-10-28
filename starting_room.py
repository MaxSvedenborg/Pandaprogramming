import time
import random
import sys

from welcome_message import welcome_message
from instructions_message import instructions_message
from menu_one import menu_one


class FirstRoom:

    welcome_message()
    instructions_message()
    while True:
        menu_one()


