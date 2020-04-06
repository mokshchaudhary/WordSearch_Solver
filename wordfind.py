import cv2
import numpy as np
import pytesseract

print() #Print of good luck 
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

#Convert into np matrix def
def st2m(r):
    mat=[] 
    c=list(r.split('\n'))
    for i in c:
        o=list(i.replace('',' ').split(' '))
        o.remove('')
        o.remove('')
        mat.append(o)
    mat=np.array([y for y in mat if len(y)>0])
    return mat

# Horizontal and Vertical
h=np.array(st2m(r))
v=np.transpose(h)

#Array to String def
def tostr(v):
    str=''
    for i in v:
        for x in i:
            str=str+x
        str=str+'\n'
    return str

# Horizontal Solve
hs = tostr(h)
for i in to_find:
    hs=hs.replace(i,'*'*len(i))
hs=st2m(hs)

# Vertical Solve
vs= tostr(v)
for i in to_find:
    vs=vs.replace(i,'*'*len(i))
vs=st2m(vs)
vs=np.transpose(vs)

#Combine Output
f=st2m(r)
for i in range(len(hs)):
    for x in range(len(hs[0])):
        if not hs[i][x]==vs[i][x]:
            f[i][x]='-'

#Print Solution
print(" Solution: ",end='\n\n')
print(tostr(f).replace('',' '))
