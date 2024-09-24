# Operators

####    
#A. Write an equation which relates   399, 543 and 12345 
#B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—How would you justify it.


##### A. Write an equation which relates   399, 543 and 12345 

# One possible solution is, if 12345 is divided by 543 we get a remainder as 399 and quotient as 22.

a = 399 
b = 543
c = 12345

equation = 22 * b + a
print(equation)

print(equation == c)

# Hence it is valid relation

##### “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—How would you justify it.

# Divide 5 by 3 using integer division
result1 = 5 // 3
print(result1)  # Output: 1



# Divide -5 by 3 using integer division
result2 = -5 // 3
print(result2)  # Output: -2


# 

### 2.         ________________a=5,b=3,c=10.. What will be the output of the following:
#A. a/=b
#B. c*=5  


a = 5
b = 3
c = 10

#####   A. a/=b

a = a / b
print(a)

#####  B. c*=5  

c = c * 5
print(c)

# 

# 3.
###     A. How to check the presence of an alphabet "s" in word "Data Science".
###     B. How can you obtain 64 by using number 4 and 3.

##### How to check the presence of an alphabet "s" in word "Data Science".  

word = "Data Science"
word.find("S")

##### How can you obtain 64 by using number 4 and 3.

# 64 is cube of 4
a = 4 ** 3
print(a)


