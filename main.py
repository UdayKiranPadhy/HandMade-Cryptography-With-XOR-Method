from handmade_crypto import *
import sys
from os.path import exists

if exists("secret.key"):
    message = input("Your secret message: ")
    crypto_key = read_file("secret.key")
    cipher = xor_fn(message, crypto_key)
    print(f"Cipher text is: {cipher}")
    write_file("ciphertext.txt", cipher)
    data = read_file("ciphertext.txt")
    plain = xor_fn(data, crypto_key)
    print(f"Decrypted text: {plain}")
else:
    key = create_key()  # Key length is 1024 bytes long.
    print(f"Key generated: {key}")
    if write_file("secret.key", key):
        print("Key is written to file.")
    else:
        print("Key has failed to write to file.")
        sys.exit(1)