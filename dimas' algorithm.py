# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

from PIL import Image
var1 = raw_input("Enter the first's image directory")
var2 = raw_input("Enter second's image directory")

image1 = Image.open(var1)
image2 = Image.open(var2)
if image1.size == image1.size:
    print "Сейчас увидешь, что эта убер-супер дабл камера делает."
else:
    print "Ты какого хуя фотки разного размера кинул?"

r1, g1, b1 = np.array(image1).T     
r2, g2, b2 = np.array(image2).T     
print g1
#Getting the mean of the RGB values
r_out = r1/2+r2/2
g_out = g1/2+g2/2
b_out = b1/2+b2/2

#Forming a new image from the new RGB values
im = Image.fromarray(np.dstack([item.T for item in (r1/2+r2/2,g_out,b_out)]))
im.save('C:/users/timofey/desktop/output.png')
print g_out