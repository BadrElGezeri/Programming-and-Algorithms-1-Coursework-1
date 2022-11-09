def key(string,key_num):
    encrypted_text = string + key_num # Scrambles value depending on it's ASCII value
    return encrypted_text # Return the result of the function

def unkey(string,user_key):
    decrypted_text = string - user_key #Reverses what the key() function does
    return decrypted_text 