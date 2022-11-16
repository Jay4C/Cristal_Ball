import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
from PyPDF2 import PdfFileReader


class UnitTestsDesktopAutomationLectures10marketing(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12(self):
		print('test_Cours12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13(self):
		print('test_Cours13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14(self):
		print('test_Cours14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15(self):
		print('test_Cours15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16(self):
		print('test_Cours16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours17(self):
		print('test_Cours17')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_17.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours18(self):
		print('test_Cours18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)

		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours19(self):
		print('test_Cours19')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_19.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours20(self):
		print('test_Cours20')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_20.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours201(self):
		print('test_Cours201')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_20_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours21(self):
		print('test_Cours21')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_21.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours22(self):
		print('test_Cours22')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_22.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours23(self):
		print('test_Cours23')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_23.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours24(self):
		print('test_Cours24')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_24.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours25(self):
		print('test_Cours25')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_25.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours26(self):
		print('test_Cours26')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_26.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours27(self):
		print('test_Cours27')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_27.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours28(self):
		print('test_Cours28')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_28.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours29(self):
		print('test_Cours29')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_29.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours30(self):
		print('test_Cours30')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_30.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/10_Marketing/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures11romans(unittest.TestCase):
	def test_bankster(self):
		print('test_bankster')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/bankster.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_bulwercomingrace(self):
		print('test_BulwerComingRace')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Bulwer__Coming_Race.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_clasonrichestmaninbabylon(self):
		print('test_ClasonRichestManInBabylon')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Clason-RichestManInBabylon.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_eustacemullinslessecretsdelarservefderale(self):
		print('test_EustaceMullinsLesSecretsdelaR�serveF�derale')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Eustace-Mullins-Les-Secrets-de-la-R�serve-F�derale.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_largentdette(self):
		print('test_Largentdette')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/L-argent-dette.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_lemeilleurdesmondes(self):
		print('test_Lemeilleurdesmondes')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Le-meilleur-des-mondes.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_lesenjeuxdelacreationmonetairechomageetalienationouprosperiteetdemocratielu(self):
		print('test_LESENJEUXDELACREATIONMONETAIRECHOMAGEETALIENATIONOUPROSPERITEETDEMOCRATIE[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/LES_ENJEUX_DE_LA_CREATION_MONETAIRE_CHOMAGE_ET_ALIENATION_OU_PROSPERITE_ET_DEMOCRATIE_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_livregalbraithlargent1975(self):
		print('test_livregalbraithlargent1975')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/livre-galbraith-l-argent-1975.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_machiavelleprince(self):
		print('test_machiavelleprince')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/machiavel_le_prince.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_mjdemarcothemillionairefastlane(self):
		print('test_MJDeMarcoTheMillionaireFastlane')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/MJ_DeMarco_The_Millionaire_Fastlane.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_moralsanddogmaoftheancientandacce(self):
		print('test_MoralsandDogmaoftheAncientandAcce')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Morals_and_Dogma_of_the_Ancient_and_Acce.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_orwell1984(self):
		print('test_Orwell1984')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Orwell_1984.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_outwittingthedevil(self):
		print('test_OutwittingTheDevil')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Outwitting_The_Devil.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_politiqueetartdelaguerre(self):
		print('test_PolitiqueEtArtDeLaGuerre')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Politique_Et_Art_De_La_Guerre.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_protocolesdessagesdesiondaprc3a8snilus(self):
		print('test_protocolesdessagesdesiondaprc3a8snilus')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/protocoles-des-sages-de-sion-daprc3a8s-nilus.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_suntzuartdelaguerre(self):
		print('test_suntzuartdelaguerre')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/sun_tzu_art_de_la_guerre.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_thecreaturefromjekyllislandbygedwardgriffin(self):
		print('test_TheCreaturefromJekyllIslandbyG.EdwardGriffin')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/The-Creature-from-Jekyll-Island-by-G.-Edward-Griffin.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_thinkandgrowrich(self):
		print('test_ThinkAndGrowRich')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Think_And_Grow_Rich.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_totalmoneymakeover(self):
		print('test_TotalMoneyMakeover')

		cours = "file:///C:/Users/DELL/Documents/Lectures/11_Romans/Total_Money_Makeover.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures16livresreligieux(unittest.TestCase):
	def test_bible(self):
		print('test_Bible')

		cours = "file:///C:/Users/DELL/Documents/Lectures/16_Livres_Religieux/Bible.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures17informatique(unittest.TestCase):
	def test_bloomuserguide12(self):
		print('test_bloomuserguide1.2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/bloom-user-guide-1.2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1latex(self):
		print('test_Cours1latex')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_1_latex.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1lu(self):
		print('test_Cours1[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_1_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2latex(self):
		print('test_Cours2latex')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_2_latex.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2lu(self):
		print('test_Cours2[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_2_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3lu(self):
		print('test_Cours3[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_3_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4lu(self):
		print('test_Cours4[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_4_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5lu(self):
		print('test_Cours5[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_5_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courstheoriquebitcoin(self):
		print('test_CoursTheoriqueBitcoin')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Cours_Theorique_Bitcoin.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cypherrefcard40(self):
		print('test_cypherrefcard4.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/cypher-refcard-4.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_developerguidewireshark(self):
		print('test_developerguidewireshark')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/developer-guide_wireshark.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_docsgit(self):
		print('test_Docsgit')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Docs_git.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_docsjenkins(self):
		print('test_DocsJenkins')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Docs_Jenkins.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_documentationdjango(self):
		print('test_Documentationdjango')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Documentation_django.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_documentationdocker1(self):
		print('test_DocumentationDocker1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Documentation_Docker_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_documentationdocker2(self):
		print('test_DocumentationDocker2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Documentation_Docker_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_documentationflask(self):
		print('test_DocumentationFlask')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Documentation_Flask.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_documentationreportlab(self):
		print('test_Documentationreportlab')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Documentation_reportlab.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_documentationscikitlearn(self):
		print('test_Documentationscikitlearn')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Documentation_scikit_learn.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_elasticsearchpyreadthedocsioenmaster(self):
		print('test_elasticsearchpyreadthedocsioenmaster')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/elasticsearch-py-readthedocs-io-en-master.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_gettingstartedfreecadscripting(self):
		print('test_GettingStartedFreeCADScripting')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/GettingStartedFreeCADScripting.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_gnupg(self):
		print('test_gnupg')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/gnupg.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_hyperledgerfabricreadthedocsioenlatest(self):
		print('test_hyperledgerfabricreadthedocsioenlatest')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/hyperledger-fabric-readthedocs-io-en-latest.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_kivy(self):
		print('test_kivy')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/kivy.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jcyphermanual40(self):
		print('test_neo4jcyphermanual4.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-cypher-manual-4.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jdrivermanual17python(self):
		print('test_neo4jdrivermanual1.7python')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-driver-manual-1.7-python.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jgettingstarted40(self):
		print('test_neo4jgettingstarted4.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-getting-started-4.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jgraphalgorithmsuserguide35(self):
		print('test_neo4jgraphalgorithmsuserguide3.5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-graph-algorithms-user-guide-3.5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jgraphdatasciencemanual10(self):
		print('test_neo4jgraphdatasciencemanual1.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-graph-data-science-manual-1.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jhttpapi40(self):
		print('test_neo4jhttpapi4.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-http-api-4.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jmigrationguide40(self):
		print('test_neo4jmigrationguide4.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-migration-guide-4.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jogmmanual32(self):
		print('test_neo4jogmmanual3.2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-ogm-manual-3.2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4joperationsmanual40(self):
		print('test_neo4joperationsmanual4.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-operations-manual-4.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_neo4jstatuscodes40(self):
		print('test_neo4jstatuscodes4.0')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/neo4j-status-codes-4.0.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_numpy1(self):
		print('test_numpy1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/numpy_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_numpy2(self):
		print('test_numpy2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/numpy_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_pythonscriptingtutorialfreecaddocumentation(self):
		print('test_PythonscriptingtutorialFreeCADDocumentation')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Python scripting tutorial - FreeCAD Documentation.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_skidlapi(self):
		print('test_skidlapi')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/skidl_api.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_snortmanual(self):
		print('test_snortmanual')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/snort_manual.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_springbootreferencedocumentation(self):
		print('test_SpringBootReferenceDocumentation')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/Spring Boot Reference Documentation.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_sympydocspdf15(self):
		print('test_sympydocspdf1.5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/sympy-docs-pdf-1.5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_usermanualvirtualbox(self):
		print('test_UserManualvirtualbox')

		cours = "file:///C:/Users/DELL/Documents/Lectures/17_Informatique/UserManualvirtualbox.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures18economie(unittest.TestCase):
	def test_coursconsommationetepargne(self):
		print('test_Coursconsommationetepargne')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_consommation_et_epargne.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courscroissanceeconomique(self):
		print('test_Courscroissanceeconomique')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_croissance_economique.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieagricole1(self):
		print('test_Courseconomieagricole1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_agricole_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieagricole2(self):
		print('test_Courseconomieagricole2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_agricole_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieapprofondie(self):
		print('test_Courseconomieapprofondie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_approfondie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiecirculaire1lu(self):
		print('test_CoursEconomieCirculaire1[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_Economie_Circulaire_1_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiecirculaire2lu(self):
		print('test_CoursEconomieCirculaire2[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_Economie_Circulaire_2_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiecomportementale(self):
		print('test_Courseconomiecomportementale')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_comportementale.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiecontemporaine(self):
		print('test_Courseconomiecontemporaine')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_contemporaine.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiedubonheuretbienetre1(self):
		print('test_Courseconomiedubonheuretbienetre1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_du_bonheur_et_bien_etre_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiedubonheuretbienetre2(self):
		print('test_Courseconomiedubonheuretbienetre2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_du_bonheur_et_bien_etre_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiedudeveloppement1(self):
		print('test_Courseconomiedudeveloppement1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_du_developpement_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieeducation1(self):
		print('test_Courseconomieeducation1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_education_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieenvironnement2(self):
		print('test_Courseconomieenvironnement2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_environnement2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieenvironnement1(self):
		print('test_Courseconomieenvironnement1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_environnement_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiefinanciere1(self):
		print('test_Courseconomiefinanciere1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_financiere_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiegeographie1(self):
		print('test_Courseconomiegeographie1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_geographie_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieindustrielle1(self):
		print('test_Courseconomieindustrielle1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_industrielle_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomieinstutionnelle1(self):
		print('test_Courseconomieinstutionnelle1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_instutionnelle_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiemondiale1(self):
		print('test_Courseconomiemondiale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_mondiale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiemondiale2(self):
		print('test_Courseconomiemondiale2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_mondiale_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiemonetaire1(self):
		print('test_Courseconomiemonetaire1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_monetaire_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiepolitique1(self):
		print('test_Courseconomiepolitique1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_politique_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiepolitique2(self):
		print('test_Courseconomiepolitique2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_politique_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomierurale1(self):
		print('test_Courseconomierurale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_rurale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiesociale1(self):
		print('test_Courseconomiesociale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_sociale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseconomiesociale2(self):
		print('test_Courseconomiesociale2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_economie_sociale_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courshistoireeconomie(self):
		print('test_Courshistoireeconomie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_histoire_economie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursintroductioneconomie1(self):
		print('test_Coursintroductioneconomie1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_introduction_economie_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursintroductioneconomie2(self):
		print('test_Coursintroductioneconomie2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_introduction_economie_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmacroeconomielu(self):
		print('test_CoursMacroeconomie[Lu]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_Macroeconomie_[Lu].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmicroeconomie(self):
		print('test_CoursMicroeconomie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_Microeconomie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursorganisationindustrielle(self):
		print('test_Coursorganisationindustrielle')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/Cours_organisation_industrielle.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_id70241fini(self):
		print('test_id70241[Fini]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/id-7024-1_[Fini].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_id70242fini(self):
		print('test_id70242[Fini]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/18_Economie/id-7024-2_[Fini].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures19management(unittest.TestCase):
	def test_courscasemanagement1(self):
		print('test_Courscasemanagement1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_case_management_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementassociatif1(self):
		print('test_Coursmanagementassociatif1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_associatif_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementchangement1(self):
		print('test_Coursmanagementchangement1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_changement_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementcollaboratif1(self):
		print('test_Coursmanagementcollaboratif1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_collaboratif_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementcommercial1(self):
		print('test_Coursmanagementcommercial1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_commercial_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementconnaissances1(self):
		print('test_Coursmanagementconnaissances1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_connaissances_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementconsultatif1(self):
		print('test_Coursmanagementconsultatif1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_consultatif1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementculturel1(self):
		print('test_Coursmanagementculturel1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_culturel_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementequipe1(self):
		print('test_Coursmanagementequipe1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_equipe_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementethique1(self):
		print('test_Coursmanagementethique1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_ethique_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementevenementiel(self):
		print('test_Coursmanagementevenementiel')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_evenementiel.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementhorizontal(self):
		print('test_Coursmanagementhorizontal')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_horizontal.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementinnovation1(self):
		print('test_Coursmanagementinnovation1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_innovation_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementinternational1(self):
		print('test_Coursmanagementinternational1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_international_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementoperationnel1(self):
		print('test_Coursmanagementoperationnel1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_operationnel_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementoperations1(self):
		print('test_Coursmanagementoperations1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_operations_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementparticipatif1(self):
		print('test_Coursmanagementparticipatif1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_participatif_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementprojet1(self):
		print('test_Coursmanagementprojet1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_projet_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementprojet2(self):
		print('test_Coursmanagementprojet2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_projet_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementqualite1(self):
		print('test_Coursmanagementqualite1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_qualite_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementqualite2(self):
		print('test_Coursmanagementqualite2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_qualite_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementressourceshumaines1(self):
		print('test_Coursmanagementressourceshumaines1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_ressources_humaines_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementrisques1(self):
		print('test_Coursmanagementrisques1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_risques_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmanagementstrategique1(self):
		print('test_Coursmanagementstrategique1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_management_strategique_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmicromanagement1(self):
		print('test_Coursmicromanagement1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_micromanagement_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursoutilsdumanagement1(self):
		print('test_Coursoutilsdumanagement1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/19_Management/Cours_outils_du_management_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures1chimie(unittest.TestCase):
	def test_1(self):
		print('test_1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_10(self):
		print('test_10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_11(self):
		print('test_11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_12(self):
		print('test_12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_13(self):
		print('test_13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_14(self):
		print('test_14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_15(self):
		print('test_15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_16(self):
		print('test_16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_17(self):
		print('test_17')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/17.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_18(self):
		print('test_18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_19(self):
		print('test_19')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/19.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_2(self):
		print('test_2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_20(self):
		print('test_20')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/20.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_21(self):
		print('test_21')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/21.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_22(self):
		print('test_22')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/22.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_23(self):
		print('test_23')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/23.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_24(self):
		print('test_24')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/24.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_25(self):
		print('test_25')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/25.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_26(self):
		print('test_26')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/26.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_27(self):
		print('test_27')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/27.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_28(self):
		print('test_28')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/28.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_29(self):
		print('test_29')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/29.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_3(self):
		print('test_3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_30(self):
		print('test_30')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/30.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_31(self):
		print('test_31')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/31.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_32(self):
		print('test_32')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/32.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_33(self):
		print('test_33')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/33.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_34(self):
		print('test_34')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/34.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_35(self):
		print('test_35')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/35.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_36(self):
		print('test_36')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/36.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_37(self):
		print('test_37')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/37.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_38(self):
		print('test_38')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/38.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_39(self):
		print('test_39')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/39.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_4(self):
		print('test_4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_40(self):
		print('test_40')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/40.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_41(self):
		print('test_41')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/41.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_42(self):
		print('test_42')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/42.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_43(self):
		print('test_43')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/43.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_44(self):
		print('test_44')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/44.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_45(self):
		print('test_45')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/45.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_46(self):
		print('test_46')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/46.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_47(self):
		print('test_47')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/47.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_48(self):
		print('test_48')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/48.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_49(self):
		print('test_49')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/49.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_5(self):
		print('test_5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_50(self):
		print('test_50')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/50.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_51(self):
		print('test_51')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/51.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_52(self):
		print('test_52')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/52.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_53(self):
		print('test_53')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/53.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_54(self):
		print('test_54')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/54.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_6(self):
		print('test_6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_7(self):
		print('test_7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_8(self):
		print('test_8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_9(self):
		print('test_9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10alchimie(self):
		print('test_Cours10alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_10_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11alchimie(self):
		print('test_Cours11alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_11_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12alchimie(self):
		print('test_Cours12alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_12_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13alchimie(self):
		print('test_Cours13alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_13_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14alchimie(self):
		print('test_Cours14alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_14_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15alchimie(self):
		print('test_Cours15alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_15_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16alchimie(self):
		print('test_Cours16alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_16_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours17alchimie(self):
		print('test_Cours17alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_17_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1alchimie(self):
		print('test_Cours1alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_1_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1mercure(self):
		print('test_Cours1mercure')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_1_mercure.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1methanation(self):
		print('test_Cours1methanation')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_1_methanation.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1petrochimie(self):
		print('test_Cours1petrochimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_1_petrochimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2alchimie(self):
		print('test_Cours2alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_2_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2mercure(self):
		print('test_Cours2mercure')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_2_mercure.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2methanation(self):
		print('test_Cours2methanation')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_2_methanation.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2petrochimie(self):
		print('test_Cours2petrochimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_2_petrochimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3alchimie(self):
		print('test_Cours3alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_3_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3methanation(self):
		print('test_Cours3methanation')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_3_methanation.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3petrochimie(self):
		print('test_Cours3petrochimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_3_petrochimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4alchimie(self):
		print('test_Cours4alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_4_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4methanation(self):
		print('test_Cours4methanation')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_4_methanation.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5alchimie(self):
		print('test_Cours5alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_5_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6alchimie(self):
		print('test_Cours6alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_6_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7alchimie(self):
		print('test_Cours7alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_7_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8alchimie(self):
		print('test_Cours8alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_8_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9alchimie(self):
		print('test_Cours9alchimie')

		cours = "file:///C:/Users/DELL/Documents/Lectures/1_Chimie/Cours_9_alchimie.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures20gestion(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/20_Gestion/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures21statistique(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12(self):
		print('test_Cours12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13(self):
		print('test_Cours13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14(self):
		print('test_Cours14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15(self):
		print('test_Cours15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16(self):
		print('test_Cours16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours171(self):
		print('test_Cours171')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_17_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours172(self):
		print('test_Cours172')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_17_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours173(self):
		print('test_Cours173')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_17_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours18(self):
		print('test_Cours18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours91(self):
		print('test_Cours91')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_9_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours94(self):
		print('test_Cours94')

		cours = "file:///C:/Users/DELL/Documents/Lectures/21_Statistique/Cours_9_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures22finance(unittest.TestCase):
	def test_1coursforexfini(self):
		print('test_1CoursForex[Fini]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/1_Cours_Forex_[Fini].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_2coursforexfini(self):
		print('test_2CoursForex[Fini]')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/2_Cours_Forex_[Fini].pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1df(self):
		print('test_Cours1DF')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_1_D_F.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1financeprojet(self):
		print('test_Cours1financeprojet')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_1_finance_projet.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursanalysefinanciere1(self):
		print('test_Coursanalysefinanciere1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_analyse_financiere_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursanalysefinanciere2(self):
		print('test_CoursAnalyseFinanciere2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_Analyse_Financiere_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancecomportementale1(self):
		print('test_Coursfinancecomportementale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_comportementale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancedebutant1(self):
		print('test_Coursfinancedebutant1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_debutant_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancedebanques1(self):
		print('test_Coursfinancedebanques1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_de_banques_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancedemarche1(self):
		print('test_Coursfinancedemarche1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_de_marche_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceentreprise1(self):
		print('test_CoursFinanceEntreprise1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_Finance_Entreprise_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceetcomptabilite1(self):
		print('test_Coursfinanceetcomptabilite1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_et_comptabilite_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceimmobiliere1(self):
		print('test_Coursfinanceimmobiliere1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_immobiliere_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceimmobiliere2(self):
		print('test_Coursfinanceimmobiliere2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_immobiliere_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceimmobiliere3(self):
		print('test_Coursfinanceimmobiliere3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_immobiliere_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceimmobiliere4(self):
		print('test_Coursfinanceimmobiliere4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_immobiliere_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceinternationale1(self):
		print('test_Coursfinanceinternationale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_internationale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceinternationale2(self):
		print('test_Coursfinanceinternationale2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_internationale_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceinternationale3(self):
		print('test_Coursfinanceinternationale3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_internationale_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinanceislamique1(self):
		print('test_Coursfinanceislamique1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_islamique_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancepersonnelle1(self):
		print('test_Coursfinancepersonnelle1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_personnelle_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancepublique1(self):
		print('test_Coursfinancepublique1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_publique_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancequantitative1(self):
		print('test_Coursfinancequantitative1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_quantitative_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfinancesolidaire1(self):
		print('test_Coursfinancesolidaire1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_finance_solidaire_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursgestionfinanciere1(self):
		print('test_Coursgestionfinanciere1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_gestion_financiere_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmathematiquesfinancieres1(self):
		print('test_Coursmathematiquesfinancieres1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/Cours_mathematiques_financieres1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_modernmoneymechanics(self):
		print('test_ModernMoneyMechanics')

		cours = "file:///C:/Users/DELL/Documents/Lectures/22_Finance/ModernMoneyMechanics.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures23psychisme(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/23_Psychisme/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures24commerce(unittest.TestCase):
	def test_comercedegrosetdetailcours1(self):
		print('test_ComerceDeGrosEtDetailCours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Comerce_De_Gros_Et_Detail_Cours_1_.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1prospectioncommerciale(self):
		print('test_Cours1prospectioncommerciale')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_1_prospection_commerciale.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1strategiecommerciale(self):
		print('test_Cours1strategiecommerciale')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_1_strategie_commerciale.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours1veillecommerciale(self):
		print('test_Cours1veillecommerciale')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_1_veille_commerciale.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2prospectioncommerciale(self):
		print('test_Cours2prospectioncommerciale')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_2_prospection_commerciale.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursactioncommerciale1(self):
		print('test_Coursactioncommerciale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_action_commerciale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursanimationcommerciale1(self):
		print('test_Coursanimationcommerciale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_animation_commerciale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursbailcommercial1(self):
		print('test_Coursbailcommercial1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_bail_commercial_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursbalancecommerciale1(self):
		print('test_Coursbalancecommerciale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_balance_commerciale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courscommerceambulant1(self):
		print('test_Courscommerceambulant1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_commerce_ambulant_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courscommerceelectronique1(self):
		print('test_Courscommerceelectronique1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_commerce_electronique_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courscommerceequitable1(self):
		print('test_Courscommerceequitable1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_commerce_equitable_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courscommerceinternational(self):
		print('test_Courscommerceinternational')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_commerce_international.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courscommercetriangualire1(self):
		print('test_Courscommercetriangualire1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_commerce_triangualire1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courscommunicationetredactioncommerciale1(self):
		print('test_Courscommunicationetredactioncommerciale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_communication_et_redaction_commerciale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursdroitetpolitiquecommerciale1(self):
		print('test_Coursdroitetpolitiquecommerciale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_droit_et_politique_commerciale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_courseffetdecommerce1(self):
		print('test_Courseffetdecommerce1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_effet_de_commerce_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursfonddecommerce1(self):
		print('test_Coursfonddecommerce1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_fond_de_commerce_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmargecommerciale1(self):
		print('test_Coursmargecommerciale1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_marge_commerciale_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_coursmobilecommerce1(self):
		print('test_Coursmobilecommerce1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/24_Commerce/Cours_mobile_commerce_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures25bim(unittest.TestCase):
	def test_cours1(self):
		print('test_cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/25_BIM/cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures26businessplan(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12(self):
		print('test_Cours12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13(self):
		print('test_Cours13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14(self):
		print('test_Cours14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15(self):
		print('test_Cours15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16(self):
		print('test_Cours16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours17(self):
		print('test_Cours17')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_17.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours18(self):
		print('test_Cours18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours19(self):
		print('test_Cours19')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_19.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours20(self):
		print('test_Cours20')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_20.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours21(self):
		print('test_Cours21')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_21.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6autiliserpourmonbusinessplan(self):
		print('test_Cours6AUtiliserPourMonBusinessPlan')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_6_A_Utiliser_Pour_Mon_Business_Plan.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/26_Business_Plan/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures27reglementreach(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12(self):
		print('test_Cours12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13(self):
		print('test_Cours13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14(self):
		print('test_Cours14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15(self):
		print('test_Cours15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16(self):
		print('test_Cours16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours17(self):
		print('test_Cours17')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_17.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours18(self):
		print('test_Cours18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours19(self):
		print('test_Cours19')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_19.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours20(self):
		print('test_Cours20')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_20.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours21(self):
		print('test_Cours21')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_21.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours22(self):
		print('test_Cours22')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_22.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours23(self):
		print('test_Cours23')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_23.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours24(self):
		print('test_Cours24')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_24.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours25(self):
		print('test_Cours25')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_25.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours26(self):
		print('test_Cours26')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_26.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours27(self):
		print('test_Cours27')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_27.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours28(self):
		print('test_Cours28')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_28.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours29(self):
		print('test_Cours29')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_29.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours30(self):
		print('test_Cours30')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_30.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours31(self):
		print('test_Cours31')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_31.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours32(self):
		print('test_Cours32')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_32.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours33(self):
		print('test_Cours33')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_33.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours34(self):
		print('test_Cours34')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_34.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours35(self):
		print('test_Cours35')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_35.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours36(self):
		print('test_Cours36')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_36.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours37(self):
		print('test_Cours37')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_37.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours38(self):
		print('test_Cours38')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_38.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours39(self):
		print('test_Cours39')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_39.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours40(self):
		print('test_Cours40')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_40.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours41(self):
		print('test_Cours41')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_41.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours42(self):
		print('test_Cours42')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_42.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours43(self):
		print('test_Cours43')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_43.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours44(self):
		print('test_Cours44')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_44.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours45(self):
		print('test_Cours45')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_45.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/27_Reglement_REACH/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures28atex(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/28_ATEX/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures29seveso(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/29_Seveso/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

class UnitTestsDesktopAutomationLectures30tradingalgorithmique(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/30_Trading_Algorithmique/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures31theoriesbreitwheeler(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/31_Theories_Breit_Wheeler/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures32worldwideenergylaw(unittest.TestCase):
	def test_1albany(self):
		print('test_1Albany')

		cours = "file:///C:/Users/DELL/Documents/Lectures/32_Worldwide_Energy_Law/1_Albany.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_2armenia(self):
		print('test_2Armenia')

		cours = "file:///C:/Users/DELL/Documents/Lectures/32_Worldwide_Energy_Law/2_Armenia.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_3bulgaria(self):
		print('test_3Bulgaria')

		cours = "file:///C:/Users/DELL/Documents/Lectures/32_Worldwide_Energy_Law/3_Bulgaria.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_4moldova(self):
		print('test_4Moldova')

		cours = "file:///C:/Users/DELL/Documents/Lectures/32_Worldwide_Energy_Law/4_Moldova.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_5montenegro(self):
		print('test_5Montenegro')

		cours = "file:///C:/Users/DELL/Documents/Lectures/32_Worldwide_Energy_Law/5_Montenegro.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_6gibraltar(self):
		print('test_6Gibraltar')

		cours = "file:///C:/Users/DELL/Documents/Lectures/32_Worldwide_Energy_Law/6_Gibraltar.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures33conventionminamata(unittest.TestCase):
	def test_minamataconventionbookletsep2019fr(self):
		print('test_MinamataConventionbookletSep2019FR')

		cours = "file:///C:/Users/DELL/Documents/Lectures/33_Convention_Minamata/Minamata-Convention-booklet-Sep2019-FR.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures34icpe(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/34_ICPE/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures35symbolisme(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/35_Symbolisme/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/35_Symbolisme/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/35_Symbolisme/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/35_Symbolisme/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/35_Symbolisme/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures36esoterisme(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/36_Esoterisme/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/36_Esoterisme/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/36_Esoterisme/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/36_Esoterisme/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/36_Esoterisme/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures37conventiondechicago(unittest.TestCase):
	def test_conventiondechicago(self):
		print('test_ConventionDeChicago')

		cours = "file:///C:/Users/DELL/Documents/Lectures/37_Convention_De_Chicago/Convention_De_Chicago.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures3assurances(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12(self):
		print('test_Cours12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13(self):
		print('test_Cours13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14(self):
		print('test_Cours14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15(self):
		print('test_Cours15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16(self):
		print('test_Cours16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours17(self):
		print('test_Cours17')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_17.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours18(self):
		print('test_Cours18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours19(self):
		print('test_Cours19')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_19.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours20(self):
		print('test_Cours20')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_20.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours21(self):
		print('test_Cours21')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_21.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours22(self):
		print('test_Cours22')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_22.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/3_Assurances/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures4banque(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/4_Banque/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/4_Banque/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/4_Banque/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures5scienceingenieure(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/5_Science_Ingenieure/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/5_Science_Ingenieure/cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/5_Science_Ingenieure/cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures6physique(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12(self):
		print('test_Cours12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13(self):
		print('test_Cours13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14(self):
		print('test_Cours14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15(self):
		print('test_Cours15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16(self):
		print('test_Cours16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours17(self):
		print('test_Cours17')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_17.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours18(self):
		print('test_Cours18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours19(self):
		print('test_Cours19')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_19.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours20(self):
		print('test_Cours20')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_20.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours21(self):
		print('test_Cours21')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_21.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours22(self):
		print('test_Cours22')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_22.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours23(self):
		print('test_Cours23')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_23.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours24(self):
		print('test_Cours24')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_24.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours25(self):
		print('test_Cours25')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_25.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours26(self):
		print('test_Cours26')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_26.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours27(self):
		print('test_Cours27')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_27.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours28(self):
		print('test_Cours28')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_28.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours29(self):
		print('test_Cours29')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_29.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours30(self):
		print('test_Cours30')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_30.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours31(self):
		print('test_Cours31')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_31.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours32(self):
		print('test_Cours32')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_32.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours33(self):
		print('test_Cours33')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_33.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours34(self):
		print('test_Cours34')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_34.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours35(self):
		print('test_Cours35')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_35.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours36(self):
		print('test_Cours36')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_36.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours37(self):
		print('test_Cours37')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_37.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours38(self):
		print('test_Cours38')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_38.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours39(self):
		print('test_Cours39')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_39.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours40(self):
		print('test_Cours40')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_40.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours41(self):
		print('test_Cours41')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_41.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours42(self):
		print('test_Cours42')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_42.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours43(self):
		print('test_Cours43')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_43.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours44(self):
		print('test_Cours44')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_44.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours45(self):
		print('test_Cours45')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_45.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/6_Physique/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures7biologie(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/7_Biologie/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/7_Biologie/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/7_Biologie/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/7_Biologie/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures8langues(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours12(self):
		print('test_Cours12')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_12.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours13(self):
		print('test_Cours13')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_13.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours14(self):
		print('test_Cours14')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_14.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours15(self):
		print('test_Cours15')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_15.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours16(self):
		print('test_Cours16')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_16.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours17(self):
		print('test_Cours17')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_17.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours18(self):
		print('test_Cours18')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_18.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours19(self):
		print('test_Cours19')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_19.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours20(self):
		print('test_Cours20')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_20.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours21(self):
		print('test_Cours21')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_21.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours22(self):
		print('test_Cours22')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_22.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours23(self):
		print('test_Cours23')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_23.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours24(self):
		print('test_Cours24')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_24.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours25(self):
		print('test_Cours25')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_25.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours26(self):
		print('test_Cours26')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_26.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours27(self):
		print('test_Cours27')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_27.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours28(self):
		print('test_Cours28')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_28.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours29(self):
		print('test_Cours29')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_29.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours30(self):
		print('test_Cours30')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_30.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours31(self):
		print('test_Cours31')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_31.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours32(self):
		print('test_Cours32')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_32.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours33(self):
		print('test_Cours33')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_33.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours34(self):
		print('test_Cours34')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_34.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours35(self):
		print('test_Cours35')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_35.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours36(self):
		print('test_Cours36')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_36.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/8_Langues/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


class UnitTestsDesktopAutomationLectures9comptabilite(unittest.TestCase):
	def test_cours1(self):
		print('test_Cours1')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_1.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours10(self):
		print('test_Cours10')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_10.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours11(self):
		print('test_Cours11')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_11.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours2(self):
		print('test_Cours2')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_2.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours3(self):
		print('test_Cours3')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_3.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours4(self):
		print('test_Cours4')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_4.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours5(self):
		print('test_Cours5')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_5.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours6(self):
		print('test_Cours6')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_6.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours7(self):
		print('test_Cours7')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_7.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours8(self):
		print('test_Cours8')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_8.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')

	def test_cours9(self):
		print('test_Cours9')

		cours = "file:///C:/Users/DELL/Documents/Lectures/9_Comptabilite/Cours_9.pdf"

		url_cours = cours.replace('file:///', '').replace('/', '\\')

		pdf = PdfFileReader(open(url_cours, 'rb'))

		number_of_pages = pdf.getNumPages()

		time.sleep(5)

		app = Application(backend="uia")

		app.start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

		time.sleep(5)
		pywinauto.keyboard.send_keys(url_cours)

		time.sleep(5)

		pywinauto.keyboard.send_keys('{ENTER}')

		time.sleep(5)

		pywinauto.mouse.click(button='left', coords=(900, 250))

		time.sleep(5)

		for i in range(0, 14*number_of_pages):
			pywinauto.keyboard.send_keys('{DOWN}')

			time.sleep(3)

		time.sleep(5)

		pywinauto.keyboard.send_keys('^w')


if __name__ == '__main__':
    unittest.main()
