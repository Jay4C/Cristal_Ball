import time
import unittest
import warnings
import requests
import socket
from requests_tor import RequestsTor
import ssl


class UnitTestsDiagnosisForCybersecurity(unittest.TestCase):
    def test_print_ssl(self):
        print("test_print_ssl")

        print(ssl.OPENSSL_VERSION)

    def test_scan_open_ports_on_my_vps_remotely_for_ssh(self):
        print("test_scan_open_ports_on_my_vps_remotely")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        vops_ip_v4 = "37.187.55.6"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        target_ip = socket.gethostbyname(vops_ip_v4)

        print('Starting scan on host:', target_ip)

        def port_scan(port):
            try:
                s.connect((target_ip, port))
                return True
            except:
                return False

        start = time.time()

        # here we are scanning port 0 to 65535
        for port in range(65536):
            if port_scan(port):
                print(f'port {port} is open')

        end = time.time()
        print(f'Time taken {end - start:.2f} seconds')

    def test_scan_open_ports_remotely_for_my_own_public_ipv4(self):
        print('test_scan_open_ports_remotely_for_my_own_public_ipv4')

        public_IP = requests.get("https://www.wikipedia.org").headers["X-Client-IP"]

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_ip = socket.gethostbyname(public_IP)
        print('Starting scan on host:', target_ip)

        def port_scan(port):
            try:
                s.connect((target_ip, port))
                return True
            except:
                return False

        start = time.time()

        # here we are scanning port 0 to 65535
        for port in range(65536):
            if port_scan(port):
                print(f'port {port} is open')

        end = time.time()
        print(f'Time taken {end - start:.2f} seconds')

    def test_scan_open_ports_remotely_for_my_router_ipv4(self):
        print('test_scan_open_ports_remotely_for_my_router_ipv4')

        router_ip_v4 = "10.20.65.18"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_ip = socket.gethostbyname(router_ip_v4)
        print('Starting scan on host:', target_ip)

        def port_scan(port):
            try:
                s.connect((target_ip, port))
                return True
            except:
                return False

        start = time.time()

        # here we are scanning port 0 to 65535
        for port in range(65536):
            if port_scan(port):
                print(f'port {port} is open')

        end = time.time()
        print(f'Time taken {end - start:.2f} seconds')


# https://lite.ip2location.com/reunion-ip-address-ranges
class UnitTestsDiagnosisForTestingIPRangesLocationInReunionIsland(unittest.TestCase):
    def test_check_ip_location_for_the_first_range(self):
        print("test_check_ip_location_for_the_first_range")

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        # begin ip address
        b1 = 102
        b2 = 135
        b3 = 232
        b4 = 0

        # end ip address
        e1 = 102
        e2 = 135
        e3 = 239
        e4 = 255

        for i1 in range(b1, e1 + 1):
            for i2 in range(b2, e2 + 1):
                for i3 in range(b3, e3 + 1):
                    for i4 in range(b4, e4 + 1):
                        ip = str(i1) + "." + str(i2) + "." + str(i3) + "." + str(i4)

                        r = rt.get("http://ipwhois.app/json/" + ip, headers=headers)

                        print(r.json())


if __name__ == '__main__':
    unittest.main()
