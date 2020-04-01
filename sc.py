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
img = cv2.imread("sample.png")
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img, (0,0), fx=2.5, fy=1.5)

r= pytesseract.image_to_string(img,config= con)
r=r.replace(' ','')

to_find=["apple",'lemon',"banana","lime","orange","watermelon","grape","kiwi","strawberry","raspberry"]
to_find=[x.upper() for x in to_find]
#rint(to_find,end='\n\n\n')

vr=''
hr=r
for i in invert(r.split('\n')):
  vr=vr+i+"\n"

print(r)
print("1 ================================================")
for i in to_find:
  vr=vr.replace(i,'*'*len(i))
for i in to_find:
  hr=hr.replace(i,'*'*len(i))

print(vr)
#print("2 ===============================================")
c=''
for x in invert(vr.split('\n')):
  c=c+x+"\n"
vr=c
print(vr)
#print("3 ===============================================")


f=r
f=list(f)
for i in range(len(f)):
  if not hr[i]==vr[i]:
    f[i]='*'

for i in f:
  print(i,end=' ')