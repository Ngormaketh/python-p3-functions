#!/usr/bin/env python3

class Greeter:
    def greet_programmer(self):
        print("Hello, programmer!")

    def greet(self, name):
        print(f"Hello, {name}!")

    def greet_with_default(self, name="programmer"):
        print(f"Hello, {name}!")

    def add(self, num1, num2):
        return num1 + num2

    def halve(self, number):
        if not isinstance(number, (int, float)):
            return None
        return number / 2
