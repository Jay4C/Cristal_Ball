import unittest
import requests
from requests_tor import RequestsTor
import string
import ssl
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from OpenSSL import SSL

url = ""
email = ""
host = ""


class UnitTestsDiagnosisPentrationTestingWithBFA(unittest.TestCase):
    #
    def test_bfa_1(self):
        print("test_bfa_1")

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
            'referer': url,
            'origin': host,
            'Scheme': 'https'
        }

        # collect the data needed from "inspect element"
        data = {
            'csrfmiddlewaretoken': '',
            'email': '',
            'password': ''
        }

        send_data_url = requests.post(url, headers=headers, data=data, verify=False)

        print(send_data_url.content)


if __name__ == '__main__':
    unittest.main()
