# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:55:39 2019

@author: Hadeel Fleifel
"""

#exercise 1 
class Employee(object):
    def __init__(self, a, b, c,d,e):
        self.employeeNumber= a
        self.__Name= b
        self.__Address= c
        self.__Salary=d
        self.__jobTitle=e
        
    def getName(self):
        return str(self.__Name)
    
    def getAddress(self):
        return str(self.__Address)
    
    def setAddress(self,address):
        self.__Address=address
    def getSalary(self):
        return float(self.__Salary)
    def getJobTitle(self):
        return str(self.__jobTitle)
    
    def __del__( self):
        print (self.__Name,"has been deleted")
        
e=Employee(1,"Hadeel","Amman",145,"Engineer")
print(e.getName())
print(e.getAddress())
print(e.getSalary())
print(e.getJobTitle())
del e

print("********************")
#********************************************
#exercise 2
employee1=Employee(1,"Mohammad Khalid","Amman,Jordan",500,"Consultant")

employee2=Employee(2,"Hala Rana","Aqaba,Jordan",750,"Manager")

print("********************")

#********************************************
#exercise 3
print(employee1.employeeNumber)
print(employee1.getName())
print(employee1.getAddress())
print(employee1.getSalary())
print(employee1.getJobTitle())
employee1.setAddress("USA")
print("Employee 1 New Address :",employee1.getAddress())

print("--------------------------------------------")
print(employee2.employeeNumber)
print(employee2.getName())
print(employee2.getAddress())
print(employee2.getSalary())
print(employee2.getJobTitle())

print("********************")

#********************************************
#exercise 4
del employee1
print("--------------------------------------------")
del employee2
