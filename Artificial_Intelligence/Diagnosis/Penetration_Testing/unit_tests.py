import unittest
import requests
from requests_tor import RequestsTor
import string
import ssl
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from OpenSSL import SSL

url = "https://s-insight.optimzen.com/account/signin?next=/"
email = ""


class UnitTestsDiagnosisPentrationTestingWithBFA(unittest.TestCase):
    #
    def test_bfa_with_one_c(self):
        print("test_bfa_with_one_c")

        context = SSL.Context(SSL.TLSv1_2_METHOD)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        # User Agent
        software_names = [
            SoftwareName.CHROME.value,
            SoftwareName.YAHOO_SLURP_WEB_CRAWLER_BOT.value,
            SoftwareName.ALEXA_BOT.value,
            SoftwareName.AMAYA.value,
            SoftwareName.AMAZON_API_GATEWAY.value
        ]

        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.ANDROID.value,
            OperatingSystem.BADA.value,
            OperatingSystem.BLACKBERRY.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.FREEBSD.value
        ]

        user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100
        )
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {
            'User-Agent': user_agent,
            'referer': 'https://s-insight.optimzen.com/account/signin?next=/',
            'origin': 'https://s-insight.optimzen.com',
            'Scheme': 'https'
        }

        # collect the data needed from "inspect element"
        data = {
            'csrfmiddlewaretoken': 'KyG7fevUoK6ZFckPHxFkmIjXAA81HPU8Z6h9B6WcSjnxDiBNe7msTmqMEoe0idug',
            'email': '',
            'password': ''
        }

        send_data_url = requests.post(url, headers=headers, data=data, verify=ssl.CERT_NONE)

        print(send_data_url.content)


if __name__ == '__main__':
    unittest.main()
