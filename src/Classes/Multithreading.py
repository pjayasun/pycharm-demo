from time import sleep
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(5):
            print("Inside A")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Inside B")
            sleep(1)

a = A()
b = B()

a.start()
sleep(0.2)
b.start()

# Hey Main Thread wait for the child threads to complete it's process
a.join()
b.join()

print("Bye")
