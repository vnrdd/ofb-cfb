import random
from bitstring import BitArray
from copy import copy
from prettytable import PrettyTable

init = bytes([random.randint(0, 255) for _ in range(0, 8)])

def image_to_bytes(image) -> list:
    W = image.width
    H = image.height
    
    bytes = []
    
    for h in range(H):
        for w in range(W):
            cur_pixel = image.getpixel((w, h))
            bytes.append((cur_pixel[0]).to_bytes(1, byteorder='big')[0])
            bytes.append((cur_pixel[1]).to_bytes(1, byteorder='big')[0])
            bytes.append((cur_pixel[2]).to_bytes(1, byteorder='big')[0])
    
    return bytes

def bytes_to_image(source_image, image_in_bytes):
    final_image = copy(source_image)
    
    W = final_image.width
    H = final_image.height
    
    w = 0
    h = 0
    
    for i in range(0, len(image_in_bytes), 3):
        new_pixel = (image_in_bytes[i], image_in_bytes[i + 1], image_in_bytes[i + 2])
        final_image.putpixel((w, h), new_pixel)
        
        w += 1
        
        if w == W:
            w = 0
            h += 1
            
    return final_image

def update_init(block, gamma) -> bytes:
    block = bytes(block[len(gamma):])
    block += gamma
    
    return block

def corrupt(bytes_array, count) -> bytes:
    bytes_array = bytearray(bytes_array)
    
    for i in range(count):
        bytes_array[i] = random.randint(0, 255)
        
    return bytes(bytes_array)

def output(source, enc, dec, count):
    table = PrettyTable()
    table.field_names = ['Byte num', 'Source', 'Encrypted', 'Decrypted', 'Status']
      
    for i in range(count):
        byte1 = BitArray(uint=source[i], length=8).bin
        byte2 = BitArray(uint=enc[i], length=8).bin
        byte3 = BitArray(uint=dec[i], length=8).bin
        
        table.add_row([i, byte1, byte2, byte3, get_status(byte1, byte3)])
        
    print(table)
        
def get_status(value1, value2) -> str:
    return 'ok' if value1 == value2 else 'error'