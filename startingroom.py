import time
import sys
import random
#lägg in user_name +1 så man aldrig automatiskt får detta meddelande två gånger. lägg in !help för commandon - dvs köra om välkomstscriptet.
#def starting_area (new_player):





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

flagga1 = 1





#new_player = newcomer()

# if newcomer == 0:
    #print welcome_msg
if __name__ == "__main__":
    main()