import hashlib
import random
import struct

def sha256_hash_truncated(input_string, size):
    return hashlib.sha256(str(input_string).encode()).hexdigest()[:size//4]

def hammingDist(str1, str2): 
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def float_to_bits(f):
    return bin(struct.unpack('>Q', struct.pack('>d', f))[0])[2:].zfill(64)

def flip_one_bit(byte_array):
    flip_index = random.randint(0, len(byte_array) * 8 - 1)
    byte_index, bit_index = divmod(flip_index, 8)
    flipped_byte = byte_array[byte_index] ^ (1 << (7 - bit_index))
    return byte_array[:byte_index] + bytes([flipped_byte]) + byte_array[byte_index + 1:]

def find_collision():
    hash_to_input_map = {}

    while True:
        random_bytes1 = bytearray(random.getrandbits(8) for _ in range(8))
        #print(random_bytes1)
        flipped_bytes1 = flip_one_bit(random_bytes1)
        #print(flipped_bytes1, "\n")

        if hammingDist(random_bytes1, flipped_bytes1) == 1:
            current_hash1 = sha256_hash_truncated(bytes(random_bytes1), len(random_bytes1))
            print("digest:", current_hash1)

            if current_hash1 in hash_to_input_map:
                return hash_to_input_map[current_hash1], bytes(random_bytes1)

            hash_to_input_map[current_hash1] = bytes(random_bytes1)

res1, res2 = find_collision()
print("Collision Found:")
print("Input 1:", res1)
print("Input 2:", res2)



# res3 = sha256_hash_truncated("hellogoodbye", 12)
# res4 = sha256_hash_truncated("hellogoodaye", 12)
# print("SHA256 digest:", res3, res4)
