import random 

def text_to_bitstream(text):
    return ''.join(format(ord(char), '08b') for char in text)

def xor_encrypt(bitstream, key):
    encrypted_bits = ''.join(chr(ord(bit) ^ key) for bit in bitstream)
    return encrypted_bits

def xor_decrypt(encrypted_bits, key):
    decrypted_bits = ''.join(chr(ord(bit) ^ key) for bit in encrypted_bits)
    return decrypted_bits

def bitstream_to_text(bitstream):
    return ''.join([chr(int(bitstream[i:i+8], 2)) for i in range(0, len(bitstream), 8)])

def demo():
    key = random.randint(0, 255) #Generate a random key
    input_text = "Afreen wants to sleep all day"

    bitstream = text_to_bitstream(input_text) #convert text to bitstream
    print(f"Original text: {input_text}")
    print(f"Bitstream: {bitstream}")

    encrypted_bits = xor_encrypt(bitstream, key)
    print(f"Encrypted bits: {encrypted_bits}")

    decrypted_bits = xor_decrypt(encrypted_bits, key) #decrypt bitstream
    print(f"Decrypted bits: {decrypted_bits}")

    recovered_text = bitstream_to_text(decrypted_bits)
    print(f"Recovered text: {recovered_text}")

if __name__ == "__main__":
    demo()
