#program takes image with ascii embedded as greyscale pixels and returns a string
#from PIL import Image
import numpy as np
from Tkinter import *
from tkFileDialog import *
import os
from PIL import Image
from time import sleep






#to_string actually gets data and converts to a string

def to_string(image):
    data = image.getdata()
    
    data =  list(data)
    
    
    string = ""
    for l in data:
        if l[0] in range(128):
            string = string + chr(l[0])
        else:
            print "contains non-standard character of value " + str(l[0]) + "; was omitted\n"
    
    return string
    
    


#non-Tkinter code

##dest = os.path.split(os.path.abspath(__file__))[0]
##dest = os.path.join(dest,"inputs")
##
##for img in os.listdir(dest):
##
##    #open image
##    image = Image.open(os.path.join(dest,img))
##    
##    #process image
##    print "'" + img + "' says \"" + to_string(image) + "\""
##    print ""
##    print ""



#Tkitner code

#define func to get image filename through GUI
def openFile():
    root = Tk()
    img = askopenfilename()
    root.destroy()
    return img

#open image
img = openFile()
image = Image.open(img)

#process image
print "'" + os.path.split(img)[1] + "' says \"" + to_string(image) + "\""
print ""
print ""

raw_input("")




