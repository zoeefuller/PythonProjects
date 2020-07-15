import random
print("Lets play a game!\n I will generate a number between 20 and 30.\n"
      "We will take it in turns to subtract a number of our choice between 1-3 from that number"
      "The person that gets the number to zero loses!")
gen_num = random.randint(20, 30)
print("The starting number is...", gen_num)
# describe game and generate number between 20 and 30 and print it
print("I will randomly generate who goes first!")
order = random.randint(1,2)
# decides who will go first
if order == 1:
    print("I will go first")
# if number generated is 1 computer goes first
elif order == 2:
    print("You will go first!")
# if number generated is 2 player goes first
new_num = gen_num
# assigns generated number (between 20 and 30) to new num to be used in functions
def player_input(new_num):
# player function
    print("Please play your number:")
    play_num = int(input())
# asks player to input number to subtract
    if play_num > 3 or play_num < 0:
        print("error you can only enter a number between 1 and 3")
        player_input(new_num)
    # ensures player only enters a number between 1 and 3
    new_num = new_num - play_num
    print(new_num)
    # take input away from number and print it
    return new_num
    # return new_num so that it may be used in the next function


def computer_input(new_num):
# computer player strategy
    print("My turn...")
    if new_num < 5:
        win_num = new_num - 1
        comp_num = win_num
        if comp_num <1:
            comp_num = 1
        print("My number is", comp_num)
    # winning strategy when number is less than 5 computer number should be that number -1
    # to ensure the player has to take away a number after.
    else:
    # if the number is greater than 5 employ below startegy
        if new_num%3 == 2:
            comp_num = 3
            print("My number is", comp_num)
        # if the remainder of number divided by 3 equals 2 take away 3
        if new_num%3 == 1:
            comp_num = 2
            print("My number is",comp_num)
    # if the remainder of number divided by 3 equals 1 take away 2
        if new_num%3 == 0:
            comp_num = 1
            print("My number is",comp_num)
    # if the remainder of number divided by 3 equals 0 take away 1
    # this strategy aims to get the computer to put the player onto 5
    # the player that puts the other onto 5 will win the game
    new_num = new_num - comp_num
    print("New total is", new_num)
    # take computer number away and print total
    return new_num
    # return number to be used in other functions


while new_num > 0:
    if order == 1:
        new_num = computer_input(new_num)
    # if order generated is 1 call computer function first
    # assign the return value of the method to new_num to be used in the next iteration of the method
        last_player = 1
        # assign last player to 1 to indicate the computer was last to play
        if new_num <= 0:
            break
            # once the number is less than or equal to 0 break the loop
        new_num = player_input(new_num)
        last_player = 2
        # call player function second
        # assign the return value of the method to new_num to be used in the next iteration of the method
        # assign last player to 2 to indicate the player was last to play
    if order == 2:
        new_num = player_input(new_num)
        last_player = 2
        if new_num <= 0:
            break
        new_num = computer_input(new_num)
        last_player = 1
        # reverse of above if the player was picked to go first

if last_player == 1:
    print("You win!")
    # if last player equals 1 player won as the last player will have taken the number to 0
elif last_player == 2:
    print("I win!")
    # if last player equals 1 player won as the last player will have taken the number to 0
