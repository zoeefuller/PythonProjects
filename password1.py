password1 = "1"
password2 = "0"
# pre-set password to be used in while loop

while password1 != password2:
    print("Please input your password")
    password1 = str(input())
    password2 = ""
    # ask user to input password and set password2 to blank
    if any(x.isdigit() for x in password1) and any(x.isupper() for x in password1) and any(
            x.islower() for x in password1) and len(password1) >= 8:
        print("Your password is strong")
        # if password contains a digit, an upper case letter and is at least 8 characters
        # print your password is strong
        print("To confirm please re-enter your password")
        password2 = str(input())
        # ask user to confirm password by re-inputting it
        if password2 != password1:
            print("The passwords do no match. Please try again")
            # if re-entered password does not equal original print password do not match
        elif password2 == password1:
            print("Your password has been set")
            # if re-entered password equals original print password set
    elif any(x.isupper() for x in password1) and any(x.islower() for x in password1) and len(password1) >= 8:
        print("Your password is medium")
        # if password contains an upper case letter and is at least 8 characters
        # print your password is medium
        print("To confirm please re-enter your password")
        password2 = str(input())
        # ask user to confirm password by re-inputting it
        if password2 != password1:
            print("The passwords do no match. Please try again")
            # if re-entered password does not equal original print password do not match
        elif password2 == password1:
            print("Your password has been set")
            # if re-entered password equals original print password set
    elif len(password1) >= 8:
        print("Your password is weak")
        # if password is at least 8 characters
        # print your password is weak
        print("To confirm please re-enter your password")
        password2 = str(input())
        # ask user to confirm password by re-inputting it
        if password2 != password1:
            print("the passwords do no match. Please try again")
            # if re-entered password does not equal original print password do not match
        elif password2 == password1:
            print("Your password has been set")
            # if re-entered password equals original print password set
    else:
        print("error")
