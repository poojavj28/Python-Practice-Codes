'''
try: Used to keep the logic in which we may get some error

except: Will be executed when exception occures in try block logic

else: Will be executed when try block logic executed without any error.

finally: will always executed irrespective of exception occured or not.
'''

def disp(a,b):
    try:
        print("Task Started")
        print(a/b) # ZeroDivisionError: division by zero
    except:
        print("Some error Handled")
    else:
        print("Task Executed without any exception.")
    finally:
        print("Task Ended")
disp(10,2) 
disp(10,0) 
disp(5,2) 



'''
OutPut:
Task Started
5.0
Task Executed without any exception.
Task Ended
Task Started
Some error Handled
Task Ended
Task Started
2.5
Task Executed without any exception.
Task Ended
'''