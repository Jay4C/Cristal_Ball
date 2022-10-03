import unittest
import base64
import hashlib
import secrets
import os


class UnitTestsTopicsSecurityHashlibForGitHub(unittest.TestCase):
    def test_hash_password(self):
        def hash_password(password, salt=None, iterations=260000):
            algorithm = "pbkdf2_sha256"

            if salt is None:
                salt = secrets.token_hex(16)

            assert salt and isinstance(salt, str) and "$" not in salt

            assert isinstance(password, str)

            pw_hash = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                salt.encode("utf-8"),
                iterations
            )

            b64_hash = base64.b64encode(pw_hash).decode("ascii").strip()

            return "{}${}${}${}".format(algorithm, iterations, salt, b64_hash)

        print(hash_password('tuto_tuta'))

    def test_hashing(self):
        salt = os.urandom(32)  # Remember this

        password = 'tuto_tuta'

        key = hashlib.pbkdf2_hmac(
            'sha256',  # The hash digest algorithm for HMAC
            password.encode('utf-8'),  # Convert the password to bytes
            salt,  # Provide the salt
            100000  # It is recommended to use at least 100,000 iterations of SHA-256
        )

        print('key : ' + str(key))


if __name__ == '__main__':
    unittest.main()
