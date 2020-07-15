import random
print("Please input your message:")
message = input()
# asks user for message
print("Please input key: ")
shift = int(input())
# asks user for key

def encryption(message, shift):
    result = ""
    random.seed(shift)
    # asks computer to generate random number using the key as the seed
    for x in range(len(message)):
        char = message[x]
        # extract 1 character from message at index of loop iteration number
        key = random.randint(1,26)
        # generate random number based off key seed between 1 and  and assign to key
        if (char.isupper()):
            result += chr((ord(char) + key - 65) %26 + 65)
            # if the character is upper add key to character number
            # and to loop through just upper case letters use the ASCII numbers
        else:
            result += chr((ord(char)+ key - 97) %26 + 97)
            # else loop use lower case ASCII numbers
    return result
    # return new number for characters


print("message: " + message)
print("key:" + str(shift))
# print message and key
cipher = encryption(message,shift)
# assign cipher to encryption method
print("cipher: "+ cipher)
# print cipher



def decryp(message, shift):
    result = ""
    random.seed(shift)
    for x in range(len(message)):
        char = message[x]
        key = random.randint(1,26)
        if (char.isupper()):
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result
# decryption uses the same method as encryption but just takes away the key

print("cipher: " + cipher)
print("key:" + str(shift))
# print cipher and key
message = decryp(cipher, shift)
# assign message to decryp function
print("message: "+ message )
# print method
