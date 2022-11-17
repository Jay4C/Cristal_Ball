import unittest
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time


class UnitTestsReportingCristalBall(unittest.TestCase):
    def test_display_a_from_table_tradingeconomics(self):
        html = requests.get('https://tradingeconomics.com/country-list/money-supply-m0')
        soup = BeautifulSoup(html.content, 'html.parser')

        a_s = []

        if soup.find("div", {"id": "ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"}) is not None:
            a_s = soup.select('#ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1')[0].find_all('a')

            for a in a_s:
                print('https://tradingeconomics.com' + a.get('href'))

    def test_power_of_10_cells(self):
        url = 'https://tradingeconomics.com/georgia/money-supply-m0'
        tradingeconomics = requests.get(
            'http://127.0.0.1:5000/web_scraping_tradindgeconomics?url=' + url)
        data_tradingeconomics = tradingeconomics.json()
        unit = data_tradingeconomics["unit"].replace(" ", "").replace("Million", " Million").replace(
            "Billion", " Billion").replace("Thousands", " Thousands").replace("\t", "").replace('\r\n', '')

        self.assertEqual(unit[4:], "Thousands")

    def test_workbook_tradingeconomics_world_bank_one_indicator(self):
        workbook = xlsxwriter.Workbook('CristalBall.xlsx')
        worksheet = workbook.add_worksheet('agricultural_area')
        worksheet.write(0, 0, 'Country')  # Column : Country
        worksheet.write(0, 1, 'Value')  # Column : Value

        i = 1

        url = 'https://tradingeconomics.com/country-list/agricultural-area-irrigated-ha-wb-data.html'
        tradingeconomics_world_bank = requests.get('http://127.0.0.1:5000/web_scraping_tradindgeconomics_world_bank?url=' + url)
        data_tradingeconomics_world_bank = tradingeconomics_world_bank.json()

        for worldBankIndicator in data_tradingeconomics_world_bank:
            worksheet.write(i, 0, worldBankIndicator['country'])
            worksheet.write(i, 1, worldBankIndicator['value'])

            i = i + 1

        workbook.close()

    def test_workbook_tradingeconomics_world_bank_multi_indicators(self):
        workbook = xlsxwriter.Workbook('CristalBall.xlsx')

        startTopic = 1
        endTopic = 3

        workbook.close()

    def test_create_worksheet(self):
        workbook = xlsxwriter.Workbook('CristalBall.xlsx')
        worksheet = workbook.add_worksheet('agricultural_area')
        worksheet = workbook.add_worksheet(worksheet)

        worksheet.write(0, 0, 'Country')  # Column : Country
        worksheet.write(0, 1, 'Exchange_Rate_In_Euro_[€]')  # Column : Exchange_Rate_Into_Euro_[€]
        worksheet.write(0, 2, 'Actual')  # Column : Actual
        worksheet.write(0, 3, 'Date')  # Column : Date
        worksheet.write(0, 4, 'Previous')  # Column : Previous
        worksheet.write(0, 5, 'Highest')  # Column : Highest
        worksheet.write(0, 6, 'Lowest')  # Column : Lowest
        worksheet.write(0, 7, 'Unit')  # Column : Unit
        worksheet.write(0, 8, 'Power_Of_10')  # Column : Power_Of_10
        worksheet.write(0, 9, 'Actual_Total')  # Column : Actual_Total
        worksheet.write(0, 10, 'Total_Global')  # Column : Total_Global

        i = 1

        url = ""

        html = requests.get(url)
        time.sleep(3)
        soup = BeautifulSoup(html.content, 'html.parser')
        a_s = []
        link = ''

        if soup.find("div", {"id": "ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"}) is not None:
            a_s = soup.select('#ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1')[
                0].find_all('a')

            for a in a_s:
                link = 'https://tradingeconomics.com' + a.get('href')

                print('Link : ' + link)

                tradingeconomics = requests.get(
                    'http://127.0.0.1:5000/web_scraping_tradindgeconomics?url=' + link)
                data_tradingeconomics = tradingeconomics.json()

                countryName = link[29:].split("/")[0]
                actual = data_tradingeconomics["actual"].replace(".", ",")
                date = data_tradingeconomics["date"]
                previous = data_tradingeconomics["previous"].replace(".", ",")
                highest = data_tradingeconomics["highest"].replace(".", ",")
                lowest = data_tradingeconomics["lowest"].replace(".", ",")
                unit = data_tradingeconomics["unit"].replace(" ", "").replace("Million", " Million").replace(
                    "Billion", " Billion").replace("Thousands", " Thousands").replace("\t", "").replace('\r\n', '')
                url_exchange_rate = 'https://fr.exchange-rates.org/converter/' + \
                                    unit[:3] + '/EUR/1'
                exchange_rate = requests.get(url_exchange_rate)

                # Parse the content of exchange_rate
                soup = BeautifulSoup(exchange_rate.content, 'html.parser')

                data_exchange_rate = ''

                if soup.find("span", {"id": "ctl00_M_lblConversion"}) is not None:
                    data_exchange_rate = soup.find(
                        "span", {"id": "ctl00_M_lblConversion"}).string.replace(' EUR', '')[8:]

                worksheet.write(i, 0, countryName)
                worksheet.write(i, 1, data_exchange_rate)
                worksheet.write(i, 2, actual)
                worksheet.write(i, 3, date)
                worksheet.write(i, 4, previous)
                worksheet.write(i, 5, highest)
                worksheet.write(i, 6, lowest)
                worksheet.write(i, 7, unit)

                if 'Million' in unit:
                    worksheet.write(i, 8, '=10^(6)')

                elif 'Billion' in unit:
                    worksheet.write(i, 8, '=10^(9)')

                elif 'Thousand' in unit:
                    worksheet.write(i, 8, '=10^(3)')

                elif 'Thousand' in unit and 'Ten' in unit:
                    worksheet.write(i, 8, '=10^(4)')

                elif 'Hundred' in unit:
                    worksheet.write(i, 8, '=100')

                else:
                    worksheet.write(i, 8, '=1')

                i = i + 1

    # Tradingeconomics __ world bank _ one indicator
    def test_create_worksheet_world_bank(self):
        workbook = xlsxwriter.Workbook('CristalBall.xlsx')
        worksheet = workbook.add_worksheet('agricultural_area')
        worksheet.write(0, 0, 'Country')  # Column : Country
        worksheet.write(0, 1, 'Value')  # Column : Value
        worksheet.write(0, 2, 'Total')  # Column : Total

        i = 1

        url = ""

        tradingeconomics_world_bank = requests.get(
            'http://127.0.0.1:5000/web_scraping_tradindgeconomics_world_bank?url=' + url)
        data_tradingeconomics_world_bank = tradingeconomics_world_bank.json()

        for worldBankIndicator in data_tradingeconomics_world_bank:
            worksheet.write(i, 0, worldBankIndicator['country'])
            worksheet.write(i, 1, worldBankIndicator['value'])

            i = i + 1

    # Tradingeconomics __ world bank _ multi indicators
    def test_report_cristal_ball(self):
        def createWorksheetsWorldBank(worbook, url, startTopic, endTopic):
            # Create a workbook
            workbook = xlsxwriter.Workbook('CristalBall.xlsx')

            # Web scraping
            '''
            # Tradingeconomics
            # Money
            # Banks balance sheet
            createWorksheet(workbook, 'Banks_Balance_Sheet', 'https://tradingeconomics.com/country-list/banks-balance-sheet')
            # Cash Reserve Ratio
            createWorksheet(workbook, 'Cash_Reserve_Ratio', 'https://tradingeconomics.com/country-list/cash-reserve-ratio')
            # Central Bank Balance Sheet
            createWorksheet(workbook, 'Central_Bank_Balance_Sheet', 'https://tradingeconomics.com/country-list/central-bank-balance-sheet')
            # Deposit Interest Rate
            createWorksheet(workbook, 'Deposit_Interest_Rate', 'https://tradingeconomics.com/country-list/deposit-interest-rate')
            # Foreign Exchange Reserves
            createWorksheet(workbook, 'Foreign_Exchange_Reserves', 'https://tradingeconomics.com/country-list/foreign-exchange-reserves')
            # Interbank Rate
            createWorksheet(workbook, 'Interbank_Rate', 'https://tradingeconomics.com/country-list/foreign-exchange-reserves')
            # Interest Rate
            createWorksheet(workbook, 'Interest_Rate', 'https://tradingeconomics.com/country-list/interest-rate')
            # Lending Rate
            createWorksheet(workbook, 'Lending_Rate', 'https://tradingeconomics.com/country-list/lending-rate')
            # Loan Growth
            createWorksheet(workbook, 'Loan_Growth', 'https://tradingeconomics.com/country-list/loan-growth')
            # Country List Loans to Private Sector
            createWorksheet(workbook, 'Loans_Private_Sector', 'https://tradingeconomics.com/country-list/loans-to-private-sector')
            # Money Supply M0
            createWorksheet(workbook, 'Money_Supply_M0', 'https://tradingeconomics.com/country-list/money-supply-m0')
            # Money Supply M1
            createWorksheet(workbook, 'Money_Supply_M1', 'https://tradingeconomics.com/country-list/money-supply-m1')
            # Money Supply M2
            createWorksheet(workbook, 'Money_Supply_M2', 'https://tradingeconomics.com/country-list/money-supply-m2')
            # Money Supply M3
            createWorksheet(workbook, 'Money_Supply_M3','https://tradingeconomics.com/country-list/money-supply-m3')
            # GDP
            # GDP
            createWorksheet(workbook, 'GDP','https://tradingeconomics.com/country-list/gdp')
            # GDP Annual Growth Rate
            createWorksheet(workbook, 'GDP_Annual_Growth_Rate', 'https://tradingeconomics.com/country-list/gdp-annual-growth-rate')
            # GDP Constant Prices
            createWorksheet(workbook, 'GDP_Constant_Prices', 'https://tradingeconomics.com/country-list/gdp-constant-prices')
            # GDP from Agriculture
            createWorksheet(workbook, 'GDP_Agriculture', 'https://tradingeconomics.com/country-list/gdp-from-agriculture')
            # GDP from Construction
            createWorksheet(workbook, 'GDP_Construction', 'https://tradingeconomics.com/country-list/gdp-from-construction')
            # GDP from Manufacturing
            createWorksheet(workbook, 'GDP_Manufacturing', 'https://tradingeconomics.com/country-list/gdp-from-manufacturing')
            # GDP from Mining
            createWorksheet(workbook, 'GDP_Mining', 'https://tradingeconomics.com/country-list/gdp-from-mining')
            # GDP from Public Administration
            createWorksheet(workbook, 'GDP_Public_Administration', 'https://tradingeconomics.com/country-list/gdp-from-public-administration')
            # GDP from Services
            createWorksheet(workbook, 'GDP_Services', 'https://tradingeconomics.com/country-list/gdp-from-services')
            # GDP from Transport
            createWorksheet(workbook, 'GDP_Transport', 'https://tradingeconomics.com/country-list/gdp-from-transport')
            # GDP from Utilities
            createWorksheet(workbook, 'GDP_Utilities', 'https://tradingeconomics.com/country-list/gdp-from-utilities')
            # GDP Growth Rate
            createWorksheet(workbook, 'GDP_Growth_Rate', 'https://tradingeconomics.com/country-list/gdp-growth-rate')
            # GDP per capita
            createWorksheet(workbook, 'GDP_Per_Capita', 'https://tradingeconomics.com/country-list/gdp-per-capita')
            # GDP per capita PPP
            createWorksheet(workbook, 'GDP_Per_Capita_PPP', 'https://tradingeconomics.com/country-list/gdp-per-capita-ppp')
            # Gross Fixed Capital Formation
            createWorksheet(workbook, 'Gross_Fixed_Capital_Formation', 'https://tradingeconomics.com/country-list/gross-fixed-capital-formation')
            # Gross National Product
            createWorksheet(workbook, 'Gross_National_Product', 'https://tradingeconomics.com/country-list/gross-national-product')
            ## Labour
            # Employed Persons
            createWorksheet(workbook, 'Employed_Persons', 'https://tradingeconomics.com/country-list/employed-persons')
            # Employment Change
            createWorksheet(workbook, 'Employment_Change', 'https://tradingeconomics.com/country-list/employment-change')
            # Employment Rate
            createWorksheet(workbook, 'Employment_Rate', 'https://tradingeconomics.com/country-list/employment-rate')
            # Full Time Employment
            createWorksheet(workbook, 'Full_Time_Employment', 'https://tradingeconomics.com/country-list/full-time-employment')
            # Initial Jobless Claims
            createWorksheet(workbook, 'Initial_Jobless_Claims', 'https://tradingeconomics.com/country-list/initial-jobless-claims')
            # Job Vacancies
            createWorksheet(workbook, 'Job_Vacancies', 'https://tradingeconomics.com/country-list/job-vacancies')
            # Labor Force Participation Rate
            createWorksheet(workbook, 'Labor_Force_Part_Rate', 'https://tradingeconomics.com/country-list/labor-force-participation-rate')
            # Labour Costs
            createWorksheet(workbook, 'Labour_Costs', 'https://tradingeconomics.com/country-list/labour-costs')
            # Long Term Unemployment Rate
            createWorksheet(workbook, 'Long_Term_Unemployment_Rate', 'https://tradingeconomics.com/country-list/long-term-unemployment-rate')
            # Minimum Wages
            createWorksheet(workbook, 'Minimum_Wages', 'https://tradingeconomics.com/country-list/minimum-wages')
            # Non Farm Payrolls
            createWorksheet(workbook, 'Non_Farm_Payrolls', 'https://tradingeconomics.com/country-list/non-farm-payrolls')
            # Part Time Employment
            createWorksheet(workbook, 'Part_Time_Employment', 'https://tradingeconomics.com/country-list/part-time-employment')
            # Population
            createWorksheet(workbook, 'Population', 'https://tradingeconomics.com/country-list/population')
            # Productivity
            createWorksheet(workbook, 'Productivity', 'https://tradingeconomics.com/country-list/productivity')
            # Retirement Age Men
            createWorksheet(workbook, 'Retirement_Age_Men', 'https://tradingeconomics.com/country-list/retirement-age-men')
            # Retirement Age Women
            createWorksheet(workbook, 'Retirement_Age_Women', 'https://tradingeconomics.com/country-list/retirement-age-women')
            # Unemployed Persons
            createWorksheet(workbook, 'Unemployed_Persons', 'https://tradingeconomics.com/country-list/unemployed-persons')
            # Unemployment Rate
            createWorksheet(workbook, 'Unemployment_Rate', 'https://tradingeconomics.com/country-list/unemployment-rate')
            # Wage Growth
            createWorksheet(workbook, 'Wage_Growth', 'https://tradingeconomics.com/country-list/wage-growth')
            # Wages
            createWorksheet(workbook, 'Wages', 'https://tradingeconomics.com/country-list/wages')
            # Wages in Manufacturing
            createWorksheet(workbook, 'Wages_In_Manufacturing', 'https://tradingeconomics.com/country-list/wages-in-manufacturing')
            # Youth Unemployment Rate
            createWorksheet(workbook, 'Youth_Unemployment_Rate', 'https://tradingeconomics.com/country-list/youth-unemployment-rate')
            ## Prices
            # Consumer Price Index (CPI)
            createWorksheet(workbook, 'Consumer_Price_Index', 'https://tradingeconomics.com/country-list/consumer-price-index-cpi')
            # Core Consumer Prices
            createWorksheet(workbook, 'Core_Consumer_Prices', 'https://tradingeconomics.com/country-list/core-consumer-prices')
            # Core Inflation Rate
            createWorksheet(workbook, 'Core_Inflation_Rate', 'https://tradingeconomics.com/country-list/core-inflation-rate')
            # Export Prices
            createWorksheet(workbook, 'Export_Prices', 'https://tradingeconomics.com/country-list/export-prices')
            # Food Inflation
            createWorksheet(workbook, 'Food_Inflation', 'https://tradingeconomics.com/country-list/food-inflation')
            # GDP Deflator
            createWorksheet(workbook, 'GDP_Deflator', 'https://tradingeconomics.com/country-list/gdp-deflator')
            # Harmonised Consumer Prices
            createWorksheet(workbook, 'Harmo_Consumer_Prices', 'https://tradingeconomics.com/country-list/harmonised-consumer-prices')
            # Import Prices
            createWorksheet(workbook, 'Import_Prices', 'https://tradingeconomics.com/country-list/import-prices')
            # Inflation Rate
            createWorksheet(workbook, 'Inflation_Rate', 'https://tradingeconomics.com/country-list/inflation-rate')
            # Inflation Rate Mom
            createWorksheet(workbook, 'Inflation_Rate_Mom', 'https://tradingeconomics.com/country-list/inflation-rate-mom')
            # Producer Prices
            createWorksheet(workbook, 'Producer Prices', 'https://tradingeconomics.com/country-list/producer-prices')
            # producer prices change
            createWorksheet(workbook, 'Producer_Prices_Change', 'https://tradingeconomics.com/country-list/producer-prices-change')
            ## Trade
            # Balance of Trade
            createWorksheet(workbook, 'Balance_Of_Trade', 'https://tradingeconomics.com/country-list/balance-of-trade')
            # Capital Flows
            createWorksheet(workbook, 'Capital_Flows', 'https://tradingeconomics.com/country-list/capital-flows')
            # Crude Oil Production
            createWorksheet(workbook, 'Crude_Oil_Production', 'https://tradingeconomics.com/country-list/crude-oil-production')
            # Current Account
            createWorksheet(workbook, 'Current_Account', 'https://tradingeconomics.com/country-list/current-account')
            # Country List Current Account to GDP
            createWorksheet(workbook, 'Current_Account_To_GDP', 'https://tradingeconomics.com/country-list/current-account-to-gdp')
            # Exports
            createWorksheet(workbook, 'Exports', 'https://tradingeconomics.com/country-list/exports')
            # External Debt
            createWorksheet(workbook, 'External_Debt', 'https://tradingeconomics.com/country-list/external-debt')
            # Foreign Direct Investment
            createWorksheet(workbook, 'Foreign_Direct_Investment', 'https://tradingeconomics.com/country-list/foreign-direct-investment')
            # Gold Reserves
            createWorksheet(workbook, 'Gold_Reserves', 'https://tradingeconomics.com/country-list/gold-reserves')
            # Imports
            createWorksheet(workbook, 'Imports', 'https://tradingeconomics.com/country-list/imports')
            # Remittances
            createWorksheet(workbook, 'Remittances', 'https://tradingeconomics.com/country-list/remittances')
            # Terms of Trade
            createWorksheet(workbook, 'Terms_Of_Trade', 'https://tradingeconomics.com/country-list/terms-of-trade')
            # Terrorism Index
            createWorksheet(workbook, 'Terrorism_Index', 'https://tradingeconomics.com/country-list/terrorism-index')
            # Tourism Revenues
            createWorksheet(workbook, 'Tourism_Revenues', 'https://tradingeconomics.com/country-list/tourism-revenues')
            # Tourist Arrivals
            createWorksheet(workbook, 'Tourist_Arrivals', 'https://tradingeconomics.com/country-list/tourist-arrivals')
            ## Government
            # Asylum Applications
            createWorksheet(workbook, 'Asylum_Applications', 'https://tradingeconomics.com/country-list/asylum-applications')
            # Credit Rating
            createWorksheet(workbook, 'Credit_Rating', 'https://tradingeconomics.com/country-list/rating')
            # Fiscal Expenditure
            createWorksheet(workbook, 'Fiscal_Expenditure', 'https://tradingeconomics.com/country-list/fiscal-expenditure')
            # Government Budget
            createWorksheet(workbook, 'Government_Budget', 'https://tradingeconomics.com/country-list/government-budget')
            # Government Budget Value
            createWorksheet(workbook, 'Government_Budget_Value', 'https://tradingeconomics.com/country-list/government-budget-value')
            # Government Debt
            createWorksheet(workbook, 'Government_Debt', 'https://tradingeconomics.com/country-list/government-debt')
            # Country List Government Debt to GDP
            createWorksheet(workbook, 'Government_Debt_To_GDP', 'https://tradingeconomics.com/country-list/government-debt-to-gdp')
            # Government Revenues
            createWorksheet(workbook, 'Government_Revenues', 'https://tradingeconomics.com/country-list/government-revenues')
            # Government Spending
            createWorksheet(workbook, 'Government_Spending', 'https://tradingeconomics.com/country-list/government-spending')
            # Country List Government Spending to GDP
            createWorksheet(workbook, 'Government_Spending_To_GDP', 'https://tradingeconomics.com/country-list/government-spending-to-gdp')
            ## Housing
            # Building Permits
            createWorksheet(workbook, 'Building_Permits', 'https://tradingeconomics.com/country-list/building-permits')
            # Construction Output
            createWorksheet(workbook, 'Construction_Output', 'https://tradingeconomics.com/country-list/construction-output')
            # Home Ownership Rate
            createWorksheet(workbook, 'Home_Ownership_Rate', 'https://tradingeconomics.com/country-list/home-ownership-rate')
            # Housing Index
            createWorksheet(workbook, 'Housing_Index', 'https://tradingeconomics.com/country-list/housing-index')
            # Housing Starts
            createWorksheet(workbook, 'Housing_Starts', 'https://tradingeconomics.com/country-list/housing-starts')
            ## Business
            # Bankruptcies
            createWorksheet(workbook, 'Bankruptcies', 'https://tradingeconomics.com/country-list/bankruptcies')
            # Business Confidence
            createWorksheet(workbook, 'Business_Confidence', 'https://tradingeconomics.com/country-list/business-confidence')
            # Capacity Utilization
            createWorksheet(workbook, 'Capacity_Utilization', 'https://tradingeconomics.com/country-list/capacity-utilization')
            # Car Production
            createWorksheet(workbook, 'Car_Production', 'https://tradingeconomics.com/country-list/car-production')
            # Car Registrations
            createWorksheet(workbook, 'Car_Registrations', 'https://tradingeconomics.com/country-list/car-registrations')
            # Cement Production
            createWorksheet(workbook, 'Cement_Production', 'https://tradingeconomics.com/country-list/cement-production')
            # Changes in Inventories
            createWorksheet(workbook, 'Changes_In_Inventories', 'https://tradingeconomics.com/country-list/changes-in-inventories')
            # Competitiveness Index
            createWorksheet(workbook, 'Competitiveness_Index', 'https://tradingeconomics.com/country-list/competitiveness-index')
            # Competitiveness Rank
            createWorksheet(workbook, 'Competitiveness_Rank', 'https://tradingeconomics.com/country-list/competitiveness-rank')
            # Composite PMI
            createWorksheet(workbook, 'Composite_PMI', 'https://tradingeconomics.com/country-list/composite-pmi')
            # Corporate Profits
            createWorksheet(workbook, 'Corporate_Profits', 'https://tradingeconomics.com/country-list/corporate-profits')
            # Corruption Index
            createWorksheet(workbook, 'Corruption_Index', 'https://tradingeconomics.com/country-list/corruption-index')
            # Corruption Rank
            createWorksheet(workbook, 'Corruption_Rank', 'https://tradingeconomics.com/country-list/corruption-rank')
            # Ease of Doing Business
            createWorksheet(workbook, 'Ease_Of_Doing_Business', 'https://tradingeconomics.com/country-list/ease-of-doing-business')
            # Electricity Production - Country List
            createWorksheet(workbook, 'Electricity_Production', 'https://tradingeconomics.com/country-list/electricity-production')
            # Factory Orders
            createWorksheet(workbook, 'Factory_Orders', 'https://tradingeconomics.com/country-list/factory-orders')
            # Industrial Production
            createWorksheet(workbook, 'Industrial_Production', 'https://tradingeconomics.com/country-list/industrial-production')
            # Industrial Production Mom
            createWorksheet(workbook, 'Industrial_Production_Mom', 'https://tradingeconomics.com/country-list/industrial-production-mom')
            # Internet Speed
            createWorksheet(workbook, 'Internet_Speed', 'https://tradingeconomics.com/country-list/internet-speed')
            # IP Addresses by Country
            createWorksheet(workbook, 'IP_Addresses_By_Country', 'https://tradingeconomics.com/country-list/ip-addresses')
            # Leading Economic Index
            createWorksheet(workbook, 'Leading_Economic_Index', 'https://tradingeconomics.com/country-list/leading-economic-index')
            # Manufacturing PMI
            createWorksheet(workbook, 'Manufacturing_PMI', 'https://tradingeconomics.com/country-list/manufacturing-pmi')
            # Manufacturing Production
            createWorksheet(workbook, 'Manufacturing_Production', 'https://tradingeconomics.com/country-list/manufacturing-production')
            # Mining Production
            createWorksheet(workbook, 'Mining_Production', 'https://tradingeconomics.com/country-list/mining-production')
            # New Orders
            createWorksheet(workbook, 'New_Orders', 'https://tradingeconomics.com/country-list/new-orders')
            # Services PMI
            createWorksheet(workbook, 'Services_PMI', 'https://tradingeconomics.com/country-list/services-pmi')
            # Small Business Sentiment
            createWorksheet(workbook, 'Small_Business_Sentiment', 'https://tradingeconomics.com/country-list/small-business-sentiment')
            # Steel Production - Country List
            createWorksheet(workbook, 'Steel_Production', 'https://tradingeconomics.com/country-list/steel-production')
            # Total Vehicle Sales
            createWorksheet(workbook, 'Total_Vehicle_Sales', 'https://tradingeconomics.com/country-list/total-vehicle-sales')
            # ZEW Economic Sentiment Index
            createWorksheet(workbook, 'ZEW Economic Sentiment Index', 'https://tradingeconomics.com/country-list/zew-economic-sentiment-index')
            ## Consumer
            # Bank Lending Rate
            createWorksheet(workbook, 'Bank_Lending_Rate', 'https://tradingeconomics.com/country-list/bank-lending-rate')
            # Consumer Confidence
            createWorksheet(workbook, 'Consumer_Confidence', 'https://tradingeconomics.com/country-list/consumer-confidence')
            # Consumer Credit
            createWorksheet(workbook, 'Consumer_Credit', 'https://tradingeconomics.com/country-list/consumer-credit')
            # Consumer Spending
            createWorksheet(workbook, 'Consumer_Spending', 'https://tradingeconomics.com/country-list/consumer-spending')
            # Disposable Personal Income
            createWorksheet(workbook, 'Disposable_Personal_Income', 'https://tradingeconomics.com/country-list/disposable-personal-income')
            # Gasoline Prices
            createWorksheet(workbook, 'Gasoline_Prices', 'https://tradingeconomics.com/country-list/gasoline-prices')
            # Households Debt to GDP
            createWorksheet(workbook, 'Households_Debt_To_GDP', 'https://tradingeconomics.com/country-list/households-debt-to-gdp')
            # Households Debt to Income
            createWorksheet(workbook, 'Households_Debt_To_Income', 'https://tradingeconomics.com/country-list/households-debt-to-income')
            # Personal Savings
            createWorksheet(workbook, 'Personal_Savings', 'https://tradingeconomics.com/country-list/personal-savings')
            # Personal Spending
            createWorksheet(workbook, 'Personal_Spending', 'https://tradingeconomics.com/country-list/personal-spending')
            # Private Sector Credit
            createWorksheet(workbook, 'Private_Sector_Credit', 'https://tradingeconomics.com/country-list/private-sector-credit')
            # Retail Sales MoM
            createWorksheet(workbook, 'Retail_Sales_MoM', 'https://tradingeconomics.com/country-list/retail-sales-mom')
            # Retail Sales YoY
            createWorksheet(workbook, 'Retail_Sales_YoY', 'https://tradingeconomics.com/country-list/retail-sales-yoy')
            ## Taxes
            # List of Countries by Corporate Tax Rate
            createWorksheet(workbook, 'Corporate_Tax_Rate', 'https://tradingeconomics.com/country-list/corporate-tax-rate')
            # List of Countries by Personal Income Tax Rate
            createWorksheet(workbook, 'Personal_Income_Tax_Rate', 'https://tradingeconomics.com/country-list/personal-income-tax-rate')
            # List of Countries by Sales Tax Rate
            createWorksheet(workbook, 'Sales_Tax_Rate', 'https://tradingeconomics.com/country-list/sales-tax-rate')
            # Social Security Rate
            createWorksheet(workbook, 'Social_Security_Rate', 'https://tradingeconomics.com/country-list/social-security-rate')
            # Social Security Rate For Companies
            createWorksheet(workbook, 'Social_Security_Rate_Companies', 'https://tradingeconomics.com/country-list/social-security-rate-for-companies')
            # Social Security Rate For Employees
            createWorksheet(workbook, 'Social_Security_Rate_Employees', 'https://tradingeconomics.com/country-list/social-security-rate-for-employees')
            ## Climate
            # Average Precipitation by Country
            createWorksheet(workbook, 'Average_Precipitation', 'https://tradingeconomics.com/country-list/precipitation')
            # Average Temperature by Country
            createWorksheet(workbook, 'Average_Temperature', 'https://tradingeconomics.com/country-list/temperature')
        
            # Tradingeconomics __ World Bank
            ## Agriculture 
            # Agricultural area irrigated (ha)
            createWorksheetWorldBank(workbook, 'Agricultural_Area_Irrigated', 'https://tradingeconomics.com/country-list/agricultural-area-irrigated-ha-wb-data.html')
            # Agricultural irrigated land (% of total agricultural land)
            createWorksheetWorldBank(workbook, 'Agricultural_Irrigated_Land', 'https://tradingeconomics.com/country-list/agricultural-irrigated-land-percent-of-total-agricultural-land-wb-data.html')
            # Agricultural land (hectares)
            createWorksheetWorldBank(workbook, 'Agricultural_Land', 'https://tradingeconomics.com/country-list/agricultural-land-hectares-wb-data.html')
            # Agricultural machinery, tractors
            createWorksheetWorldBank(workbook, 'Agricultural_Machinery_Tractors', 'https://tradingeconomics.com/country-list/agricultural-machinery-tractors-wb-data.html')
            # Agricultural methane emissions (% of total)
            createWorksheetWorldBank(workbook, 'Agricultural_Methane_Emission', 'https://tradingeconomics.com/country-list/agricultural-methane-emissions-percent-of-total-wb-data.html')
            # Agricultural nitrous oxide emissions (% of total)
            createWorksheetWorldBank(workbook, 'Agricultural_NO_Emission', 'https://tradingeconomics.com/country-list/agricultural-nitrous-oxide-emissions-percent-of-total-wb-data.html')
            # Agricultural raw materials exports (% of merchandise exports)
            createWorksheetWorldBank(workbook, 'AgriculturalRaw_Material_Export', 'https://tradingeconomics.com/country-list/agricultural-raw-materials-exports-percent-of-merchandise-exports-wb-data.html')
            # Agricultural support estimate (% of GDP)
            createWorksheetWorldBank(workbook, 'Agricultural_Support_Estimate', 'https://tradingeconomics.com/country-list/agricultural-support-estimate-percent-of-gdp-wb-data.html')
            # Agricultural tractors, exports (FAO, current US$)
            createWorksheetWorldBank(workbook, 'Agricultural_Tractors_Exports', 'https://tradingeconomics.com/country-list/agricultural-tractors-exports-fao-us-dollar-wb-data.html')
            # Agricultural tractors, imports (FAO, current US$)
            createWorksheetWorldBank(workbook, 'Agricultural_Tractors_Imports', 'https://tradingeconomics.com/country-list/agricultural-tractors-imports-fao-us-dollar-wb-data.html')
            # Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)
            createWorksheetWorldBank(workbook, 'Annual_Freshwater_Withdrawals', 'https://tradingeconomics.com/country-list/annual-freshwater-withdrawals-agriculture-percent-of-total-freshwater-withdrawal-wb-data.html')
            # Arable land (hectares)
            createWorksheetWorldBank(workbook, 'Arable_Land', 'https://tradingeconomics.com/country-list/arable-land-hectares-wb-data.html')
            # Crop production index (1999-2001 = 100)
            createWorksheetWorldBank(workbook, 'Crop_Production_Index', 'https://tradingeconomics.com/country-list/crop-production-index-1999-2001--100-wb-data.html')
            # Employees, agriculture, male (% of male employment)
            createWorksheetWorldBank(workbook, 'Employees_Agriculture_Male', 'https://tradingeconomics.com/country-list/employees-agriculture-male-percent-of-male-employment-wb-data.html')
            # Fertilizer consumption (% of fertilizer production)
            createWorksheetWorldBank(workbook, 'Fertilizer_Consumption', 'https://tradingeconomics.com/country-list/fertilizer-consumption-percent-of-fertilizer-production-wb-data.html')
            # Food production index (1999-2001 = 100)
            createWorksheetWorldBank(workbook, 'Food_Production_Index', 'https://tradingeconomics.com/country-list/food-production-index-1999-2001--100-wb-data.html')
            # Forest area (sq. km)
            createWorksheetWorldBank(workbook, 'Forest_Area', 'https://tradingeconomics.com/country-list/forest-area-sq-km-wb-data.html')
            # Land under cereal production (hectares)
            createWorksheetWorldBank(workbook, 'Land_Under_Cereal_Production', 'https://tradingeconomics.com/country-list/land-under-cereal-production-hectares-wb-data.html')
            # Average tariffs imposed by developed countries on agricultural products from developing countries
            createWorksheetWorldBank(workbook, 'AverageTarifDevelopedDeveloping', 'https://tradingeconomics.com/country-list/average-tariffs-imposed-by-developed-countries-on-agricultural-products-from-developing-countries-wb-data.html')
            # Cereal production (metric tons)
            createWorksheetWorldBank(workbook, 'Cereal_Production', 'https://tradingeconomics.com/country-list/cereal-production-metric-tons-wb-data.html')
            # Permanent cropland (% of land area)
            createWorksheetWorldBank(workbook, 'Permanent_Cropland', 'https://tradingeconomics.com/country-list/permanent-cropland-percent-of-land-area-wb-data.html')
            # Real agricultural GDP growth rates
            createWorksheetWorldBank(workbook, 'RealAgriculturalGDPGrowthRates', 'https://tradingeconomics.com/country-list/real-agricultural-gdp-growth-rates-wb-data.html')
            # Rural land area (sq. km)
            createWorksheetWorldBank(workbook, 'Rural_Land_Area', 'https://tradingeconomics.com/country-list/rural-land-area-sq-km-wb-data.html')
            # Rural land area where elevation is below 5 meters (sq. km)
            createWorksheetWorldBank(workbook, 'Rural_Land_Area_Where_Elevation', 'https://tradingeconomics.com/country-list/rural-land-area-where-elevation-is-below-5-meters-sq-km-wb-data.html')
            # Total agricultural imports (FAO, current US$)
            createWorksheetWorldBank(workbook, 'Total_Agricultural_Imports', 'https://tradingeconomics.com/country-list/total-agricultural-imports-fao-us-dollar-wb-data.html')
            # Agricultural census
            createWorksheetWorldBank(workbook, 'Agricultural_Census', 'https://tradingeconomics.com/country-list/agricultural-census-wb-data.html')
            # Agricultural land (% of land area)
            createWorksheetWorldBank(workbook, 'AgriculturalLandPerc', 'https://tradingeconomics.com/country-list/agricultural-land-percent-of-land-area-wb-data.html')
            # Agricultural land (sq. km)
            createWorksheetWorldBank(workbook, 'AgriculturalLandSqKm', 'https://tradingeconomics.com/country-list/agricultural-land-sq-km-wb-data.html')
            # Agricultural machinery, tractors per 100 sq. km of arable land
            createWorksheetWorldBank(workbook, 'Agricultural_Machinery_Arable ', 'https://tradingeconomics.com/country-list/agricultural-machinery-tractors-per-100-sq-km-of-arable-land-wb-data.html')
            # Agricultural methane emissions (thousand metric tons of CO2 equivalent)
            createWorksheetWorldBank(workbook, 'Agricultural_Methane_CO2_Eq', 'https://tradingeconomics.com/country-list/agricultural-methane-emissions-thousand-metric-tons-of-co2-equivalent-wb-data.html')
            # Agricultural nitrous oxide emissions (thousand metric tons of CO2 equivalent)
            createWorksheetWorldBank(workbook, 'Agricultural_NO_CO2_Eq', 'https://tradingeconomics.com/country-list/agricultural-nitrous-oxide-emissions-thousand-metric-tons-of-co2-equivalent-wb-data.html')
            # Agricultural raw materials imports (% of merchandise imports)
            createWorksheetWorldBank(workbook, 'AgriculturalRawMaterialsImports', 'https://tradingeconomics.com/country-list/agricultural-raw-materials-imports-percent-of-merchandise-imports-wb-data.html')
            # Agricultural tractors, exports
            createWorksheetWorldBank(workbook, 'AgriculturalTractors_Exports', 'https://tradingeconomics.com/country-list/agricultural-tractors-exports-wb-data.html')
            # Agricultural tractors, imports
            createWorksheetWorldBank(workbook, 'AgriculturalTractorsImports', 'https://tradingeconomics.com/country-list/agricultural-tractors-imports-wb-data.html')
            # Agriculture value added per worker (constant 2000 US$)
            createWorksheetWorldBank(workbook, 'AgricultureValueAddedPerWorker', 'https://tradingeconomics.com/country-list/agriculture-value-added-per-worker-constant-2000-us-dollar-wb-data.html')
            # Arable land (% of land area)
            createWorksheetWorldBank(workbook, 'ArableLandPerc', 'https://tradingeconomics.com/country-list/arable-land-percent-of-land-area-wb-data.html')
            # Arable land (hectares per person)
            createWorksheetWorldBank(workbook, 'ArableLandHectaresPerPerson', 'https://tradingeconomics.com/country-list/arable-land-hectares-per-person-wb-data.html')
            # Average precipitation in depth (mm per year)
            createWorksheetWorldBank(workbook, 'AveragePrecipitationInDepth', 'https://tradingeconomics.com/country-list/average-precipitation-in-depth-mm-per-year-wb-data.html')
            # Average tariffs imposed by developed countries on agricultural products from least developed countries
            createWorksheetWorldBank(workbook, 'AverageTariffsAgricultural', 'https://tradingeconomics.com/country-list/average-tariffs-imposed-by-developed-countries-on-agricultural-products-from-least-developed-countries-wb-data.html')
            # Cereal yield (kg per hectare)
            createWorksheetWorldBank(workbook, 'CerealYield', 'https://tradingeconomics.com/country-list/cereal-yield-kg-per-hectare-wb-data.html')
            # Employees, agriculture, female (% of female employment)
            createWorksheetWorldBank(workbook, 'EmployeesAgricultureFemale', 'https://tradingeconomics.com/country-list/employees-agriculture-female-percent-of-female-employment-wb-data.html')
            # Employment in agriculture (% of total employment)
            createWorksheetWorldBank(workbook, 'EmploymentInAgriculture', 'https://tradingeconomics.com/country-list/employment-in-agriculture-percent-of-total-employment-wb-data.html')
            # Fertilizer consumption (kilograms per hectare of arable land)
            createWorksheetWorldBank(workbook, 'FertilizerConsumptionArableLand', 'https://tradingeconomics.com/country-list/fertilizer-consumption-kilograms-per-hectare-of-arable-land-wb-data.html')
            # Forest area (% of land area)
            createWorksheetWorldBank(workbook, 'ForestArea', 'https://tradingeconomics.com/country-list/forest-area-percent-of-land-area-wb-data.html')
            # Land area (sq. km)
        createWorksheetWorldBank(workbook, 'LandAreaSqKm',
                                     'https://tradingeconomics.com/country-list/land-area-sq-km-wb-data.html')
            # Livestock production index (1999-2001 = 100)
            createWorksheetWorldBank(workbook, 'LivestockProductionIndex', 'https://tradingeconomics.com/country-list/livestock-production-index-1999-2001--100-wb-data.html')
            # Poverty gap at rural poverty line
            createWorksheetWorldBank(workbook, 'PovertyGapAtRuralPovertyLine', 'https://tradingeconomics.com/country-list/poverty-gap-at-rural-poverty-line-percent-wb-data.html')
            # Real agricultural GDP per capita growth rate
            createWorksheetWorldBank(workbook, 'RealAgriculturalGDPCapitaGrowth', 'https://tradingeconomics.com/country-list/real-agricultural-gdp-per-capita-growth-rate-wb-data.html')
            # Rural land area where elevation is below 5 meters (% of total land area)
            createWorksheetWorldBank(workbook, 'RuralLandAreaElevationUnder5M', 'https://tradingeconomics.com/country-list/rural-land-area-where-elevation-is-below-5-meters-percent-of-total-land-area-wb-data.html')
            # Surface area (sq. km)
            createWorksheetWorldBank(workbook, 'SurfaceAreaSqKm', 'https://tradingeconomics.com/country-list/surface-area-sq-km-wb-data.html')
            # Total agricultural exports (FAO, current US$)
            createWorksheetWorldBank(workbook, 'TotalAgriculturalExportUSD', 'https://tradingeconomics.com/country-list/total-agricultural-exports-fao-us-dollar-wb-data.html')
            '''
            workbook.close()


if __name__ == '__main__':
    unittest.main()
