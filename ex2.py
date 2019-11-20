# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:31:53 2019

@author: Hadeel Fleifel
"""
#exercise 1 
numberOne=int(input("Enter First Number :"))
numberTwo=int(input("Enter Second Number :"))

if numberOne>numberTwo :
    print(numberOne,"is Greater than ",numberTwo)
else:
    print(numberTwo,"is Greater than", numberOne)

#--------------------------------------------------
#exercise 2

number=int(input("Enter Number :"))
print(number,"* 1 =",number*1)
print(number,"* 2 =",number*2)
print(number,"* 3 =",number*3)
print(number,"* 4 =",number*4)
print(number,"* 5 =",number*5)
print(number,"* 6 =",number*6)
print(number,"* 7 =",number*7)
print(number,"* 8 =",number*8)
print(number,"* 9 =",number*9)


#--------------------------------------------------
#exercise 3 

star="*"
i=1
while i<=5:
    print(star*i)
    i+=1
i-=2
while i>=1:
    print(star*i)
    i-=1
    

#--------------------------------------------------
#exercise 4 

letters =['x','y','z','a','b','c']
for i in letters:
    if i =='a':
        continue
    elif i =='c':
        break
    print(i)
    
"""
x
y
z
b

"""

#--------------------------------------------------
#exercise 5

for x in range (12,25,3):
    print(x)
    
"""
12
15
18
21
24

"""
#--------------------------------------------------
#exercise 6 

i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    
"""
1
2
3

"""

#--------------------------------------------------
#exercise 7 


number=int(input("Enter Number :"))
sumation=0
for i in range(number+1):
    sumation+=i
print(sumation)


#--------------------------------------------------
#exercise 8 


number=int(input("Enter Number :"))
if number%2==0:
    print(number,"is Even")
else:
    print(number,"is Odd")


#--------------------------------------------------
#exercise 9 

for i in range(1, 10):
    for j in range(i,0, -1):
        print(j,end=""),
    print("")
    
for h in range(8,0,-1):
    for k in range(h,0,-1):
        print(k,end=""),
    print("")

"""
for i in range(1,10):
    for j in range (10 - i):
        print(" ",end = " ")
    for j in range(1,i):
        print(j,end=" ")
    for i in range(i,0,-1):
        print(i,end=" ")
    print("\n")
    
"""

#--------------------------------------------------
#exercise 10


while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")

#--------------------------------------------------
#exercise 11

"""
try:
    a=3
    if a<4:
        b=a/(a-3)
        print("Value of b = ",b)
except (ZeroDivisionError,NameError):
    print("\n Error Occurred and Handled")
 """  
# Error Occurred and Handled