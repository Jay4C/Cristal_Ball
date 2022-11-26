import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
from bs4 import BeautifulSoup
import requests
import string
import json
import xlsxwriter


class UnitTestSmsMarketing(unittest.TestCase):
    def test_send_sms_for_vivastreet(self):
        url_de_depart = 'https://www.vivastreet.com/annonces/ile-de-france/t+2'

        app = Application(backend="uia")

        # Open the Google Chrome Application
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Move to (690, 340)
        pywinauto.mouse.move(coords=(690, 340))

        time.sleep(2)

        # Click left on "log in" button
        pywinauto.mouse.click(button='left', coords=(690, 340))

        time.sleep(5)

        # Click left on "Advanced" button
        pywinauto.mouse.click(button='left', coords=(750, 130))

        time.sleep(5)

        # Click left on "SMS" button
        pywinauto.mouse.click(button='left', coords=(250, 400))

        time.sleep(5)

        # Click left on "New message" button
        pywinauto.mouse.click(button='left', coords=(270, 335))

        time.sleep(5)

        text = ""

        html_url_de_depart = requests.get(url_de_depart)

        # Parse the content of phone_number_html
        html_url_de_depart_soup = BeautifulSoup(html_url_de_depart.content, 'html.parser')

        if html_url_de_depart_soup.find('div', {'class': 'results-summary'}) is None:
            print('no counter')

        else:
            nombre_annonces = html_url_de_depart_soup.find('div', {'class': 'results-summary'}).text \
                .replace('annonces', '') \
                .replace('<h1>', '') \
                .replace('</h1>', '') \
                .replace('Annonces', '') \
                .replace(',', '') \
                .replace(' ', '') \
                .replace('\n', '') \
                .lower()

            for letter in string.ascii_lowercase:
                nombre_annonces = nombre_annonces.replace(letter, '')

            nombre_pages = int(round(int(nombre_annonces) / 25))

            for i in range(2, nombre_pages):

                url = url_de_depart[:-1] + str(i)

                print(url)

                phone_numbers = []

                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("ul", {"class", "list"}) is None:
                    print("the list is empty")

                else:
                    li_all = soup.find("ul", {"class", "list"}).find_all("li")

                    for li in li_all:
                        try:
                            url = li.find("div", {"class", "clad"}).find("a", {"class", "clad__wrapper"}).get("href")

                            # Request the content of a page from the url
                            phone_number_html = requests.get(url)

                            time.sleep(3)

                            # Parse the content of phone_number_html
                            phone_number_soup = BeautifulSoup(phone_number_html.content, 'html.parser')

                            if phone_number_soup.find("div",
                                                      {"class",
                                                       "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) is None:
                                print("sorry there is no phone number")

                            else:
                                phone_number = phone_number_soup.find("div", {"class",
                                                                              "vs-phone-button kiwii-font-weight-bold kiwii-position-relative"}) \
                                    .find("span", {"class", "phone_link"}).get("data-phone-number")

                                if phone_number in phone_numbers:
                                    print("phone number : " + phone_number + " already exists")

                                else:
                                    if phone_number[:2] == "06" or phone_number[:2] == "07":
                                        phone_numbers.append(phone_number)

                                        print("phone number : " + phone_number)

                                        # Click left on "Phone Number:" input
                                        pywinauto.mouse.click(button='left', coords=(670, 255))

                                        time.sleep(5)

                                        # Type a phone umber
                                        pywinauto.keyboard.send_keys(phone_number)

                                        time.sleep(5)

                                        # Click left on "Content:" input
                                        pywinauto.mouse.click(button='left', coords=(670, 350))

                                        time.sleep(5)

                                        # Type a text message
                                        pywinauto.keyboard.send_keys(text)

                                        time.sleep(10)

                                        # Move to the "Send" button
                                        pywinauto.mouse.move(coords=(1070, 500))

                                        time.sleep(5)

                                        # Click left on the "Send" button
                                        pywinauto.mouse.click(button='left', coords=(1070, 500))

                                        time.sleep(10)

                        except:
                            print("no phone number")

    def test_effacer_sms(self):
        app = Application(backend="uia")

        # Open the Google Chrome Application
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Move to (690, 340)
        pywinauto.mouse.move(coords=(690, 340))

        time.sleep(2)

        # Click left on "log in" button
        pywinauto.mouse.click(button='left', coords=(690, 340))

        time.sleep(5)

        # Click left on "Advanced" button
        pywinauto.mouse.click(button='left', coords=(750, 130))

        time.sleep(5)

        # Click left on "SMS" button
        pywinauto.mouse.click(button='left', coords=(250, 400))

        time.sleep(5)

        # Click left on Outbox button
        pywinauto.mouse.click(button='left', coords=(270, 380))

        time.sleep(5)

        for i in range(14):
            time.sleep(5)

            # Click left on Selection button
            pywinauto.mouse.click(button='left', coords=(500, 280))

            time.sleep(5)

            # Click left on delete button
            pywinauto.mouse.click(button='left', coords=(1100, 240))

            time.sleep(5)

            # Move to the yes button
            pywinauto.mouse.move(coords=(770, 360))

            time.sleep(5)

            # Click left on yes button
            pywinauto.mouse.click(button='left', coords=(770, 360))

            time.sleep(10)

    def test_send_sms_for_escorte_com(self):
        url_search = 'https:///paris/1er-arrondissement-du-louvre/#age=2&is_smoking=2'

        filename = url_search.split("https:///")[1][:10] \
            .replace("-", "") \
            .replace("_", "") \
            .replace("/", "")

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(filename + '.xlsx')
        worksheet = workbook.add_worksheet()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        app = Application(backend="uia")

        # Open the Google Chrome Application
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(5)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Move to (690, 340)
        pywinauto.mouse.move(coords=(690, 340))

        time.sleep(2)

        # Click left on "log in" button
        pywinauto.mouse.click(button='left', coords=(690, 340))

        time.sleep(5)

        # Click left on "Advanced" button
        pywinauto.mouse.click(button='left', coords=(750, 130))

        time.sleep(5)

        # Click left on "SMS" button
        pywinauto.mouse.click(button='left', coords=(250, 400))

        time.sleep(5)

        # Click left on "New message" button
        pywinauto.mouse.click(button='left', coords=(270, 335))

        time.sleep(5)

        # Request the content of a page from the url
        html_search = requests.get(url_search)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_search.content, 'html.parser')

        if soup.find("div", {"class", "col-xs-4 escort"}) is None:
            print("sorry there is no escorts")

        else:
            url_escorts = soup.find_all("div", {"class", "col-xs-4 escort"})

            for url_escort in url_escorts:
                url_result = "https://www.escorte.com" + url_escort.find("a").get("href")

                # Request the content of a page from the url
                html_result = requests.get(url_result)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html_result.content, 'html.parser')

                if soup.find("div", {"class", "phone"}) is None:
                    print("sorry there is no phone number")

                else:
                    show_number = soup.find("div", {"class", "phone"}) \
                        .find("a") \
                        .get("onclick") \
                        .replace("showNumber(", "") \
                        .replace(")", "") \
                        .replace(";", "")

                    url_phone_number = "https://www.escorte.com/escort/get_phone/" + show_number

                    payload = {}
                    headers = {
                        'Host': 'www.escorte.com',
                        'Referer': url_result,
                        'Connection': 'keep-alive',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'TE': 'Trailers',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    response = requests.request("GET", url_phone_number, headers=headers, data=payload)

                    data = response.text \
                        .replace("", "") \
                        .replace("�", "") \
                        .replace("", "")

                    json_data = json.loads(data)

                    if "ok" in json_data:
                        if not (json_data.get('ok') is None):
                            phone_number = json_data.get('ok') \
                                .replace("+", "00") \
                                .replace(" ", "") \
                                .replace("-", "")

                            if phone_number[:4] == "0033":
                                print("phone_number : " + phone_number)

                                # Iterate over the data and write it out row by row.
                                worksheet.write(row, col, url_result)
                                worksheet.write(row, col + 1, phone_number)
                                row += 1

                                # Click left on "Phone Number:" input
                                pywinauto.mouse.click(button='left', coords=(670, 255))

                                time.sleep(5)

                                # Type a phone umber
                                pywinauto.keyboard.send_keys(phone_number)

                                time.sleep(5)

                                # Click left on "Content:" input
                                pywinauto.mouse.click(button='left', coords=(670, 350))

                                time.sleep(5)

                                message = ""

                                # Type a text message
                                pywinauto.keyboard.send_keys(message)

                                time.sleep(10)

                                # Move to the "Send" button
                                pywinauto.mouse.move(coords=(1070, 500))

                                time.sleep(5)

                                # Click left on the "Send" button
                                pywinauto.mouse.click(button='left', coords=(1070, 500))

                                time.sleep(10)

                        else:
                            print("Key ok has no value")
                    else:
                        print("Key ok doesn't exist in JSON data")

        workbook.close()

    def test_send_sms_for_love_meeting_for_one_phone_number(self):
        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(5)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Click left on "Advanced" button
        pywinauto.mouse.click(button='left', coords=(750, 130))

        time.sleep(5)

        # Click left on "SMS" button
        pywinauto.mouse.click(button='left', coords=(250, 400))

        time.sleep(5)

        # Click left on "New message" button
        pywinauto.mouse.click(button='left', coords=(270, 335))

        time.sleep(5)

        # Click left on "Phone Number:" input
        pywinauto.mouse.click(button='left', coords=(670, 255))

        time.sleep(5)

        # Type a phone umber
        pywinauto.keyboard.send_keys("")

        time.sleep(5)

        # Click left on "Content:" input
        pywinauto.mouse.click(button='left', coords=(670, 350))

        time.sleep(5)

        message = ""

        # Type a text message
        pywinauto.keyboard.send_keys(message)

        time.sleep(10)

        # Move to the "Send" button
        pywinauto.mouse.move(coords=(1070, 500))

        time.sleep(5)

        # Click left on the "Send" button
        #pywinauto.mouse.click(button='left', coords=(1070, 500))

        time.sleep(10)

    def test_send_sms_for_love_meeting_from_phone_numbers(self):
        phone_numbers = [

        ]

        app = Application(backend="uia")

        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(5)

        # Open the TP Link Modem Web Page
        pywinauto.keyboard.send_keys("http://tplinkmodem.net/")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(5)

        # Enter the password
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        # Enter
        pywinauto.keyboard.send_keys("{ENTER}")

        time.sleep(10)

        # Click left on "Advanced" button
        pywinauto.mouse.click(button='left', coords=(750, 130))

        time.sleep(5)

        # Click left on "SMS" button
        pywinauto.mouse.click(button='left', coords=(250, 400))

        time.sleep(5)

        # Click left on "New message" button
        pywinauto.mouse.click(button='left', coords=(270, 335))

        time.sleep(5)

        for phone_number in phone_numbers:
            # Click left on "Phone Number:" input
            pywinauto.mouse.click(button='left', coords=(670, 255))

            time.sleep(5)

            # Type a phone umber
            pywinauto.keyboard.send_keys(phone_number)

            time.sleep(5)

            # Click left on "Content:" input
            pywinauto.mouse.click(button='left', coords=(670, 350))

            time.sleep(5)

            message = ""

            # Type a text message
            pywinauto.keyboard.send_keys(message)

            time.sleep(10)

            # Move to the "Send" button
            pywinauto.mouse.move(coords=(1070, 500))

            time.sleep(5)

            # Click left on the "Send" button
            pywinauto.mouse.click(button='left', coords=(1070, 500))

            time.sleep(10)


if __name__ == '__main__':
    unittest.main()
