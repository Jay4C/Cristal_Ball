import unittest
import xlsxwriter
import os
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from datetime import datetime


class UnitTestsArtificialCreativity(unittest.TestCase):
    def test_print_today_date_and_hour(self):
        print('test_print_today_date_and_hour')

        # datetime object containing current date and time
        now = datetime.now()

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)

    # https://github.com/daviddrysdale/python-phonenumbers
    def test_create_phone_numbers(self):
        print("test_verify_phone_number")

        phone_number = "+33749163329"

        x = phonenumbers.parse(phone_number, None)

        print("x : " + str(x))

        type("type x : " + str(x))

        y = phonenumbers.parse(phone_number, "GB")

        print("y : " + str(y))

        if x == y:
            print("true")
        else:
            print("false")

        z1 = phonenumbers.parse("00 1 650 253 2222", "GB")

        print("z1 : " + str(z1))

        z2 = phonenumbers.parse("+120012301", None)

        print("z2 : " + str(z2))

        print("z1 is possible number : " + str(phonenumbers.is_possible_number(z1)))

        print("z2 is possible number : " + str(phonenumbers.is_possible_number(z2)))

        print("x PhoneNumberFormat.NATIONAL : " + str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)))

        print("x PhoneNumberFormat.INTERNATIONAL : " + str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)))

        print("x PhoneNumberFormat.E164 : " + str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)))

        ch_number = phonenumbers.parse("0431234567", "CH")

        print("geocoder de : " + str(geocoder.description_for_number(ch_number, "de")))

        print("geocoder en : " + str(geocoder.description_for_number(ch_number, "en")))

        print("geocoder fr : " + str(geocoder.description_for_number(ch_number, "fr")))

        print("geocoder it : " + str(geocoder.description_for_number(ch_number, "it")))

        ro_number = phonenumbers.parse("+40721234567", "RO")

        print("carrier : " + carrier.name_for_number(ro_number, "en"))

        gb_number = phonenumbers.parse("+447986123456", "GB")

        print("timezone : " + str(timezone.time_zones_for_number(gb_number)))

    def test_check_if_phone_number_is_valid(self):
        print("test_check_if_phone_number_is_valid")

        phone_number = "+33164062258"

        x = phonenumbers.parse(phone_number, None)

        print("x : " + str(x))

        print("x is possible number : " + str(phonenumbers.is_possible_number(x)))

        print("x is valid number : " + str(phonenumbers.is_valid_number(x)))

        print("x is can_be_internationally_dialled : " + str(phonenumbers.can_be_internationally_dialled(x)))

        print("x is is_sms_service_for_region : " + str(phonenumbers.is_sms_service_for_region(x, "fr")))

        print("x is expected_cost : " + str(phonenumbers.expected_cost(x)))

        print("x PhoneNumberFormat.NATIONAL : " + str(
            phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)))

        print("x PhoneNumberFormat.INTERNATIONAL : " + str(
            phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)))

        print("x PhoneNumberFormat.E164 : " + str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)))

        print("x geocoder fr : " + str(geocoder.description_for_number(x, "fr")))

        print("x carrier : " + carrier.name_for_number(x, "fr"))

        print("x timezone : " + str(timezone.time_zones_for_number(x)))

    def test_create_rpa_lectures(self):
        print("test_create_rpa_lectures")

        main_folder = "C:\\Users\\DELL\\Documents\\Lectures"

        # Writing to file
        with open("lectures.txt", "w") as text_file:
            for folder in os.listdir(main_folder):
                # create a class
                text_file.write("class UnitTestsDesktopAutomationLectures"
                                + folder.replace("_", "").replace("-", "").replace(" ", "").replace(".pdf", "")
                                .replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace('.', '')
                                .replace("�", "").replace("è", "e").replace("é", "e").replace("à", "a").lower()
                                + "(unittest.TestCase):" + "\n")

                for file in os.listdir("C:\\Users\\DELL\\Documents\\Lectures\\" + folder):
                    if ".pdf" in file:
                        # create a test
                        text_file.write("\t" + "def test_" + file.replace("_", "").replace("-", "").replace(" ", "")
                                        .replace(".pdf", "").replace('[', '').replace(']', '').replace('(', '')
                                        .replace(')', '').replace('.', '').replace("�", "").replace("è", "")
                                        .replace("é", "").replace("à", "a").lower() + "(self):" + "\n")

                        text_file.write("\t\t" + "print('test_" + file.replace("_", "").replace("-", "")
                                        .replace(" ", "").replace(".pdf", "") + "')" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + 'cours = "file:///C:/Users/DELL/Documents/Lectures/'
                                        + folder + "/" + file + '"' + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "url_cours = cours.replace('file:///', '').replace('/', '\\\\')" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "pdf = PdfFileReader(open(url_cours, 'rb'))" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "number_of_pages = pdf.getNumPages()" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "time.sleep(5)" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + 'app = Application(backend="uia")' + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + 'app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")' + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "time.sleep(5)" + "\n")

                        text_file.write("\t\t" + "pywinauto.keyboard.send_keys(url_cours)" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "time.sleep(5)" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "pywinauto.keyboard.send_keys('{ENTER}')" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "time.sleep(5)" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "pywinauto.mouse.click(button='left', coords=(900, 250))" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "time.sleep(5)" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "for i in range(0, 14*number_of_pages):" + "\n")

                        text_file.write("\t\t\t" + "pywinauto.keyboard.send_keys('{DOWN}')" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t\t" + "time.sleep(3)" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "time.sleep(5)" + "\n")

                        text_file.write("\n")

                        text_file.write("\t\t" + "pywinauto.keyboard.send_keys('^w')" + "\n")

                        text_file.write("\n")

                text_file.write("\n")

    def test_create_emails_for_dreal_driee(self):
        print("test_create_emails_for_dreal_driee")

        workbook = xlsxwriter.Workbook('emails_dreal_driee.xlsx')

        worksheet = workbook.add_worksheet('data')

        worksheet.write(0, 0, 'emails')

        row = 1

        for i in range(1, 96):
            if (1 <= int(i) <= 9):
                email = "'vehicule0" + str(i) + "@developpement-durable.gouv.fr',"
                worksheet.write(row, 0, email)
                row += 1
            else:
                email = "'vehicule" + str(i) + "@developpement-durable.gouv.fr',"
                worksheet.write(row, 0, email)
                row += 1

        for i in range(1, 96):
            if (1 <= int(i) <= 9):
                email = "'vehicules0" + str(i) + "@developpement-durable.gouv.fr',"
                worksheet.write(row, 0, email)
                row += 1
            else:
                email = "'vehicules" + str(i) + "@developpement-durable.gouv.fr',"
                worksheet.write(row, 0, email)
                row += 1

        numbers = [
            "971",
            "972",
            "973",
            "974",
            "976"
        ]

        for number in numbers:
            email = "'vehicule" + str(number) + "@developpement-durable.gouv.fr',"
            worksheet.write(row, 0, email)
            row += 1

        for number in numbers:
            email = "'vehicules" + str(number) + "@developpement-durable.gouv.fr',"
            worksheet.write(row, 0, email)
            row += 1

        workbook.close()

    def test_create_c_c(self):
        print('test_create_c_c')

        # n_c
        for n_c in range(3000000000000000, 6000000000000000):
            # e_m
            for e_m in range(1, 13):
                # e_a
                for e_a in range(21, 26):
                    # c
                    for c in range(0, 1000):
                        # datetime object containing current date and time
                        now = datetime.now()

                        # dd/mm/YY H:M:S
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        print("date and time =", dt_string)

                        # n_c
                        print("n_c : " + str(n_c))

                        # e_m
                        if e_m < 10:
                            print("e_m : 0" + str(e_m))
                        else:
                            print("e_m : " + str(e_m))

                        # e_a
                        print("e_a : " + str(e_a))

                        # c
                        if c < 10:
                            print("c : 00" + str(c))
                        elif 10 < c < 100:
                            print("c : 0" + str(c))
                        else:
                            print("c : " + str(c))

                        print("\n")


if __name__ == '__main__':
    unittest.main()
