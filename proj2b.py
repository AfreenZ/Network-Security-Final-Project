from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def generate_aes_key():
    return get_random_bytes(16)  # 128-bit key for AES

def encrypt_message_ecb(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return ciphertext

def decrypt_message_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode('utf-8')

def encrypt_message_cbc(message, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return iv + ciphertext

def decrypt_message_cbc(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
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
    key = generate_aes_key()

    plaintext_message_ecb = read_text_file(file_path)
    ciphertext_ecb = encrypt_message_ecb(plaintext_message_ecb, key)
    print(f"Ciphertext (ECB): {ciphertext_ecb}")

    decrypted_message_ecb = decrypt_message_ecb(ciphertext_ecb, key)
    print(f"Decrypted message (ECB): {decrypted_message_ecb}")

    plaintext_message_cbc = read_text_file(file_path)
    ciphertext_cbc = encrypt_message_cbc(plaintext_message_cbc, key)
    print(f"Ciphertext (CBC): {ciphertext_cbc}")

    decrypted_message_cbc = decrypt_message_cbc(ciphertext_cbc, key)
    print(f"Decrypted message (CBC): {decrypted_message_cbc}")