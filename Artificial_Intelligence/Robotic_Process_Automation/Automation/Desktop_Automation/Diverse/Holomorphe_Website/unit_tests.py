import os
import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse


class UnitTestsDesktopAutomationHolomorpheWebsite(unittest.TestCase):
    def test_holomorphe_website_working_well_with_google_chrome(self):
        print("test_holomorphe_website_working_well_with_google_chrome")

        app = Application(backend="uia")

        urls = [
            "http://127.0.0.1:8000/tax-haven/corporation-tax",
            "http://127.0.0.1:8000/tax-haven/vat-tax",
            "http://127.0.0.1:8000/produits-chimiques/vehicules-hydrogene",
            "http://127.0.0.1:8000/edition-logiciels-applicatifs/",
            "http://127.0.0.1:8000/tax-haven/eu-members",
            "http://127.0.0.1:8000/tax-haven/currency",
            "http://127.0.0.1:8000/tax-haven/carry-forward-of-ordinary-tax-losses",
            "http://127.0.0.1:8000/tax-haven/carry-back-of-ordinary-tax-losses",
            "http://127.0.0.1:8000/tax-haven/capital-gains-tax-rate",
            "http://127.0.0.1:8000/tax-haven/capital-losses",
            "http://127.0.0.1:8000/tax-haven/vat-reduced-rate",
            "http://127.0.0.1:8000/tax-haven/vat-registration-threshhold",
            "http://127.0.0.1:8000/tax-haven/vat-filing-and-payment",
            "http://127.0.0.1:8000/tax-haven/other-taxes",
            "http://127.0.0.1:8000/tax-haven/taxable-period",
            "http://127.0.0.1:8000/tax-haven/tax-return-requirement",
            "http://127.0.0.1:8000/tax-haven/tax-return-due-date",
            "http://127.0.0.1:8000/tax-haven/tax-residency-requirements",
            "http://127.0.0.1:8000/tax-haven/tax-rate-on-dividends-from-local-investments",
            "http://127.0.0.1:8000/tax-haven/tax-rate-on-dividends-from-foreign-investments",
            "http://127.0.0.1:8000/tax-haven/withholding-tax-on-dividend-payments-to-foreign-shareholders",
            "http://127.0.0.1:8000/tax-haven/tax-rate-on-interest-income",
            "http://127.0.0.1:8000/tax-haven/withholding-tax-on-interest-payments-to-foreign-recipients",
            "http://127.0.0.1:8000/tax-haven/tax-deductibility-of-interest-expense",
            "http://127.0.0.1:8000/tax-haven/tax-rate-on-royalty-income",
            "http://127.0.0.1:8000/tax-haven/withholding-tax-on-royalty-payments-to-foreign-recipients",
            "http://127.0.0.1:8000/tax-haven/tax-deductibility-of-royalty-expense",
            "http://127.0.0.1:8000/tax-haven/taxability-of-disposal-of-shares-by-foreign-shareholder",
            "http://127.0.0.1:8000/tax-haven/taxation-of-partnership-profits",
            "http://127.0.0.1:8000/tax-haven/taxation-of-branch-profits",
            "http://127.0.0.1:8000/tax-haven/branch-remittance-tax",
            "http://127.0.0.1:8000/tax-haven/stamp-duty",
            "http://127.0.0.1:8000/tax-haven/spoken-languages",
            "http://127.0.0.1:8000/tax-haven/oecd-members",
            "http://127.0.0.1:8000/tax-haven/death-penalty",
            "http://127.0.0.1:8000/tax-haven/airport",
            "http://127.0.0.1:8000/tax-haven/average-lowest-temperature",
            "http://127.0.0.1:8000/tax-haven/average-annual-precipitation",
            "http://127.0.0.1:8000/tax-haven/registry-of-commerce",
            "http://127.0.0.1:8000/tax-haven/highest-personal-income-tax",
            "http://127.0.0.1:8000/tax-haven/land-area",
            "http://127.0.0.1:8000/tax-haven/population",
            "http://127.0.0.1:8000/tax-haven/taxation-on-foreign-income",
            "http://127.0.0.1:8000/tax-haven/net-worth-tax",
            "http://127.0.0.1:8000/tax-haven/free-mobile-operator",
            "http://127.0.0.1:8000/tax-haven/become-permanent-resident",
            "http://127.0.0.1:8000/tax-haven/social-security-rate-for-corporations",
            "http://127.0.0.1:8000/tax-haven/social-security-rate-for-employees",
            "http://127.0.0.1:8000/tax-haven/post-office-box-for-private-person",
            "http://127.0.0.1:8000/tax-haven/tax-treaties",
            "http://127.0.0.1:8000/tax-haven/tax-information-exchange-agreements",
            "http://127.0.0.1:8000/tax-haven/company-liability-of-shareholder",
            "http://127.0.0.1:8000/tax-haven/company-minimum-number-of-shareholder",
            "http://127.0.0.1:8000/tax-haven/company-maximum-number-of-shareholder",
            "http://127.0.0.1:8000/tax-haven/company-restriction-on-nationality-residency-of-shareholder",
            "http://127.0.0.1:8000/tax-haven/company-corporate-shareholders-allowe",
            "http://127.0.0.1:8000/tax-haven/company-minimum-number-of-director",
            "http://127.0.0.1:8000/tax-haven/company-restriction-on-nationality-residency-of-director",
            "http://127.0.0.1:8000/tax-haven/company-local-director-requiremen",
            "http://127.0.0.1:8000/tax-haven/company-corporate-directors-allowe",
            "http://127.0.0.1:8000/tax-haven/company-shareholders--meeting-requiremen",
            "http://127.0.0.1:8000/tax-haven/company-shareholders--meetings-locatio",
            "http://127.0.0.1:8000/tax-haven/company-minimum-capital-requiremen",
            "http://127.0.0.1:8000/tax-haven/company-can-the-capital-be-denominated-in-foreign-currenc",
            "http://127.0.0.1:8000/tax-haven/company-non-par-value-shares-allowe",
            "http://127.0.0.1:8000/tax-haven/company-bearer-shares-allowe",
            "http://127.0.0.1:8000/tax-haven/company-capital-duty-on-issurance-of-share",
            "http://127.0.0.1:8000/tax-haven/company-registered-office-needs-to-be-in-the-countr",
            "http://127.0.0.1:8000/tax-haven/company-company-secretary-registered-agent-requiremen",
            "http://127.0.0.1:8000/tax-haven/company-restrictions-to-foreign-investor",
            "http://127.0.0.1:8000/tax-haven/company-time-needed-for-registratio",
            "http://127.0.0.1:8000/tax-haven/company-shelf-companies-availabl",
            "http://127.0.0.1:8000/tax-haven/company-publicly-accessible-records-of-director",
            "http://127.0.0.1:8000/tax-haven/company-publicly-accessible-records-of-shareholder",
            "http://127.0.0.1:8000/tax-haven/company-publicly-accessible-financial-statements",
            "http://127.0.0.1:8000/tax-haven/company-beneficial-ownership-disclosure",
            "http://127.0.0.1:8000/tax-haven/company-nominee-shareholder-allowed",
            "http://127.0.0.1:8000/tax-haven/company-annual-return-requirement",
            "http://127.0.0.1:8000/tax-haven/company-tax-return-requirement",
            "http://127.0.0.1:8000/tax-haven/company-requirement-to-maintain-accounting-records",
            "http://127.0.0.1:8000/tax-haven/company-foreign-currency-accounting-allowed",
            "http://127.0.0.1:8000/tax-haven/company-accounting-records-can-be-held-outside-the-country",
            "http://127.0.0.1:8000/tax-haven/company-financial-statements-requirement",
            "http://127.0.0.1:8000/tax-haven/company-financial-statements-filing-requirement",
            "http://127.0.0.1:8000/tax-haven/company-accounting-principles-for-financial-statement",
            "http://127.0.0.1:8000/tax-haven/company-consolidated-financial-statements-requirement",
            "http://127.0.0.1:8000/tax-haven/company-exemption-to-consolidated-financial-statements-requirement",
            "http://127.0.0.1:8000/tax-haven/company-audit-requirement",
            "http://127.0.0.1:8000/tax-haven/company-exemptions-to-audit-requirement",
            "http://127.0.0.1:8000/tax-haven/trust-registration-requiremen",
            "http://127.0.0.1:8000/tax-haven/trust-settlor-residency-requiremen",
            "http://127.0.0.1:8000/tax-haven/trust-beneficiary-residency-requiremen",
            "http://127.0.0.1:8000/tax-haven/trust-trustee-residency-requiremen",
            "http://127.0.0.1:8000/tax-haven/trust-should-the-trustee-be-license",
            "http://127.0.0.1:8000/tax-haven/trust-protector-allowe",
            "http://127.0.0.1:8000/tax-haven/trust-protector-requiremen",
            "http://127.0.0.1:8000/tax-haven/trust-perpetuity-perio",
            "http://127.0.0.1:8000/tax-haven/trust-restriction-on-trust-propert",
            "http://127.0.0.1:8000/tax-haven/trust-taxatio",
            "http://127.0.0.1:8000/tax-haven/trust-confidentialit",
            "http://127.0.0.1:8000/tax-haven/trust-asset-protectio",
            "http://127.0.0.1:8000/tax-haven/trust-reporting-requiremen"
        ]

        for i in range(20):
            for url in urls:
                time.sleep(5)

                # Ouvrir l'application Google Chrome
                app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                time.sleep(10)

                # Type the website address
                pywinauto.keyboard.send_keys(url)

                time.sleep(5)

                # Type Enter button
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(10)

                # Press down button in 10 times
                pywinauto.keyboard.send_keys('{DOWN 15}')

                time.sleep(5)

                # Close the browser
                pywinauto.keyboard.send_keys('%{F4}')

                time.sleep(3)

                # clean the PC with Ccleaner commande-line
                os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                os.system("start ccleaner /AUTO")

                time.sleep(25)

    def test_holomorphe_website_working_well_with_tor_browser(self):
        print("test_holomorphe_website_working_well_with_tor_browser")

        app = Application(backend="uia")

        time.sleep(5)

        urls = [
            "https://holomorphe.com/",
            "https://holomorphe.com/chemical-products/gas-mixture-of-pure-dihydrogen",
            "https://holomorphe.com/chemical-products/fundamental-research-of-the-us-patent-us4936961a",
            "https://holomorphe.com/chemical-products/cad-stanley-meyer-water-electrolyser",
            "https://holomorphe.com/chemical-products/comparison_of_electrolysers",
            "https://holomorphe.com/chemical-products/investment",
            "https://holomorphe.com/reporting/business_model_canvas",
            "https://holomorphe.com/reporting/business_plan",
            "https://holomorphe.com/reporting/use_case_form",
            "https://holomorphe.com/reporting/kanban_board",
            "https://holomorphe.com/reporting/gap_analysis",
            "https://holomorphe.com/reporting/job_analysis",
            "https://holomorphe.com/reporting/pricing_strategy",
            "https://holomorphe.com/reporting/value_proposition_canvas",
            "https://holomorphe.com/reporting/business_plan_cleaning_services",
            "https://holomorphe.com/reporting/competitor_worksheet",
            "https://holomorphe.com/reporting/operational_plan",
            "https://holomorphe.com/reporting/swot_analysis",
            "https://holomorphe.com/reporting/business_requirement_document",
            "https://holomorphe.com/reporting/target_market_worksheet",
            "https://holomorphe.com/reporting/product_service_worksheet",
            "https://holomorphe.com/reporting/marketing_plan",
            "https://holomorphe.com/reporting/fund_sources_and_uses",
            "https://holomorphe.com/reporting/physical_inventory_count_sheet",
            "https://holomorphe.com/reporting/operational_budget",
            "https://holomorphe.com/reporting/vendor_contact_sheet",
            "https://holomorphe.com/reporting/petty_cash_journal",
            "https://holomorphe.com/reporting/vendor_product_pricing_sheet",
            "https://holomorphe.com/reporting/vendor_comparison_worksheet",
            "https://holomorphe.com/reporting/business_goals_worksheet",
            "https://holomorphe.com/reporting/daily_business_log_sheet",
            "https://holomorphe.com/reporting/employee_log_sheet",
            "https://holomorphe.com/reporting/management_plan",
            "https://holomorphe.com/reporting/risk_management_worksheet",
            "https://holomorphe.com/reporting/vendor_service_pricing_sheet",
            "https://holomorphe.com/reporting/start_up_budget_calculator",
            "https://holomorphe.com/reporting/monthly_budget",
            "https://holomorphe.com/reporting/project_budget",
            "https://holomorphe.com/reporting/quarterly_budget",
            "https://holomorphe.com/reporting/annual_budget",
            "https://holomorphe.com/reporting/twelve_month_budget_forecast",
            "https://holomorphe.com/reporting/start_up_budget_variance",
            "https://holomorphe.com/reporting/flexible_static_budget_variance",
            "https://holomorphe.com/reporting/twelve_month_marketing_budget",
            "https://holomorphe.com/reporting/twelve_month_marketing_budget_variance",
            "https://holomorphe.com/reporting/flexible_budget_variance",
            "https://holomorphe.com/reporting/month_operating_budget_variance",
            "https://holomorphe.com/reporting/static_budget_variance",
            "https://holomorphe.com/reporting/static_budget",
            "https://holomorphe.com/reporting/flexible_budget",
            "https://holomorphe.com/reporting/annual_expense_budget",
            "https://holomorphe.com/reporting/department_budget",
            "https://holomorphe.com/reporting/twelve_month_operating_budget",
            "https://holomorphe.com/cad/patent_us_4661747",
            "https://holomorphe.com/application-software-editions/",
            "https://holomorphe.com/tax-haven/",
            "https://holomorphe.com/contents/international_energy",
            "https://holomorphe.com/contents/international_free_trade_agreements",
            "https://holomorphe.com/contents/international_lands_for_injecting_gas",
            "https://holomorphe.com/contents/international_electricity_generation_without_license",
            "https://holomorphe.com/contents/countries_with_gas_networks",
            "https://holomorphe.com/contents/international_energy_needs_for_abundance",
            "https://holomorphe.com/contents/forecast_of_worldwide_ammonia_production",
            "https://holomorphe.com/contents/forecast_of_worldwide_natural_gas_reserves",
            "https://holomorphe.com/contents/international_real_estate_price",
            "https://holomorphe.com/contents/international_plastic_waste",
            "https://holomorphe.com/contents/forecast_of_worldwide_coal_reserves",
            "https://holomorphe.com/contents/forcecast_of_worldwide_crude_oil_reserves",
            "https://holomorphe.com/contents/forecast_of_worldwide_uranium_reserves",
            "https://holomorphe.com/contents/worldwide_mercury_producers",
            "https://holomorphe.com/contents/countries_ratified_minamata_convention",
            "https://holomorphe.com/legal-notice/",
            "https://holomorphe.com/terms-and-conditions/",
            "https://holomorphe.com/contact/",
            "https://holomorphe.com/tax-haven/corporation-tax",
            "https://holomorphe.com/tax-haven/vat-tax",
            "https://holomorphe.com/tax-haven/eu-members",
            "https://holomorphe.com/tax-haven/currency",
            "https://holomorphe.com/tax-haven/carry-forward-of-ordinary-tax-losses",
            "https://holomorphe.com/tax-haven/carry-back-of-ordinary-tax-losses",
            "https://holomorphe.com/tax-haven/capital-gains-tax-rate",
            "https://holomorphe.com/tax-haven/capital-losses",
            "https://holomorphe.com/tax-haven/vat-reduced-rate",
            "https://holomorphe.com/tax-haven/vat-registration-threshhold",
            "https://holomorphe.com/tax-haven/vat-filing-and-payment",
            "https://holomorphe.com/tax-haven/other-taxes",
            "https://holomorphe.com/tax-haven/taxable-period",
            "https://holomorphe.com/tax-haven/tax-return-requirement",
            "https://holomorphe.com/tax-haven/tax-return-due-date",
            "https://holomorphe.com/tax-haven/tax-residency-requirements",
            "https://holomorphe.com/tax-haven/tax-rate-on-dividends-from-local-investments",
            "https://holomorphe.com/tax-haven/tax-rate-on-dividends-from-foreign-investments",
            "https://holomorphe.com/tax-haven/withholding-tax-on-dividend-payments-to-foreign-shareholders",
            "https://holomorphe.com/tax-haven/tax-rate-on-interest-income",
            "https://holomorphe.com/tax-haven/withholding-tax-on-interest-payments-to-foreign-recipients",
            "https://holomorphe.com/tax-haven/tax-deductibility-of-interest-expense",
            "https://holomorphe.com/tax-haven/tax-rate-on-royalty-income",
            "https://holomorphe.com/tax-haven/withholding-tax-on-royalty-payments-to-foreign-recipients",
            "https://holomorphe.com/tax-haven/tax-deductibility-of-royalty-expense",
            "https://holomorphe.com/tax-haven/taxability-of-disposal-of-shares-by-foreign-shareholder",
            "https://holomorphe.com/tax-haven/taxation-of-partnership-profits",
            "https://holomorphe.com/tax-haven/taxation-of-branch-profits",
            "https://holomorphe.com/tax-haven/branch-remittance-tax",
            "https://holomorphe.com/tax-haven/stamp-duty",
            "https://holomorphe.com/tax-haven/spoken-languages",
            "https://holomorphe.com/tax-haven/oecd-members",
            "https://holomorphe.com/tax-haven/death-penalty",
            "https://holomorphe.com/tax-haven/airport",
            "https://holomorphe.com/tax-haven/average-lowest-temperature",
            "https://holomorphe.com/tax-haven/average-annual-precipitation",
            "https://holomorphe.com/tax-haven/registry-of-commerce",
            "https://holomorphe.com/tax-haven/highest-personal-income-tax",
            "https://holomorphe.com/tax-haven/land-area",
            "https://holomorphe.com/tax-haven/population",
            "https://holomorphe.com/tax-haven/taxation-on-foreign-income",
            "https://holomorphe.com/tax-haven/net-worth-tax",
            "https://holomorphe.com/tax-haven/free-mobile-operator",
            "https://holomorphe.com/tax-haven/become-permanent-resident",
            "https://holomorphe.com/tax-haven/social-security-rate-for-corporations",
            "https://holomorphe.com/tax-haven/social-security-rate-for-employees",
            "https://holomorphe.com/tax-haven/post-office-box-for-private-person",
            "https://holomorphe.com/tax-haven/tax-treaties",
            "https://holomorphe.com/tax-haven/tax-information-exchange-agreements",
            "https://holomorphe.com/tax-haven/company-liability-of-shareholder",
            "https://holomorphe.com/tax-haven/company-minimum-number-of-shareholder",
            "https://holomorphe.com/tax-haven/company-maximum-number-of-shareholder",
            "https://holomorphe.com/tax-haven/company-restriction-on-nationality-residency-of-shareholder",
            "https://holomorphe.com/tax-haven/company-corporate-shareholders-allowe",
            "https://holomorphe.com/tax-haven/company-minimum-number-of-director",
            "https://holomorphe.com/tax-haven/company-restriction-on-nationality-residency-of-director",
            "https://holomorphe.com/tax-haven/company-local-director-requiremen",
            "https://holomorphe.com/tax-haven/company-corporate-directors-allowe",
            "https://holomorphe.com/tax-haven/company-shareholders--meeting-requiremen",
            "https://holomorphe.com/tax-haven/company-shareholders--meetings-locatio",
            "https://holomorphe.com/tax-haven/company-minimum-capital-requiremen",
            "https://holomorphe.com/tax-haven/company-can-the-capital-be-denominated-in-foreign-currenc",
            "https://holomorphe.com/tax-haven/company-non-par-value-shares-allowe",
            "https://holomorphe.com/tax-haven/company-bearer-shares-allowe",
            "https://holomorphe.com/tax-haven/company-capital-duty-on-issurance-of-share",
            "https://holomorphe.com/tax-haven/company-registered-office-needs-to-be-in-the-countr",
            "https://holomorphe.com/tax-haven/company-company-secretary-registered-agent-requiremen",
            "https://holomorphe.com/tax-haven/company-restrictions-to-foreign-investor",
            "https://holomorphe.com/tax-haven/company-time-needed-for-registratio",
            "https://holomorphe.com/tax-haven/company-shelf-companies-availabl",
            "https://holomorphe.com/tax-haven/company-publicly-accessible-records-of-director",
            "https://holomorphe.com/tax-haven/company-publicly-accessible-records-of-shareholder",
            "https://holomorphe.com/tax-haven/company-publicly-accessible-financial-statements",
            "https://holomorphe.com/tax-haven/company-beneficial-ownership-disclosure",
            "https://holomorphe.com/tax-haven/company-nominee-shareholder-allowed",
            "https://holomorphe.com/tax-haven/company-annual-return-requirement",
            "https://holomorphe.com/tax-haven/company-tax-return-requirement",
            "https://holomorphe.com/tax-haven/company-requirement-to-maintain-accounting-records",
            "https://holomorphe.com/tax-haven/company-foreign-currency-accounting-allowed",
            "https://holomorphe.com/tax-haven/company-accounting-records-can-be-held-outside-the-country",
            "https://holomorphe.com/tax-haven/company-financial-statements-requirement",
            "https://holomorphe.com/tax-haven/company-financial-statements-filing-requirement",
            "https://holomorphe.com/tax-haven/company-accounting-principles-for-financial-statement",
            "https://holomorphe.com/tax-haven/company-consolidated-financial-statements-requirement",
            "https://holomorphe.com/tax-haven/company-exemption-to-consolidated-financial-statements-requirement",
            "https://holomorphe.com/tax-haven/company-audit-requirement",
            "https://holomorphe.com/tax-haven/company-exemptions-to-audit-requirement",
            "https://holomorphe.com/tax-haven/trust-registration-requiremen",
            "https://holomorphe.com/tax-haven/trust-settlor-residency-requiremen",
            "https://holomorphe.com/tax-haven/trust-beneficiary-residency-requiremen",
            "https://holomorphe.com/tax-haven/trust-trustee-residency-requiremen",
            "https://holomorphe.com/tax-haven/trust-should-the-trustee-be-license",
            "https://holomorphe.com/tax-haven/trust-protector-allowe",
            "https://holomorphe.com/tax-haven/trust-protector-requiremen",
            "https://holomorphe.com/tax-haven/trust-perpetuity-perio",
            "https://holomorphe.com/tax-haven/trust-restriction-on-trust-propert",
            "https://holomorphe.com/tax-haven/trust-taxatio",
            "https://holomorphe.com/tax-haven/trust-confidentialit",
            "https://holomorphe.com/tax-haven/trust-asset-protectio",
            "https://holomorphe.com/tax-haven/trust-reporting-requiremen"
        ]

        for i in range(30):
            for url in urls:
                time.sleep(5)

                # Ouvrir l'application Tor Browser
                app.start("C:\\Users\\DELL\\Desktop\\Tor Browser\\Browser\\firefox.exe")

                time.sleep(60)

                # Big window for Tor Browser
                pywinauto.mouse.click(button='left', coords=(940, 50))

                time.sleep(30)

                # Select the url bar
                pywinauto.mouse.click(button='left', coords=(500, 50))

                time.sleep(5)

                # Type the website address
                pywinauto.keyboard.send_keys(url)

                time.sleep(5)

                # Type Enter button
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(60)

                # New identity (Ctrl + Shift + U)
                pywinauto.keyboard.send_keys('^+u')

                time.sleep(5)

                # Type Enter button
                pywinauto.keyboard.send_keys('{ENTER}')

                time.sleep(5)

                # Close the browser
                pywinauto.keyboard.send_keys('^w')

                time.sleep(5)

                # Clean the PC with Ccleaner commande line
                print('ccleaner running')
                os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                os.system("start ccleaner /AUTO")

                time.sleep(60)


if __name__ == '__main__':
    unittest.main()
