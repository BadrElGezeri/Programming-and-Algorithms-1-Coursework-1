import RailFenceCipher as R
import CaesarCipher as C

def listToString(s):
    str1 = ""  # Creating an empty Variable
    for i in s:  # add part of the list to the string
        str1 += i
    return str1 # return string
def encrypt(text,key_num):
    new_list = []
    dec_list = []
    string = R.encryptRailFence(text, key_num) # Changes the position of the chracters
    list = ([*string])
    length = len(string)
    for i in range(length):
        new_list.append(C.key(ord(list[i]),key_num)) # Changes the value of every character
        dec_list.append(chr(new_list[i]))
    # print("".join(map(str,dec_list)), end = " - is the encrypted form\n")
    # print("The cryptography key = ", key_num)
    done = listToString(dec_list)
    return done

def decrypt(text,key_num):
    new_list = []
    dec_list = []
    user_key = key_num
    string = R.decryptRailFence(text,user_key)
    list = ([*string])
    length = len(string)
    for i in range(length):
        new_list.append(C.unkey(ord(list[i]),user_key))
        dec_list.append(chr(new_list[i]))
    done = listToString(dec_list)
    return done