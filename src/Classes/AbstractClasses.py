from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("It's running")


class Whiteboard(Computer):
    def write(self):
        print("It's writing")

    def process(self):
        print("Process inherited")


class Programmer:
    def work(self, com):
        print("Solving bugs")
        com.process()


laptop = Laptop()
whiteboard = Whiteboard()
programmer = Programmer()

programmer.work(whiteboard)
