# encryption program
import random
import string

# create character list
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# create key
key = chars.copy()
random.shuffle(key)

# show mapping (optional)
# print(f"chars: {chars}")
# print(f"key:   {key}")

# -------- ENCRYPT --------
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]
    else:
        cipher_text += letter  # keep unknown chars same

print(f"\nEncrypted message: {cipher_text}")

# -------- DECRYPT --------
decrypted_text = ""

for letter in cipher_text:
    if letter in key:
        index = key.index(letter)
        decrypted_text += chars[index]
    else:
        decrypted_text += letter

print(f"Decrypted message: {decrypted_text}")