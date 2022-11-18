import json
import time
import unittest
import websocket

userId = ''
password = ''


class UnitTestsArchivesTradingXTBAvailableCommands(unittest.TestCase):
    # ok
    def test_login(self):
        print('test_login')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
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

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

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


class UnitTestsArchivesTradingXTBAvailableStreamingCommands(unittest.TestCase):
    # command not found
    def test_get_balance(self):
        print('test_get_balance')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/realStream'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

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

    # command not found
    def test_get_candles(self):
        print('test_get_candles')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_get_candles = '{"command": "getCandles", "streamSessionId": "' \
                              + streamsessionid \
                              + '", "symbol": "EURUSD"}'
        ws.send(request_get_candles)
        response_get_candles = str(ws.recv())
        print("response_get_candles : " + response_get_candles)

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

    # command not found
    def test_get_keep_alive(self):
        print('test_get_keep_alive')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_get_keep_alive = '{"command": "getKeepAlive", "streamSessionId": "' + streamsessionid + '"}'
        ws.send(request_get_keep_alive)
        response_get_keep_alive = str(ws.recv())
        print("response_get_keep_alive : " + response_get_keep_alive)

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

    # command not found
    def test_get_news(self):
        print('test_get_news')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_get_news = '{"command": "getNews", "streamSessionId": "' + streamsessionid + '"}'
        ws.send(request_get_news)
        response_get_news = str(ws.recv())
        print("response_get_news : " + response_get_news)

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

    # command not found
    def test_getProfits(self):
        print('test_getProfits')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response_login : " + str(response_login))

        time.sleep(3)

        request_getProfits = '{"command": "getProfits", "streamSessionId": "' + streamsessionid + '"}'
        ws.send(request_getProfits)
        request_getProfits = str(ws.recv())
        print("request_getProfits : " + request_getProfits)

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

    # command not found
    def test_getTickPrices(self):
        print('test_getTickPrices')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response_login : " + str(response_login))

        time.sleep(3)

        request_getTickPrices = '{"command": "getTickPrices", "streamSessionId": "' + streamsessionid + '", "symbol": "EURUSD", "minArrivalTime": 5000, "maxLevel": 2}'
        ws.send(request_getTickPrices)
        response = str(ws.recv())
        print("response : " + response)

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

    # command not found
    def test_getTrades(self):
        print('test_getTrades')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response_login : " + str(response_login))

        time.sleep(3)

        request = '{"command": "getTrades", "streamSessionId": "' + streamsessionid + '"}'
        ws.send(request)
        response = str(ws.recv())
        print("response : " + response)

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

    # command not found
    def test_getTradeStatus(self):
        print('test_getTradeStatus')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response_login : " + str(response_login))

        time.sleep(3)

        request = '{"command": "getTradeStatus", "streamSessionId": "' + streamsessionid + '"}'
        ws.send(request)
        response = str(ws.recv())
        print("response : " + response)

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

    # ok
    def test_ping(self):
        print('test_ping')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response_login : " + str(response_login))

        time.sleep(3)

        request = '{"command": "ping", "streamSessionId": "' + streamsessionid + '"}'
        ws.send(request)
        response = str(ws.recv())
        print("response : " + response)

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


