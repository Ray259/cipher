import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char.lower()) - ord('a')

            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) %
                                  26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) %
                                  26 + ord('a'))

            key_index += 1
        else:
            ciphertext += char

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) %
                                 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) %
                                 26 + ord('a'))
            key_index += 1
        else:
            plaintext += char
    return plaintext


def mono_encrypt(plaintext, subAlphabet):
    i = 0
    subAUpper = subAlphabet.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            for chr_alphabet, chr_alphabetUpper, chr_sub, chr_subUpper in zip(alphabet, alphabetUpper, subAlphabet, subAUpper):
                if plaintext[i].islower():
                    if (plaintext[i] == chr_alphabet):
                        ciphertext += chr_sub
                else:
                    if (plaintext[i] == chr_alphabetUpper):
                        ciphertext += chr_subUpper
        else:
            ciphertext += plaintext[i]
    return ciphertext


def mono_decrypt(ciphertext, subAlphabet):
    i = 0
    subAUpper = subAlphabet.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            for chr_alphabet, chr_alphabetUpper, chr_sub, chr_subUpper in zip(alphabet, alphabetUpper, subAlphabet, subAUpper):
                if ciphertext[i].islower():
                    if (ciphertext[i] == chr_sub):
                        plaintext += chr_alphabet
                else:
                    if (ciphertext[i] == chr_subUpper):
                        plaintext += chr_alphabetUpper
        else:
            plaintext += ciphertext[i]
    return plaintext


def process(input, key, method, mode):
    if method == 0 or mode == 0:
        print("\nExit program...")
    if method == 1 and mode == 1:
        print("\n****THIS IS THE CIPHERTEXT**** \n \n"+mono_encrypt(input, key)+"\n")
    elif method == 1 and mode == 2:
        print("\n****THIS IS THE PLAINTEXT****\n \n"+mono_decrypt(input, key)+"\n")
    elif method == 2 and mode == 1:
        print("\n****THIS IS THE CIPHERTEXT**** \n \n" + vigenere_encrypt(input, key)+"\n")
    elif method == 2 and mode == 2:
        print("\n****THIS IS THE PLAINTEXT**** \n \n"+vigenere_decrypt(input, key) +"\n")


def mainMenu():
    print("\n >> Choose encryption method")
    print("1. Mono-alphabet")
    print("2. Vigenere encryption")
    print("0. Exit")
    a = int(input("\nEnter your choice: "))
    while a > 3 or a < 0:
        print("\nInvalid option!")
        a = int(input("Enter your choice: "))
    return a


def processMenu():
    print("\n >> Choose process:")
    print("1. Encrypt mode")
    print("2. Decrypt mode")
    print("3. Return to method")
    print("0. Exit")
    b = int(input("\nSelect your choice: "))
    while b > 5 or b < 0:
        print("\nInvalid option!")
        b = int(input("Select your choice: "))
    if b == 5:
        mainMenu()
    return b


def main():
    while (1):
        a = mainMenu()
        if a == 0:
            print("\nProgram exited. \n...")
            sys.exit(0)
        elif a == 'alpha_freq':
            print("Here is the alphabet frequency: ")
        else:
            inputText = input("Enter plain/ciphertext: \n")
            b = processMenu()
            if b == 0:
                print("\nProgram exited. \n...")
                sys.exit()
            elif b == 3:
                main()
            elif b == 1 or b == 2:
                key = input("Enter encryption key: \n")
                if a == 1:
                    while (len(key) != 26):
                        print(
                            "Invalid key! The key must be a substituted alphabet (26 characters).")
                        print("Your key has", len(key),
                              "characters. Please re-enter your key!")
                        key = input("Enter encryption key: \n")
                process(inputText, key, a, b)


main()



# test 
# print(mono_encrypt('The Quick Brown fox jumps over thirteen lazy dogs','zyxwvutsrqponmlkjihgfedcba'))
# print(mono_decrypt('Gsv Jfrxp Yildm ulc qfnkh levi gsrigvvm ozab wlth','zyxwvutsrqponmlkjihgfedcba'))
# print(vigenere_encrypt('The quick brown fox jumps over thirteen lazy dogs','key')
# print(vigenere_decrypt('Dlc aygmo zbsux jmh nswtq yzcb xfsvroil vexi hmqw', 'key')
