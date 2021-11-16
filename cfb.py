from bfish import *
from util import *

def encrypt(bytes_array, BLOCK_SIZE) -> bytes:
    init_block = copy(init)
    result = []
    
    for i in range(0, len(bytes_array), BLOCK_SIZE):
        block = bytes_array[i:i+BLOCK_SIZE]
        enc_init_block = cipher.encrypt_block(init_block)
        
        gamma = bytes(enc_init_block[:BLOCK_SIZE])  
        
        block = bytes(a ^ b for (a, b) in zip(block, gamma))
        
        init_block = update_init(init_block, block)
        
        result.extend(block)
        
    return bytes(result)

def decrypt(bytes_array, BLOCK_SIZE) -> bytes:
    init_block = copy(init)
    result = []
    
    for i in range(0, len(bytes_array), BLOCK_SIZE):
        block = bytes_array[i:i+BLOCK_SIZE]
        
        enc_init_block = cipher.encrypt_block(init_block)
        
        gamma = bytes(enc_init_block[:BLOCK_SIZE])
        
        init_block = update_init(init_block, bytes(block))  
        
        block = bytes(a ^ b for (a, b) in zip(block, gamma))
        
        result.extend(block)
        
    return bytes(result)