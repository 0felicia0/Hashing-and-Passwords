import bcrypt
import hashlib
import random


# create SHA256 hash object
# sha256 = hashlib.sha256()

def sha256_hash_truncated(input_string, size):
    return ((hashlib.sha256(str(input_string).encode()).hexdigest())[0:size//4])
    

def find_collision():
    hash_to_input_map = {}

    while True:
        input_string = ''.join(random.choice('01') for _ in range(16))  # You can adjust the length
        #print(input_string)
        current_hash = sha256_hash_truncated(input_string, size)

        if current_hash in hash_to_input_map:
            # Collision found
            colliding_input = hash_to_input_map[current_hash]
            return colliding_input, input_string

        hash_to_input_map[current_hash] = input_string


res1, res2 = find_collision()

print(res1, res2)
