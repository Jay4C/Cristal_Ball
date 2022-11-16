import os
import unittest
import imaplib
from imap_tools import MailBox


class UnitTestsEmailSpamFilteringOutlookPersonalAccount(unittest.TestCase):
    # outlook personal account
    def test_print_the_subject_of_each_email_in_outlook_personal_account_from_inbox(self):
        print("test_print_the_subject_of_each_email_in_outlook_personal_account_1_from_inbox")

        imap_host = 'outlook.office365.com'
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
            for msg in mailbox.fetch():
                print("subject : " + msg.subject + " ; text : " + msg.text)

    def test_print_the_subject_of_each_email_in_outlook_personal_account_from_deleted_items(self):
        print("test_print_the_subject_of_each_email_in_outlook_personal_account_1_from_deleted_items")

        imap_host = 'outlook.office365.com'
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='Deleted') as mailbox:
            subjects = [msg.subject for msg in mailbox.fetch()]

            for subject in subjects:
                print(subject)

    def test_list_all_mailboxes_of_email_outlook_personal_account(self):
        print("test_list_all_mailboxes_of_email_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_port = 993
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()[1]

            for directory in directories:
                l = str(directory).split(' "/" ')
                # print(str(directory))
                print(str(l[0]) + " = " + str(l[1]).replace("'", ""))

            imap.logout()

    def test_list_all_mailboxes_from_deleted_folder_of_email_outlook_personal_account_1(self):
        print("test_list_all_mailboxes_of_email_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_port = 993
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()[1]

            for directory in directories:
                l = str(directory).split(' "/" ')

                if "Deleted" in str(l[1]).replace("'", ""):
                    print(str(l[1]).replace("'", ""))

            imap.logout()

    def test_print_mails_from_specific_folder_from_outlook_personal_account(self):
        print("test_print_mails_from_specific_folder_from_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        specific_folder = 'Junk'

        directory = specific_folder.replace("/", "_")

        if not os.path.isdir(directory):
            os.mkdir(directory)

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=specific_folder) as mailbox:
            i = 1

            for msg in mailbox.fetch():
                try:
                    print("email : " + str(i))

                    subject = str(msg.subject)
                    date = str(msg.date)
                    date_str = str(msg.date_str)
                    from_ = str(msg.from_)
                    from_values = str(msg.from_values)
                    to = str(msg.to)
                    to_values = str(msg.to_values)
                    reply_to = str(msg.reply_to)
                    reply_to_values = str(msg.reply_to_values)
                    cc = str(msg.cc)
                    cc_values = str(msg.cc_values)
                    bcc = str(msg.bcc)
                    bcc_values = str(msg.bcc_values)
                    text = str(msg.text)
                    html = str(msg.html)

                    with open(directory + "\\Page_" + str(i) + ".txt", "w", encoding='utf-8-sig') as file:
                        file.write("subject : " + subject)
                        file.write("\n\n")

                        file.write("date : " + date)
                        file.write("\n\n")

                        file.write("date_str : " + date_str)
                        file.write("\n\n")

                        file.write("from_ : " + from_)
                        file.write("\n\n")

                        file.write("from_values : " + from_values)
                        file.write("\n\n")

                        file.write("to : " + to)
                        file.write("\n\n")

                        file.write("to_values : " + to_values)
                        file.write("\n\n")

                        file.write("reply_to : " + reply_to)
                        file.write("\n\n")

                        file.write("reply_to_values : " + reply_to_values)
                        file.write("\n\n")

                        file.write("cc : " + cc)
                        file.write("\n\n")

                        file.write("cc_values : " + cc_values)
                        file.write("\n\n")

                        file.write("bcc : " + bcc)
                        file.write("\n\n")

                        file.write("bcc_values : " + bcc_values)
                        file.write("\n\n")

                        file.write("text : " + text)
                        file.write("\n\n")

                        file.write("html : " + html)
                        file.write("\n\n")

                        file.close()
                except Exception as e:
                    print("error : " + str(e))

                i += 1

    def test_download_all_attachments_from_all_folders_from_outlook_personal_account(self):
        print("test_print_all_mails_from_all_folders_from_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_port = 993
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()[1]

            imap.logout()

            i = 1

            for directory in directories:
                initial_folder = str(directory).split(' "/" ')[1].replace("'", "")

                print(initial_folder)

                if not os.path.isdir(initial_folder.replace("/", "")):
                    os.mkdir(initial_folder)
                    os.chmod(initial_folder, 0o777)

                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=initial_folder) as mailbox:
                    for msg in mailbox.fetch():
                        try:
                            for att in msg.attachments:
                                print(att.filename.replace(" ", "")
                                                  .replace("-", "")
                                                  .replace("_", "")
                                                  .replace("[", "")
                                                  .replace("]", "")
                                                  .replace("'", "")
                                                  .replace("Jason", "")
                                                  .replace("ALOYAU", "")
                                                  .replace("\r", "")
                                                  .replace("\n", ""), att.content_type)
                                with open(initial_folder + "\\" + format(att.filename
                                                                            .replace(" ", "")
                                                                            .replace("-", "")
                                                                            .replace("_", "")
                                                                            .replace("[", "")
                                                                            .replace("]", "")
                                                                            .replace("'", "")
                                                                            .replace("Jason", "")
                                                                            .replace("ALOYAU", "")
                                                                            .replace("\r", "")
                                                                            .replace("\n", "")
                                                                         ), 'wb') as f:
                                    f.write(att.payload)
                                    f.close()
                        except Exception as e:
                            print("error : " + str(e))

                        i += 1

    def test_print_all_mails_from_all_folders_from_outlook_personal_account(self):
        print("test_print_all_mails_from_all_folders_from_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_port = 993
        imap_user = 'aymerick.aloyau@outlook.fr'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()[1]

            imap.logout()

            i = 1

            for directory in directories:
                initial_folder = str(directory).split(' "/" ')[1].replace("'", "")

                print(initial_folder)

                if not os.path.isdir(initial_folder):
                    os.mkdir(initial_folder)
                    os.chmod(initial_folder, 0o777)

                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=initial_folder) as mailbox:
                    for msg in mailbox.fetch():
                        try:
                            print("email : " + str(i))

                            with open(initial_folder + "\\Page_" + str(i) + ".txt", "w", encoding='utf-8-sig') as file:
                                subject = str(msg.subject)
                                file.write("subject : " + subject)
                                file.write("\n\n")

                                date = str(msg.date)
                                file.write("date : " + date)
                                file.write("\n\n")

                                date_str = str(msg.date_str)
                                file.write("date_str : " + date_str)
                                file.write("\n\n")

                                from_ = str(msg.from_)
                                file.write("from_ : " + from_)
                                file.write("\n\n")

                                from_values = str(msg.from_values)
                                file.write("from_values : " + from_values)
                                file.write("\n\n")

                                to = str(msg.to)
                                file.write("to : " + to)
                                file.write("\n\n")

                                to_values = str(msg.to_values)
                                file.write("to_values : " + to_values)
                                file.write("\n\n")

                                reply_to = str(msg.reply_to)
                                file.write("reply_to : " + reply_to)
                                file.write("\n\n")

                                reply_to_values = str(msg.reply_to_values)
                                file.write("reply_to_values : " + reply_to_values)
                                file.write("\n\n")

                                cc = str(msg.cc)
                                file.write("cc : " + cc)
                                file.write("\n\n")

                                cc_values = str(msg.cc_values)
                                file.write("cc_values : " + cc_values)
                                file.write("\n\n")

                                bcc = str(msg.bcc)
                                file.write("bcc : " + bcc)
                                file.write("\n\n")

                                bcc_values = str(msg.bcc_values)
                                file.write("bcc_values : " + bcc_values)
                                file.write("\n\n")

                                text = str(msg.text)
                                file.write("text : " + text)
                                file.write("\n\n")

                                html = str(msg.html)
                                file.write("html : " + html)
                                file.write("\n\n")

                                file.close()

                            for att in msg.attachments:
                                print(att.filename.replace(" ", "")
                                                  .replace("-", "")
                                                  .replace("_", "")
                                                  .replace("[", "")
                                                  .replace("]", "")
                                                  .replace("'", "")
                                                  .replace("Jason", "")
                                                  .replace("ALOYAU", "")
                                                  .replace("\r", "")
                                                  .replace("\n", ""), att.content_type)
                                with open(initial_folder + "\\" + format(att.filename
                                                                            .replace(" ", "")
                                                                            .replace("-", "")
                                                                            .replace("_", "")
                                                                            .replace("[", "")
                                                                            .replace("]", "")
                                                                            .replace("'", "")
                                                                            .replace("Jason", "")
                                                                            .replace("ALOYAU", "")
                                                                            .replace("\r", "")
                                                                            .replace("\n", "")
                                                                         ), 'wb') as f:
                                    f.write(att.payload)
                                    f.close()
                        except Exception as e:
                            print("error : " + str(e))

                        i += 1

    def test_delete_all_dirty_mails_from_all_folders_from_outlook_personal_account(self):
        print("test_print_all_mails_from_all_folders_from_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        initial_folders = [
            ''
        ]

        for initial_folder in initial_folders:
            for i in range(0, 10):
                print("tour : " + str(i))
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=initial_folder) as mailbox:
                    try:
                        for msg in mailbox.fetch():
                            if (
                                    "Undelivered" in msg.subject
                                    or
                                    "Undeliverable" in msg.subject
                                    or
                                    "Non remis" in msg.subject
                                    or
                                    "Returned mail" in msg.subject
                                    or
                                    "DELIVERY FAILURE" in msg.subject
                                    or
                                    "Non recapitabile" in msg.subject
                                    or
                                    "Failure" in msg.subject
                                    or
                                    "Mail not delivered" in msg.subject
                                    or
                                    "Returned Mail" in msg.subject
                                    or
                                    "Impossible d'envoyer l'email" in msg.subject
                                    or
                                    "Delivery has failed" in msg.text
                                    or
                                    "failed" in msg.text
                                    or
                                    "failed" in msg.subject
                                    or
                                    "failure" in msg.subject
                                    or
                                    "couldn't be delivered" in msg.subject
                                    or
                                    "couldn't be delivered" in msg.text
                                    or
                                    "rejected" in msg.text
                                    or
                                    "rejected" in msg.subject
                                    or
                                    "Rejected" in msg.text
                                    or
                                    "Rejected" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "Fehler bei der Nachrichtenzustellung" in msg.text
                                    or
                                    "Uw bericht kan niet worden bezorgd bij de volgende geadresseerden of groepen" in msg.text
                                    or
                                    "Bad destination host 'DNS Soft Error looking up" in msg.text
                                    or
                                    "A message that you sent has not yet been delivered to one or more of its" in msg.text
                                    or
                                    "Your message could not be delivered for" in msg.text
                                    or
                                    "Unzustellbar" in msg.subject
                                    or
                                    "could not be delivered" in msg.text
                                    or
                                    "not able to deliver" in msg.text
                                    or
                                    "postmaster" in msg.from_
                            ):
                                mailbox.move(msg.uid, 'Deleted')
                                print("moved Deleted : " + str(msg.uid))
                    except Exception as e:
                        print("error : " + str(e))

    def test_delete_all_mail_from_deleted_folders_from_outlook_personal_account(self):
        print("test_print_all_mails_from_all_folders_from_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_port = 993
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        folder_deleted = []

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()[1]

            for directory in directories:
                l = str(directory).split(' "/" ')

                if "Deleted" in str(l[1]).replace("'", ""):
                    print(str(l[1]).replace("'", ""))

                    folder_deleted.append(str(l[1]).replace("'", ""))

            imap.logout()

        for initial_folder in folder_deleted:
            for i in range(0, 10):
                print("tour : " + str(i))
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=initial_folder) as mailbox:
                    try:
                        for msg in mailbox.fetch():
                            mailbox.move(msg.uid, "Deleted")
                            print("move to deleted : " + str(msg.uid))
                    except Exception as e:
                        print("error : " + str(e))

    def test_count_deleted_folders_from_outlook_personal_account(self):
        print("test_print_all_mails_from_all_folders_from_outlook_personal_account_1")

        imap_host = 'outlook.office365.com'
        imap_port = 993
        imap_user = 'jason.aloyau@outlook.fr'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()[1]

            i = 1

            for directory in directories:
                l = str(directory).split(' "/" ')

                if "Deleted" in str(l[1]).replace("'", ""):
                    print(str(i) + " _ " + str(l[1]).replace("'", ""))
                    i += 1

            imap.logout()
    # outlook personal account


class UnitTestsEmailSpamFilteringGmailAccount(unittest.TestCase):
    # gmail 1
    def test_print_the_subject_of_each_email_in_gmail_1_from_inbox(self):
        print("test_print_the_subject_of_each_email_in_outlook_personal_account_1_from_inbox")

        imap_host = 'imap.gmail.com'
        imap_user = 'jay1993izi@gmail.com'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
            for msg in mailbox.fetch():
                #print("subject : " + msg.subject)
                print("subject : " + msg.subject + " ; text : " + msg.text)

    # gmail 2
    # ok
    def test_sort_all_emails_in_gmail_2_from_inbox_v1(self):
        print("test_sort_all_emails_in_gmail_2_from_inbox")

        imap_host = 'imap.gmail.com'
        imap_user = 'jason.aymerick.aloyau@gmail.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
                    for msg in mailbox.fetch():
                        if "Demande d'informations pour un partenariat d'injection de dihydrogène et/ou de méthane " \
                           "de synthèse dans un réseau de gaz naturel – " \
                           "Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Injection_Gaz/Receptions"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la diffusion de publicités - Société Holomorphe".lower() \
                                in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Agences_De_Publicites/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Spontaneous application".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Clients/Candidature_Freelance_Monde/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "candidature spontanée".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Clients/Candidature_Freelance_France/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour l'achat de matériels électriques - Société " \
                             "Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Materiels_Electriques/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la fabrication de transformateurs électriques, bobines " \
                             "électriques et circuits électroniques aux normes ISO / TC 197 pour les technologies " \
                             "de l'hydrogène – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Transformateurs_Bobines_ISO_TC_197/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la transformation de tous types de véhicules avec des " \
                             "technologies de l'hydrogène aux normes ISO / TC 197 – " \
                             "Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Filiales/Achat_Vente_Vehicule/Marketing/Fournisseurs" \
                                     "/Garages_Vehicules_Hydrogene/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la gravure de cadenas et clés contre la falsification " \
                             "et le vol – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Serruriers/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour l'achat de chaudières fonctionnant à l'hydrogène " \
                             "gazeux – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Chauffage/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour le contrôle technique de tous types de véhicules " \
                             "équipés de technologies de l'hydrogène aux normes ISO / TC 197 " \
                             "– Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Controle_Technique/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la certification ISO TC 197 et les certifications " \
                             "ISO conformes pour les technologies de l'hydrogène – " \
                             "Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Certificateurs_ISO/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour l'achat de palettes de manutention – " \
                             "Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Palettes/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour l'achat de containers – Société " \
                             "Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Container/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour un partenariat concernant l'accès et le " \
                             "raccordement à un réseau de transport de gaz naturel – Société " \
                             "Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Acces_Reseau_Gaz_Naturel/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour l'achat de biens immobiliers pour installer des " \
                             "installations classées pour la protection de l'environnement pour la production " \
                             "d'hydrogène gazeux pur raccordée à un réseau de transport de gaz naturel " \
                             "– Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Agents_Immobiliers/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la rédaction de contrats spécifiques pour " \
                             "l'énergie – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Avocats/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour le dépôt de la demande de permis de construire et " \
                             "le dépôt de la demande d'autorisation préfectorale pour la construction  d'une " \
                             "installation classée pour la protection de l'environnement concernant la production " \
                             "d'hydrogène gazeux par électrolyse de l'eau".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Architectes/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la construction d'une installation classée pour " \
                             "la protection de l'environnement concernant la production de dihydrogène gazeux " \
                             "pur par électrolyse de l'eau – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Constructeurs_Batiments/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la fabrication d'armoires métalliques et réservoirs " \
                             "en plexiglas – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Menuiseries/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Information request for electricity production".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Production_Electricite/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour un partenariat pour la production " \
                             "d'électricité".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Production_Electricite/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Information request for a partnership for producing " \
                             "electricity".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Production_Electricite/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour un partenariat concernant la transmutation du " \
                             "plomb ou mercure ou un autre élément chimique en or par bombardements à " \
                             "neutrons ou une autre technique – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Transmutation_Plomb_En_Or/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Information request for a partnership for producing CH4 from C02".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/CO2_Into_CH4/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d’informations pour un partenariat de conversion de dioxyde de carbone " \
                             "CO2 en méthane de synthèse CH4".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/CO2_Into_CH4/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la vente de générateurs Marx".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Generateur_Marx/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Information request for the injection of pure hydrogen gas and synthetic methane " \
                             "into your natural gas network – Holomorphe company".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Injection_Gaz/Receptions"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour des octrois de prêts professionnels – " \
                             "Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Octroi_Prets_Professionnels/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour un partenariat commercial pour vos missions – " \
                             "Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Editeurs_De_Logiciels/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour un partenariat commercial pour vendre des véhicules " \
                             "à eau – Société Holomorphe".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Vehicule_A_Eau/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Request for information for a future partnership concerning the transmutation of lead " \
                             "or mercury or another chemical element into gold by neutron bombardment " \
                             "or another technique".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Transmutation_Plomb_En_Or/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Request information for the sale of pure liquid mercury".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Mercure/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour l'achat de mercure".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Mercure/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "request information for the sale of pure mercury".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Mercure/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour effectuer des recherches scientifiques dans " \
                             "les eaux internationales".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Bateau/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Open source".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Open_source/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "free prove of concept".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Open_source/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d’informations pour les déclarations EDI-TDFC des démarches " \
                             "administratives fiscales".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Comptable/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour des dépenses de recherches et " \
                             "développements".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Recherches_Et_Developpements/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "anti-gravité".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Recherches_Et_Developpements/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la vente de vis, rondelles, écrous M10".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Vis_Ecrous/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la vente de sels chimiques".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Sels_Chimiques/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la vente de tube quartz".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Tube_Quartz/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Free software development".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Open_source/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Free proof of concept for software development".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Open_source/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour la vente de batterie " \
                             "électrique".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Batteries_Electriques/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour assurer un site de production de dihydrogène ou " \
                             "méthane de synthèse raccordé à un réseau de gaz naturel".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Assurance/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Information request for your solutions of direct air capture for " \
                             "CO2".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Partenaires/Direct_Air_Capture_CO2/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Demande d'informations pour fabriquer des pièces mécaniques".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Pieces_Mecaniques/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Mise à jour de votre tableau de bord".lower() in msg.subject.lower():
                            folder = "Test_Net_Entreprises"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "alerte de sécurité concernant votre compte google associé".lower() in msg.subject.lower():
                            folder = "Poubelle"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        else:
                            print("msg : " + msg.subject.lower())
            except Exception as e:
                print('error : ' + str(e))

    # ok
    def test_sort_all_emails_in_gmail_2_from_inbox_v2(self):
        print("test_sort_all_emails_in_gmail_2_from_inbox")

        imap_host = 'imap.gmail.com'
        imap_user = 'jason.aymerick.aloyau@gmail.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
                    for msg in mailbox.fetch():
                        if "candidature spontanée".lower() in msg.subject.lower():
                            folder = "Candidature_spontanee"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Mise à jour de votre tableau de bord".lower() in msg.subject.lower():
                            folder = "Test_Net_Entreprises"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "presentation of Stanley Meyer's water electrolyser for the generation of dihydrogen"\
                                .lower() in msg.subject.lower():
                            folder = "Presentation_Generation_Hydrogen"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "demande d'informations pour la production d'engrais azotés"\
                                .lower() in msg.subject.lower():
                            folder = "Production_Engrais_Azotes"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "demande d'informations pour la fabrication de transformateur électrique en ligne " \
                             "par commerce électronique"\
                                .lower() in msg.subject.lower():
                            folder = "Transformateur_Electrique_En_Ligne"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "demande d'informations pour tester des chaudières avec de l'hydrogène"\
                                .lower() in msg.subject.lower():
                            folder = "Chaudieres_Hydrogene"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "request of information for licensing an electricity power plant by using free " \
                             "energy devices"\
                                .lower() in msg.subject.lower():
                            folder = "Licensing_Electricity_Free_Energy"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "demande d'informations pour tester des engins de manutention et de transport avec " \
                             "de l'hydrogène"\
                                .lower() in msg.subject.lower():
                            folder = "Tester_Engins_Manutention_Hydrogene"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "alerte de sécurité concernant votre compte google associé".lower() in msg.subject.lower():
                            folder = "Poubelle"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "request for a presentation of your direct air capture technology for producing carbon " \
                             "dioxide from air in the goal of a partnership - " \
                             "holomorphe company".lower() in msg.subject.lower():
                            folder = "Direct_Air_Capture"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "demande d'informations pour l'adaptation de groupe électrogène avec les " \
                             "technologies de l'hydrogène de stanley meyer - " \
                             "société holomorphe".lower() in msg.subject.lower():
                            folder = "Achats_Groupes_Electrogenes_Turbines_Gaz"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "demande d'informations pour faire des travaux de fabrication de transformateurs " \
                             "voltage intensifier circuit (vic) - société holomorphe".lower() in msg.subject.lower():
                            folder = "Transformateur_Electrique_En_Ligne"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "delivery status notification (failure)".lower() in msg.subject.lower():
                            folder = "[Gmail]/Corbeille"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "undeliverable: spontaneous application for a job as renewable energy engineer in full " \
                             "time contract - jason aloyau".lower() in msg.subject.lower():
                            folder = "[Gmail]/Corbeille"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "non remis : spontaneous application for a job as renewable energy " \
                             "engineer in full time contract - jason aloyau".lower() in msg.subject.lower():
                            folder = "[Gmail]/Corbeille"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "delivery status notification (delay)".lower() in msg.subject.lower():
                            folder = "[Gmail]/Corbeille"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        else:
                            print("msg : " + msg.subject.lower())
            except Exception as e:
                print('error : ' + str(e))

    # ok
    def test_sort_all_emails_in_gmail_2_from_spam(self):
        print("test_sort_all_emails_in_gmail_2_from_inbox")

        imap_host = 'imap.gmail.com'
        imap_user = 'jason.aymerick.aloyau@gmail.com'
        imap_pass = ''
        initial_folder = "[Gmail]/Spam"

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=initial_folder) as mailbox:
                    for msg in mailbox.fetch():
                        if "Demande d'informations pour faire une preuve de concept".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Fournisseurs/Preuve_Concept_Hydrogene/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "Spontaneous application for a Full-Stack developer in freelance".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Clients/Candidature_Freelance_Monde/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "candidature spontanée pour un poste de développeur full-stack en freelance".lower() in msg.subject.lower():
                            folder = "Holomorphe/Marketing/Clients/Candidature_Freelance_France/Reception"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        else:
                            print("msg : " + msg.subject.lower())
            except Exception as e:
                print('error : ' + str(e))

    # ok
    def test_print_the_subject_of_each_email_in_gmail_2_from_inbox(self):
        print("test_print_the_subject_of_each_email_in_gmail_2_from_inbox")

        imap_host = 'imap.gmail.com'
        imap_user = 'jason.aymerick.aloyau@gmail.com'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
            for msg in mailbox.fetch():
                print("subject : " + msg.subject)
                # print("subject : " + msg.subject + " ; text : " + msg.text)

    # ok
    def test_print_all_mailboxes_in_gmail_2(self):
        print('test_print_all_mailboxes_in_gmail_2')

        imap_host = 'imap.gmail.com'
        imap_port = 993
        imap_user = 'jason.aymerick.aloyau@gmail.com'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()

            for directory in directories:
                print(directory)

            imap.logout()

    # gmail 3
    # ok
    def test_print_the_subject_of_each_email_in_gmail_3_from_inbox(self):
        print("test_print_the_subject_of_each_email_in_outlook_personal_account_1_from_inbox")

        imap_host = 'imap.gmail.com'
        imap_user = 'jason.jean.aloyau@gmail.com'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
            for msg in mailbox.fetch():
                print("subject : " + msg.subject)
                #print("subject : " + msg.subject + " ; text : " + msg.text)

    # ok
    def test_sort_all_emails_in_gmail_3_from_inbox(self):
        print("test_sort_all_emails_in_gmail_3_from_inbox")

        imap_host = 'imap.gmail.com'
        imap_user = 'jason.jean.aloyau@gmail.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
                    for msg in mailbox.fetch():
                        if "nous vous informons qu'elle n'a pas été retenue pour ce poste".lower() in msg.text.lower():
                            folder = "[Gmail]/Corbeille"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "alerte de sécurité concernant votre compte google associé".lower() in msg.subject.lower():
                            folder = "[Gmail]/Corbeille"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        elif "adecco: accusé de réception de votre candidature".lower() in msg.subject.lower():
                            folder = "[Gmail]/Corbeille"
                            mailbox.move(msg.uid, folder)
                            print("moved " + folder + " : " + msg.uid)
                        else:
                            print("msg : " + msg.subject.lower())
            except Exception as e:
                print('error : ' + str(e))

    # ok
    def test_print_all_mailboxes_in_gmail_3(self):
        print('test_print_all_mailboxes_in_gmail_3')

        imap_host = 'imap.gmail.com'
        imap_port = 993
        imap_user = 'jason.jean.aloyau@gmail.com'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()

            for directory in directories:
                print(directory)

            imap.logout()

    # other
    def test_print_all_mails_from_all_folders_from_gmail_personal_account(self):
        print("test_print_all_mails_from_all_folders_from_outlook_personal_account_1")

        imap_host = 'imap.gmail.com'
        imap_port = 993
        imap_user = 'jason.jean.aloyau@gmail.com'
        imap_pass = ''

        initial_folder = 'Google_Adsense'

        print(initial_folder)

        if not os.path.isdir(initial_folder):
            os.mkdir(initial_folder)
            os.chmod(initial_folder, 0o777)

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=initial_folder) as mailbox:
            i = 0

            for msg in mailbox.fetch():
                try:
                    print("email : " + str(i))

                    with open(initial_folder + "\\Page_" + str(i) + ".txt", "w", encoding='utf-8-sig') as file:
                        subject = str(msg.subject)
                        file.write("subject : " + subject)
                        file.write("\n\n")

                        date = str(msg.date)
                        file.write("date : " + date)
                        file.write("\n\n")

                        date_str = str(msg.date_str)
                        file.write("date_str : " + date_str)
                        file.write("\n\n")

                        from_ = str(msg.from_)
                        file.write("from_ : " + from_)
                        file.write("\n\n")

                        from_values = str(msg.from_values)
                        file.write("from_values : " + from_values)
                        file.write("\n\n")

                        to = str(msg.to)
                        file.write("to : " + to)
                        file.write("\n\n")

                        to_values = str(msg.to_values)
                        file.write("to_values : " + to_values)
                        file.write("\n\n")

                        reply_to = str(msg.reply_to)
                        file.write("reply_to : " + reply_to)
                        file.write("\n\n")

                        reply_to_values = str(msg.reply_to_values)
                        file.write("reply_to_values : " + reply_to_values)
                        file.write("\n\n")

                        cc = str(msg.cc)
                        file.write("cc : " + cc)
                        file.write("\n\n")

                        cc_values = str(msg.cc_values)
                        file.write("cc_values : " + cc_values)
                        file.write("\n\n")

                        bcc = str(msg.bcc)
                        file.write("bcc : " + bcc)
                        file.write("\n\n")

                        bcc_values = str(msg.bcc_values)
                        file.write("bcc_values : " + bcc_values)
                        file.write("\n\n")

                        text = str(msg.text)
                        file.write("text : " + text)
                        file.write("\n\n")

                        html = str(msg.html)
                        file.write("html : " + html)
                        file.write("\n\n")

                        file.close()

                    for att in msg.attachments:
                        print(att.filename.replace(" ", "")
                                          .replace("-", "")
                                          .replace("_", "")
                                          .replace("[", "")
                                          .replace("]", "")
                                          .replace("'", "")
                                          .replace("Jason", "")
                                          .replace("ALOYAU", "")
                                          .replace("\r", "")
                                          .replace("\n", ""), att.content_type)
                        with open(initial_folder + "\\" + format(att.filename
                                                                    .replace(" ", "")
                                                                    .replace("-", "")
                                                                    .replace("_", "")
                                                                    .replace("[", "")
                                                                    .replace("]", "")
                                                                    .replace("'", "")
                                                                    .replace("Jason", "")
                                                                    .replace("ALOYAU", "")
                                                                    .replace("\r", "")
                                                                    .replace("\n", "")
                                                                 ), 'wb') as f:
                            f.write(att.payload)
                            f.close()
                except Exception as e:
                    print("error : " + str(e))

                i += 1


