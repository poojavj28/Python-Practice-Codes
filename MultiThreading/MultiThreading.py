import threading
import time
print(threading.current_thread())
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def displayDigit(li1):
    print(t1.is_alive())
    print(threading.current_thread())
    for i in li1:
        print(i)
        time.sleep(2)

def displayLetters(li2):
    print(threading.current_thread())
    for i in li2:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=displayDigit,args=(li1,),name="Tester")
t2 = threading.Thread(target=displayLetters,args=(li2,),name="Developer")

print(t1.is_alive())

t1.start()
t1.join()     # it will first complete the first task then it will continue the next task if we not give as join it will excute first task if if it stuck some where the second task will execute
print(t1.is_alive())
t2.start()