import hashlib
import itertools

def truncate_hash(input_str, bits):
    full_hash = hashlib.sha256(input_str.encode()).hexdigest()
    # Convert hexadecimal digest to an integer
    full_hash_int = int(full_hash, 16)
    # Right shift to keep only the desired number of bits
    truncated_hash_int = full_hash_int >> (256 - bits)
    return truncated_hash_int

def find_collision(target_bits):
    seen_hashes = {}

    for message in itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', repeat=5):
        message_str = ''.join(message)
        truncated_hash = truncate_hash(message_str, target_bits)

        if truncated_hash in seen_hashes:
            print(f'Collision found for {target_bits}-bit hash:')
            print(f'Message 1: {seen_hashes[truncated_hash]}')
            print(f'Message 2: {message_str}')
            return

        seen_hashes[truncated_hash] = message_str

    print(f'No collision found for {target_bits}-bit hash')

# Example: Find a collision for a 8-bit truncated hash
find_collision(12)