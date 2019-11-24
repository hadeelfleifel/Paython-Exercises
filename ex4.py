# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:02:19 2019

@author: Hadeel Fleifel
"""
#exercise 1
o=lambda x=1,y=2,z=3:x+y+z
print(o())
# 6
print(o(10))
#15
print(o(10,20))
print("******************************")


#----------------------------------------
#exercise 2
"""
def my_function(*x):
    print(x * x)

my_function(9,10)

"""

list=(2,4,5)
def fun(list):
    for x in list:
        print(x*x)
        
fun(list)
    
#----------------------------------------
#exercise 3

print((lambda arg_1, arg_2: arg_1 * arg_2)(2, 3))

#----------------------------------------
#exercise 4

filtered = list( filter(lambda x: x % 2 == 0, range(-5,5)))
print(filtered)

#----------------------------------------
#exercise 5
x=lambda a,b,c:a+b+c
print (x(5,6,2))

"""
 13
"""
print("******************************")

#----------------------------------------
#exercise 6
x=("Joey","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Courtney")
result=list(zip(x,y,z))
print(result)

"""
[('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]
"""
print("******************************")

#----------------------------------------
#exercise 7

coin=("Bitcoin","Ether","Ripple","Litecoin")
code=("BTC","ETH","XRP","LTC")
d=dict(zip(coin,code))
print(d)

"""
{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
"""
print("******************************")
#----------------------------------------
#exercise 8

def fun(variable):
    letters = ['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False


sequence =['g','j','e','j','k','o','p','r']

filtered = list(filter(fun, sequence))
print(filtered)

"""
['e', 'o']
"""

print("******************************")

#----------------------------------------
#exercise 9
"""
x = list(map(int,input('Enter a multiple value:').split()))
print("List of students:",x)
"""
"""
List of students: [1, 20, 10]
"""
print("******************************")

#----------------------------------------
#exercise 10

def newfunc(a):
    return a*a
x= list(map(newfunc,(1,2,3,4)))
print(x)

"""
[1, 4, 9, 16]
"""
print("******************************")
#----------------------------------------
#exercise 11
def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)

"""
[3, 6, 8]
"""

print("******************************")

#----------------------------------------
#exercise12

c=map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))

"""
[6, 8]
"""
print("******************************")

#----------------------------------------
#exercise 13

c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))

"""
[4, 6, 8]
"""
print("******************************")

#----------------------------------------
#exercise 14
import functools
MyList= [2,3,4,10,13,22,25,100,120]
print (functools.reduce(lambda a,b: a if a < b else b,MyList))
print("******************************")

#----------------------------------------
#exercise 15
numbers=[1,2,3]
letters=["a","b","c"]

print(list(zip(numbers,letters)))