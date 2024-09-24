# 1. Write the code in python to open a file named “try.txt”
file_path = "F:/Liser Time/360digitmg\Python/Module1/Assignments/Module 5 File_Exception handling/try.txt"

try:
    with open(file_path,mode = "r") as file:
        print(file.readlines())
except FileNotFoundError:
    
    print(f"Error: The file '{file_path}' was not found.")
    


file.close()

# 2. )What is the purpose of ‘r’ as a prefix in the given statement? 
     '''f = open(r, “d:/color/flower.txt”) '''

the purpose of 'r' denotes raw string which is denote before the string 
e.g: f= open(r"d:/color/flower.txt", "mode")

we can denote the mode in read format as mentioned in below example:
    
e.g: f= open(r"d:/color/flower.txt", mode="r")

#3. Write a note on the following
'''A.Purpose of Exception Handling :'''
    By using the exception handling we easily identify syantical errors and exceptions by using try and except block.
    
'''B.Try block '''
    Normal block of code is mentioned in the try block and if any exception is exist in try block then it will move to except
    block.
    try:
        # block of try code

'''C.Except block '''
    Exception related code is mention in the except block. 
    except:
        # except block code
'''D.Else block'''
    If the code is executed in try block if no exception is raised then it will executed.
    
    try:
        #block of code
    except:
        # except block
    else:
        #else block
'''E.Finally block'''
    The purpose of finally block is used to execute at every time when we excute try block
    
    finally:
        #final block code
        
'''F.Built-in exceptions'''
    Bulid in functions are pre defined functions in python.
    
    print(dir(locals()['__builtins__']))
    
# 4. Write 2 Custom exceptions

a. FileNotFoundError 
b. ZeroDivisionError 
