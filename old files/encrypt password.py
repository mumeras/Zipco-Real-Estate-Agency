from cryptography.fernet import Fernet

# ✅ Step 1: Generate a secret encryption key (Only run once)
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# ✅ Step 2: Encrypt the password
password = "Shanika@2015"  # Your Gmail password
cipher_suite = Fernet(key)
encrypted_password = cipher_suite.encrypt(password.encode())

# ✅ Step 3: Save the encrypted password to a file
with open("encrypted_password.txt", "wb") as enc_file:
    enc_file.write(encrypted_password)

print("🔐 Password encrypted and saved securely!")
