import random 
import string 

chars = "  " + string.punctuation + string.digits + string.ascii_letters

chars = list (chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  :{key}")

#Encrypt
plain_text = input("Enter a message to encrypt:")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}") 
print(f"encrypt message: {cipher_text}")       


#Decrypt
cipher_text = input("Enter a message to encrypt:")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypt message: {cipher_text}") 
print(f"Original message: {plain_text}")       

<<<<<<< HEAD
=======

# WhY
# Becuase it ensures security, privacy and intergrity of Data.

# How
# It is done by converting data into an unreadable format that can only be deciphered with a correct Key.
# - It can be used to Prevent unauthorised access to sensitive data like Passwords, credit card details or personal.
# - it ensures confidentiality when sending data over the internet.
# - To ensure data intergrity by making it difficult for attackers to modify
# And some encryption methods help verify authenticity.
# You can utelize these libraries : Cryptography, pycryptodome and hashlib

# WHAT
#  It protects Data.
>>>>>>> 20c49d7df4cd1a50d85a0e2eff8df9f12efca796
