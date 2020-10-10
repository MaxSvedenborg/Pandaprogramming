
def welcome_message_counter():
    counter_list = []
    while True:

        if counter_list.count(1) == 0:
            #welcome_message()
            print("first")
            #instructions_message()
            counter_list.append(1)

        elif counter_list.count(1) > 0:
            #user_door_choice()
            print("second")
            break


welcome_message_counter()
