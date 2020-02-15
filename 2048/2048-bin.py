#!/usr/bin/env python
from PIL import Image
import struct

for k in range(1,17):
    im = Image.open(str(2**k)+'.png') # Can be many different formats.
    pix = im.load()
    #print(im.size)
    F = open(str(2**k)+'.bin','wb')
    s=''
    c=0
    for i in range((im.size)[0]):
        for j in range((im.size)[1]):# Get the width and hight of the image for iterating over
            if(c!=15):
                s+=str(min(pix[i,j],1))
                c+=1
            else:
                s+=str(min(pix[i,j],1))
                s=s[8:16]+s[0:8]
                F.write(struct.pack('H',int(s[::-1],2)))
                s=''
                c=0
    F.close()
