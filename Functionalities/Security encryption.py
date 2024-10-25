import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key= chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key : {key}")

# ENCRYPT 

# plain_text= input("Enter a message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"original message: {plain_text}")
# print(f"original message: {cipher_text}")

# DECRYPTING 

while True:
    plain_text = input("Enter a message to encrypt (or type 'exit' to stop): ")
    
    # Condition to break the loop and end the program
    if plain_text.lower() == 'exit':
        print("Exiting the program.")
        break

    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)  # Assuming `chars` is defined earlier in your program
        cipher_text += key[index]  # Assuming `key` is defined earlier in your program

    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {cipher_text}")