# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:02:48 2019

@author: Hadeel Fleifel
"""

#exercise 1
list= [1,20,100,5,3,20]
for item in list:
    print(item)
    
print("***********************************************")   

#-----------------------------
#exercise 2

print(sum(list))    
    
print("***********************************************")   
  
#-----------------------------
#exercise 3

print(max(list))
print("***********************************************")   

#-----------------------------
#exercise 4

a = {10,20,30,20,10,50,60,40,80,50,40}
print(a)
print("***********************************************")   

#-----------------------------
#exercise 5

if len(a) == 0:
    print("list is Empty")
else:
    print("list is not Empty")
print("***********************************************")   

#-----------------------------
#exercise 6

tupleList=('Apple', 1, 2, 3, 'a', 'b')
for item in tupleList:
    print(item)

print("***********************************************")   

#-----------------------------
#exercise 7

num_set= set([0, 1, 2, 3, 4, 5])
for item in num_set:
    print(item)
    
print("***********************************************")   

#-----------------------------
#exercise 8   

set1 = {2, 4, 5, 6}  
set2 = {4, 6, 7, 8}  
set3 = {4,8} 
print(set1.intersection(set2))
print(set1.intersection(set2).intersection(set3))

print("***********************************************")   

#-----------------------------
#exercise 9 

setx=set(['green','blue'])
sety=set(['blue','yellow'])
seta=setx|sety
print(seta)
print("***********************************************")   

"""
{'yellow', 'blue', 'green'}

"""
#-----------------------------
#exercise 10
seta=set([5,10,3,15,2,20])
print(len(seta))
print("***********************************************")   
"""
6
"""

#-----------------------------
#exercise 11 

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
print("***********************************************")   

"""
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

#-----------------------------
#exercise 12

a="Hello,World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","J"))
print("***********************************************")   

"""
e
llo
orl
12
hello,world!
Jello,World!

"""









