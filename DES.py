import base64
from Crypto.Cipher import DES 
from Crypto.Random import get_random_bytes

#Input plaintext
plaintext = input("Enter the plaintext: ");
#Padding the plaintext
while len(plaintext) % 8 != 0:
    plaintext = plaintext + " "
#Create a random key
key = get_random_bytes(8)

#Create model of the cipher
des = DES.new(key, DES.MODE_ECB)

#Encryption Part
ciphertext = des.encrypt(plaintext.encode('utf-8'))
print("Ciphertext: ", base64.b64encode(ciphertext))
#Decryptiom Part
decryptedtext = des.decrypt(ciphertext)
print("Decrypted text : ", decryptedtext.decode())