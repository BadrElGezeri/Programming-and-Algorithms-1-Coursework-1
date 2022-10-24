import time
from pathlib import Path
import sys
from time import sleep
words = "Booting up..."
for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
words2 = "\nWelcome to Encrypto"
for char in words2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

input("\nPress any key to start\n")
def key(x):
    y = x + 3 # A random function to scramble the ASCII values
    return y # Return the result of the function

def unkey(x):
    y = x - 3 #Reverses what the key() function does
    return y 

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

new_list = []
dec_list = []

state = str(input("Do you want to Encrypt or Decrypt? ")).lower()


if state == "encrypt":
    choice = input("Do you want to encrypt a string or a file? ").lower()
    if choice == "string":
        string = input("Input a string: \n")
        list = ([*string])
        # print(list)
        length = len(string)
        for i in range(length):
            # print(ord(list[i]))
            new_list.append(key(ord(list[i])))
            dec_list.append(chr(new_list[i]))
        print("".join(map(str,dec_list)), end = " - is the encrypted form\n")
        done = listToString(dec_list)
    elif choice == "file":
        file_name = str(input("Please enter the file path: "))
        file_name = file_name.replace("\"","")
        with open(file_name) as f:
            string = f.read()
        print("The file contains the string:",string)
        list = ([*string])
        # print(list)
        length = len(string)
        for i in range(length):
            # print(ord(list[i]))
            new_list.append(key(ord(list[i])))
            dec_list.append(chr(new_list[i]))
        done = listToString(dec_list)
        print(done, "is the encrypted form\n")
    file = input("Do you want to save the encrypted form in a file? ")
    if file == "Yes" or file == "yes":
        timestr = time.strftime("_%d-%m-%Y_%H-%M-%S")
        filename_saved = "encrypted" + str(timestr) + ".txt"
        with open(filename_saved, 'w') as f:
            f.write(str(done))
        print("File saved as", filename_saved,"at", Path.cwd())
if state == "decrypt":
    choice = input("Do you want to decrypt a string or a file? ").lower()
    if choice == "file":
        file_name = str(input("Please enter the file path: "))
        file_name = file_name.replace("\"","")
        with open(file_name) as f:
            string = f.read()
            print("The file contains the string: ",string)
            # print(type(string))
            list = ([*string])
            length = len(string)
            for i in range(length):
                new_list.append(unkey(ord(list[i])))
                dec_list.append(chr(new_list[i]))
            done = listToString(dec_list)
        print("".join(map(str,dec_list)), end = " - is the decrypted form\n")
    elif choice == "string":
        string = input("Input a string\n")
        list = ([*string])
        length = len(string)
        for i in range(length):
            new_list.append(unkey(ord(list[i])))
            dec_list.append(chr(new_list[i]))
        done = listToString(dec_list)
    print("".join(map(str,dec_list)), end = " - is the decrypted form\n")
    file = input("Do you want to save the decrypted form in a file? ")
    if file == "Yes" or file == "yes":
        timestr = time.strftime("_%d-%m-%Y_%H-%M-%S")
        filename_saved = "decrypted" + str(timestr) + ".txt"
        with open(filename_saved, 'w') as f:
            f.write(str(done))
        print("File saved as", filename_saved,"at", Path.cwd())
input("\nPress any key to close")
