import ofb
import cfb
import random
from PIL import Image
from util import *

BLOCK_SIZE = 2
random.seed("i_am_seed_from_ice_age")

def test_OFB(image):
    image_in_bytes = image_to_bytes(image)
    
    encrypted = ofb.OFB(image_in_bytes, BLOCK_SIZE=BLOCK_SIZE)
    
    final_image = bytes_to_image(image, encrypted)
    final_image.save('data/ofb_enc.bmp')
    
    corr_encrypted = corrupt(encrypted, 1)
    decrypted = ofb.OFB(corr_encrypted, BLOCK_SIZE=BLOCK_SIZE)
        
    final_image = bytes_to_image(image, decrypted)
    final_image.save('data/ofb_dec_with_error.bmp')
    
    output(bytearray(image_in_bytes), bytearray(encrypted), bytearray(decrypted), 20)
    
def test_CFB(image):
    image_in_bytes = image_to_bytes(image)
    
    encrypted = cfb.encrypt(image_in_bytes, BLOCK_SIZE=BLOCK_SIZE)
    
    final_image = bytes_to_image(image, encrypted)
    final_image.save('data/cfb_enc.bmp')
    
    corr_encrypted = corrupt(encrypted, 1)
    decrypted = cfb.decrypt(corr_encrypted, BLOCK_SIZE=BLOCK_SIZE)
        
    final_image = bytes_to_image(image, decrypted)
    final_image.save('data/cfb_dec_with_error.bmp')
    
    output(bytearray(image_in_bytes), bytearray(encrypted), bytearray(decrypted), 20)

if __name__ == '__main__':
    source_image = Image.open('data/test.bmp', 'r')
    
    test_OFB(source_image)
    test_CFB(source_image)