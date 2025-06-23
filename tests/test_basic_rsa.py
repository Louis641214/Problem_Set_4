from src.rsa import generate_keys, encrypt, decrypt, attack

# Generate RSA Keys 
e, d, n = generate_keys(100, 300)

# Louis encrypts a message 
message = 77
ciphertext = encrypt(message, e, n)
print(f"Original message: {message}")
print(f"Encrypted message: {ciphertext}")

# Sergii decrypts the message 
decrypted = decrypt(ciphertext, d, n)
print(f"Sergii decrypted: {decrypted}")

# Marek tries to break the encryption 
print("\n[Marek tries to break it...]")
message, duration = attack(e, n, ciphertext)
if message is not None:
    print(f"Marek recovered: {message} in {duration:.4f} seconds")
else:
    print("Marek failed to factorize n.")
