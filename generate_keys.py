#%%
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

""" Gerar Par de Chaves """

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

pem_public_key = private_key.public_key().public_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PublicFormat.SubjectPublicKeyInfo
)

abs_path = os.path.dirname(__file__)

private_key_file = open(f"{abs_path}\\keys\\rsa.pem", "w")
private_key_file.truncate()
private_key_file.write(pem_private_key.decode())
private_key_file.close()

private_key_file = open(f"{abs_path}\\keys\\rsa.pub", "w")
private_key_file.truncate()
private_key_file.write(pem_public_key.decode())
private_key_file.close()