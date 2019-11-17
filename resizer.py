## Bulk image resizer

# This script simply resizes all the images in a folder to one-eigth their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: place this script in a folder of images you want to shrink,
# and then run it.

import glob
from PIL import Image
import os

class_name = 'disease'

os.mkdir('images')
file_list = sorted(glob.glob('*.jpg'))
for idx,file_name in enumerate(file_list):
    im = Image.open(file_name)
    new_width = 640
    new_height = 480
    im = im.resize((new_width,new_height), Image.ANTIALIAS)
    im.save('images/' + class_name + '_' + str(idx+1).zfill(3) + '.jpg')