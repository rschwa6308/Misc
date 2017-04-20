#program takes string input, encode it into numerical ascii, and embedds it in an image
import math,os
import numpy as np
from Tkinter import *
from tkFileDialog import *
from PIL import Image


#get_ascii takes a string and returns a list of ascii values

def get_ascii(string):
    z = []
    for l in string:
        z.append(ord(l))
    return z


#get_string takes a list of ascii values and returns a string

def get_string(ascii):
    z = []
    for n in ascii:
        z.append(chr(n))
    return "".join(z)
    

#to_hex takes a list of deciaml numbers and returns a list of hexadecimal numbers

def to_hex(dec):
    z = []
    for n in dec:
        z.append(hex(n))
    return z




##print get_ascii("Hello")





#get_array takes a string as an input and returns a 3d image array where every row has 8 letters and each letter corresponds to 1 pixel (greyscale)

def get_array(string):
    ascii = get_ascii(string)
    #ascii = to_hex(ascii)
    
    width = int(math.floor(math.sqrt(len(ascii))))
    print width

    #build empty array
    h = int(math.ceil(float(len(ascii))/width))
    array = np.zeros((h,width,3),dtype=np.uint8)
    #print array

    #fill array
    for i in range(len(ascii)):
        array[int(math.floor(float(i)/width)),i%width] = ((ascii[i],ascii[i],ascii[i]))

    #add spaces at end of array to rectangularize
    last = len(array)-1
    for i in range(width-len(array[last])):
        array[last].append((0,0,0))
        
    return array



#string = "this is a long test string"
#print get_ascii(string)
#print ""
#for row in get_array(string):
#    print row




def openFile():
    root = Tk()
    txt = askopenfilename()
    root.destroy()
    return txt


#create array from input string
choice = raw_input("Enter S for manual string entry or T for text file.").upper()

if choice == "S":
    string = raw_input("Enter String to be Embedded:\n")
else:
    string = open(openFile()).read()
    
array = get_array(string)
print array



#create image from array

image = Image.fromarray(array,'RGB')





#non-Tkinter code

##dest = os.path.split(os.path.abspath(__file__))[0]
##dest = os.path.join(dest,"outputs")
##dest = dest + "\\" + string[:15] + ".png"
##image.save(dest)


#Tkinter code

#get destination filename
root = Tk()

##photo = ImageTK.PhotoImage(image)
##TKinter.Label(root, image=photo).pack()

folder = os.path.join(os.path.split(os.path.abspath(__file__))[0],"images")
dest = asksaveasfilename(filetypes=[("image",".png")], initialdir=folder, defaultextension="png", initialfile=string[:15])
root.destroy()

#save image
image.save(dest)














