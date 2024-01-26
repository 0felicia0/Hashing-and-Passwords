import bcrypt
import hashlib
import random
import struct
# create SHA256 hash object
# sha256 = hashlib.sha256()

def sha256_hash_truncated(input_string, size):
    return ((hashlib.sha256(str(input_string).encode()).hexdigest())[0:8])

#b Hamming distance is exactly 1 bit (i.e. differ in only 1 bit)
def hammingDist(str1, str2): 
    i = 0
    count = 0

    while(i < len(str1)): 
        if(str1[i] != str2[i]): 
            count += 1
        i += 1
    return count #needs to be exactly one
    

# def flip_one_bit_binary(number):
#     # Convert the number to binary representation
#     binary_number = bin(number)[2:]
#     index_to_flip = random.randint(0, len(binary_number) - 1)
#     flipped_bit = '1' if binary_number[index_to_flip] == '0' else '0'
#     new_binary_number = binary_number[:index_to_flip] + flipped_bit + binary_number[index_to_flip + 1:]
#     return new_binary_number

def float_to_bits(f):
    # Convert a float to its bit representation
    return bin(struct.unpack('>Q', struct.pack('>d', f))[0])[2:]

def flip_one_bit(binary_string):
    # Convert the binary string to a list of characters
    bits_list = list(binary_string)
    
    # Find the index of the bit to flip (you can choose any bit)
    flip_index = 2
    
    # Flip the bit at the chosen index
    bits_list[flip_index] = '0' if bits_list[flip_index] == '1' else '1'
    
    # Convert the list back to a string
    flipped_binary_string = ''.join(bits_list)
    
    return flipped_binary_string

def find_collision():
    hash_to_input_map = {}

    while True:

        #random floating point number 0-1
        #run through hashing
        random_float = random.uniform(0.1, 1)  # Generate a random float from 0 to 1
        random_float = round(random_float, 5)
        print("random float:", random_float)
        bin_float = float_to_bits(random_float)
        print("Original binary number:", bin_float)  # Print the original binary number
        
        flipped_bit_float = flip_one_bit(bin_float)
        print("Binary number with one random bit flipped:", flipped_bit_float)

        random_float = str(random_float)
        flipped_bit_float = str(flipped_bit_float)

        if hammingDist(random_float, flipped_bit_float) == 1: 
            # input_string = ''.join(random.choice('01') for _ in range(16))  # You can adjust the length
            #print(input_string)
            current_hash = sha256_hash_truncated(random_float, len(random_float))

            if current_hash in hash_to_input_map:
                colliding_input = hash_to_input_map[current_hash]
                #print("Collision Found: ")
                return colliding_input, random_float

            hash_to_input_map[current_hash] = random_float


res1, res2 = find_collision()

print(res1, res2)
