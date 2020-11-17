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