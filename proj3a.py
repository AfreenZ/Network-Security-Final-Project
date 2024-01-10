from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt(message, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate key pairs for U1 and U2
private_key_u1, public_key_u1 = generate_key_pair()
private_key_u2, public_key_u2 = generate_key_pair()

# U1 sends a message to U2
message_from_u1 = "Hello U2, it's me U1!"
encrypted_message_u1 = encrypt(message_from_u1, public_key_u2)

# U2 receives the message and decrypts it
decrypted_message_u2 = decrypt(encrypted_message_u1, private_key_u2)
print("U2 received message from U1:", decrypted_message_u2)

# U2 responds to U1
message_from_u2 = "Hello U1, nice to meet you!"
encrypted_message_u2 = encrypt(message_from_u2, public_key_u1)

# U1 receives the response and decrypts it
decrypted_message_u1 = decrypt(encrypted_message_u2, private_key_u1)
print("U1 received message from U2:", decrypted_message_u1)

