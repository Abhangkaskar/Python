import threading
import time

def print_number():
    for i  in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)
        
def print_letter():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)
        
thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished.")