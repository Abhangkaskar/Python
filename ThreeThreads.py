import threading
import time

def thread_function():
    print("Thread is running")
    time.sleep(2)
    print("Thread has finished")

thread = threading.Thread(target=thread_function)

print("Thread active before starting:", thread.is_alive())

thread.start()

print("Thread active after starting:", thread.is_alive())

thread.join()

print("Thread active after joining:", thread.is_alive())
