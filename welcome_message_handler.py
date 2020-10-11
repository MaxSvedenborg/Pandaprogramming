import time
import random
import sys

from welcome_message import *
from instructions_message import *


def welcome_message_counter():
    counter_list = [] #ska nog ligga utanför så den blir global, så ha med kontroll metoden innan 1.1.1, men ha denna utanför

    if counter_list.count(1) == 0:
        welcome_message()
        instructions_message()
        counter_list.append(1)

    elif counter_list.count(1) > 0:
        print("second")




