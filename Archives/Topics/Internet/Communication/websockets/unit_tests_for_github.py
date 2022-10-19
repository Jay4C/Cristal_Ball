import ssl
import unittest
from websocket import create_connection


class UnitTestsInternetCommunicationWebsockets(unittest.TestCase):
    # ok
    def test_short_lived_one_off_send_receive(self):
        print('test_short_lived_one_off_send_receive')

        ws = create_connection(
            "wss://ws.xtb.com/real",
            sslopt={
                "cert_reqs": ssl.CERT_NONE,
                "check_hostname": False,
                "ssl_version": ssl.PROTOCOL_TLSv1
            }
        )
        print("Sending 'Hello, World'...")
        ws.send("Hello, World")
        print("Sent")
        print("Receiving...")
        result = ws.recv()
        print("Received '%s'" % result)
        ws.close()


if __name__ == '__main__':
    unittest.main()
