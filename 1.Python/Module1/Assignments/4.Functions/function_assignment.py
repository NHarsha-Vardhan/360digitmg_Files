#1. 1.Write a Python function to find the Max of three numbers.

def maximum(a,b,c):
    list_1 = [a,b,c]
    return max(list_1)

m = maximum(10, 20, 30)    
print(m)

#2.Write a Python function to sum all the numbers in a list.

def addition(a,b,c):
    list_1 = [a,b,c]
    return sum(list_1)

ad = addition(10, 20.6, 30)    
print(ad)

#3. Write a Python function to multiply all the numbers in a list.

def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
numbers_list = [2, 3, 4, 5]
result = multiply_numbers(numbers_list)
print("Result:", result)
