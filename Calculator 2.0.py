print("Hello! Welcome to the calculator!")
# print greeting


def calculator():
    # create calculator function so that it may be re-called as needed
    print("Calculations available:\n +   Add\n -   Subtract\n *   Multiply\n /   Divide\n ^   Square\n **  Power")
    print("Please input your calculation:  ")
    calcinput = input()
    # ask user to input calculation they wish to perform
    inputlist = calcinput.split()
    # split the inputted string using the whitespace to identify individual numbers/operator

    if len(inputlist) == 2 or len(inputlist) == 3:
        # check that user has inputted 2 numbers and an operator separated by spaces
        # or if calculating a square check if 1 number and operator inputted
        num1 = int(inputlist[0])
        # set variable num1 to the character at index 0 (first character)
        # converts string to an int
        operator = inputlist[1]
        # sets variable operator to the character at index 1 (second character)
        if operator == "^":
            print("The answer is...", num1 * num1)
            # if operator is ^ multiply num1 by itself
        num2 = 0
        # sets num2 to 0 so that it is always assigned a value
        if len(inputlist) == 3:
            # checks that there are 3 characters (not a square calculation) so that there is a second number to assign
            num2 = int(inputlist[2])
            # set variable num2 to the character at index 2 (last/third character)
            # converts string to an int
        if operator == "+":
            print("The answer is...", num1 + num2)
            # if operator + add nums together
        elif operator == "-":
            print("The answer is...", num1 - num2)
            # if operator - subtract nums
        elif operator == "*":
            print("The answer is...", num1 * num2)
            # if operator is * multiply nums
        elif operator == "/":
            print("The answer is...", int(num1 / num2))
            # if operator is / divide nums
        elif operator == "**":
            print("The answer is...", num1 ** num2)
            # if operator is ** calculate num1 to the power of num2

        print("Would you like to perform another calculation?")
        choice = input()
        if choice == "yes":
            calculator()
        # recursion so that the function may re-run as many times as needed
        # asks user if they want to use calculator again
        # if they input yes the calculator function is called again
        else:
            print("Thank you, have a nice day!")
        # if the user inputs any thing other than yes the code will end

    else:
        print("Ooops something went wrong\n please try again and make sure you are using spaces!")
        calculator()
        # safety - if anything else inputted will return an error.
        # this includes the calculation be inputted without spaces around the operator.


calculator()
