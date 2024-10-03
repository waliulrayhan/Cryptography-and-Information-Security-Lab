import base64
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes

plaintext = b'This is a secret message'
key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
print("Ciphertext : ", base64.b64encode(ciphertext))
print("Tag : ", tag)

decrypt_cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_text =decrypt_cipher.decrypt_and_verify(ciphertext, tag)
print("Decrypted text: ", decrypted_text.decode())