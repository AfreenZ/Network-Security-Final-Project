import random
def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y & 1:
            result = (result * x) % p
        y = y >> 1
        x = (x * x) % p
    return result

def diffie_hellman_key_exchange(p, a):
    
    private_key_u1 = random.randint(2, p - 2)    # select private keys for U1 and U2
    private_key_u2 = random.randint(2, p - 2)

    public_key_u1 = power(a, private_key_u1, p)   # calculate public keys for U1 and U2
    public_key_u2 = power(a, private_key_u2, p)

    shared_key_u1 = power(public_key_u2, private_key_u1, p)  # exchange public keys
    shared_key_u2 = power(public_key_u1, private_key_u2, p)

    # Print results
    print("Prime (p):", p)
    print("Primitive Root (g):", a)
    print("Private Key U1:", private_key_u1)
    print("Private Key U2:", private_key_u2)
    print("Public Key U1:", public_key_u1)
    print("Public Key U2:", public_key_u2)
    print("Shared Key U1:", shared_key_u1)
    print("Shared Key U2:", shared_key_u2)

if __name__ == "__main__":
    input_p = 102188617217178804476387977160129334431745945009730065519337094992129677228373
    input_a = 2   # primitive root modulo p
    diffie_hellman_key_exchange(input_p, input_a)