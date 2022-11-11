import time
import unittest
from mailjet_rest import Client
import base64


# https://github.com/mailjet/mailjet-apiv3-python
class UnitTestsEmailMarketingWithMailjetAPIForEnergyLawyersForMe(unittest.TestCase):
    # ok
    def test_send_one_mail_to_energy_lawyer_in_france(self):
        print('test_send_one_mail_to_energy_lawyer_in_france')

        # Credentials
        api_key = ''
        api_secret = ''

        # Client
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        # Filenames
        # Filename_1
        filename_1 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\Passeport_De_Jason_ALOYAU.pdf"
        pdf_filename_1 = open(filename_1, 'rb')
        filename_1_base64 = base64.b64encode(pdf_filename_1.read()).decode('utf-8')
        pdf_filename_1.close()

        # Filename_2
        filename_2 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\Diplome_Ingenieur_[Jason_ALOYAU].pdf"
        pdf_filename_2 = open(filename_2, 'rb')
        filename_2_base64 = base64.b64encode(pdf_filename_2.read()).decode('utf-8')
        pdf_filename_2.close()

        # Filename_3
        filename_3 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\CV_De_Jason_ALOYAU_[Ingenieur_Energies_Renouvelables].pdf"
        pdf_filename_3 = open(filename_3, 'rb')
        filename_3_base64 = base64.b64encode(pdf_filename_3.read()).decode('utf-8')
        pdf_filename_3.close()

        # Filename_4
        filename_4 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\WO1995008210A1_Homopolar_Generator.pdf"
        pdf_filename_4 = open(filename_4, 'rb')
        filename_4_base64 = base64.b64encode(pdf_filename_4.read()).decode('utf-8')
        pdf_filename_4.close()

        # Filename_5
        filename_5 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\CAO_N_Machine_Jason_ALOYAU.pdf"
        pdf_filename_5 = open(filename_5, 'rb')
        filename_5_base64 = base64.b64encode(pdf_filename_5.read()).decode('utf-8')
        pdf_filename_5.close()

        to = ""

        # Data
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "",
                        "Name": ""
                    },
                    "To": [
                        {
                            "Email": to
                        }
                    ],
                    "Cc": [
                        {
                            "Email": '',
                            "Name": ""
                        }
                    ],
                    "Subject": "Demande d'étude du générateur d'électricité de Bruce DePalma pour l'autorisation "
                               "d'exploiter des installations de production d'électricité - Monsieur Jason ALOYAU",
                    "TextPart": "Bonjour, Maître, \n\n"
                                "Actuellement, je travaille sur le générateur d'électricité de l'inventeur Bruce "
                                "DePalma dont le brevet est tombé dans le domaine public et numéroté : "
                                "WO1995008210A1. \n\n"
                                "Ce type de générateur d'électricité se base sur les principes du disque de Faraday et "
                                "le paradoxe de Faraday concernant l'induction électromagnétique. \n\n"
                                "Selon l'inventeur Bruce DePalma, son générateur d'électricité communément appelé la "
                                "'machine N' extrait de l'énergie via l'énergie de l'espace ou l'énergie du vide, "
                                "c'est-à-dire de notre espace environnant. \n\n"
                                "Aujourd'hui, je dois mener des travaux d'expérimentation auprès de quelques "
                                "laboratoires scientifiques pour rédiger des rapports scientifiques sur ce générateur "
                                "d'électricité. \n\n"
                                "Je comprends très bien que l'énergie de l'espace ou l'énergie du vide n'est pas "
                                "répertoriée parmi les énergies primaires qui sont citées dans la liste des "
                                "installations de production d'électricité réputées autorisées en vertu de l'article "
                                "R311-2 du code de l'énergie. \n\n"
                                "Ma question est : \n"
                                "- Est-ce que le ministre chargé de l'énergie pourrait censurer, refuser et interdire "
                                "l'utilisation de ce générateur d'électricité pour une demande d'autorisation "
                                "d'exploiter une installation de production d'électricité en vertu des articles "
                                "L311-1 à L311-27 du code de l'énergie s'il vous plaît ? \n\n"
                                "De plus, je mets en pièces jointes les documents suivants : \n"
                                "- La copie de mon passeport \n"
                                "- La copie de mon diplôme d'ingénieur généraliste \n"
                                "- Mon CV \n"
                                "- La copie du brevet WO1995008210A1 \n"
                                "- Quelques vues de ma conception assistée par ordinateur de ce générateur "
                                "d'électricité \n\n"
                                "Dans l'attente de votre retour, je vous prie de croire, Maître, mes sincères "
                                "salutations.\n\n"
                                " \n"
                                "Téléphone :  \n\n"
                                "Références : \n"
                                "- Disque de Faraday : "
                                "https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_homopolaire_(machine_%C3%A9lectrique) \n"
                                "- Paradoxe de Faraday : https://fr.wikipedia.org/wiki/Paradoxe_de_Faraday \n"
                                "- La 'N machine' de Bruce DePalma : https://www.brucedepalma.com/ / "
                                "https://freebanzai.wixsite.com/badaboum/bruce-de-palma / "
                                "https://www.paperblog.fr/3988159/du-disque-de-faraday-a-la-n-machine-de-bruce-de-palma/ / "
                                "https://depalma.pairsite.com/ \n"
                                "- Inventeur Bruce DePalma : https://arc-ethic.com/tout-les-articles/inventeur-bruce-de-palma/ / "
                                "https://brucedepalma.com/PDF/BruceopenletterplusTewari.pdf / "
                                "https://www.youtube.com/watch?v=kB-tYsqKZgY / "
                                "https://www.youtube.com/watch?v=-gZI-Hs7-3I / "
                                "https://www.youtube.com/watch?v=qOX6o4fDNlI \n"
                                "- Machines similaires : https://www.youtube.com/watch?v=wyzuiS_oMQI / "
                                "http://www.free-energy-info.tuks.nl/index2.html \n"
                                "- Induction électromagnétique : https://fr.wikipedia.org/wiki/Induction_%C3%A9lectromagn%C3%A9tique / "
                                "https://femto-physique.fr/electromagnetisme/induction-electromagnetique.php / "
                                "https://ipag.osug.fr/~ferreirj/enseignement/BChapitreIV.pdf \n"
                                "- Mécanique quantique : http://www.lcar.ups-tlse.fr/IMG/pdf/Poly-2.pdf / "
                                "http://espace-fpn.ump.ma/ftp/etudiants/cours/M%C3%A9canique%20Quantique%20-%20Cours.pdf / "
                                "https://fr.wikipedia.org/wiki/M%C3%A9canique_quantique \n"
                                "- Energie de l'espace ou énergie du vide ou énergie du point zéro : "
                                "https://www.techno-science.net/glossaire-definition/Effet-Casimir.html / "
                                "https://www.techno-science.net/definition/2828.html / "
                                "https://fr.wikipedia.org/wiki/%C3%89nergie_du_vide / "
                                "https://fr.wikipedia.org/wiki/Fluctuation_quantique / "
                                "https://fr.wikipedia.org/wiki/%C3%89nergie_du_point_z%C3%A9ro / "
                                "https://spiegato.com/fr/quest-ce-que-lenergie-du-point-zero#:~:text=L%E2%80%99%C3%A9nergie%20du%20point%20z%C3%A9ro%20est%20une%20petite%20quantit%C3%A9,connue%20sous%20le%20nom%20d%E2%80%99%C3%A9nergie%20de%20l%E2%80%99%C3%A9tat%20fondamental. / "
                                "https://headinghometodinner.org/fr/quest-ce-que-l%C3%A9nergie-du-point-z%C3%A9ro-et-comment-pourrait-elle-changer-le-monde/",
                    'Attachments': [
                        {
                            "Filename": filename_1,
                            "ContentType": "application/pdf",
                            "Base64Content": filename_1_base64
                        },
                        {
                            "Filename": filename_2,
                            "ContentType": "application/pdf",
                            "Base64Content": filename_2_base64
                        },
                        {
                            "Filename": filename_3,
                            "ContentType": "application/pdf",
                            "Base64Content": filename_3_base64
                        },
                        {
                            "Filename": filename_4,
                            "ContentType": "application/pdf",
                            "Base64Content": filename_4_base64
                        },
                        {
                            "Filename": filename_5,
                            "ContentType": "application/pdf",
                            "Base64Content": filename_5_base64
                        }
                    ]
                }
            ]
        }

        # Send email
        result = mailjet.send.create(data=data)

        # Result
        print(result.status_code)
        print(result.json())

    # ok
    def test_send_many_mails_to_energy_lawyer_in_france(self):
        print('test_send_many_mails_to_energy_lawyer_in_france')

        # Credentials
        api_key = ''
        api_secret = ''

        # Client
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        # Filenames
        # Filename_1
        filename_1 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\Passeport_De_Jason_ALOYAU.pdf"
        pdf_filename_1 = open(filename_1, 'rb')
        filename_1_base64 = base64.b64encode(pdf_filename_1.read()).decode('utf-8')
        pdf_filename_1.close()

        # Filename_2
        filename_2 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\Diplome_Ingenieur_[Jason_ALOYAU].pdf"
        pdf_filename_2 = open(filename_2, 'rb')
        filename_2_base64 = base64.b64encode(pdf_filename_2.read()).decode('utf-8')
        pdf_filename_2.close()

        # Filename_3
        filename_3 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\CV_De_Jason_ALOYAU_[Ingenieur_Energies_Renouvelables].pdf"
        pdf_filename_3 = open(filename_3, 'rb')
        filename_3_base64 = base64.b64encode(pdf_filename_3.read()).decode('utf-8')
        pdf_filename_3.close()

        # Filename_4
        filename_4 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\WO1995008210A1_Homopolar_Generator.pdf"
        pdf_filename_4 = open(filename_4, 'rb')
        filename_4_base64 = base64.b64encode(pdf_filename_4.read()).decode('utf-8')
        pdf_filename_4.close()

        # Filename_5
        filename_5 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\CAO_N_Machine_Jason_ALOYAU.pdf"
        pdf_filename_5 = open(filename_5, 'rb')
        filename_5_base64 = base64.b64encode(pdf_filename_5.read()).decode('utf-8')
        pdf_filename_5.close()

        # emails
        emails = [

        ]

        for email in emails:
            to = email

            # Data
            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": "",
                            "Name": ""
                        },
                        "To": [
                            {
                                "Email": to
                            }
                        ],
                        "Cc": [
                            {
                                "Email": '',
                                "Name": ""
                            }
                        ],
                        "Subject": "Demande d'étude du générateur d'électricité de Bruce DePalma pour l'autorisation "
                                   "d'exploiter des installations de production d'électricité - Monsieur Jason ALOYAU",
                        "TextPart": "Bonjour, Maître, \n\n"
                                    "Actuellement, je travaille sur le générateur d'électricité de l'inventeur Bruce "
                                    "DePalma dont le brevet est tombé dans le domaine public et numéroté : "
                                    "WO1995008210A1. \n\n"
                                    "Ce type de générateur d'électricité se base sur les principes du disque de Faraday et "
                                    "le paradoxe de Faraday concernant l'induction électromagnétique. \n\n"
                                    "Selon l'inventeur Bruce DePalma, son générateur d'électricité communément appelé la "
                                    "'machine N' extrait de l'énergie via l'énergie de l'espace ou l'énergie du vide, "
                                    "c'est-à-dire de notre espace environnant. \n\n"
                                    "Aujourd'hui, je dois mener des travaux d'expérimentation auprès de quelques "
                                    "laboratoires scientifiques pour rédiger des rapports scientifiques sur ce générateur "
                                    "d'électricité. \n\n"
                                    "Je comprends très bien que l'énergie de l'espace ou l'énergie du vide n'est pas "
                                    "répertoriée parmi les énergies primaires qui sont citées dans la liste des "
                                    "installations de production d'électricité réputées autorisées en vertu de l'article "
                                    "R311-2 du code de l'énergie. \n\n"
                                    "Ma question est : \n"
                                    "- Est-ce que le ministre chargé de l'énergie pourrait censurer, refuser et interdire "
                                    "l'utilisation de ce générateur d'électricité pour une demande d'autorisation "
                                    "d'exploiter une installation de production d'électricité en vertu des articles "
                                    "L311-1 à L311-27 du code de l'énergie s'il vous plaît ? \n\n"
                                    "De plus, je mets en pièces jointes les documents suivants : \n"
                                    "- La copie de mon passeport \n"
                                    "- La copie de mon diplôme d'ingénieur généraliste \n"
                                    "- Mon CV \n"
                                    "- La copie du brevet WO1995008210A1 \n"
                                    "- Quelques vues de ma conception assistée par ordinateur de ce générateur "
                                    "d'électricité \n\n"
                                    "Dans l'attente de votre retour, je vous prie de croire, Maître, mes sincères "
                                    "salutations.\n\n"
                                    " \n"
                                    "Téléphone :  \n\n"
                                    "Références : \n"
                                    "- Disque de Faraday : "
                                    "https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_homopolaire_(machine_%C3%A9lectrique) \n"
                                    "- Paradoxe de Faraday : https://fr.wikipedia.org/wiki/Paradoxe_de_Faraday \n"
                                    "- La 'N machine' de Bruce DePalma : https://www.brucedepalma.com/ / "
                                    "https://freebanzai.wixsite.com/badaboum/bruce-de-palma / "
                                    "https://www.paperblog.fr/3988159/du-disque-de-faraday-a-la-n-machine-de-bruce-de-palma/ / "
                                    "https://depalma.pairsite.com/ \n"
                                    "- Inventeur Bruce DePalma : https://arc-ethic.com/tout-les-articles/inventeur-bruce-de-palma/ / "
                                    "https://brucedepalma.com/PDF/BruceopenletterplusTewari.pdf / "
                                    "https://www.youtube.com/watch?v=kB-tYsqKZgY / "
                                    "https://www.youtube.com/watch?v=-gZI-Hs7-3I / "
                                    "https://www.youtube.com/watch?v=qOX6o4fDNlI \n"
                                    "- Machines similaires : https://www.youtube.com/watch?v=wyzuiS_oMQI / "
                                    "http://www.free-energy-info.tuks.nl/index2.html \n"
                                    "- Induction électromagnétique : https://fr.wikipedia.org/wiki/Induction_%C3%A9lectromagn%C3%A9tique / "
                                    "https://femto-physique.fr/electromagnetisme/induction-electromagnetique.php / "
                                    "https://ipag.osug.fr/~ferreirj/enseignement/BChapitreIV.pdf \n"
                                    "- Mécanique quantique : http://www.lcar.ups-tlse.fr/IMG/pdf/Poly-2.pdf / "
                                    "http://espace-fpn.ump.ma/ftp/etudiants/cours/M%C3%A9canique%20Quantique%20-%20Cours.pdf / "
                                    "https://fr.wikipedia.org/wiki/M%C3%A9canique_quantique \n"
                                    "- Energie de l'espace ou énergie du vide ou énergie du point zéro : "
                                    "https://www.techno-science.net/glossaire-definition/Effet-Casimir.html / "
                                    "https://www.techno-science.net/definition/2828.html / "
                                    "https://fr.wikipedia.org/wiki/%C3%89nergie_du_vide / "
                                    "https://fr.wikipedia.org/wiki/Fluctuation_quantique / "
                                    "https://fr.wikipedia.org/wiki/%C3%89nergie_du_point_z%C3%A9ro / "
                                    "https://spiegato.com/fr/quest-ce-que-lenergie-du-point-zero#:~:text=L%E2%80%99%C3%A9nergie%20du%20point%20z%C3%A9ro%20est%20une%20petite%20quantit%C3%A9,connue%20sous%20le%20nom%20d%E2%80%99%C3%A9nergie%20de%20l%E2%80%99%C3%A9tat%20fondamental. / "
                                    "https://headinghometodinner.org/fr/quest-ce-que-l%C3%A9nergie-du-point-z%C3%A9ro-et-comment-pourrait-elle-changer-le-monde/",
                        'Attachments': [
                            {
                                "Filename": filename_1,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_1_base64
                            },
                            {
                                "Filename": filename_2,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_2_base64
                            },
                            {
                                "Filename": filename_3,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_3_base64
                            },
                            {
                                "Filename": filename_4,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_4_base64
                            },
                            {
                                "Filename": filename_5,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_5_base64
                            }
                        ]
                    }
                ]
            }

            # Send email
            result = mailjet.send.create(data=data)

            # Result
            print('For email : ' + email + ' - Result : ' + str(result.json()))

            time.sleep(5)

    # ok
    def test_send_many_mails_to_energy_lawyer_in_switzerland(self):
        print('test_send_many_mails_to_energy_lawyer_in_switzerland')

        # Credentials
        api_key = ''
        api_secret = ''

        # Client
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        # Filenames
        # Filename_1
        filename_1 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\Passeport_De_Jason_ALOYAU.pdf"
        pdf_filename_1 = open(filename_1, 'rb')
        filename_1_base64 = base64.b64encode(pdf_filename_1.read()).decode('utf-8')
        pdf_filename_1.close()

        # Filename_2
        filename_2 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\Diplome_Ingenieur_[Jason_ALOYAU].pdf"
        pdf_filename_2 = open(filename_2, 'rb')
        filename_2_base64 = base64.b64encode(pdf_filename_2.read()).decode('utf-8')
        pdf_filename_2.close()

        # Filename_3
        filename_3 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\CV_De_Jason_ALOYAU_[Ingenieur_Energies_Renouvelables].pdf"
        pdf_filename_3 = open(filename_3, 'rb')
        filename_3_base64 = base64.b64encode(pdf_filename_3.read()).decode('utf-8')
        pdf_filename_3.close()

        # Filename_4
        filename_4 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\WO1995008210A1_Homopolar_Generator.pdf"
        pdf_filename_4 = open(filename_4, 'rb')
        filename_4_base64 = base64.b64encode(pdf_filename_4.read()).decode('utf-8')
        pdf_filename_4.close()

        # Filename_5
        filename_5 = "C:\\Users\\Jason\\Dropbox\\2_Professionnel\\Voltorus\\3_Marketing\\3_Fournisseurs\\1_Avocats" \
                     "\\CAO_N_Machine_Jason_ALOYAU.pdf"
        pdf_filename_5 = open(filename_5, 'rb')
        filename_5_base64 = base64.b64encode(pdf_filename_5.read()).decode('utf-8')
        pdf_filename_5.close()

        # emails
        emails = [
            
        ]

        for email in emails:
            to = email

            # Data
            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": "",
                            "Name": ""
                        },
                        "To": [
                            {
                                "Email": to
                            }
                        ],
                        "Cc": [
                            {
                                "Email": '',
                                "Name": ""
                            }
                        ],
                        "Subject": "Demande d'étude du générateur d'électricité de Bruce DePalma pour l'autorisation "
                                   "d'exploiter des installations de production d'électricité en Suisse - Monsieur "
                                   "Jason ALOYAU",
                        "TextPart": "Bonjour, \n\n"
                                    "Actuellement, je travaille sur le générateur d'électricité de l'inventeur Bruce "
                                    "DePalma dont le brevet est tombé dans le domaine public et numéroté : "
                                    "WO1995008210A1. \n\n"
                                    "Ce type de générateur d'électricité se base sur les principes du disque de Faraday et "
                                    "le paradoxe de Faraday concernant l'induction électromagnétique. \n\n"
                                    "Selon l'inventeur Bruce DePalma, son générateur d'électricité communément appelé la "
                                    "'machine N' extrait de l'énergie via l'énergie de l'espace ou l'énergie du vide, "
                                    "c'est-à-dire de notre espace environnant. \n\n"
                                    "Aujourd'hui, je dois mener des travaux d'expérimentation auprès de quelques "
                                    "laboratoires scientifiques pour rédiger des rapports scientifiques sur ce générateur "
                                    "d'électricité. \n\n"
                                    "Je comprends très bien que l'énergie de l'espace ou l'énergie du vide n'est pas "
                                    "répertoriée parmi les énergies primaires qui sont citées dans la liste des "
                                    "installations de production d'électricité en vertu de la loi sur l'énergie du "
                                    "30 septembre 2016. \n\n"
                                    "Ma question est : \n"
                                    "- Est-ce que l'organe d'exécution pourrait censurer, refuser et interdire "
                                    "l'utilisation de ce générateur d'électricité pour une demande d'autorisation "
                                    "d'exploiter une installation de production d'électricité en vertu de la loi sur "
                                    "l'énergie du 30 septembre 2016 et l'ordonnance sur l'énergie du 1er novembre 2017 "
                                    "s'il vous plaît ? \n\n"
                                    "De plus, je mets en pièces jointes les documents suivants : \n"
                                    "- La copie de mon passeport \n"
                                    "- La copie de mon diplôme d'ingénieur généraliste \n"
                                    "- Mon CV \n"
                                    "- La copie du brevet WO1995008210A1 \n"
                                    "- Quelques vues de ma conception assistée par ordinateur de ce générateur "
                                    "d'électricité \n\n"
                                    "Dans l'attente de votre retour, je vous prie de croire, mes sincères "
                                    "salutations.\n\n"
                                    " \n"
                                    "Téléphone :  \n\n"
                                    "Références : \n"
                                    "- Disque de Faraday : "
                                    "https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_homopolaire_(machine_%C3%A9lectrique) \n"
                                    "- Paradoxe de Faraday : https://fr.wikipedia.org/wiki/Paradoxe_de_Faraday \n"
                                    "- La 'N machine' de Bruce DePalma : https://www.brucedepalma.com/ / "
                                    "https://freebanzai.wixsite.com/badaboum/bruce-de-palma / "
                                    "https://www.paperblog.fr/3988159/du-disque-de-faraday-a-la-n-machine-de-bruce-de-palma/ / "
                                    "https://depalma.pairsite.com/ \n"
                                    "- Inventeur Bruce DePalma : https://arc-ethic.com/tout-les-articles/inventeur-bruce-de-palma/ / "
                                    "https://brucedepalma.com/PDF/BruceopenletterplusTewari.pdf / "
                                    "https://www.youtube.com/watch?v=kB-tYsqKZgY / "
                                    "https://www.youtube.com/watch?v=-gZI-Hs7-3I / "
                                    "https://www.youtube.com/watch?v=qOX6o4fDNlI \n"
                                    "- Machines similaires : https://www.youtube.com/watch?v=wyzuiS_oMQI / "
                                    "http://www.free-energy-info.tuks.nl/index2.html \n"
                                    "- Induction électromagnétique : https://fr.wikipedia.org/wiki/Induction_%C3%A9lectromagn%C3%A9tique / "
                                    "https://femto-physique.fr/electromagnetisme/induction-electromagnetique.php / "
                                    "https://ipag.osug.fr/~ferreirj/enseignement/BChapitreIV.pdf \n"
                                    "- Mécanique quantique : http://www.lcar.ups-tlse.fr/IMG/pdf/Poly-2.pdf / "
                                    "http://espace-fpn.ump.ma/ftp/etudiants/cours/M%C3%A9canique%20Quantique%20-%20Cours.pdf / "
                                    "https://fr.wikipedia.org/wiki/M%C3%A9canique_quantique \n"
                                    "- Energie de l'espace ou énergie du vide ou énergie du point zéro : "
                                    "https://www.techno-science.net/glossaire-definition/Effet-Casimir.html / "
                                    "https://www.techno-science.net/definition/2828.html / "
                                    "https://fr.wikipedia.org/wiki/%C3%89nergie_du_vide / "
                                    "https://fr.wikipedia.org/wiki/Fluctuation_quantique / "
                                    "https://fr.wikipedia.org/wiki/%C3%89nergie_du_point_z%C3%A9ro / "
                                    "https://spiegato.com/fr/quest-ce-que-lenergie-du-point-zero#:~:text=L%E2%80%99%C3%A9nergie%20du%20point%20z%C3%A9ro%20est%20une%20petite%20quantit%C3%A9,connue%20sous%20le%20nom%20d%E2%80%99%C3%A9nergie%20de%20l%E2%80%99%C3%A9tat%20fondamental. / "
                                    "https://headinghometodinner.org/fr/quest-ce-que-l%C3%A9nergie-du-point-z%C3%A9ro-et-comment-pourrait-elle-changer-le-monde/",
                        'Attachments': [
                            {
                                "Filename": filename_1,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_1_base64
                            },
                            {
                                "Filename": filename_2,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_2_base64
                            },
                            {
                                "Filename": filename_3,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_3_base64
                            },
                            {
                                "Filename": filename_4,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_4_base64
                            },
                            {
                                "Filename": filename_5,
                                "ContentType": "application/pdf",
                                "Base64Content": filename_5_base64
                            }
                        ]
                    }
                ]
            }

            # Send email
            result = mailjet.send.create(data=data)

            # Result
            print('For email : ' + email + ' - Result : ' + str(result.json()))

            time.sleep(5)


if __name__ == '__main__':
    unittest.main()
