##### 1)  Write the code in python to open a file named “try.txt” 

# Open a file named "try.txt" in write mode
file = open("try.txt", "w")

# Open a file named "try.txt" in the current directory
file = open("try.txt")

# Remember to close the file when you're done with it
file.close()    

##### 2)    What is the purpose of ‘r’ as prefix in the given statement? 
#         f = open(r,“d:\color\flower.txt”)

# In the given statement, the use of "r" as a prefix before the file path string indicates that the string should be treated as a "raw string".

# In Python, backslashes (\) have a special meaning in strings, as they can be used to represent escape sequences that have a special meaning, such as newline (\n) or tab (\t). For example, the string "hello\nworld" would represent a string with the word "hello" followed by a newline character and the word "world".

# However, if you want to include backslashes in a string without them being interpreted as escape sequences, you can use a "raw string" by prefixing the string with an "r" character. In a raw string, backslashes are treated as literal characters, and do not have any special meaning.

# For example, in the code:

# python

f = open(r"d:\color\flower.txt")

# The r before the string "d:\color\flower.txt" tells Python to treat the string as a raw string, so that the backslashes are not interpreted as escape sequences. This is useful when dealing with file paths in Windows, as file paths in Windows typically use backslashes to separate directory and file names.

# I hope this helps! Let me know if you have any further questions.

##### 3)  Write a note on the following
    #Purpose of Exception Handling
    #Except block
    #Else block
    #Finally block
    #Bulit-in exceptions


###### Purpose of Exception Handling
#Exception handling is a programming construct that allows developers to handle runtime errors that may occur during program execution. The purpose of exception handling is to gracefully handle runtime errors and prevent them from crashing the program or causing data loss. Exception handling involves writing code to handle specific types of errors, or exceptions, that may occur during program execution.

###### Try block
#The try block is a section of code that is used to enclose code that may raise an exception during program execution. The code inside the try block is executed normally, and if an exception occurs, it is caught by the except block.

###### Except block
#The except block is a section of code that is executed if an exception is raised in the try block. The except block is used to handle specific types of exceptions by providing code to handle the error or provide a message to the user. If no exception occurs in the try block, the except block is skipped.

###### Else block
#The else block is a section of code that is executed if no exception is raised in the try block. The else block is typically used to provide code that should be executed if the code in the try block is successful.

###### Finally block 
#The finally block is a section of code that is always executed, regardless of whether an exception occurs in the try block. The finally block is typically used to provide cleanup code, such as closing files or releasing system resources.

###### Built-in exceptions
#Python provides a number of built-in exceptions that can be raised during program execution. These exceptions are predefined error types that can be caught and handled using exception handling. Examples of built-in exceptions include ValueError, TypeError, NameError, IndexError, and KeyError, among others. By handling these exceptions, developers can ensure that their programs are robust and can recover from runtime errors.

### 4) Write 2 Custom exceptions


###### 1. "InvalidInputError:"
#This exception can be used to handle cases where the input provided by the user is invalid. For example:

class InvalidInputError(Exception):
    pass

def get_user_age():
    age_str = input("Enter your age: ")
    try:
        age = int(age_str)
        if age < 0:
            raise InvalidInputError("Age cannot be negative.")
        return age
    except ValueError:
        raise InvalidInputError("Invalid age entered: '{}'".format(age_str))

try:
    age = get_user_age()
    print("Your age is:", age)
except InvalidInputError as e:
    print("Invalid input:", str(e))

#In this example, we define a custom exception InvalidInputError, which is raised if the user enters an invalid age (either a non-integer or a negative integer). We then define a function get_user_age() that prompts the user to enter their age, and handles any exceptions that may occur while converting the input to an integer. If an exception occurs, we raise an InvalidInputError with an appropriate error message. Finally, we use a try-except block to handle any InvalidInputErrors that may occur when calling get_user_age().

###### 2. "FileNotFoundError": 
#This exception can be used to handle cases where a file could not be found. For example:

class FileNotFoundError(Exception):
    pass

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError:
        raise FileNotFoundError("File not found: {}".format(filename))

try:
    contents = read_file("my_file.txt")
    print(contents)
except FileNotFoundError as e:
    print("Error reading file:", str(e))

#In this example, we define a custom exception FileNotFoundError, which is raised if the file specified by filename cannot be opened for reading. We then define a function read_file() that attempts to open the file specified by filename, and raises a FileNotFoundError if an exception occurs. Finally, we use a try-except block to handle any FileNotFoundErrors that may occur when calling read_file().

