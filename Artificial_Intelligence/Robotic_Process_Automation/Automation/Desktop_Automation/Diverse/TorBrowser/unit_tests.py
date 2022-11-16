import os
import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse


class UnitTestsDesktopAutomationTorBrowser(unittest.TestCase):
    def test_open_window_for_showing_videos(self):
        app = Application(backend="uia")

        time.sleep(5)

        # Ouvrir l'application Tor Browser
        app.start("C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")

        videos = [
            'https://www.youtube.com/watch?v=vQC_QkgFbkc'
        ]

        for video in videos:
            time.sleep(15)

            # Big window
            pywinauto.mouse.click(button='left', coords=(940, 20))

            time.sleep(5)

            # Select the url bar
            pywinauto.mouse.click(button='left', coords=(240, 50))

            time.sleep(5)

            # Type the website address
            pywinauto.keyboard.send_keys(video)

            time.sleep(5)

            # Type the website address
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(60)

            # Click on the video
            pywinauto.mouse.click(button='left', coords=(420, 320))

            time.sleep(60)

            # New identity (Ctrl + Shift + U)
            pywinauto.keyboard.send_keys('^+u')

    def test_new_identity(self):
        app = Application(backend="uia")

        time.sleep(5)

        # Ouvrir l'application Tor Browser
        app.start("C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")

        time.sleep(15)

        # New identity (Ctrl + Shift + U)
        pywinauto.keyboard.send_keys('^+u')

    def test_open_window_for_showing_free_energy_feedback(self):
        app = Application(backend="uia")

        time.sleep(5)

        # Ouvrir l'application Tor Browser
        app.start("C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")

        for i in range(3):
            time.sleep(15)

            # Big window
            pywinauto.mouse.click(button='left', coords=(940, 20))

            time.sleep(5)

            # Select the url bar
            pywinauto.mouse.click(button='left', coords=(240, 50))

            time.sleep(5)

            # Type the website address
            pywinauto.keyboard.send_keys('')

            time.sleep(5)

            # Type the website address
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(60)

            # Click on the video
            pywinauto.mouse.click(button='left', coords=(420, 320))

            time.sleep(60)

            # New identity (Ctrl + Shift + U)
            pywinauto.keyboard.send_keys('^+u')


