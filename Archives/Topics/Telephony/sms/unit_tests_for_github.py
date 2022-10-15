import unittest
import sms


class UnitsTestsTelephonySms(unittest.TestCase):
    #
    def test_send_sms(self):
        print("test_send_sms")

        m = sms.Modem('COM3')
        m.send('1'.encode('utf-8'), 'This is a message')
        m.conn.sent()


if __name__ == '__main__':
    unittest.main()
