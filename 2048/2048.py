from PIL import Image


for k in range(1,17):
    im = Image.open(str(2**k)+'.png') # Can be many different formats.
    pix = im.load()
    #print(im.size)
    F = open(str(2**k)+'.txt','w')
    for i in range((im.size)[0]):
        for j in range((im.size)[1]):# Get the width and hight of the image for iterating over
           F.write((str(min(pix[i,j],1))).rstrip('\n'))  # Get the RGBA Value of the a pixel of an image
