#!/usr/bin/python3

  # caesar cipher


def caesar_cipher(message, key):
    # variable storing the encrypted message
    enc_msg = ''

    for i in message:
        if i.isalpha():
            number = ord(i)
            number += key
            if i.isupper():
                if number > 90:
                    number -= 26
            else:
                if number > 122:
                    number -= 26
            enc_msg += chr(number)
        else:
            enc_msg += i
    return enc_msg

print("Give me your message.")
message = input()
print("Give me your key.")
key = int(input())

print("Your encrypted message is:")
print(caesar_cipher(message, key))