import blowfish
import random
from PIL import Image
from util import *

cipher = blowfish.Cipher(b"6550f58df5a6b1a2c277ee87381fa5ee")
BLOCK_SIZE = 8
random.seed("i_am_seed_from_ice_age")

def encrypt(bytes_array) -> bytes:
    encrypted = []
    
    for i in range(0, len(bytes_array), 8):
        cur_block = bytes_array[i:i+8]
        enc = cipher.encrypt_block(cur_block)
        
        encrypted.extend(enc)
        
    return bytes(encrypted)

def decrypt(bytes_array) -> bytes:
    encrypted = []
    
    for i in range(0, len(bytes_array), 8):
        cur_block = bytes_array[i:i+8]
        enc = cipher.encrypt_block(cur_block)
        
        encrypted.extend(enc)
        
    return bytes(encrypted)

def OFB(bytes_array) -> bytearray:
    init_block = bytes([random.randint(0, 255) for _ in range(0, 8)])
    result = []
    
    for i in range(0, len(bytes_array), BLOCK_SIZE):
        block = bytes_array[i:i+BLOCK_SIZE]
        enc_init_block = cipher.encrypt_block(init_block)
        
        gamma = bytes(enc_init_block[:BLOCK_SIZE])
        init_block = update_init(init_block, gamma)  
        
        block = bytes(a ^ b for (a, b) in zip(block, gamma))
        
        result.extend(block)
        
    return bytes(result)


if __name__ == '__main__':
    source_image = Image.open('data/res.bmp', 'r')
    
    image_in_bytes = image_to_bytes(source_image)
    
    image_in_bytes = bytearray(image_in_bytes)
    image_in_bytes[0] = 255
    image_in_bytes[1] = 255
    image_in_bytes[2] = 255
    image_in_bytes[3] = 255
    image_in_bytes[4] = 255
    image_in_bytes[5] = 255
    
    image_in_bytes = bytes(image_in_bytes)
    
    encrypted = OFB(image_in_bytes)
        
    final_image = bytes_to_image(source_image, encrypted)
    final_image.save('data/test2.bmp')
    