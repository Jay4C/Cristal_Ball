import time
import unittest
import requests
from requests_tor import RequestsTor


class UnitTestsCognitiveArchitecture(unittest.TestCase):
    def test_request_over_tor_browser(self):
        print('test_request_over_tor_browser')

        # for Tor Browser
        rt = RequestsTor()

        # for Tor
        # rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)

        url = 'https://github.com/deedy5/requests_tor'

        r = rt.get(url)

        ip_v6 = rt.check_ip()

        print('my ip address : ' + str(ip_v6))
        # print(r.text)

    def test_rotate_ip_address_over_tor_browser(self):
        print('test_rotate_ip_address_over_tor_browser')

        rt = RequestsTor()

        url = 'https://github.com/deedy5/requests_tor'

        r = rt.get(url)

        for i in range(10):
            ip = rt.check_ip()

            print('my ip address : ' + str(ip))

            time.sleep(2)

            rt.new_id()

    def test_compare_my_tor_ip_with_my_free_ip(self):
        print('test_compare_my_tor_ip_with_my_free_ip')

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }

        url = 'https://api.my-ip.io/ip'

        # for Tor Browser
        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        print(html_with_tor.text)

        convert_ipv6_to_ipv4_with_tor = rt.get("https://ipworld.info/ipv6-to-ipv4/" + str(html_with_tor.text), headers=headers)

        print(convert_ipv6_to_ipv4_with_tor)

        html_without_tor = requests.get(url, headers=headers)

        print(html_without_tor.text)


if __name__ == '__main__':
    unittest.main()
