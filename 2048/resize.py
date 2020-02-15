#!/usr/bin/env python
from PIL import Image


for k in range(1,17):
    im = Image.open(str(2**k)+'.png') # Can be many different formats.
    image = im.resize((80,80))
    image.save(str(2**k)+'.png')
