import bcrypt
import hashlib
import random

# create SHA256 hash object
# sha256 = hashlib.sha256()

def sha256_hash_truncated(input_string, size):
    return ((hashlib.sha256(str(input_string).encode()).hexdigest())[0:size//4])

#b Hamming distance is exactly 1 bit (i.e. differ in only 1 bit)
def hammingDist(str1, str2): 
    i = 0
    count = 0

    while(i < len(str1)): 
        if(str1[i] != str2[i]): 
            count += 1
        i += 1
    return count #needs to be exactly one
    

def flip_one_bit_binary(number):
    # Convert the number to binary representation
    binary_number = bin(number)[2:]

    # Choose a random index to flip
    index_to_flip = random.randint(0, len(binary_number) - 1)

    # Flip the bit at the chosen index
    flipped_bit = '1' if binary_number[index_to_flip] == '0' else '0'

    # Construct the new binary number with the flipped bit
    new_binary_number = binary_number[:index_to_flip] + flipped_bit + binary_number[index_to_flip + 1:]

    return new_binary_number

def find_collision():
    hash_to_input_map = {}

    while True:
        random_int = random.randint(0, 1000)  # Generate a random integer
        print("Original binary number:", bin(random_int)[2:])  # Print the original binary number
        flipped_binary = flip_one_bit_binary(random_int)
        print("Binary number with one random bit flipped:", flipped_binary)
        random_int = str(random_int)
        flipped_binary = str(flipped_binary)

        if hammingDist(random_int, flipped_binary) == 1: 

            # input_string = ''.join(random.choice('01') for _ in range(16))  # You can adjust the length
            #print(input_string)
            current_hash = sha256_hash_truncated(random_int, len(random_int))

            if current_hash in hash_to_input_map:
                # Collision found
                colliding_input = hash_to_input_map[current_hash]
                print("Collision Found: ")
                return colliding_input, random_int

            hash_to_input_map[current_hash] = random_int


res1, res2 = find_collision()

print(res1, res2)
