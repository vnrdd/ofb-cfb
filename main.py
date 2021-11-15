import ofb
import cfb
import random
from PIL import Image
from util import *

BLOCK_SIZE = 2
random.seed("i_am_seed_from_ice_age")

if __name__ == '__main__':
    source_image = Image.open('data/res.bmp', 'r')
    
    image_in_bytes = image_to_bytes(source_image)
    
    image_in_bytes = corrupt(image_in_bytes, 3)
    
    encrypted = cfb.decrypt(image_in_bytes, BLOCK_SIZE=BLOCK_SIZE)
        
    final_image = bytes_to_image(source_image, encrypted)
    final_image.save('data/res2.bmp')
    