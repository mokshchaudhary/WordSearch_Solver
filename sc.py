import cv2
import numpy as np
import pytesseract
from termcolor import colored

def invert(v):
  r=["" for x in range(len(v[0]))]
  for i in range(len(v[0])):
    for k in range(len(v)):
      r[i]=r[i]+v[k][i]
  return r

con = r'--psm 6 -l eng -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ'
img = cv2.imread("3.png")
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img, (0,0), fx=2.5, fy=1.5)

result= pytesseract.image_to_string(img,config= con)
a=result
a=a.replace(' ','')

to_find=["apple",'lemon',"banana","lime","orange","watermelon","grape","kiwi","strawberry","raspberry"]
to_find=[x.upper() for x in to_find]
#rint(to_find,end='\n\n\n')
data = np.zeros((14,14),dtype='int')

v=invert(a.split('\n'))
z=np.array(v)
b=""
for i in v:
  b=b+i+"\n"

for i in to_find:
  b=b.replace(i,'0'*len(i))
for i in to_find:
  a=a.replace(i,'0'*len(i))

print(b)
print("1 ===============================================")
c=''
for x in invert(a.split('\n')):
  c=c+x+"\n"
print(c)
print("2 ===============================================")
print(data)
print("3 ===============================================")
print(np.array(list(c)))
print("4 ===============================================")
print(np.char.rsplit(np.array(c),sep='\n'))
