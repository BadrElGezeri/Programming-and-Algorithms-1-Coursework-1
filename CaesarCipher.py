def key(x,key_num):
    y = x + key_num # Scrambles value depending on it's ASCII value
    return y # Return the result of the function

def unkey(x,user_key):
    y = x - user_key #Reverses what the key() function does
    return y 