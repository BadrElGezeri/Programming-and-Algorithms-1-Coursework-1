print("Booting up...")
input("Welcome to Encrypto \nPress any key to start\n")

def key(x):
    y = x + 3 # A random function to scramble the ASCII values
    return y # Return the result of the function

def unkey(x):
    y = x - 3
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

state = str(input("Do you want to Encrypt or Decrypt? "))

if state == "Encrypt" or state == "encrypt":
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
    file = input("Do you want to save the encrypted form in a file? ")
    if file == "Yes" or file == "yes":
        with open('encrypted.txt', 'w') as f:
            f.write(str(done))

if state == "Decrypt" or state == "decrypt":
    file = input("Do you want to decrypt by inputting a string or form a file? ")
    if file == "file" or file == "File":
        with open('E:\encrypted.txt') as f:
            string = f.readlines()
        list = ([*string])
        print(list)
        list.append(list)
        length = len(string)
        for i in range(length):
            new_list.append(unkey(ord(list[i])))
            dec_list.append(chr(new_list[i]))
        print("".join(map(str,dec_list)), end = " - is the decrypted form")
    else:
        string = input("Input a string\n")
        list = ([*string])
        length = len(string)
        for i in range(length):
            new_list.append(unkey(ord(list[i])))
            dec_list.append(chr(new_list[i]))
        print("".join(map(str,dec_list)), end = " - is the decrypted form")
input("\nPress any key to close")


