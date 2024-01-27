import hashlib
import itertools
import random
import time

def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def generate_strings_with_hamming_distance(length, distance=1):
    message1 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))
    bit_to_flip = random.randint(0, length - 1)
    message2 = message1[:bit_to_flip] + chr(ord(message1[bit_to_flip]) ^ 1) + message1[bit_to_flip + 1:]
    return message1, message2

def truncate_hash(input_str, bits):
    full_hash = hashlib.sha256(input_str.encode()).hexdigest()
    full_hash_int = int(full_hash, 16)
    truncated_hash_int = full_hash_int >> (256 - bits)
    return truncated_hash_int

def find_collision(target_bits):
    seen_hashes = {}

    start_time = time.time()

    while True:
        message = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
        truncated_hash = truncate_hash(message, target_bits)


        if truncated_hash in seen_hashes:
            end_time = time.time()
            print(f'Collision found for {target_bits}-bit hash (Target Hash Collision):')
            print(f'Message 1: {seen_hashes[truncated_hash]}')
            print(f'Message 2: {message}')
            print(f'Time taken: {end_time - start_time} seconds\n')
            return
        seen_hashes[truncated_hash] = message


# Part b: Generate strings with Hamming distance of 1 bit
for _ in range(3):
    message1, message2 = generate_strings_with_hamming_distance(10)
    print(f'Message 1: {message1}')
    print(f'Message 2: {message2}')
    print(f'Hamming Distance: {hamming_distance(message1, message2)}\n')

# Part c: Find collisions in truncated hash domains
for bits in range(8, 51, 2):
    find_collision(bits)  # Choose 'target' or 'birthday' for the desired method