#!/usr/bin/python3

  # caesar cipher
  # Message to cipher
print("Give me your message.")
message = input()
print("Give me your key.")
key = int(input())
  # variable storing the encrypted message
enc_msg = ''
for i in message:
    number = ord(i)
    number += key
    if i.isupper():
        if number > 90:
            number -= 26
    else:
        if number > 122:
            number -= 26
    enc_msg += chr(number)

print("Your encrypted message is:", enc_msg)