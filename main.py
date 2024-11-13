import random
import string

chars=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")


#enc
text=input("Enter a messege to encrypt: ")
cipher_text=""

for letter in text:
    index=chars.index(letter)
    cipher_text+=key[index]
    
print(f"Orginal text: {text}")
print(f"Encrypted text: {cipher_text}")


#decrypt
cipher_text=input("Enter a messege to decrypt: ")
text=""

for letter in cipher_text:
    index=key.index(letter)
    text+=chars[index]
    
print(f"Decrypted text: {cipher_text}")
print(f"Orginal text: {text}")
