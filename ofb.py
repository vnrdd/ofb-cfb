import random
from bfish import *
from util import *

def OFB(bytes_array, BLOCK_SIZE) -> bytes:
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