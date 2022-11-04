import json
import time
import unittest
import websocket


class UnitTestsArchivesTradingXTB(unittest.TestCase):
    # ok
    def test_login(self):
        print('test_login')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request = """
        {
            "command": "login",
            "arguments": {
                "userId": "",
                "password": ""
            },
            "prettyPrint": true
        }
        """

        ws.send(request)
        response = json.loads(ws.recv())
        status = response['status']
        streamsessionid = response['streamSessionId']
        print("status : " + str(status) + " - streamsessionid : " + str(streamsessionid))
        ws.close()

    # ok
    def test_logout(self):
        print('test_logout')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = """
        {
            "command": "login",
            "arguments": {
                "userId": "",
                "password": ""
            },
            "prettyPrint": true
        }
        """
        ws.send(request_login)
        print("response login : " + str(ws.recv()))

        time.sleep(3)

        request_logout = """
        {
            "command": "logout"
        }
        """
        ws.send(request_logout)
        print("response logout : " + str(ws.recv()))

        ws.close()

    #
    def test_get_balance(self):
        print('test_get_balance')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = """
        {
            "command": "login",
            "arguments": {
                "userId": "",
                "password": ""
            },
            "prettyPrint": true
        }
        """

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_get_balance = '{"command": "getBalance", "streamSessionId": "' + streamsessionid + '"}'
        ws.send(request_get_balance)
        response_get_balance = str(ws.recv())
        print("request_get_balance : " + response_get_balance)

        time.sleep(3)
        
        request_logout = """
        {
            "command": "logout"
        }
        """
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()


if __name__ == '__main__':
    unittest.main()
