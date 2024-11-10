<h1 align="center">Cryptography and Information Security Lab</h1>

Welcome to the **Cryptography and Information Security Lab** repository. This repository contains Python implementations of various cryptographic techniques, ranging from classic to modern ciphers. Each file demonstrates a different cryptographic concept, complete with supporting images for better understanding.

## Table of Contents

- [Overview](#overview)
- [Implemented Ciphers and Algorithms](#implemented-ciphers-and-algorithms)
- [Detailed File Descriptions](#detailed-file-descriptions)
- [How to Run](#how-to-run)
- [License](#license)

## Overview

This repository is designed for students, researchers, and anyone interested in learning about cryptography. Each file in this repository is a standalone Python script that implements a specific cryptographic algorithm, showcasing the principles behind secure data transmission and encryption.

## Implemented Ciphers and Algorithms

### Classic Ciphers
- **Additive Cipher**: `1-Additive_cipher.py`
- **Multiplicative Cipher**: `2-Multiplicative_cipher.py`
- **Affine Cipher**: `3-Affine_cipher.py`
- **AutoKey Cipher**: `4-AutoKey_cipher.py` and `4-AutoKey-Cipher-Photo.png`
- **Playfair Cipher**: `5-Playfair_cipher.py`
- **Vigenère Cipher**: `6-Vigenere_cipher.py` and `6-Vigenere-Cipher-Photo.png`
- **Hill Cipher**: `7-Hill_cipher.py` and `7-Hill-Cipher-Photo.png`
- **One-Time Pad Cipher**: `8-One_Time_Pad_cipher.py`
- **Rail Fence Cipher**: `9-Rail_Fence_cipher.py` and `9-Rail-Fence-Cipher-Photo.png`
- **Keyless Row-Column Transposition**: `10-Keyless_Row_Column_Transposition.py`
- **Keyed Row Transposition**: `11-Keyed_Row_Transposition.py` and `11-Keyed_Row_Transposition-Photo.png`
- **Keyed Row-Column Transposition**: `12-Keyed_Row_Column_Transposition.py` and `12-Keyed_Row_Column_Transposition-Photo.png`

### Modern Cryptographic Algorithms
- **DES (Data Encryption Standard)**: `13-DES.py` and `13-DES1-Photo.png` to `13-DES4-Photo.png`
- **AES (Advanced Encryption Standard)**: `14-AES.py` and `14-AES1-Photo.png` to `14-AES9-Photo.png`
- **ElGamal Cryptosystem**: `15-Elgamal.py` and `15-Elgamal-Photo.png`
- **RSA Cryptosystem**: `16-RSA.py`, `16-RSA-Photo.png`, and `16-RSA2-Photo.png`
- **Knapsack Cryptosystem**: `17-Knapsack_Cryptography.py` and `17-Knapsack_Cryptography-Photo.png`, `17-Knapsack_Cryptography2-Photo.png`
- **Rabin Cryptosystem**: `18-Rabin_Cryptosystem.py` and `18-Rabin_Cryptosystem1-Photo.png`, `18-Rabin_Cryptosystem2-Photo.png`
- **Diffie-Hellman Key Exchange**: `19-DiffieHellman_Key_Exchange.py` and `19-DiffieHellman_Key_Exchange1-Photo.png`
- **Digital Signature Standard (DSS)**: `20-DSS.py` and `20-DSS-Photo.png`
- **Feistel Cipher**: `21-Feistal_cipher.py`

### Additional Utilities
- **Euclidean Algorithm**: `z-Euclidean_algorithm.py`
- **Co-primality Check**: `z-is-coPrime.py`

## Detailed File Descriptions

### 1. Additive Cipher (`1-Additive_cipher.py`)
Implements a simple shift cipher where each character in the plaintext is shifted by a certain number of positions.

### 2. Multiplicative Cipher (`2-Multiplicative_cipher.py`)
Implements a substitution cipher that multiplies the position of each character to create the ciphertext.

### 3. Affine Cipher (`3-Affine_cipher.py`)
Combines additive and multiplicative transformations to create an affine transformation of the characters.

### 4. AutoKey Cipher (`4-AutoKey_cipher.py`)
A polyalphabetic substitution cipher that uses a dynamic key. Supplemented with an image file (`4-AutoKey-Cipher-Photo.png`) to explain the key structure.

### 5. Playfair Cipher (`5-Playfair_cipher.py`)
Encrypts digraphs (pairs of letters) using a 5x5 matrix to introduce more complexity than single-character encryption.

### 6. Vigenère Cipher (`6-Vigenere_cipher.py`)
A polyalphabetic substitution cipher enhanced with images (`6-Vigenere-Cipher-Photo.png`) for better visualization of the key structure.

### 7. Hill Cipher (`7-Hill_cipher.py`)
Implements the Hill cipher, which uses linear algebra and matrix multiplication to encrypt blocks of plaintext. An accompanying image (`7-Hill-Cipher-Photo.png`) demonstrates the matrix setup.

### 8. One-Time Pad Cipher (`8-One_Time_Pad_cipher.py`)
A theoretically unbreakable cipher that uses a random key as long as the plaintext. Each letter is encrypted with a different part of the key.

### 9. Rail Fence Cipher (`9-Rail_Fence_cipher.py`)
A transposition cipher that arranges the plaintext in a zigzag pattern across multiple "rails" and reads it in a linear fashion to create the ciphertext. Includes an explanatory image (`9-Rail-Fence-Cipher-Photo.png`).

### 10. Keyless Row-Column Transposition Cipher (`10-Keyless_Row_Column_Transposition.py`)
A transposition cipher that rearranges the characters of the plaintext into a grid format and reads them in a different order to produce the ciphertext.

### 11. Keyed Row Transposition Cipher (`11-Keyed_Row_Transposition.py`)
An extension of the row transposition cipher that uses a key to determine the order of columns when rearranging the characters. Visual representation is provided in `11-Keyed_Row_Transposition-Photo.png`.

### 12. Keyed Row-Column Transposition Cipher (`12-Keyed_Row_Column_Transposition.py`)
Combines row and column transpositions with the use of a key to increase the security of the transposition process. Illustrated with `12-Keyed_Row_Column_Transposition-Photo.png`.

### 13. DES (Data Encryption Standard) (`13-DES.py`)
Implements the DES algorithm, a symmetric-key block cipher that encrypts data in 64-bit blocks using a 56-bit key. Images (`13-DES1-Photo.png` to `13-DES4-Photo.png`) show the DES process and key schedule.

### 14. AES (Advanced Encryption Standard) (`14-AES.py`)
Implements the AES algorithm, which is a widely used block cipher for securing data. It supports key sizes of 128, 192, or 256 bits. Images (`14-AES1-Photo.png` to `14-AES9-Photo.png`) provide visual representations of the different steps in the AES encryption process.

### 15. ElGamal Cryptosystem (`15-Elgamal.py`)
A public key cryptosystem based on the Diffie-Hellman key exchange. It encrypts data using asymmetric keys, providing security for data transmission. Supplementary image: `15-Elgamal-Photo.png`.

### 16. RSA Cryptosystem (`16-RSA.py`)
Implements the RSA algorithm, one of the most secure and widely used public key cryptosystems. It is based on the mathematical properties of large prime numbers. Visuals `16-RSA-Photo.png` and `16-RSA2-Photo.png` show the key generation and encryption process.

### 17. Knapsack Cryptosystem (`17-Knapsack_Cryptography.py`)
A public key cryptosystem based on the knapsack problem, which is a combinatorial optimization problem. Images `17-Knapsack_Cryptography-Photo.png` and `17-Knapsack_Cryptography2-Photo.png` illustrate the process of encryption and decryption.

### 18. Rabin Cryptosystem (`18-Rabin_Cryptosystem.py`)
A public key cryptosystem similar to RSA but relies on the difficulty of integer factorization. Images `18-Rabin_Cryptosystem1-Photo.png` and `18-Rabin_Cryptosystem2-Photo.png` help explain the cryptographic steps involved.

### 19. Diffie-Hellman Key Exchange (`19-DiffieHellman_Key_Exchange.py`)
Implements the Diffie-Hellman protocol for securely exchanging cryptographic keys over a public channel. Image `19-DiffieHellman_Key_Exchange1-Photo.png` provides a visual representation of the key exchange process.

### 20. Digital Signature Standard (DSS) (`20-DSS.py`)
Implements the Digital Signature Standard, which provides a way to verify the authenticity and integrity of a message. An accompanying image (`20-DSS-Photo.png`) showcases the process of generating and verifying digital signatures.

### 21. Feistel Cipher (`21-Feistal_cipher.py`)
Explains and implements the Feistel network structure, which forms the basis for various block ciphers like DES.

### Additional Tools:
- **Euclidean Algorithm (`z-Euclidean_algorithm.py`)**: Finds the greatest common divisor (GCD) of two numbers.
- **Co-primality Check (`z-is-coPrime.py`)**: Checks if two numbers are co-prime (i.e., their GCD is 1).

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/waliulrayhan/Cryptography-and-Information-Security-Lab.git
2. Navigate to the project directory:
   ```bash
   cd Cryptography-and-Information-Security-Lab
3. Run the desired Python script:
   ```bash
   python3 <filename>.py

## Prerequisites

- **Python 3.x must be installed.**
- **Install any required libraries using:**
  ```bash
  pip install -r requirements.txt

## Contribution

Feel free to open an issue or submit a pull request for any feature requests, bug fixes, or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
