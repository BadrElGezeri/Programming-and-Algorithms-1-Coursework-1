import time
import random
from pathlib import Path
import sys
import os
import RailFenceCipher as R
import CaesarCipher as C

def listToString(s):
    str1 = ""  # Creating an empty Variable
    for i in s:  # add part of the list to the string
        str1 += i
    return str1 # return string

keys= []
for i in range(1,4,1):
    keys.append(2+(i-1)*2)
os.system( "attrib -h Keys.txt" ) # Makes the file visible for writting
with open("Keys.txt", 'w') as f:
    f.writelines(str(keys))

with open("Keys.txt") as f:
    rand_num = f.read()
os.system( "attrib +h Keys.txt" ) # Makes the file hidden to make it inaccessible to users
listToString(rand_num)
rand_num = rand_num.replace(" ","") # All of
rand_num = rand_num.replace("[","") # these
rand_num = rand_num.replace("]","") # are used
rand_num = rand_num.replace(",","") # to remove certain characters so when the 

words = "Booting up..."
for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
words2 = "\nWelcome to Encrypto"
for char in words2:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

input("\nPress any key to start\n")

new_list = []
dec_list = []

while True:
    state = str(input("Do you want to Encrypt or Decrypt?\n> ")).lower()
    key_num = int(random.choice(rand_num))
    if state == "encrypt":
        choice = input("Do you want to encrypt text or a file?\n> ").lower()
        if choice == "string" or choice == "text": # If the user chooses to encrypt via text
            text = input("Input the text: \n> ")
            string = R.encryptRailFence(text, key_num) # Changes the position of the chracters
            list = ([*string])
            length = len(string)
            for i in range(length):
                new_list.append(C.key(ord(list[i]),key_num)) # Changes the value of every character
                dec_list.append(chr(new_list[i]))
            print("".join(map(str,dec_list)), end = " - is the encrypted form\n")
            print("The cryptography key = ", key_num)
            done = listToString(dec_list)
        elif choice == "file": # If the user chooses to encrypt via a file
            file_name = str(input("Please enter the file path: \n> "))
            file_name = file_name.replace("\"","") # Removes the quotations that are placed by windows when you copy a file path
            with open(file_name) as f:
                text = f.read()
            string = R.encryptRailFence(text, key_num)
            print("The file contains the string:",text)
            list = ([*string])
            length = len(string)
            for i in range(length):
                new_list.append(C.key(ord(list[i]),key_num))
                dec_list.append(chr(new_list[i]))
            done = listToString(dec_list)
            print(done, "is the encrypted form")
            print("The cryptography key = ", key_num)
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
                text = f.read()
            print("The file contains the string:",text)
            user_key = int(input("Enter your cryptography key:\n> "))
            string = R.decryptRailFence(text,user_key)
            list = ([*string])
            length = len(string)
            for i in range(length):
                new_list.append(C.unkey(ord(list[i]),user_key))
                dec_list.append(chr(new_list[i]))
            done = listToString(dec_list)
            print("".join(map(str,dec_list)), end = " - is the decrypted form\n")
        elif choice == "string" or choice == "text":
            text = input("Input the text\n> ")
            user_key = int(input("Enter your cryptography key:\n> "))
            string = R.decryptRailFence(text,user_key)
            list = ([*string])
            length = len(string)
            for i in range(length):
                new_list.append(C.unkey(ord(list[i]),user_key))
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