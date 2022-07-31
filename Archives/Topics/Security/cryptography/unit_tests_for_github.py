import unittest
from cryptography.fernet import Fernet, MultiFernet
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class UnitTestsTopicsSecurityCryptographyForGitHub(unittest.TestCase):
    # ok
    def test_1(self):
        print('test_1 \n')

        # Put this somewhere safe!
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt(b"A really secret message. Not for prying eyes.")
        print(token)
        print(f.decrypt(token))

    # ok
    def test_2(self):
        key1 = Fernet(Fernet.generate_key())
        key2 = Fernet(Fernet.generate_key())
        f = MultiFernet([key1, key2])
        token = f.encrypt(b"Secret message!")
        print(token)
        print(f.decrypt(token))

    # ok
    def test_3(self):
        key1 = Fernet(Fernet.generate_key())
        key2 = Fernet(Fernet.generate_key())
        f = MultiFernet([key1, key2])
        token = f.encrypt(b"Secret message!")
        print(token)
        print(f.decrypt(token))

        key3 = Fernet(Fernet.generate_key())
        f2 = MultiFernet([key3, key1, key2])
        rotated = f2.rotate(token)
        print(rotated)
        print(f2.decrypt(rotated))

    # ok
    def test_4(self):
        print('test_4')

        password = b"password"
        salt = os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        token = f.encrypt(b"Secret message!")
        print(token)
        print(f.decrypt(token))


if __name__ == '__main__':
    unittest.main()
