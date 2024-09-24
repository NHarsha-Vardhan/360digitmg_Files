isalnum()
isdigit()
isalpha()
capitalize()
center()
replace()
count(),lower(),upper(),len()
##################
total = string.count(substring,7,9)

print(total)
com = complex(3,2)
print(com)

x= [1,2,3,4,1]

y= tuple(x)
y
fSet.next()

score = 500
money = 60000
age = 65

if score >100:
    print("You have good points")
    if money>=500:
        print("You won")
        if age >= 30:
            print("You are middle age person")
        else:
            print("You are having Young age person")
    else:
        print("You have high points but dont have emough ,money")
else :
    print("You are losser")
    
def fact(N):
    if N<0:
        print("Input the positive number")
    elif N==0:
        print(f'Factorial of {N}! is {1}!')
    else:
        fact =1
        for i in range(1,N+1):
            fact *= i
        print(f"Factorial of {N}! is {fact}")

fact(5)        


def fact(N):
    if N<0:
        print("Input the positive number")
    elif N==0:
        print(f'Factorial of {N}! is {1}')
    elif N==1:
        return 1
    else:
        return (N* fact(N-1))
    
        
        
val1 = tuple([1,2,3,4,5,6])    

a_1 = list(map(lambda x: x*2,val1))
print(a_1)


a_2 = list(filter(lambda x:x%2==0 ,val1))
print(a_2)
import numpy as np
a= [1,2,2,3]
c= np.unique(a)
c
######
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_excel(r'F:\Liser Time\360digitmg\4.PowerBI\Data sets for sessions\data sets for sessions\Superstore_dataset.xlsx')
data.describe()
data.info()


plt.figure(figsize=[12,8])
'''sns.barplot(x="Class",y="ShapeFactor1",data=data)'''
sns.barplot(data=data,y="Profit",x="Segment",hue=None)
plt.show()

a= data.value_counts()
a.describe()
a.shape
a.info()
data.info()


b = pd.DataFrame(data= a)
b.info()
b.shape()
data.describe().T


    
             