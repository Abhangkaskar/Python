from time import sleep
from threading import *
class Program1(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)
            
class Program2(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
            
class Program3(Thread):
    def run(self):
        for i in range(5):
            print("Hey")
            sleep(1)
                        
t1 = Program1()
t2 = Program2()
t3 = Program3()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("Bye")