# 1. Take a variable ‘age’ which is of positive value and check the following:
''' a.If age is less than 10, print “Children”.
b.If age is more than 60 , print ‘senior citizens’
c. If it is in between 10 and 60, print ‘normal citizen’ '''

age = int(input("Enter Age:"))

if age < 10:
    print("Children")
elif age>60:
    print("senior citizen")
elif  10 < age < 60:
    print("normal citizen")
    
# 2 . Find the final train ticket 
''' a.If male and sr.citizen, 70% of fare is applicable
b.If female and sr.citizen, 50% of fare is applicable.
c.If female and normal citizen, 70% of fare is applicable
d.If male and normal citizen, 100% of fare is applicable
[Hint: First check for the gender, then calculate the fare based on age factor.. For both Male and Female ,consider them as sr.citizens if their age >=60] '''

age = int(input("Enter Age greater than 10:"))
gender = input("Enter your gender:")
fare = 2000
# checking the citizen based on age
if 10<age<60:
    citizen = "normal citizen"
elif age>60:
    citizen = 'senior citizen'
    
if gender == 'male':
    if citizen == 'normal citizen':
        discount_fare = fare
    elif citizen == 'senior citizen':
        print("70% of fare is applicable")
        discount_fare = fare * 0.7
elif gender == 'female':
    if citizen == 'normal citizen':
        print("70% of fare is apllicable")
        discount_fare = fare *0.7
    elif citizen == 'senior citizen':
        print("50% of fare is applicable")
        discount_fare = fare *0.5
    
    
# 3. Check whether the given number is positive and divisible by 5 or not. 

number = int(input("Enter the number:"))    
divisible = number % 5
if (number>0 and  divisible==0) or (number>0 and divisible !=0):
    print("Entered number is positive and divisible by 5 ")
elif (number<0 and  divisible==0) or (number<0 and divisible !=0) :
    print("Entered number is negative and divisible by 5")
  
  ###############################################################################
'''part - 2  '''
# 1.A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exist in list1.
'''B) How do we create a sequence of numbers in Python?
C)  Read the input from keyboard and print a sequence of numbers up to that number '''
    
list1=[1,5.5,(10+20j),'data science']    
  
print(dir(list1)) # Print default functions and parameters exist

#create a sequence of numbers
print(list(range(1,10)))

# input from keyboard and print a sequence of numbers

num = int(input("enter the number:"))    

sequence = range(num)

print(list(sequence))

#2. 2.Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
#list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
 #Create a dictionary such that list2 are keys and list 1 are values..  
  
list1 = list(range(0,10))
list2 = ['zero','one','two','three','four','five','six','seven','eight','nine']  

list3 = dict(zip(list2,list1))
print(list3)  

#3. Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is an odd number in the list1..    
  
list_1 =  [3,4,5,6,7,8]
 
list2 =[]

for i in list_1:
    if i%2 == 0:
        list2.append(i+10)
    else:
        list.append(i*5)
  
print(list2)    
    
 
  
### 4.Write a simple user defined function that greets a person in such a way that :
'''             i) It should accept both the name of the person and message you want to deliver.
              ii) If no message is provided, it should greet a default message ‘How are you’ '''
    
def greet_person(name, message='How are you'):
     formatted_message = f"Hello {name}, {message}"
     return formatted_message

# Example usage:
person_name = "John"
default_greeting = greet_person(person_name)
custom_greeting = greet_person(person_name, "Have a great day!")

print(default_greeting)
print(custom_greeting) 
    




