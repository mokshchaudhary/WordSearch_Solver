import cv2
import numpy as np
import pytesseract
from termcolor import colored

print()

# Image Processesing
img = cv2.imread("sample.png")
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img, (0,0), fx=2.5, fy=1.5)

# OCR 
r= pytesseract.image_to_string(img,config= '--psm 6 -l eng -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
r=r.replace(' ','')

# To find
to_find=["apple",'lemon',"banana","lime","orange","watermelon","grape","kiwi","strawberry","raspberry"]
to_find=[x.upper() for x in to_find]

# Real
print("=========== Real ===========",end='\n\n')
print(r.replace('',' '),end='\n\n')

# Horizontal Solve
print("======== Horizontal ========",end='\n\n')
h=r
for i in to_find:
    h=h.replace(i,'*'*len(i))
print(h.replace('',' '),end='\n\n')

# Vertical Solve



    