import threading
def print_numbers():
    for i in range(10):
        print(f"Thread {threading.current_thread().name}: {i}")
        
thread1=threading.Thread(target=print_numbers,name="Thread 1")        
thread2=threading.Thread(target=print_numbers,name="Thread 2")  

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Completion of the execution of the program")