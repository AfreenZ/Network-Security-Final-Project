import random

class LFSR:
    def __init__(self, seed, taps):
        self.state = seed
        self.taps = taps

    def shift(self):
        feedback = sum(self.state[tap] for tap in self.taps) % 2
        self.state = self.state[1:] + [feedback]

    def generate_key(self, length):
        key = []
        for _ in range(length):
            key.append(self.state[0])
            self.shift()
        return key

def generate_rsa_keypair():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Commonly used value
    d = pow(e, -1, phi)
    return (n, e), (n, d)

def encrypt_rsa(message, public_key):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

def decrypt_rsa(ciphertext, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message

def main():
    lfsr_seed = [1, 0, 1, 0]  
    lfsr_taps = [3, 2]  

    lfsr_u1 = LFSR(seed=lfsr_seed, taps=lfsr_taps)
    shared_key = lfsr_u1.generate_key(128)  

    public_key_u1, private_key_u1 = generate_rsa_keypair()
    encrypted_key = encrypt_rsa(''.join(map(str, shared_key)), public_key_u1)

    decrypted_key = decrypt_rsa(encrypted_key, private_key_u1)

    print("Shared Key:", ''.join(map(str, shared_key)))
    print("Encrypted Key:", encrypted_key)
    print("Decrypted Key by U2:", decrypted_key)

if __name__ == "__main__":
    main()

