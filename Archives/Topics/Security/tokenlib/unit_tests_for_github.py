import unittest
import tokenlib

token = tokenlib.make_token({"userid": 42}, secret="I_LIKE_UNICORNS")


class UnitTestsTopicsSecurityTokenlibForGitHub(unittest.TestCase):
    # ok
    def test_1(self):
        print('test_1 \n')

        token = tokenlib.make_token({"userid": 42}, secret="I_LIKE_UNICORNS")
        print(token)

    # ok
    def test_2(self):
        print('test_2')

        token = tokenlib.make_token({"userid": 42}, secret="I_LIKE_UNICORNS")
        data = tokenlib.parse_token(token, secret="I_LIKE_UNICORNS")
        print(data)

    # ok
    def test_3(self):
        print('test_3')

        token = tokenlib.make_token({"userid": 42}, secret="I_LIKE_UNICORNS")
        key = tokenlib.get_token_secret(token, secret="I_LIKE_UNICORNS")
        print(key)

    # ok
    def test_4(self):
        print('test_4')

        token = tokenlib.make_token({"userid": 42}, secret="I_LIKE_UNICORNS")
        manager = tokenlib.TokenManager(secret="I_LIKE_UNICORNS")
        data = manager.parse_token(token)
        print(data)

    # ok
    def test_5(self):
        print('test_5')

        # Use now=XXX to simulate a time in the future.
        tokenlib.parse_token(token, secret="I_LIKE_UNICORNS", now=9999999999)

    # ok
    def test_6(self):
        print('test_6')

        tokenlib.parse_token(token, secret="I_HATE_UNICORNS")


if __name__ == '__main__':
    unittest.main()
