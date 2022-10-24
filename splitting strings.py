print("Booting up...")
print("Welcome to Encrypto \nPress any key to start\n")

def key(x):
    y = x + 3 # A random function to scramble the ASCII values
    return y # Return the result of the function


from math import sqrt #import square root function from math libary

def unkey(x):
    y = x - 3
    return y


string = input("Input a string: \n")
list = ([*string])
print(list)
length = len(string)
count = 0
new_list = []
dec_list = []
state = str(input("Do you want to Encrypt or Decrypt? "))

if state == "Encrypt" or state == "encrypt":
    for i in range(length):
        # print(ord(list[i]))
        new_list.append(key(ord(list[i])))
        dec_list.append(chr(new_list[i]))
    print("".join(map(str,dec_list)))

if state == "Decrypt" or state == "decrypt":
    size = int(input("How many values do you have?"))
    for i in range(size):
        dec_list.append(int(input("Enter the values of the list: ")))
        new_list.append(chr(unkey(dec_list[i])))
    print("".join(map(str,new_list)))