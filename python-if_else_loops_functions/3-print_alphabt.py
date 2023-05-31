#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    letter = chr(i)
    if letter != 'q' and letter != 'e':
        print(letter, end='')
