# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:33:43 2019

@author: Hadeel
"""

from sympy import *
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
from sympy.plotting import plot3d
import xlsxwriter
from xlrd import open_workbook


#exercise 1 

y,x,z = sym.symbols('y x z')
#A
x = sym.symbols('x')
expr= x**2+x**3+21*x**4+10*x+1
print(expr.subs(x, 7))

#B
print(sym.expand((x + y) ** 2 ))

#C
print(sym.simplify(4*x**3+21*x**2+10*x+12))

#D
print(sym.limit(1/(x**2),x,sym.oo))

#E)
print(sym.summation(2*i+i-1,(i,5,n)))

#F
print(sym.integrate( sin(x) + exp(x)*cos(x)+tan(x),x))

#G
print( sym.factor(x**3+12*x*y*z+3*y**2*z))

#H
print( sym.solveset(x -4, x))

#I
m1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
m2 = sym.Matrix([2, 1, 0])
print(m1*m2)

#J
plot(x**3+3, (x, -10, 10))

#k
x, y = symbols('x y')
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))

#***********************************
#exercise 2 

workbook=xlsxwriter.Workbook("ex10.xlsx")
worksheet=workbook.add_worksheet()
worksheet.autofilter('A1:A4')

data=['This is Example','My first export example',1,2,3]

format=workbook.add_format()
format.set_font_color('red')


worksheet.write_column('A1',data)
#worksheet.write|('A1:1',format)
worksheet.set_row(0,'A',format)
worksheet.set_row(4,'A',format)

workbook.close()

#**************************************
#exercise 3
workbook=xlsxwriter.Workbook('fi.xlsx')
worksheet1=workbook.add_worksheet('sheet1')
worksheet1.autofilter('A1:C2')

worksheet2=workbook.add_worksheet('sheet2')
worksheet2.autofilter('A1:C2')

col1=['Mohammad','Ahlam','Noor']
col2=[1,2,3]
col3=[500,200,400]

worksheet1.write_column('A1',col1)
worksheet1.write_column('B1',col2)
worksheet1.write_column('C1',col3)

coll1=['Shaker','Yasmeen','Haya']
coll2=[1,2,3]
coll3=[600,500,123]

worksheet2.write_column('A1',coll1)
worksheet2.write_column('B1',coll2)
worksheet2.write_column('C1',coll3)

workbook.close()


wb = open_workbook('fi.xlsx')
for s in wb.sheets():
    print ('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print (values,"'")
    