class UnitTestsArchivesTradingXTBRetrievingTradingDataCommands(unittest.TestCase):
    # ok
    def test_getAllSymbols(self):
        print('test_getAllSymbols')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getAllSymbols"}'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # ok
    def test_getCalendar(self):
        print('test_getCalendar')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getCalendar"}'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # ok
    def test_getChartLastRequest(self):
        print('test_getChartLastRequest')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getChartLastRequest", "arguments": { "info": { "period": 5, "start": 1262944112000, "symbol": "USD" } }}'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # ok
    def test_getChartRangeRequest(self):
        print('test_getChartRangeRequest')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getChartRangeRequest", "arguments": { "info": { "end": 1262944412000, "period": 5, "start": 1262944112000, "symbol": "USD", "ticks": 0 } }}'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # ok
    def test_getCommissionDef(self):
        print('test_getCommissionDef')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getCommissionDef", "arguments": { "symbol": "T.US", "volume": 1.0 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # ok
    def test_getCurrentUserData(self):
        print('test_getCurrentUserData')
        ws = websocket.WebSocket()
        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getCurrentUserData", "arguments": { "symbol": "T.US", "volume": 1.0 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # command deprecated
    def test_getIbsHistory(self):
        print('test_getIbsHistory')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getIbsHistory", "arguments": { "end": 1395053810991, "start": 1394449010991 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # ok
    def test_getMarginLevel(self):
        print('test_getMarginLevel')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getMarginLevel"}'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

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

    # ok
    def test_getMarginTrade(self):
        print('test_getMarginTrade')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getMarginTrade", "arguments": { "symbol": "EURPLN", "volume": 1.0 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getNews(self):
        print('test_getNews')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getNews", "arguments": { "end": 0, "start": 1275993488000 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getProfitCalculation(self):
        print('test_getProfitCalculation')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getProfitCalculation", "arguments": { "closePrice": 1.3000, "cmd": 0, "openPrice": 1.2233, "symbol": "EURPLN", "volume": 10 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getServerTime(self):
        print('test_getServerTime')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getServerTime"}'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getStepRules(self):
        print('test_getStepRules')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getStepRules"}'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getSymbol(self):
        print('test_getSymbol')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getSymbol", "arguments": { "symbol": "EURPLN" } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getTickPrices(self):
        print('test_getTickPrices')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getTickPrices", "arguments": { "level": 0, "symbols": ["EURPLN", "EURUSD"], "timestamp": 1262944112000 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getTradeRecords(self):
        print('test_getTradeRecords')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getTradeRecords", "arguments": { "orders": [7489839, 7489841] } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getTrades(self):
        print('test_getTrades')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getTrades", "arguments": { "openedOnly": true } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getTradesHistory(self):
        print('test_getTradesHistory')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getTradesHistory", "arguments": { "end": 0, "start": 1275993488000 } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getTradingHours(self):
        print('test_getTradingHours')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{"command": "getTradingHours", "arguments": { "symbols": ["EURUSD"] } }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_getVersion(self):
        print('test_getVersion')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{ "command": "getVersion" }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_ping(self):
        print('test_ping')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '{ "command": "ping" }'
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_tradeTransaction(self):
        print('test_tradeTransaction')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '''
        { 
            "command": "tradeTransaction", 
            "arguments": { 
                "cmd": 2, 
                "customComment": "Some text", 
                "expiration": 1462006335000,
                "offset": 0,
                "order": 82188055,
                "price": 1.12,
                "sl": 0.0,
                "symbol": "EURUSD",
                "tp": 0.0,
                "type": 0,
                "volume": 5.0
            } 
        }
        '''
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()

    # ok
    def test_tradeTransactionStatus(self):
        print('test_tradeTransactionStatus')

        ws = websocket.WebSocket()

        url = 'wss://ws.xtb.com/real'

        ws.connect(url=url)

        request_login = '{"command": "login", "arguments": {"userId": "%s", "password": "%s"}, "prettyPrint": true}' % \
                        (userId, password)

        ws.send(request_login)
        response_login = json.loads(ws.recv())
        status = response_login['status']
        streamsessionid = response_login['streamSessionId']
        print("response login : " + str(response_login))

        time.sleep(3)

        request_command = '''
        { 
            "command": "tradeTransactionStatus", 
            "arguments": { 
                "order": 43
            } 
        }
        '''
        ws.send(request_command)
        response_command = str(ws.recv())
        print("response_command : " + response_command)

        time.sleep(3)

        request_logout = '{"command": "logout"}'
        ws.send(request_logout)
        response_logout = str(ws.recv())
        print("response_logout : " + response_logout)

        ws.close()


if __name__ == '__main__':
    unittest.main()
