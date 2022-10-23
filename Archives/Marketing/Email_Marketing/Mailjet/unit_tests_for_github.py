import unittest
from mailjet_rest import Client


# https://github.com/mailjet/mailjet-apiv3-python
class UnitTestsEmailMarketingWithMailjetAPIForGitHub(unittest.TestCase):
    # ok
    def test_send_one_mail(self):
        print('test_send_one_mail')

        # Credentials
        api_key = ''
        api_secret = ''

        # Client
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        # Data
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "emailfrom@emailfrom.com",
                        "Name": "emailfrom"
                    },
                    "To": [
                        {
                            "Email": "emailto@emailto.com",
                            "Name": "emailto"
                        }
                    ],
                    "Subject": "Greetings from Mailjet.",
                    "TextPart": "My first Mailjet email",
                    "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }

        # Send email
        result = mailjet.send.create(data=data)

        # Result
        print(result.status_code)
        print(result.json())


if __name__ == '__main__':
    unittest.main()
