#!/usr/bin/env python3


class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        print("The dog is sitting.")

    def bark(self):
        print("Woof!")


fido = Dog("Fido")  # Pass the name parameter

fido.sit()
fido.bark()
