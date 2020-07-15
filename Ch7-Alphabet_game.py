import time
times_list = []
# list to keep players times in

def alph_game():
    print("Lets play a game!\n "
          "Press enter to start the timer and the type the alphabet as fast as you can!\n"
          "Press enter to stop the timer when your done\n"
          "Fastest time wins!")
    start = input()
    # player press enter key to start the timer
    if start == "":
        start_time = time.perf_counter()
        # if player presses enter record start time
        alphabet = input()
        end_time = time.perf_counter()
        # player inputs alphabet and presses enter to record end time
        time_taken = round(end_time - start_time,2)
        # take start time away from end time to get the players time
        # rounds player's time to 2 decimal places
        if alphabet == "abcdefghijklmnopqrstuvwxyz" or alphabet == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # checks user has inputted the alphabet correctly
            times_list.append(time_taken)
            # if alphabet correct add player time to times list
            times_list.sort()
            # sort list numerically (default - smallest to largest)
            print("\nScore board:\n",times_list)
            # prints time list
            print("The best time is", times_list[0])
            # prints index 0 of list (fastest time)
            print(" \n Well done! Your time was", time_taken, "seconds!")
            if time_taken == times_list[0]:
                 print("HIGH SCORE!")
                # if players time is equal to the fastest time (time at index one) print high score!
        else:
            print("Sorry you got it wrong!")
            # if alphabet inputted incorrectly inform player
        print("Would you like to try again?")
        # if alphabet inputted wrong or player has successfully inputted alphabet ask if they wish to try again
        choice = input()
        if choice == "yes":
            alph_game()
            # if yes call game again
        else:
            print("Okay, have a nice day!")
            # if anything else inputted end game
    else:
        print("error, please try again")
        alph_game()
        # if anything other than enter key pressed to start timer display error


alph_game()
# calls game to be executed
