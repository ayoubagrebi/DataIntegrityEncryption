This project demonstrates a simple encryption and decryption process for a 1MB file using the cryptography library in Python. The process includes generating a 1MB file, creating an encryption key, hashing the file for integrity verification, encrypting the file, and finally decrypting it.
## How to Use

1. **Generate 1MB File:**
   - Run `python file.py` to create a 1MB text file.

2. **Generate Encryption Key:**
   - Run `python key.py` to generate an encryption key and store it in `filekey.key`.

3. **Hash the 1MB File:**
   - Run `python hash.py` to calculate the SHA-256 hash of the 1MB file and store it in `hashed_file.txt`.

4. **Encrypt the 1MB File:**
   - Run `python encrypt.py` to encrypt the 1MB file using the generated key.

5. **Decrypt the 1MB File:**
   - Run `python decrypt.py` to decrypt the encrypted file.

## Verification of Integrity

- The project ensures data integrity by generating a hash of the 1MB file before encryption.
- After decryption, the hash of the decrypted file is compared with the original hash to verify data integrity.
