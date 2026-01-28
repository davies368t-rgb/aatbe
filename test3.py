from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(ABC):
    def move(self):
        print("I can walk and run")

class Snake(ABC):
    def move(self):
        print("I can crawl")
    
class Dog(ABC):
    def move(self):
        print("I can bark")

class Lion(ABC):
    def move(self):
        print("I can roar")

R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()