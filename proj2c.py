from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_des_key():
    return get_random_bytes(8) 

def encrypt_message_ecb(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), DES.block_size))
    return ciphertext

def decrypt_message_ecb(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_message.decode('utf-8')

def encrypt_message_cbc(message, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), DES.block_size))
    return ciphertext

def decrypt_message_cbc(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_message.decode('utf-8')

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

if __name__ == "__main__":
    file_path = "test.txt"  
    key = generate_des_key()

    plaintext_message_ecb = read_text_file(file_path)
    ciphertext_ecb = encrypt_message_ecb(plaintext_message_ecb, key)
    print(f"Ciphertext (ECB): {ciphertext_ecb}")

    decrypted_message_ecb = decrypt_message_ecb(ciphertext_ecb, key)
    print(f"Decrypted message (ECB): {decrypted_message_ecb}")

    iv_cbc = get_random_bytes(8)
    plaintext_message_cbc = read_text_file(file_path)
    ciphertext_cbc = encrypt_message_cbc(plaintext_message_cbc, key, iv_cbc)
    print(f"Ciphertext (CBC): {ciphertext_cbc}")

    decrypted_message_cbc = decrypt_message_cbc(ciphertext_cbc, key, iv_cbc)
    print(f"Decrypted message (CBC): {decrypted_message_cbc}")
