from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def sign_message(message, private_key):
    key = RSA.import_key(private_key)
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(key).sign(h)
    return signature


def verify_signature(message, signature, public_key):
    key = RSA.import_key(public_key)
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

private_key_u1, public_key_u1 = generate_key_pair()
private_key_u2, public_key_u2 = generate_key_pair()

message_to_sign = "Hey did my message reach you?"
signature_u1 = sign_message(message_to_sign, private_key_u1)

is_valid_signature_unchanged = verify_signature(message_to_sign, signature_u1, public_key_u1)


if is_valid_signature_unchanged:
    print("U1's signature is valid for the unchanged document.")
else:
    print("U1's signature is not valid for the unchanged document.")

changed_message_to_sign = "Mwahahah I changed ur message!!!"
is_valid_signature_changed = verify_signature(changed_message_to_sign, signature_u1, public_key_u1)

if is_valid_signature_changed:
    print("U1's signature is valid for the changed document. (This should not happen)")
else:
    print("U1's signature is not valid for the changed document.")