# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:10:15 2019

@author: Hadeel
"""
import statistics as st
import random
import math
from PIL import Image,ImageFilter
from PIL import ImageDraw

#exercise 1 
x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))

print(st.median_high(x))
print(st.median_low(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))

print(st.pvariance(x))

print(st.stdev(x))
print(st.variance(x))

#***************************************************************
#exercise 2
print( random.random() )
print ( random.randrange(10) )
print ( random.choice(['Ali', 'Khaleed', 'Hussam']) )
print ( random.sample(range(1000), 10) )
print ( random.choice('OrangeAcademy') )
items = [1,5,8,9,2,4]
random.shuffle(items)
print ( random.randint(20, 30) )
print ( random.randrange(1000,2111,5))
print  ( random.uniform(10000, 11000))

#***************************************************************
#exercise 3
print ('pi: %.40f' % math.pi) 
n=30
print ('arcsine(%.1f)    = %5.2f' % (n, math.sin(n)))
n=200
print ('arccosine(%.1f)  = %5.2f' % (n, math.cos(n)))
n=180
print ('arctangent(%.1f) = %5.2f' % (n, math.tan(n)))
n = 10.8
print(math.floor(n))
print(math.ceil(n))
#***************************************************************
#exercise 4 
originalOne = Image.open("one.JPG")
originalTwo = Image.open("two.JPG").resize(originalOne.size)
"""
originalOne.show()
originalTwo.show()
"""
print(originalOne.format,originalOne.size,originalOne.mode)

trans1=originalOne.transpose(Image.FLIP_TOP_BOTTOM)
trans2=originalTwo.transpose(Image.FLIP_TOP_BOTTOM)
"""
trans1.show()
trans2.show()
"""
grey1=originalOne.convert('L')
grey2=originalTwo.convert('L')
"""
grey1.show()
grey2.show()
"""
crop1=originalOne.crop((0,0,50,50))
crop2=originalTwo.crop((0,0,50,50))
"""
crop1.show()
crop2.show()
"""
draw1=ImageDraw.Draw(originalOne)
draw1.line((0,0)+originalOne.size,fill=(255,255,255))
draw1.line((0,originalOne.size[1],originalOne.size[0],0),fill=(255,255,255))
draw1.text((originalOne.size[0]/2- originalOne.size[0]/2,originalOne.size[1]/2+20),"HADEEL",fill=(255,255,0))

draw2=ImageDraw.Draw(originalTwo)
draw2.line((0,0)+originalTwo.size,fill=(255,255,255))
draw2.line((0,originalTwo.size[1],originalTwo.size[0],0),fill=(255,255,255))
draw2.text((originalTwo.size[0]/2- originalTwo.size[0]/2,originalTwo.size[1]/2+20),"HADEEL",fill=(255,255,0))
"""
originalOne.show()
originalTwo.show()
"""
edge1enh=originalOne.filter(ImageFilter.EDGE_ENHANCE)
edge2enh=originalTwo.filter(ImageFilter.EDGE_ENHANCE)
"""
edge1enh.show()
edge2enh.show()
"""
find1edg=originalOne.filter(ImageFilter.FIND_EDGES)
find2edg=originalTwo.filter(ImageFilter.FIND_EDGES)
"""
find1edg.show()
find2edg.show()
"""
sm1=originalOne.filter(ImageFilter.SMOOTH)
sm2=originalTwo.filter(ImageFilter.SMOOTH)
"""
sm1.show()
sm2.show()
"""
sh1=originalOne.filter(ImageFilter.SHARPEN)
sh2=originalTwo.filter(ImageFilter.SHARPEN)
"""
sh2.show()
sh1.show()
"""
alpha=0.5
Image.blend(originalOne,originalTwo,alpha).save("newBlend.JPG".format(alpha))
im=Image.open("newBlend.JPG")
"""
im.show()
"""
fil1=originalOne.filter(ImageFilter.BLUR)
fil2=originalTwo.filter(ImageFilter.BLUR)
"""
fil1.show()
fil2.sho2()
"""
size=(128,128)
saved1="thumb1.jpg"
saved2="thumb2.jpg"

originalOne.thumbnail(size)
originalOne.save(saved1)

originalTwo.thumbnail(size)
originalTwo.save(saved1)
"""
originalOne.show()
originalTwo.show()
"""
rot1=originalOne.rotate(90)
rot2=originalTwo.rotate(90)
"""
rot1.show()
rot2.show()
"""
mask=Image.open("ozHM5.JPG")
mask=mask.resize("originalOne")
Image.composite(originalOne,originalTwo,mask).save("new.JPG")
im=Image.open("new.JPG")
"""
im.show()
"""

#***************************************************************