class UnitTestsEmailSpamFilteringHolomorpheOvhAccount(unittest.TestCase):
    def test_print_the_subject_and_the_text_of_each_email_from_holomorphe_ovh_account_from_inbox(self):
        print("test_print_the_subject_of_each_email_from_holomorphe_ovh_account_from_inbox")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
            i = 1
            for msg in mailbox.fetch():
                try:
                    # print(str(i) + " subject : " + str(msg.subject))
                    """
                    print(str(i) +
                          " subject : " + str(msg.subject) +
                          " ; text : " + str(msg.text) +
                          " ; from : " + str(msg.from_) +
                          " ; uid : " + str(msg.uid))
                    """
                    print(str(i) + ' msg from : ' + str(msg.from_))
                    i += 1
                except Exception as e:
                    print('error : ' + str(e))

    def test_print_the_subject_of_each_email_from_holomorphe_ovh_account_from_deleted_items(self):
        print("test_print_the_subject_of_each_email_from_holomorphe_ovh_account_from_deleted_items")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='Éléments supprimés') as mailbox:
            for msg in mailbox.fetch():
                print("subject: " + str(msg.subject) + " , to: " + str(msg.to) + " , text: " + str(msg.text))

    def test_print_the_subject_of_each_email_from_holomorphe_ovh_account_from_Undelivered_Mail_Returned_To_Sender(self):
        print("test_print_the_subject_of_each_email_from_holomorphe_ovh_account_from_undelivered_mail_returned_to_sender_mailbox")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='Undelivered_Mail_Returned_To_Sender') as mailbox:
            for msg in mailbox.fetch():
                print("subject: " + str(msg.subject))

    def test_move_emails_from_inbox_folder_and_indesirable_folder_and_deleted_folder_to_specific_folder_from_holomorphe_ovh_account_version_1(self):
        print("test_move_emails_from_inbox_folder_and_indesirable_folder_and_deleted_folder_to_specific_folder_from_holomorphe_ovh_account")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
                    for msg in mailbox.fetch():
                        try:
                            if (
                                    "Undelivered" in msg.subject
                                    or
                                    "Undeliverable" in msg.subject
                                    or
                                    "Non remis" in msg.subject
                                    or
                                    "Returned mail" in msg.subject
                                    or
                                    "DELIVERY FAILURE" in msg.subject
                                    or
                                    "Non recapitabile" in msg.subject
                                    or
                                    "Failure" in msg.subject
                                    or
                                    "Mail not delivered" in msg.subject
                                    or
                                    "Returned Mail" in msg.subject
                                    or
                                    "Impossible d'envoyer l'email" in msg.subject
                                    or
                                    "Delivery has failed" in msg.text
                                    or
                                    "failed" in msg.text
                                    or
                                    "failed" in msg.subject
                                    or
                                    "failure" in msg.subject
                                    or
                                    "couldn't be delivered" in msg.subject
                                    or
                                    "couldn't be delivered" in msg.text
                                    or
                                    "rejected" in msg.text
                                    or
                                    "rejected" in msg.subject
                                    or
                                    "Rejected" in msg.text
                                    or
                                    "Rejected" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "Fehler bei der Nachrichtenzustellung" in msg.text
                                    or
                                    "Uw bericht kan niet worden bezorgd bij de volgende geadresseerden of groepen" in msg.text
                                    or
                                    "Bad destination host 'DNS Soft Error looking up" in msg.text
                                    or
                                    "A message that you sent has not yet been delivered to one or more of its" in msg.text
                                    or
                                    "Your message could not be delivered for" in msg.text
                                    or
                                    "Unzustellbar" in msg.subject
                                    or
                                    "could not be delivered" in msg.text
                                    or
                                    "not able to deliver" in msg.text
                            ):
                                mailbox.move(msg.uid, 'Undelivered_Mail_Returned_To_Sender')
                                print("moved Undelivered_Mail_Returned_To_Sender : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "la diffusion de publicités" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Agences_De_Publicite')
                                print("moved Marketing/Fournisseurs/Agences_De_Publicite : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "la transformation de tous types de véhicules" in msg.subject:
                                mailbox.move(msg.uid,
                                             'Filiales/Achat_Vente_Vehicule/Marketing/Fournisseurs/Garages_Voiture_Hydrogene')
                                print(
                                    "moved Filiales/Achat_Vente_Vehicule/Marketing/Fournisseurs/Garages_Voiture_Hydrogene : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "l'achat de matériels électriques" in msg.subject:
                                mailbox.move(msg.uid,
                                             'Filiales/Production_Electricite/Marketing/Fournisseurs/Materiels_Electriques')
                                print(
                                    "moved Filiales/Production_Electricite/Marketing/Fournisseurs/Materiels_Electriques : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "la fabrication de transformateurs électriques" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Transformateurs_Bobines_Circuits')
                                print("moved Marketing/Fournisseurs/Transformateurs_Bobines_Circuits : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "l'achat de chaudières" in msg.subject:
                                mailbox.move(msg.uid,
                                             'Filiales/Production_Chaleur/Marketing/Fournisseurs/Materiels_Chauffage')
                                print(
                                    "moved Filiales/Production_Chaleur/Marketing/Fournisseurs/Materiels_Chauffage : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "l'achat de biens immobiliers" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Agents_Immobiliers')
                                print("moved Marketing/Fournisseurs/Agents_Immobiliers : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "de gaz naturel" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Partenaires/Acces_Raccordement_Gaz_Naturel')
                                print("moved Marketing/Partenaires/Acces_Raccordement_Gaz_Naturel : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "certification ISO TC 197" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Certificateurs_ISO')
                                print("moved Marketing/Fournisseurs/Certificateurs_ISO : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "gravure de cadenas et clés" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Serruriers_Cadenas_Graves')
                                print("moved Marketing/Fournisseurs/Serruriers_Cadenas_Graves : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "palette" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Palettes')
                                print("moved Marketing/Fournisseurs/Palettes : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "containers" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Containers')
                                print("moved Marketing/Fournisseurs/Containers : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "matériels informatiques" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Fournisseurs/Materiels_Informatiques')
                                print("moved Marketing/Fournisseurs/Materiels_Informatiques : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                            ) and "pour vos missions" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Partenaires/Editeurs_De_Logiciels')
                                print("moved Marketing/Partenaires/Editeurs_De_Logiciels : " + msg.uid)

                            elif (
                                    "absence" in msg.subject
                                    or
                                    "Congés" in msg.subject
                                    or
                                    "congés" in msg.text
                                    or
                                    "absent" in msg.text
                                    or
                                    "absente" in msg.text
                                    or
                                    "fermés" in msg.text
                                    or
                                    "fermé" in msg.text
                                    or
                                    "fermée" in msg.text
                                    or
                                    "ALTOSPAM" in msg.text
                                    or
                                    "congé" in msg.text
                                    or
                                    "Fermeture" in msg.subject
                                    or
                                    "Absent" in msg.text
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "Absent" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Indisponible" in msg.subject
                                    or
                                    "indisponible" in msg.subject
                                    or
                                    "conge" in msg.text
                                    or
                                    "automatique" in msg.text
                                    or
                                    "automatique" in msg.subject
                                    or
                                    "FERMETURE" in msg.subject
                                    or
                                    "Automatic reply" in msg.subject
                                    or
                                    "Automatique" in msg.text
                                    or
                                    "Automatique" in msg.subject
                                    or
                                    "meilleurs délais" in msg.text
                                    or
                                    "ABSEN" in msg.subject
                                    or
                                    "fermeture" in msg.text
                                    or
                                    "inconnu" in msg.text
                                    or
                                    "inconnu" in msg.subject
                                    or
                                    "désolé" in msg.text
                                    or
                                    "ne sommes pas" in msg.text
                                    or
                                    "ne réalisons pas" in msg.text
                                    or
                                    "ne vendons pas" in msg.text
                                    or
                                    "ne proposons pas" in msg.text
                                    or
                                    "absent" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "vacance" in msg.text
                                    or
                                    "AUTOMATIQUE" in msg.subject
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                                    or
                                    "postmaster" in msg.from_
                                    or
                                    "Automatische" in msg.text
                                    or
                                    "Automatische" in msg.subject
                                    or
                                    "Auto:" in msg.subject
                                    or
                                    "geschlossen" in msg.text
                                    or
                                    "abwesend" in msg.text
                                    or
                                    "Betriebsferien" in msg.text
                                    or
                                    "AutoReply" in msg.subject
                                    or
                                    "Abwesenheit" in msg.text
                                    or
                                    "Ferienabwesenheiten" in msg.text
                                    or
                                    "Auto-Response" in msg.subject
                                    or
                                    "Corona" in msg.subject
                                    or
                                    "Ferien" in msg.subject
                                    or
                                    "Ferientage" in msg.subject
                                    or
                                    "automatisch" in msg.text
                                    or
                                    "Automatisch" in msg.subject
                                    or
                                    "Autoresponder" in msg.subject
                                    or
                                    "SPAM" in msg.text
                                    or
                                    "Patientin" in msg.text
                                    or
                                    "Autoantwort" in msg.text
                                    or
                                    "AUTOREPLY" in msg.text
                                    or
                                    "AUTOREPLY" in msg.subject
                                    or
                                    "keine_antwort" in msg.from_
                                    or
                                    "vielen Dank für Ihre E-Mail" in msg.text
                                    or
                                    "automatisiert" in msg.text
                                    or
                                    "tigungsmail" in msg.subject
                                    or
                                    "Vielen Dank für Ihre" in msg.text
                                    or
                                    "Ihr Anliegen werden wir schnellstmöglich bearbeiten" in msg.text
                                    or
                                    "Eingangsbestätigung" in msg.subject
                                    or
                                    "Kundin" in msg.text
                                    or
                                    "vielen Dank für Ihre Nachricht" in msg.text
                                    or
                                    "noreply" in msg.from_
                                    or
                                    "Sehr geehrter Gast," in msg.text
                                    or
                                    "This mail account is not valid" in msg.text
                                    or
                                    "Sehr geehrte Damen und Herren" in msg.text
                                    or
                                    "Sehr geehrter Sender" in msg.text
                                    or
                                    "Gäste" in msg.text
                                    or
                                    "Dear sender" in msg.text
                                    or
                                    "Patienten" in msg.text
                                    or
                                    "Sehr geehrter Kunde" in msg.text
                                    or
                                    "Dank für Ihre Nachricht" in msg.text
                                    or
                                    "Vielen Dank für die e-mail" in msg.text
                                    or
                                    "Ticket" in msg.text
                                    or
                                    "Sehr geehrter Absender" in msg.text
                                    or
                                    "Dear Sender" in msg.text
                                    or
                                    "Vielen Dank für Ihre Nachricht" in msg.subject
                                    or
                                    "Ihre Nachricht" in msg.subject
                                    or
                                    "received your request" in msg.text
                                    or
                                    "autoreply" in msg.from_
                                    or
                                    "Anfrage eingegangen" in msg.subject
                                    or
                                    "Request received" in msg.subject
                                    or
                                    "Dank für Ihre Email" in msg.text
                                    or
                                    "Open source files for building hydrogen technologies" in msg.subject
                            ) and (
                                    "Re:" in msg.subject
                                    or
                                    "Retard de livraison" in msg.subject
                                    or
                                    "Absence" in msg.subject
                                    or
                                    "absence" in msg.subject
                                    or
                                    "[SPAM]" in msg.subject
                                    or
                                    "CONGES" in msg.subject
                                    or
                                    "CONGÉS" in msg.subject
                                    or
                                    "congé" in msg.subject
                                    or
                                    "Congé" in msg.subject
                                    or
                                    "Nous sommes en" in msg.subject
                                    or
                                    "Retour" in msg.subject
                                    or
                                    "En:" in msg.subject
                                    or
                                    "Espace Eco Habitat" in msg.subject
                                    or
                                    "Réponse automatique" in msg.subject
                                    or
                                    "vacance" in msg.subject
                                    or
                                    "Automatische" in msg.text
                                    or
                                    "Automatische" in msg.subject
                                    or
                                    "Auto:" in msg.subject
                                    or
                                    "geschlossen" in msg.text
                                    or
                                    "abwesend" in msg.text
                                    or
                                    "Betriebsferien" in msg.text
                                    or
                                    "AutoReply" in msg.subject
                                    or
                                    "Abwesenheit" in msg.text
                                    or
                                    "Ferienabwesenheiten" in msg.subject
                                    or
                                    "Auto-Response" in msg.subject
                                    or
                                    "Corona" in msg.subject
                                    or
                                    "Ferien" in msg.subject
                                    or
                                    "Ferientage" in msg.subject
                                    or
                                    "automatisch" in msg.text
                                    or
                                    "Automatisch" in msg.subject
                                    or
                                    "Autoresponder" in msg.subject
                                    or
                                    "SPAM" in msg.text
                                    or
                                    "Patientin" in msg.text
                                    or
                                    "Autoantwort" in msg.text
                                    or
                                    "AUTOREPLY" in msg.text
                                    or
                                    "AUTOREPLY" in msg.subject
                                    or
                                    "keine_antwort" in msg.from_
                                    or
                                    "vielen Dank für Ihre E-Mail" in msg.text
                                    or
                                    "vielen Dank für Ihre Nachricht" in msg.text
                                    or
                                    "automatisiert" in msg.text
                                    or
                                    "automatisch" in msg.text
                                    or
                                    "tigungsmail" in msg.subject
                                    or
                                    "Vielen Dank für Ihre" in msg.text
                                    or
                                    "Ihr Anliegen werden wir schnellstmöglich bearbeiten" in msg.text
                                    or
                                    "Eingangsbestätigung" in msg.subject
                                    or
                                    "Kundin" in msg.text
                                    or
                                    "vielen Dank für Ihre Nachricht" in msg.text
                                    or
                                    "noreply" in msg.from_
                                    or
                                    "Sehr geehrter Gast," in msg.text
                                    or
                                    "This mail account is not valid" in msg.text
                                    or
                                    "Sehr geehrte Damen und Herren" in msg.text
                                    or
                                    "Sehr geehrter Sender" in msg.text
                                    or
                                    "Gäste" in msg.text
                                    or
                                    "Dear sender" in msg.text
                                    or
                                    "Patienten" in msg.text
                                    or
                                    "Sehr geehrter Kunde" in msg.text
                                    or
                                    "Dank für Ihre Nachricht" in msg.text
                                    or
                                    "Vielen Dank für die e-mail" in msg.text
                                    or
                                    "Ticket" in msg.text
                                    or
                                    "Sehr geehrter Absender" in msg.text
                                    or
                                    "Dear Sender" in msg.text
                                    or
                                    "Vielen Dank für Ihre Nachricht" in msg.subject
                                    or
                                    "Ihre Nachricht" in msg.subject
                                    or
                                    "received your request" in msg.text
                                    or
                                    "autoreply" in msg.from_
                                    or
                                    "Anfrage eingegangen" in msg.subject
                                    or
                                    "Request received" in msg.subject
                                    or
                                    "Dank für Ihre Email" in msg.text
                                    or
                                    "Open source files for building hydrogen technologies" in msg.subject
                            ):
                                mailbox.move(msg.uid, 'Archivage')
                                print("moved Archivage : " + msg.uid)

                            elif (
                                    "captcha" in msg.text
                                    or
                                    "mailinblack" in msg.from_
                                    or
                                    "antispam" in msg.subject
                                    or
                                    "antispam" in msg.text
                                    or
                                    "antispam" in msg.from_
                            ):
                                mailbox.move(msg.uid, 'Captcha')
                                print("moved Captcha : " + msg.uid)

                            elif "transmutation du plomb en or" in msg.subject:
                                mailbox.move(msg.uid, 'Marketing/Partenaires/Transmutation_Plomb_En_Or')
                                print("moved Marketing/Partenaires/Transmutation_Plomb_En_Or : " + msg.uid)

                            elif "contact@freelance-info.fr" in msg.from_:
                                mailbox.move(msg.uid, 'Freelance-info')
                                print("moved Freelance-info : " + msg.uid)
                        except Exception as e:
                            print("error for msg : " + str(e))
            except Exception as e:
                print('error for loop : ' + str(e))

    def test_move_emails_from_inbox_to_specific_folder_from_holomorphe_ovh_account(self):
        print("test_move_emails_from_inbox_to_specific_folder_from_holomorphe_ovh_account")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
                    for msg in mailbox.fetch():
                        if ("Undelivered" in msg.subject
                                or "Undeliverable" in msg.subject
                                or "Failure" in msg.subject
                                or "failed" in msg.subject
                                or "failure" in msg.subject
                                or "rejected" in msg.text
                                or "rejected" in msg.subject):
                                mailbox.move(msg.uid, 'Undelivered_Mail_Returned_To_Sender')
                                print("moved Undelivered_Mail_Returned_To_Sender : " + msg.uid)
                        elif "freelance-info.fr" in msg.from_:
                            mailbox.move(msg.uid, 'Freelance-info')
                            print("moved Freelance-info : " + msg.uid)
            except Exception as e:
                print('error : ' + str(e))

    def test_move_emails_from_inbox_to_specific_folder_from_holomorphe_ovh_account_for_freelance_info(self):
        print("test_move_emails_from_inbox_to_specific_folder_from_holomorphe_ovh_account")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='INBOX') as mailbox:
                    for msg in mailbox.fetch():
                        if "freelance-info" in str(msg.from_):
                            mailbox.move(msg.uid, 'Freelance-info')
                            print("moved Freelance-info : " + str(msg.uid))
            except Exception as e:
                print('error : ' + str(e))

    def test_move_emails_from_elements_envoyes_folder_to_specific_folder(self):
        print("test_move_emails_from_elements_envoyes_folder_to_specific_folder")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='Éléments envoyés') as mailbox:
                    for msg in mailbox.fetch():
                        if "la diffusion de publicités" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Agences_De_Publicite')
                            print("moved Marketing/Fournisseurs/Agences_De_Publicite : " + msg.uid)

                        elif "la transformation de tous types de véhicules" in msg.subject:
                            mailbox.move(msg.uid, 'Filiales/Achat_Vente_Vehicule/Marketing/Fournisseurs/Garages_Voiture_Hydrogene')
                            print("moved Filiales/Achat_Vente_Vehicule/Marketing/Fournisseurs/Garages_Voiture_Hydrogene : " + msg.uid)

                        elif "l'achat de matériels électriques" in msg.subject:
                            mailbox.move(msg.uid, 'Filiales/Production_Electricite/Marketing/Fournisseurs/Materiels_Electriques')
                            print("moved Filiales/Production_Electricite/Marketing/Fournisseurs/Materiels_Electriques : " + msg.uid)

                        elif "la fabrication de transformateurs électriques" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Transformateurs_Bobines_Circuits')
                            print("moved Marketing/Fournisseurs/Transformateurs_Bobines_Circuits : " + msg.uid)

                        elif "l'achat de chaudières" in msg.subject:
                            mailbox.move(msg.uid, 'Filiales/Production_Chaleur/Marketing/Fournisseurs/Materiels_Chauffage')
                            print("moved Filiales/Production_Chaleur/Marketing/Fournisseurs/Materiels_Chauffage : " + msg.uid)

                        elif "l'achat de biens immobiliers" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Agents_Immobiliers')
                            print("moved Marketing/Fournisseurs/Agents_Immobiliers : " + msg.uid)

                        elif "de gaz naturel" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Partenaires/Acces_Raccordement_Gaz_Naturel')
                            print("moved Marketing/Partenaires/Acces_Raccordement_Gaz_Naturel : " + msg.uid)

                        elif "certification ISO TC 197" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Certificateurs_ISO')
                            print("moved Marketing/Fournisseurs/Certificateurs_ISO : " + msg.uid)

                        elif "gravure de cadenas et clés" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Serruriers_Cadenas_Graves')
                            print("moved Marketing/Fournisseurs/Serruriers_Cadenas_Graves : " + msg.uid)

                        elif "palette" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Palettes')
                            print("moved Marketing/Fournisseurs/Palettes : " + msg.uid)

                        elif "containers" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Containers')
                            print("moved Marketing/Fournisseurs/Containers : " + msg.uid)

                        elif "matériels informatiques" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Materiels_Informatiques')
                            print("moved Marketing/Fournisseurs/Materiels_Informatiques : " + msg.uid)

                        elif "rédaction" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Avocats')
                            print("moved Marketing/Fournisseurs/Avocats : " + msg.uid)

                        elif "contrôle technique de tous de types de véhicules" in msg.subject:
                            mailbox.move(msg.uid, 'Filiales/Achat_Vente_Vehicule/Marketing/Fournisseurs/Controleurs_Techniques')
                            print("moved Filiales/Achat_Vente_Vehicule/Marketing/Fournisseurs/Controleurs_Techniques : " + msg.uid)

                        elif "dépôt de la demande de permis de construire" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Architectes')
                            print("moved Marketing/Fournisseurs/Architectes : " + msg.uid)

                        elif "la construction d'une installation classée" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Entreprises_Du_Batiment')
                            print("moved Marketing/Fournisseurs/Entreprises_Du_Batiment : " + msg.uid)

                        elif "Information request for electricity production" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Institutions/Ministeres_Energie_Du_Monde')
                            print("moved Marketing/Institutions/Ministeres_Energie_Du_Monde : " + msg.uid)

                        elif "la fabrication d'armoires métalliques" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Fournisseurs/Menuiseries')
                            print("moved Marketing/Fournisseurs/Menuiseries : " + msg.uid)

                        elif "partenariat commercial pour vos missions" in msg.subject:
                            mailbox.move(msg.uid, 'Marketing/Partenaires/Editeurs_De_Logiciels')
                            print("moved Marketing/Partenaires/Editeurs_De_Logiciels : " + msg.uid)

            except Exception as e:
                print("error for msg : " + str(e))

    def test_move_emails_from_specific_folder_to_specific_folder(self):
        print("test_move_emails_from_elements_envoyes_folder_to_specific_folder")

        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        for i in range(0, 100):
            print("tour : " + str(i))

            try:
                with MailBox(imap_host).login(imap_user, imap_pass, initial_folder='Marketing/Partenaires/Acces_Raccordement_Gaz_Naturel') as mailbox:
                    for msg in mailbox.fetch():
                        if "pour vos missions" in msg.subject:
                            mailbox.move(msg.uid, 'INBOX')
                            print("moved INBOX : " + msg.uid)

            except Exception as e:
                print("error for msg : " + str(e))

    def test_list_all_mailboxes_of_email_pro_holomorphe_ovh_account(self):
        print("test_list_all_mailboxes_of_email_pro_holomorphe_ovh_account")

        imap_host = 'pro2.mail.ovh.net'
        imap_port = 993
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()

            for directory in directories:
                print(directory)

            imap.logout()

    # ok
    def test_print_all_mails_from_all_folders_from_of_email_pro_holomorphe_ovh_account(self):
        print("test_print_all_mails_from_all_folders_from_of_email_pro_holomorphe_ovh_account")

        imap_host = 'pro2.mail.ovh.net'
        imap_port = 993
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        with imaplib.IMAP4_SSL(imap_host, imap_port) as imap:
            # login to server
            imap.login(imap_user, imap_pass)

            # print all mailboxes
            directories = imap.list()[1]

            imap.logout()

            i = 1

            for directory in directories:
                try:
                    initial_folder = str(directory).split(' "/" ')[1]\
                        .replace("'", "")\
                        .replace('"', '')

                    print(initial_folder)

                    if not os.path.isdir(initial_folder):
                        os.mkdir(initial_folder)
                        os.chmod(initial_folder, 0o777)

                    with MailBox(imap_host).login(imap_user, imap_pass, initial_folder=initial_folder) as mailbox:
                        for msg in mailbox.fetch():
                            try:
                                print("email : " + str(i))

                                with open(initial_folder + "\\Page_" + str(i) + ".txt", "w", encoding='utf-8-sig') as file:
                                    subject = str(msg.subject)
                                    file.write("subject : " + subject)
                                    file.write("\n\n")

                                    date = str(msg.date)
                                    file.write("date : " + date)
                                    file.write("\n\n")

                                    date_str = str(msg.date_str)
                                    file.write("date_str : " + date_str)
                                    file.write("\n\n")

                                    from_ = str(msg.from_)
                                    file.write("from_ : " + from_)
                                    file.write("\n\n")

                                    from_values = str(msg.from_values)
                                    file.write("from_values : " + from_values)
                                    file.write("\n\n")

                                    to = str(msg.to)
                                    file.write("to : " + to)
                                    file.write("\n\n")

                                    to_values = str(msg.to_values)
                                    file.write("to_values : " + to_values)
                                    file.write("\n\n")

                                    reply_to = str(msg.reply_to)
                                    file.write("reply_to : " + reply_to)
                                    file.write("\n\n")

                                    reply_to_values = str(msg.reply_to_values)
                                    file.write("reply_to_values : " + reply_to_values)
                                    file.write("\n\n")

                                    cc = str(msg.cc)
                                    file.write("cc : " + cc)
                                    file.write("\n\n")

                                    cc_values = str(msg.cc_values)
                                    file.write("cc_values : " + cc_values)
                                    file.write("\n\n")

                                    bcc = str(msg.bcc)
                                    file.write("bcc : " + bcc)
                                    file.write("\n\n")

                                    bcc_values = str(msg.bcc_values)
                                    file.write("bcc_values : " + bcc_values)
                                    file.write("\n\n")

                                    text = str(msg.text)
                                    file.write("text : " + text)
                                    file.write("\n\n")

                                    html = str(msg.html)
                                    file.write("html : " + html)
                                    file.write("\n\n")

                                    file.close()

                                for att in msg.attachments:
                                    print(att.filename.replace(" ", "")
                                                      .replace("-", "")
                                                      .replace("_", "")
                                                      .replace("[", "")
                                                      .replace("]", "")
                                                      .replace("'", "")
                                                      .replace("Jason", "")
                                                      .replace("ALOYAU", "")
                                                      .replace("\r", "")
                                                      .replace("\n", ""), att.content_type)
                                    with open(initial_folder + "\\" + format(att.filename
                                                                                .replace(" ", "")
                                                                                .replace("-", "")
                                                                                .replace("_", "")
                                                                                .replace("[", "")
                                                                                .replace("]", "")
                                                                                .replace("'", "")
                                                                                .replace("Jason", "")
                                                                                .replace("ALOYAU", "")
                                                                                .replace("\r", "")
                                                                                .replace("\n", "")
                                                                             ), 'wb') as f:
                                        f.write(att.payload)
                                        f.close()
                            except Exception as e:
                                print("error : " + str(e))

                            i += 1
                except Exception as e:
                    print('error directory : ' + str(e))


class UnitTestsEmailSpamFilteringMiscelleanous(unittest.TestCase):
    def test_read_emails_with_imaplib(self):
        print('test_read_emails_with_imaplib')

        """
        imap_host = 'pro2.mail.ovh.net'
        imap_user = 'jason.aloyau@holomorphe.com'
        imap_pass = ''

        # Connect to inbox
        imap_server = imaplib.IMAP4_SSL(host=imap_host)
        imap_server.login(imap_user, imap_pass)
        imap_server.select()  # Default is `INBOX`

        # Find all emails in inbox
        _, message_numbers_raw = imap_server.search(None, 'ALL')

        for i in range(0, 100):
            print("tour : " + str(i))

            for message_number in message_numbers_raw[0].split():
                _, msg = imap_server.fetch(message_number, '(RFC822)')
                message = email.message_from_bytes(msg[0][1])
                print("message : " + str(i))
                print(message.get_payload())  # print FULL message
                i += 1
                
                print('== Email details =====')
                print(f'From: {message["from"]}')
                print(f'To: {message["to"]}')
                print(f'Cc: {message["cc"]}')
                print(f'Bcc: {message["bcc"]}')
                print(f'Body : {message[""]}')
                print(f'Urgency (1 highest 5 lowest): {message["x-priority"]}')
                print(f'Content disposition: {message.get_content_disposition()}')
        """


if __name__ == '__main__':
    unittest.main()
