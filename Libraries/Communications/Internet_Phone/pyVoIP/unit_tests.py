import unittest
from pyVoIP.VoIP import VoIPPhone, InvalidStateError


class UnitTestspyVoIP(unittest.TestCase):
    # ok
    def test_Basic_operations(self):
        print('test_Basic_operations')

        # This will be your callback function for when you receive a phone call.
        def answer(call):
            try:
                call.answer()
                call.hangup()
            except InvalidStateError:
                pass

        if __name__ == "__main__":
            phone = VoIPPhone(
                '<SIP Server IP >',
                '<SIP Server Port >',
                '<SIPServer Username>',
                '<SIP Server Password>',
                callCallback=answer,
                myIP="< Your computer's local IP>",
                sipPort="<Port to use for SIP (int, default 5060)>",
                rtpPortLow="<low end of the RTP Port Range>",
                rtpPortHigh="<high end of the RTP Port Range>"
            )
            phone.start()
            input('Press enter to disable the phone')
            phone.stop()


if __name__ == '__main__':
    unittest.main()
