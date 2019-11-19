# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:21:54 2019

@author: Hadeel Fleifel
"""

# exercise 1

print('Hello\n \t Hello \n \t \t Hello')

#-----------------------------------------------
# exercise 2

print("Orange Academy \n"*20 )

#-----------------------------------------------
# exercise 3

x=float(1)
print(x)
#1.0

y=float(2.8)
print(y)
#2.8

z=float("3")
print (z)
#3.0

w=float("4.2")
print(w)
#4.2

print(x,y,z,w,sep='10')
#1.0102.8103.0104.2

#-----------------------------------------------
# exercise 4
"""
ProductOne=int(input("Enter Your Value :"))
ProductTwo=int(input("Enter Your Value :"))

print(ProductOne)
print(ProductTwo)
"""

#-----------------------------------------------
# exercise 5
"""
A=int(input("Number One:"))
B=int(input("Number Two :"))
C=int(input("Number Three :"))
D=int(input("Number Four :"))
E=int(input("Number Five :"))

sumation = A+B+C+D+E
avg=sumation /5

print (avg)
"""
#-----------------------------------------------

# exercise 6


x=1
print(type(x))
#<class 'int'>

y=2.8
print(type(y))
#<class 'float'>

z=1j
print(type(z))
#<class 'complex'>

o="Orange"
print(type(o))
#<class 'str'>

A=True
print(type(A))
#<class 'bool'>

#-----------------------------------------------
# exercise 7

x,y="Orange",1
print(x)
#Orange

print (y)
#1

x1,y1=100,-10
print(x1)
#100

print(y1)
#-10

#-----------------------------------------------
# exercise 8
"""
5x=10
print (5x)
#invalid syntax
#x=10 or x5=10
#cant start var. name with number
"""

"""
X_q$="Orange"
print(X_q$)
#invalid syntax
#X_q="Orange"
#cant use $
"""
"""
A B =14
print(A B)
#invalid syntax
#AB =14
#cant use $=space between characters
"""

print("10"*10)
#No error Here
#print the string 10 for 10 times


#-----------------------------------------------
# exercise 9

x,y="Orange",1
print(x)
#Orange

print (y)
#1

x1,y1=100,-10
print(x1)
#100

print(y1)
#-10


#-----------------------------------------------
# exercise 10


"""
5x=10
print (5x)
#invalid syntax
#x=10 or x5=10
#cant start var. name with number
"""

"""
X_q$="Orange"
print(X_q$)
#invalid syntax
#X_q="Orange"
#cant use $
"""
"""
A B =14
print(A B)
#invalid syntax
#AB =14
#cant use $=space between characters
"""

print("10"*10)
#No error Here
#print the string 10 for 10 times


#-----------------------------------------------
# exercise 11

print("Hello,World!")
#Hello,World!

print("Cheera,Mate!")# This is the program
"""Testing
The Code
"""
#Cheera,Mate!

#-----------------------------------------------
# exercise 12
"""
Name=input("Your Name:")
Age=int(input("Your Age:"))

print(Name,"Your Age Will be 100 after",100-Age,"Years")

"""
#-----------------------------------------------
# exercise 13

Base=int(input("Triangle Base: "))
Height=int(input("Triangle Height: "))

triangleArea=0.5*Base*Height

print("Triangle Area is ",triangleArea)


#-----------------------------------------------
# exercise 14

x=11
y=3
print(x+y)
#14

print(x-y)
#8

print(x*y)
#33

print(x/y)
#3.6666666666666665

print(x//y)
#3

print(x%y)
#2

print(abs(x*-1))
#11

print(int(x))
#11

print(float(x))
#11.0

print(divmod(x,y))
#(3, 2)

print(pow(x,y))
#1331

print(x**y)
#1331

print(x>y)
#True

print(x==y)
#False

print(x!=y)
#True

