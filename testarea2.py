def run():
    user_input = input()
    while user_input == 'instructions':
        counter()


def counter():
    count = []

    if count < 1:
        print ("första meddelandet")
        count += 1
    elif count > 1:
        print ("andra meddelandet")


run()



