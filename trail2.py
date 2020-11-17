from itertools import cycle

key = "secretkey"
message = "this is my message, see if it can be encrypted completely."

cipher_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(message, cycle(key)))
print(cipher_text)
plain_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(cipher_text, cycle(key)))
print(plain_text)