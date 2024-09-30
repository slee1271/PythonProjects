import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters 

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key:   {key}")

#Encryption 
og_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in og_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original Message: {og_text}")
print(f"Encrypted Message: {cipher_text}")

#Decryption 
cipher_text = input("Enter a message to decrypt: ")
og_text = ""

for letter in cipher_text:
    index = key.index(letter)
    og_text += chars[index]

print(f"Encrypted Message: {cipher_text}")
print(f"Original Message: {og_text}")
