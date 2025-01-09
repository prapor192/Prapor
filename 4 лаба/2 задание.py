def greet(mymodule):
    print("Hello, " + mymodule + "!")

class Person:
    def __init__(self, mymodule):
        self.mymodule = mymodule

    def say_hello(self):
        print("Hello, my name is " + self.mymodule)
import mymodule
mymodule.greet("Alice")
person = mymodule.Person("Bob")
person.say_hello()