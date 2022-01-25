"""
Author: Situ Feng

It is only meant to be used by students who are taking CSC427 LEC9201.
"""


# Make sure module <pycryptodome> in installed
# If the moduel is missing, try <pip install pycrotodome>

from typing import Any
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


def generate_keys(seed) -> Any:
    """
    This function prints out the public key & private key with <seed>
    """

    # TODO: Generate the key pair with the given seed
    # HINT: Look up RSA.generate()
    key_pair = None

    return key_pair


if __name__ == "__main__":

    keys = generate_keys(3072)

    message = b"I LOVE CSC427!"

    # TODO: Encrypt the message
    # HINT: Look up PKCS1_OAEP.new()
    encryptor = None
    encrypted_msg = encryptor.encrypt(message)
    print(f"Encrypted Message: \n{binascii.hexlify(encrypted_msg)}")
