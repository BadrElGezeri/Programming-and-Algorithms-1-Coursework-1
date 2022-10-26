import time
import random
from pathlib import Path
import sys
from time import sleep
def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
x= []
for i in range(4):
    x.append(4+(i-1)*2)

with open("Keys.txt", 'w') as f:
    f.writelines(str(x))

with open("Keys.txt") as f:
    rand_num = f.read()
listToString(rand_num)
rand_num = rand_num.replace(" ","")
rand_num = rand_num.replace("[","")
rand_num = rand_num.replace("]","")
rand_num = rand_num.replace(",","")

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
    y = x + key_num # A random function to scramble the ASCII values
    return y # Return the result of the function

def unkey(x,user_key):
    y = x - user_key #Reverses what the key() function does
    return y 



new_list = []
dec_list = []



while True:
    state = str(input("Do you want to Encrypt or Decrypt?\n> ")).lower()
    key_num = int(random.choice(rand_num))
    if state == "encrypt":
        choice = input("Do you want to encrypt text or a file?\n> ").lower()
        if choice == "string" or choice == "text":
            string = input("Input the text: \n> ")
            list = ([*string])
            # print(list)
            length = len(string)
            for i in range(length):
                # print(ord(list[i]))
                new_list.append(key(ord(list[i])))
                dec_list.append(chr(new_list[i]))
            print("".join(map(str,dec_list)), end = " - is the encrypted form\n")
            print("The cryptography key = ", key_num)
            done = listToString(dec_list)
        elif choice == "file":
            file_name = str(input("Please enter the file path: \n> "))
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
        file = input("Do you want to save the encrypted form in a file? \n> ")
        if file == "Yes" or file == "yes":
            timestr = time.strftime("_%d-%m-%Y_%H-%M-%S")
            filename_saved = "encrypted" + str(timestr) + ".txt"
            with open(filename_saved, 'w') as f:
                f.write(str(done))
            print("File saved as", filename_saved,"at", Path.cwd())
    if state == "decrypt":
        choice = input("Do you want to decrypt text or a file? \n> ").lower()
        if choice == "file":
            file_name = str(input("Please enter the file path: \n> "))
            file_name = file_name.replace("\"","")
            with open(file_name) as f:
                string = f.read()
                print("The file contains the string: ",string)
                # print(type(string))
                user_key = input("Enter the decryption key:\n> ")
                list = ([*string])
                length = len(string)
                for i in range(length):
                    new_list.append(unkey(ord(list[i])),user_key)
                    dec_list.append(chr(new_list[i]))
                done = listToString(dec_list)
            print("".join(map(str,dec_list)), end = " - is the decrypted form\n")
        elif choice == "string" or choice == "text":
            string = input("Input the text\n> ")
            user_key = int(input("Enter the decryption key:\n> "))
            list = ([*string])
            length = len(string)
            for i in range(length):
                new_list.append(unkey(ord(list[i]),user_key))
                dec_list.append(chr(new_list[i]))
            done = listToString(dec_list)
        print("".join(map(str,dec_list)), end = " - is the decrypted form\n")
        file = input("Do you want to save the decrypted form in a file? \n> ")
        if file == "Yes" or file == "yes":
            timestr = time.strftime("_%d-%m-%Y_%H-%M-%S")
            filename_saved = "decrypted" + str(timestr) + ".txt"
            with open(filename_saved, 'w') as f:
                f.write(str(done))
            print("File saved as", filename_saved,"at", Path.cwd())
    program_state = str(input("Do you want to retry?\n> ")).lower()
    if program_state == "yes":
        new_list = []
        dec_list = []
        continue
    else:
        break
input("\nPress any key to close")
