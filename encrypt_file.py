#%%
import os

from base64 import b64decode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_der_public_key

abs_path = os.path.dirname(__file__)

""" Load Public Key """

pub_file = open(f"{abs_path}\\keys\\rsa.pub")
der_data = b64decode('\n'.join(pub_file.read().splitlines()[1:-1]))
pub_file.close()

pub_key = load_der_public_key(der_data)

""" Encrypt File """

file = open(f"{abs_path}\\files\\file.txt")
data = file.read()
file.close()

encrypted_data = pub_key.encrypt(
    data.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

new_file = open(f"{abs_path}\\files\\file.bin", "wb")
new_file.truncate()
new_file.write(encrypted_data)
new_file.close()

""" Remove Original File """

os.remove(f"{abs_path}\\files\\file.txt")