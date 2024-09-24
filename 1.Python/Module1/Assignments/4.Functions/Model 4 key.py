# MODULE – 4 ASSIGNMENT KEY

###  Write a Python function to find the Max of three numbers.

n1=int(input("Enter first number: "));
n2=int(input("Enter second number: "));
n3=int(input("Enter Third number: "));
def f():
    if(n1>=n2) and (n1>=n3):
        l=n1
    elif(n2>=n1) and (n2>=n3):
         l=n2
    else:
         l=n3

    print("Largest number among  the three is",l)

f()

### Write a Python function to sum all the numbers in a list.

def sum_list(numbers):
    """
    This function takes a list of numbers as input and returns the sum of all the numbers.
    """
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
    return total

my_list = [1, 2, 3, 4, 5, 'hello']
total = sum_list(my_list)
print(total)  # Output: 15

###  Write a Python function to multiply all the numbers in a list.

def multiply_list(numbers):
    """
    This function takes a list of numbers as input and returns the product of all the numbers.
    """
    product = 1
    for num in numbers:
        if isinstance(num, (int, float)):
            product *= num
    return product

my_list = [1, 2, 3, 4, 5, 'hello']
product = multiply_list(my_list)
print(product)  # Output: 120


