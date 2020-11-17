# HandMade-Cryptography-With-XOR-Method
This is a self made cryptograph using XOR method.

```ord``` function is to convert a character to its equivalent integer representation.
```chr``` function is to convert the integer to its character representation.

random.choice() method randomly picks a character from a series of characters to form a string of N length, this is the key for encryption and decryption.

A message is taken from user’s input, for each character in a message it is mapped together with a character of a key with the zip function.
The zip object is a collection of a message’s character and key’s character pair, each pair is exclusively ORed and form a string.

itertools.cycle() method is to cycle through the key string, hence there is no need to check the length of the key string.

Without itertools.cycle() the key string length has to be more than or equal to the message otherwise the message will not be fully encrypted causing a lost of original message.

This is a simple demonstration if the key string length is shorter than the message length.

```
key = "secretkey"
message = "this is my message, see if it can be encrypted completely."

cipher_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(message, key))
print(cipher_text)
plain_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(cipher_text, key))
print(plain_text)
```

The result is like this


With itertools.cycle the characters of the key string will be re-cycled until the entire message is completed.


```
from itertools import cycle

key = "secretkey"
message = "this is my message, see if it can be encrypted completely."

cipher_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(message, cycle(key)))
print(cipher_text)
plain_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(cipher_text, cycle(key)))
print(plain_text)
```

The result is the entire message is encrypted and preserved after decryption.




Package of all the functions to encrypt and decrypt message.
```
from itertools import cycle
import random
import string

# The string of lower and upper case alphabets and all digits.
str_types = string.ascii_lowercase + string.ascii_uppercase + string.digits
# tuple of errors.
errors = IOError, OSError


def xor_fn(message, cipher_key):
    """
    This is an Exclusive OR function
    :param message:
        plaintext or cipher text.
    :param cipher_key:
        key chosen by create_key function.
    :return:
        return a string either cipher text or plain text.
    """
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(message, cycle(cipher_key)))


def create_key(key_len=1024):
    """
    Create a key string picked from str_types object.
    :param key_len:
        The length of the key string, default is 1024 bytes.
    :return:
        return key string.
    """
    return "".join(random.choice(str_types) for _ in range(0, key_len))


def write_file(filename, data):
    """
    Write the string to file
    :param filename:
        filename
    :param data:
        the data to be written to the file.
    :return:
        Status.
    """
    try:
        with open(filename, "w") as file:
            file.write(data)
        print(f"{filename} is written successfully.")
        return True
    except errors as e:
        print(e)
        return False
    except:  # Generic errors that are not expected.
        print(f"Unknown error has occurred while writing to {filename}.")
        return False


def read_file(filename):
    """
    Open the specified file and read its contents.
    :param filename:
        filename
    :return:
        contents from the file.
    """
    try:
        with open(filename, "r") as file:
            data = file.read()
        return data
    except errors as e:
        print(e)
    except:  # Generic errors that are not expected.
        print(f"Unknown error has occurred while reading {filename}.")
```

So here is the example code that creates the key file, and then prompts user to enter a message for encryption, then after that decrypts the message.

```
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

```

So here is the result, as there is no key yet, a key is created on the first run.




The secret key string is this 
NRkjYdXVhoXfommw72dgEPd6SBrtalrtPCKitoz5Gw6uGJNVa2oCRQVaZo3a5UjO83MgcCkiXVbImr48cVIoXpGoOEsM2hx2BGFQpk7kc4SQz1CQFKXeMf6JESS81yv5ioNnF0J1R7prRKdjcRMExO0VA7OAjZX3mYCkjb4PKXj5hr6bo14PzW0Lp3G9h3gK2NKjKvOy4k7gjOinOVkrBtJOts1oZNkMTZATvh6yVghNcj3GW6rtPXYOGABtzv8g9zutLxX95vVwY6ZeA0Gi6FcNqWyYDegR3kiPSVlTZ5kd4pwV5eeFqNHQsuTo0uIP4h39bHwrk6wIMS8K04BhKM9iLWtecs1ievlP3pGgdA7spyDneUfwZMxHrMPyfaUMp3zBxzvbmstktjl6iCSjpEsMsF8HUAEzkuRzf5aGRgxewaXYwiyM7eGGpo08m6GHPENvGy5Io3Uey6SIdt4V1CYnGPsqEkhH16AE33LRkXaJ3vHkC6oanev0Wm0ddJZmdGBl6Fsb2VIGS8yAfQwVYcg7HhtmZzWw7C8FZHYPHQOdk2iglSeGCKWatIBS6Mwza35qZFb8jflyMwShosKbfB0FJyHdpQezMzLw2aZsgUuGtpRCPHY25E5YUCoyjq7vRNU6RJh0vh8gyKy6dGz2zYhtK67ABqXIY3vJjhVGbaFmiBSWoWWFoIe2qNCzbgPlWybUKD1TyFR7SGlNP7aa9L2qwCjgT04VwnDtCHWp7J9JOfP5bEmVaNXidM9HdKHzE9VhninFXX6Kow3hAJZrorg5fdKCXVr9LhOQ14MoggfrYV6wMTVfraAjkmk71yuuLOEFIK4S66ylLXadXq1L1oKBVnQWCaLnBt72pHMhfLCeuzQgrVGT0nVLOOkrGwPFnxW4ChXw1191FJ9oz7qPMCGXiPxwjFkDSaBF6W0lmRyCEDcbmpa1c3kxBK2Hq7HSF7sFn11dssMWHnn14TK1fuP0EQX02iisYeezOetYV3hmqF9yp9YNTh9O2xVg50go
which is 1024 characters Long.

On the second run a prompt appears to get the message input from user then it encrypts and decrypts with the key file.

