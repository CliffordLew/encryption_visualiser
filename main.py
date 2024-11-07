
class ECaesarCipher:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    plaintext = ''
    ciphertext = ''
    shift = -1
    def __init__(self):
        self.plaintext = input("Input string to be encrypted/decrypted: \n")
        self.shift = int(input("Input # of letters to shift by (if decrypting, use negative #s) \n"))
    
    def encrypt(self):
        temp = list(self.plaintext)
        print(f"temp is {temp}")
        for index, letter in enumerate(temp):
            alph_index = self.ALPHABET.find(letter)
            print(f"index of {letter} is {alph_index}")
            alph_index += self.shift
            temp[int(index)] = self.ALPHABET[alph_index]
            print(f"new letter is {self.ALPHABET[alph_index]}")
        self.ciphertext = "".join(temp)
        print(f"Ciphertext is {self.ciphertext}")

def main(): 
    
    test = ECaesarCipher()
    test.encrypt()




if __name__ == "__main__":
    main()
