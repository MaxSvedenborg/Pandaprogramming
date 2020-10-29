import time
import random
import sys


def health_info(health):

    out_of_lives_message = "You are out of lives, and the game is sadly over.\n"
    suggest_buy_more_message = (f"you have {health} health left, and I suggest you to buy "
                                "more in the starting room with your earned Panda Cash.\n")
    good_health_message = f"you have {health} health left.\n"

    if health < 1:
        for char in out_of_lives_message:
            timer_value1 = random.uniform(0.01, 0.02)
            sys.stdout.write(char)
            time.sleep(timer_value1)
        quit()

    elif 0 < health < 5:
        for char in suggest_buy_more_message:
            timer_value1 = random.uniform(0.01, 0.02)
            sys.stdout.write(char)
            time.sleep(timer_value1)

    elif health >= 5:
        for char in good_health_message:
            timer_value1 = random.uniform(0.01, 0.02)
            sys.stdout.write(char)
            time.sleep(timer_value1)



