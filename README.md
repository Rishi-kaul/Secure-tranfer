
# secure-tranfer

This repository contains a simple Python script for file encryption and decryption using the `cryptography` library. The script allows you to generate a key, encrypt a file, and decrypt a file with the generated key.

## Prerequisites

Make sure you have the `cryptography` library installed. You can install it using pip:

```bash
pip install cryptography
```

## Usage

The script includes functions to:

- Generate an encryption key
- Load an existing encryption key
- Encrypt a file
- Decrypt a file

### Generating a Key

To generate a key, run the following command:

```python
from cryptography1 import generate_key

generate_key()
```

This will create a file named `Secret.key` containing your encryption key.

### Loading the Key

To load the key from the `Secret.key` file, use the following command:

```python
from cryptography1 import load_key

key = load_key()
```

### Encrypting a File

To encrypt a file, use the `encrpt` function:

```python
from cryptography1 import encrpt

filename = 'path/to/your/file.txt'
key = load_key()
encrpt(filename, key)
```

This will encrypt the contents of the specified file.

### Decrypting a File

To decrypt a file, use the `decrypt` function:

```python
from cryptography1 import decrypt

filename = 'path/to/your/file.txt'
key = load_key()
decrypt(filename, key)
```

This will decrypt the contents of the specified file, provided the correct key is used.

## Example Script

Here is an example script demonstrating how to use the above functions:

```python
from cryptography1 import generate_key, load_key, encrpt, decrypt

# Generate a key
generate_key()

# Load the key
key = load_key()

# Encrypt a file
filename = 'path/to/your/file.txt'
encrpt(filename, key)
print(f"{filename} has been encrypted.")

# Decrypt the file
decrypt(filename, key)
print(f"{filename} has been decrypted.")
```

## Interactive Mode

The script also supports an interactive mode. Run the script and follow the prompts to encrypt or decrypt a file:

```bash
python cryptography1.py
```

---

Save this as `README.md` in your repository. Make sure to replace `cryptography1.py` with the correct filename and adjust any paths as necessary.

## Notes

- The interactive mode prompt in the code needs a small correction. Replace `ch = input(" Enter  E to Encrypt  or D to Decrypt : ").lower` with `ch = input(" Enter  E to Encrypt  or D to Decrypt : ").lower()`.
- Similarly, replace `filename = input` with `filename = input("Enter the filename: ")`.

Here's the corrected part of the interactive mode:

```python
ch = input(" Enter  E to Encrypt  or D to Decrypt : ").lower()
if ch == 'e':
    filename = input("Enter the filename: ")
    key = load_key()
    encrpt(filename, key)
    print(f"{filename} has been encrypted.")
elif ch == 'd':
    filename = input("Enter the filename: ")
    key = load_key()
    decrypt(filename, key)
    print(f"{filename} has been decrypted.")
else:
    print("Invalid option selected.")
```
