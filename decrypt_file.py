#%%
import os

from base64 import b64decode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_der_private_key

abs_path = os.path.dirname(__file__)

""" Load Private Key """

pem_file = open(f"{abs_path}\\keys\\rsa.pem")
der_data = b64decode('\n'.join(pem_file.read().splitlines()[1:-1]))
pem_file.close()

pem_key = load_der_private_key(der_data, password=None)

""" Decrypt File """

file = open(f"{abs_path}\\files\\file.bin", "rb")
data = file.read()
file.close()

decrypted_data = pem_key.decrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

file = open(f"{abs_path}\\files\\file.txt", "wb")
file.truncate()
file.write(decrypted_data)
file.close()

""" Remove Encrypted File """

os.remove(f"{abs_path}\\files\\file.bin")