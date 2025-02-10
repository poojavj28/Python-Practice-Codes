import threading
import time

def background_tasks():
    print(threading.current_thread())
    while True:
        print("Background task running...")
        time.sleep(1)

thread = threading.Thread(target=background_tasks,name="Daemon")
thread.daemon = True
thread.start()
time.sleep(2)

print("Main Thread is Dead.")