import unittest
import endfile as E

class Testmycode(unittest.TestCase):            #Test Suite
    
    def test_encrypt(self): # Encryption test
        done = E.encrypt("Hello",2) # → ("Text",Key)
        # ↑ Passes through Rail Fence Cipher, (Which is equal to "Hloel"). Then it passes to Caesar Cipher, where "Hloel" is changed to "Jnqgn"
        self.assertEqual(done,"Jnqgn","The encryption has failed")
    
    def test_decrypt(self): #Decryption test
        done = E.decrypt("Jnqgn",2) 
        self.assertEqual(done,"Hello","The decryption has failed")



if __name__ == "__main__":
    unittest.main()