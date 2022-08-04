import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror
import unittest


class UnitTestsEmailMarketingForGitHub(unittest.TestCase):
    def test_send_one_email_with_outlook_account(self):
        fromaddr = ''
        password = ''

        ccaddr = ''

        smtp_server = 'smtp-mail.outlook.com'  # smtp.office365.com
        smtp_port = 587

        emails = [
            ''
        ]

        body = (
            "Hello,\n\n"
            "Do you ship your products internationally please ? \n"
            "Kind regards,\n\n"
        )

        for email in emails:
            toaddr = email
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Cc'] = ccaddr
            msg['Subject'] = "Request of information about your products"

            msg.attach(MIMEText(body, 'plain'))

            text = msg.as_string()

            try:
                server_ssl = smtplib.SMTP_SSL(smtp_server, smtp_port)
                server_ssl.ehlo()
                server_ssl.login(fromaddr, password)
                server_ssl.sendmail(fromaddr, toaddr, text)
                server_ssl.quit()
            except (gaierror, ConnectionRefusedError):
                # tell the script to report if your message was sent or which errors need to be fixed
                print('Failed to connect to the server. Bad connection settings?')
            except smtplib.SMTPServerDisconnected:
                print('Failed to connect to the server. Wrong user/password?')
            except smtplib.SMTPException as e:
                print('SMTP error occurred: ' + str(e))
            else:
                print('Sent to : ' + str(email) + ' from ' + str(fromaddr))


if __name__ == '__main__':
    unittest.main()
