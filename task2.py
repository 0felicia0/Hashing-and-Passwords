from bcrypt import *
import base64
import time
import nltk
import ssl
from nltk.corpus import words

ssl._create_default_https_context = ssl._create_unverified_context


nltk.download('words')
word_list = words.words()

# Function to decode salt and hash from shadow file entry
def decode_shadow_entry(entry):
    parts = entry.split('$')
    algorithm = parts[1]
    workfactor = parts[2]
    hash_val = parts[3]
    return algorithm, workfactor, hash_val

# Function to crack password for a given shadow file entry
def crack_password(username, entire_hash):
    print(f"Cracking password for user: {username}")
    start_time = time.time()
    
    # Iterate through words in NLTK corpus
    for word in word_list:
        # Check word length
        if 6 <= len(word) <= 10:
            candidate_password = word.encode()
            
            generated_hash = checkpw(candidate_password, entire_hash.encode())
            
            if generated_hash:
                end_time = time.time()
                print(f"Time taken: {end_time - start_time} seconds")
                return word
    
    print("Password not cracked.")

# Read shadow file
with open("shadow.txt", "r") as file:
    for line in file:
        # Split entry into components
        username, entire_hash = line.strip().split(":")

        algorithm, workfactor, hash_val = decode_shadow_entry(entire_hash)
        
        word = crack_password(username, entire_hash)
        print(f"Username: {username}")
        print(f"Algorithm: {algorithm}")
        print(f"Workfactor: {workfactor}")
        print(f"Word: {word}")