def main():
    import time
    import sys
    import random

    text = "Hello, this is a test text to see if all works fine."

    for char in text:
        timer_value = random.uniform(0.01, 0.6)
        sys.stdout.write(char)
        time.sleep(timer_value)


if __name__ == "__main__":
    main()