class UnitTestsDesktopAutomationTorBrowserHolomorpheWebsite(unittest.TestCase):
    def test_display_and_click_ads_from_all_urls(self):
        print("test_display_and_click_business_model_canvas")

        app = Application(backend="uia")

        urls = [
            "https://www.holomorphe.com",
            "https://www.holomorphe.com/chemical-products/gas-mixture-of-pure-dihydrogen",
            "https://www.holomorphe.com/chemical-products/fundamental-research-of-the-us-patent-us4936961a",
            "https://www.holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser",
            "https://www.holomorphe.com/chemical-products/comparison_of_electrolysers",
            "https://www.holomorphe.com/chemical-products/investment",
            "https://www.holomorphe.com/reporting/business_model_canvas",
            "https://www.holomorphe.com/reporting/business_plan",
            "https://www.holomorphe.com/reporting/use_case_form",
            "https://www.holomorphe.com/reporting/kanban_board",
            "https://www.holomorphe.com/reporting/gap_analysis",
            "https://www.holomorphe.com/reporting/job_analysis",
            "https://www.holomorphe.com/reporting/pricing_strategy",
            "https://www.holomorphe.com/cad/patent_us_4661747",
            "https://www.holomorphe.com/application-software-editions/",
            "https://www.holomorphe.com/tax-haven/corporation-tax",
            "https://www.holomorphe.com/tax-haven/vat-tax",
            "https://www.holomorphe.com/tax-haven/eu-members",
            "https://www.holomorphe.com/tax-haven/currency",
            "https://www.holomorphe.com/tax-haven/carry-forward-of-ordinary-tax-losses",
            "https://www.holomorphe.com/tax-haven/carry-back-of-ordinary-tax-losses",
            "https://www.holomorphe.com/tax-haven/capital-gains-tax-rate",
            "https://www.holomorphe.com/tax-haven/capital-losses",
            "https://www.holomorphe.com/tax-haven/vat-reduced-rate",
            "https://www.holomorphe.com/tax-haven/vat-registration-threshhold",
            "https://www.holomorphe.com/tax-haven/vat-filing-and-payment",
            "https://www.holomorphe.com/tax-haven/other-taxes",
            "https://www.holomorphe.com/tax-haven/taxable-period",
            "https://www.holomorphe.com/tax-haven/tax-return-requirement",
            "https://www.holomorphe.com/tax-haven/tax-return-due-date",
            "https://www.holomorphe.com/tax-haven/tax-residency-requirements",
            "https://www.holomorphe.com/tax-haven/tax-rate-on-dividends-from-local-investments",
            "https://www.holomorphe.com/tax-haven/tax-rate-on-dividends-from-foreign-investments",
            "https://www.holomorphe.com/tax-haven/withholding-tax-on-dividend-payments-to-foreign-shareholders",
            "https://www.holomorphe.com/tax-haven/tax-rate-on-interest-income",
            "https://www.holomorphe.com/tax-haven/withholding-tax-on-interest-payments-to-foreign-recipients",
            "https://www.holomorphe.com/tax-haven/tax-deductibility-of-interest-expense",
            "https://www.holomorphe.com/tax-haven/tax-rate-on-royalty-income",
            "https://www.holomorphe.com/tax-haven/withholding-tax-on-royalty-payments-to-foreign-recipients",
            "https://www.holomorphe.com/tax-haven/tax-deductibility-of-royalty-expense",
            "https://www.holomorphe.com/tax-haven/taxability-of-disposal-of-shares-by-foreign-shareholder",
            "https://www.holomorphe.com/tax-haven/taxation-of-partnership-profits",
            "https://www.holomorphe.com/tax-haven/taxation-of-branch-profits",
            "https://www.holomorphe.com/tax-haven/branch-remittance-tax",
            "https://www.holomorphe.com/tax-haven/stamp-duty",
            "https://www.holomorphe.com/tax-haven/spoken-languages",
            "https://www.holomorphe.com/tax-haven/oecd-members",
            "https://www.holomorphe.com/tax-haven/death-penalty",
            "https://www.holomorphe.com/tax-haven/airport",
            "https://www.holomorphe.com/tax-haven/average-lowest-temperature",
            "https://www.holomorphe.com/tax-haven/average-annual-precipitation",
            "https://www.holomorphe.com/tax-haven/registry-of-commerce",
            "https://www.holomorphe.com/tax-haven/highest-personal-income-tax",
            "https://www.holomorphe.com/tax-haven/land-area",
            "https://www.holomorphe.com/tax-haven/population",
            "https://www.holomorphe.com/tax-haven/taxation-on-foreign-income",
            "https://www.holomorphe.com/tax-haven/net-worth-tax",
            "https://www.holomorphe.com/tax-haven/free-mobile-operator",
            "https://www.holomorphe.com/tax-haven/become-permanent-resident",
            "https://www.holomorphe.com/tax-haven/social-security-rate-for-corporations",
            "https://www.holomorphe.com/tax-haven/social-security-rate-for-employees",
            "https://www.holomorphe.com/tax-haven/post-office-box-for-private-person",
            "https://www.holomorphe.com/tax-haven/tax-treaties",
            "https://www.holomorphe.com/tax-haven/tax-information-exchange-agreements",
            "https://www.holomorphe.com/tax-haven/company-liability-of-shareholder",
            "https://www.holomorphe.com/tax-haven/company-minimum-number-of-shareholder",
            "https://www.holomorphe.com/tax-haven/company-maximum-number-of-shareholder",
            "https://www.holomorphe.com/tax-haven/company-restriction-on-nationality-residency-of-shareholder",
            "https://www.holomorphe.com/tax-haven/company-corporate-shareholders-allowe",
            "https://www.holomorphe.com/tax-haven/company-minimum-number-of-director",
            "https://www.holomorphe.com/tax-haven/company-restriction-on-nationality-residency-of-director",
            "https://www.holomorphe.com/tax-haven/company-local-director-requiremen",
            "https://www.holomorphe.com/tax-haven/company-corporate-directors-allowe",
            "https://www.holomorphe.com/tax-haven/company-shareholders--meeting-requiremen",
            "https://www.holomorphe.com/tax-haven/company-shareholders--meetings-locatio",
            "https://www.holomorphe.com/tax-haven/company-minimum-capital-requiremen",
            "https://www.holomorphe.com/tax-haven/company-can-the-capital-be-denominated-in-foreign-currenc",
            "https://www.holomorphe.com/tax-haven/company-non-par-value-shares-allowe",
            "https://www.holomorphe.com/tax-haven/company-bearer-shares-allowe",
            "https://www.holomorphe.com/tax-haven/company-capital-duty-on-issurance-of-share",
            "https://www.holomorphe.com/tax-haven/company-registered-office-needs-to-be-in-the-countr",
            "https://www.holomorphe.com/tax-haven/company-company-secretary-registered-agent-requiremen",
            "https://www.holomorphe.com/tax-haven/company-restrictions-to-foreign-investor",
            "https://www.holomorphe.com/tax-haven/company-time-needed-for-registratio",
            "https://www.holomorphe.com/tax-haven/company-shelf-companies-availabl",
            "https://www.holomorphe.com/tax-haven/company-publicly-accessible-records-of-director",
            "https://www.holomorphe.com/tax-haven/company-publicly-accessible-records-of-shareholder",
            "https://www.holomorphe.com/tax-haven/company-publicly-accessible-financial-statements",
            "https://www.holomorphe.com/tax-haven/company-beneficial-ownership-disclosure",
            "https://www.holomorphe.com/tax-haven/company-nominee-shareholder-allowed",
            "https://www.holomorphe.com/tax-haven/company-annual-return-requirement",
            "https://www.holomorphe.com/tax-haven/company-tax-return-requirement",
            "https://www.holomorphe.com/tax-haven/company-requirement-to-maintain-accounting-records",
            "https://www.holomorphe.com/tax-haven/company-foreign-currency-accounting-allowed",
            "https://www.holomorphe.com/tax-haven/company-accounting-records-can-be-held-outside-the-country",
            "https://www.holomorphe.com/tax-haven/company-financial-statements-requirement",
            "https://www.holomorphe.com/tax-haven/company-financial-statements-filing-requirement",
            "https://www.holomorphe.com/tax-haven/company-accounting-principles-for-financial-statement",
            "https://www.holomorphe.com/tax-haven/company-consolidated-financial-statements-requirement",
            "https://www.holomorphe.com/tax-haven/company-exemption-to-consolidated-financial-statements-requirement",
            "https://www.holomorphe.com/tax-haven/company-audit-requirement",
            "https://www.holomorphe.com/tax-haven/company-exemptions-to-audit-requirement",
            "https://www.holomorphe.com/tax-haven/trust-registration-requiremen",
            "https://www.holomorphe.com/tax-haven/trust-settlor-residency-requiremen",
            "https://www.holomorphe.com/tax-haven/trust-beneficiary-residency-requiremen",
            "https://www.holomorphe.com/tax-haven/trust-trustee-residency-requiremen",
            "https://www.holomorphe.com/tax-haven/trust-should-the-trustee-be-license",
            "https://www.holomorphe.com/tax-haven/trust-protector-allowe",
            "https://www.holomorphe.com/tax-haven/trust-protector-requiremen",
            "https://www.holomorphe.com/tax-haven/trust-perpetuity-perio",
            "https://www.holomorphe.com/tax-haven/trust-restriction-on-trust-propert",
            "https://www.holomorphe.com/tax-haven/trust-taxatio",
            "https://www.holomorphe.com/tax-haven/trust-confidentialit",
            "https://www.holomorphe.com/tax-haven/trust-asset-protectio",
            "https://www.holomorphe.com/tax-haven/trust-reporting-requiremen",
            "https://www.holomorphe.com/contents/international_energy",
            "https://www.holomorphe.com/contents/international_free_trade_agreements",
            "https://www.holomorphe.com/contents/international_lands_for_injecting_gas",
            "https://www.holomorphe.com/contents/international_electricity_generation_without_license",
            "https://www.holomorphe.com/contents/countries_with_gas_networks",
            "https://www.holomorphe.com/contents/international_energy_needs_for_abundance",
            "https://www.holomorphe.com/contents/forecast_of_worldwide_ammonia_production",
            "https://www.holomorphe.com/contents/forecast_of_worldwide_natural_gas_reserves",
            "https://www.holomorphe.com/contents/international_real_estate_price",
            "https://www.holomorphe.com/contents/international_plastic_waste",
            "https://www.holomorphe.com/contents/forecast_of_worldwide_coal_reserves",
            "https://www.holomorphe.com/contents/forcecast_of_worldwide_crude_oil_reserves",
            "https://www.holomorphe.com/contents/forecast_of_worldwide_uranium_reserves",
            "https://www.holomorphe.com/contents/worldwide_mercury_producers",
            "https://www.holomorphe.com/contents/countries_ratified_minamata_convention",
            "https://www.holomorphe.com/legal-notice/",
            "https://www.holomorphe.com/terms-and-conditions/",
            "https://www.holomorphe.com/contact/"
        ]

        for url in urls:
            time.sleep(5)

            # Ouvrir l'application Tor Browser
            app.start("C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")

            time.sleep(30)

            # New identity (Ctrl + Shift + U)
            pywinauto.keyboard.send_keys('^+u')

            time.sleep(15)

            # Big window
            pywinauto.mouse.click(button='left', coords=(940, 20))

            time.sleep(10)

            # Select the url bar
            pywinauto.mouse.click(button='left', coords=(240, 50))

            time.sleep(10)

            # Type the website address
            pywinauto.keyboard.send_keys(url)

            time.sleep(5)

            # Type ENTER
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(30)

            # Scroll down several times
            for i in range(50):
                time.sleep(2)

                pywinauto.keyboard.send_keys('{DOWN}')

            time.sleep(15)

            # Click on the last ad
            # pywinauto.mouse.click(button='left', coords=(240, 50))
            # time.sleep(10)

            # Close the browser (Alt + F4)
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)

            # start ccleaner
            print("ccleaner running")
            os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
            os.system("start ccleaner /AUTO")

            time.sleep(5)


if __name__ == '__main__':
    unittest.main()
