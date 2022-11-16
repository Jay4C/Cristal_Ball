import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationMeilleurTauxPro(unittest.TestCase):
    def test_simuler_sans_headless(self):
        print("test_simuler_sans_headless")

        resultat_exploitation_positif = "non"
        # resultat_exploitation_positif = "oui sur le dernier exercice"
        # resultat_exploitation_positif = "oui depuis deux exercices au moins"

        fonds_propres_actuellement_positifs = "oui"
        # fonds_propres_actuellement_positifs = "non"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.meilleurtauxpro.com/')
        print("page opened")

        time.sleep(25)

        # click on 'continuer sans accepter' button
        continuer_sans_accepter_button = browser.find_element_by_xpath(
            '/html/body/div[8]/div/div[2]/button[3]'
        )
        continuer_sans_accepter_button.click()
        print('continuer_sans_accepter_button clicked')

        time.sleep(10)

        # click on 'déposer ma demande de prêt' button
        deposer_ma_demande_de_pret_button = browser.find_element_by_xpath(
            '/html/body/header/div/div[2]/a'
        )
        deposer_ma_demande_de_pret_button.click()
        print('deposer_ma_demande_de_pret_button clicked')

        time.sleep(10)

        # click on 'Trésorerie' button
        tresorerie_button = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[1]/div[3]/div[1]/div[6]/a'
        )
        tresorerie_button.click()
        print('tresorerie_button clicked')

        time.sleep(10)

        # click on 'Autres financements de trésorerie' button
        autres_financements_de_tresorerie_button = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[2]/div[2]/div[4]/div[4]/a'
        )
        autres_financements_de_tresorerie_button.click()
        print('autres_financements_de_tresorerie_button clicked')

        time.sleep(10)

        # click on '3 ou +' button
        # Combien d'exercices comptables complets avez-vous clos ?
        trois_ou_plus_button = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[5]/div[2]/div[1]/div[4]/a'
        )
        trois_ou_plus_button.click()
        print('trois_ou_plus_button clicked')

        # Votre résultat d'exploitation est-il positif ?
        if resultat_exploitation_positif == "non":
            resultat_exploitation_non_button = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[6]/div[2]/div[1]/div[1]/a'
            )
            resultat_exploitation_non_button.click()
            print('resultat_exploitation_non_button clicked')
        elif resultat_exploitation_positif == "oui sur le dernier exercice":
            resultat_exploitation_oui_dernier_exercice_button = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[6]/div[2]/div[1]/div[2]/a'
            )
            resultat_exploitation_oui_dernier_exercice_button.click()
            print('resultat_exploitation_oui_dernier_exercice_button clicked')
        elif resultat_exploitation_positif == "oui depuis deux exercices au moins":
            resultat_exploitation_oui_deux_derniers_exercices_button = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[6]/div[2]/div[1]/div[3]/a'
            )
            resultat_exploitation_oui_deux_derniers_exercices_button.click()
            print('resultat_exploitation_oui_deux_derniers_exercices_button clicked')

        time.sleep(10)

        # Vos fonds propres sont-ils actuellement positifs ?
        if fonds_propres_actuellement_positifs == "non":
            fonds_propres_actuellement_positifs_non_button = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[7]/div[2]/div[1]/div[1]/a'
            )
            fonds_propres_actuellement_positifs_non_button.click()
            print('fonds_propres_actuellement_positifs_non_button clicked')
        elif fonds_propres_actuellement_positifs == "oui":
            fonds_propres_actuellement_positifs_non_button_oui_button = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[7]/div[2]/div[1]/div[1]/a'
            )
            fonds_propres_actuellement_positifs_non_button_oui_button.click()
            print('fonds_propres_actuellement_positifs_non_button_oui_button clicked')

        time.sleep(10)
        
        # Définissons le montant du prêt
        # MONTANT TOTAL DE VOTRE PROJET
        montant_total_de_votre_projet = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[8]/div[2]/div[1]/input'
        )
        montant_total_de_votre_projet.clear()
        montant_total_de_votre_projet.send_keys('1000000')
        print("montant_total_de_votre_projet inserted")

        time.sleep(10)

        # MONTANT DE VOTRE APPORT
        montant_de_votre_apport = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[8]/div[2]/div[3]/input'
        )
        montant_de_votre_apport.clear()
        montant_de_votre_apport.send_keys('10000')
        print("montant_de_votre_apport inserted")

        time.sleep(10)

        # Click on "Suivant" button
        suivant_button = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
        )
        suivant_button.click()
        print("suivant_button clicked")

        time.sleep(10)

        # Quelle durée de remboursement envisagez-vous ?
        duree_de_remboursement_cinq_ans_button = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[10]/div[2]/div[1]/div[5]/a'
        )
        duree_de_remboursement_cinq_ans_button.click()
        print("duree_de_remboursement_cinq_ans_button clicked")

        time.sleep(10)

        # Localisation de votre projet
        # VILLE OU CODE POSTAL DE VOTRE PROJET
        ville_ou_code_postal_de_votre_projet_input = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[11]/div[2]/div[1]/div[1]/input'
        )
        ville_ou_code_postal_de_votre_projet_input.clear()
        ville_ou_code_postal_de_votre_projet_input.send_keys('')
        print("ville_ou_code_postal_de_votre_projet_input inserted")

        time.sleep(10)

        ville_ou_code_postal_de_votre_projet_select = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[11]/div[2]/div[1]/div[1]/div/ul/li[3]'
        )
        ville_ou_code_postal_de_votre_projet_select.click()
        print("ville_ou_code_postal_de_votre_projet_select clicked")

        time.sleep(10)

        code_postal_projet_identique_du_siege_social_non_button = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[11]/div[2]/div[2]/div[1]/span[2]'
        )
        code_postal_projet_identique_du_siege_social_non_button.click()
        print("code_postal_projet_identique_du_siege_social clicked")

        time.sleep(10)

        # CODE POSTAL DU SIÈGE SOCIAL
        code_postal_siege_social_input = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[11]/div[2]/div[3]/div[1]/input'
        )
        code_postal_siege_social_input.clear()
        code_postal_siege_social_input.send_keys('')
        print("code_postal_siege_social_input inserted")

        time.sleep(10)

        code_postal_siege_social_select = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[11]/div[2]/div[3]/div[1]/div/ul/li'
        )
        code_postal_siege_social_select.click()
        print("code_postal_siege_social_select clicked")

        time.sleep(10)

        suivant_button_v1 = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
        )
        suivant_button_v1.click()
        print("suivant_button_v1 clicked")

        time.sleep(10)

        # Quel est votre niveau de chiffre d'affaires ?
        plus_deux_millions_euros = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[12]/div[2]/div[1]/div[4]/a'
        )
        plus_deux_millions_euros.click()
        print("plus_deux_millions_euros clicked")

        time.sleep(10)

        # Avez-vous déjà contacté des établissements financiers ?
        contacte_etablissements_financiers_non = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[15]/div[2]/div[1]/div[2]/a'
        )
        contacte_etablissements_financiers_non.click()
        print('contacte_etablissements_financiers_non clicked')

        time.sleep(10)

        # Quel est le nom de votre entreprise ?
        # NOM DE L'ENTREPRISE
        nom_de_l_entreprise = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[20]/div[2]/div[1]/div[1]/input'
        )
        nom_de_l_entreprise.clear()
        nom_de_l_entreprise.send_keys('HOLOMORPHE')
        print("nom_de_l_entreprise inserted")

        time.sleep(10)

        nom_de_l_entreprise_select = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[20]/div[2]/div[1]/div[1]/div/ul/li'
        )
        nom_de_l_entreprise_select.click()
        print("nom_de_l_entreprise_select clicked")

        time.sleep(10)

        nom_enseigne_identique_a_la_raison_sociale_oui = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[20]/div[2]/div[2]/div[1]/span[1]'
        )
        nom_enseigne_identique_a_la_raison_sociale_oui.click()
        print("nom_enseigne_identique_a_la_raison_sociale_oui clicked")

        time.sleep(10)

        suivant_button_v2 = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
        )
        suivant_button_v2.click()
        print("suivant_button_v2 clicked")

        time.sleep(10)

        # Votre email
        email_input = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[21]/div[3]/div[2]/input[4]'
        )
        email_input.clear()
        email_input.send_keys('.@holomorphe.com')

        time.sleep(10)

        suivant_button_v3 = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
        )
        suivant_button_v3.click()
        print("suivant_button_v3 clicked")

        time.sleep(10)

        # Décrivez votre projet
        description_du_projet = """
        Bonjour,\n\n
        Tout d'abord, je suis en train de monter un projet de production de gaz (hydrogène et/ou méthane de synthèse) 
        directement injectée dans un réseau de transport de gaz naturel.\n\n
        Après, je voudrai lancer une installation de production d'hydrogène à partir de l'électrolyse de l'eau en 
        utilisant l'électrolyseur de Stanley Meyer dont l'installation sera raccordée au réseau de transport de gaz 
        naturel.\n\n
        Puis, le but final de ce projet est de créer un gisement artificiel d'hydrogène comme une source 
        d'énergie.\n\n
        Ainsi, je dois effectuer des investissements pour l'achat d'un terrain en zone industrielle, de matériels 
        industriels et assurer une trésorerie pour mener à bien la vie de la société Holomorphe.\n\n
        Très bonne journée à vous,\n\n
        Mr  \n
        Président de la société Holomorphe
        """

        description_du_projet_input = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[22]/div[3]/div/textarea'
        )
        description_du_projet_input.clear()
        description_du_projet_input.send_keys(description_du_projet)

        time.sleep(20)

        suivant_button_v4 = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
        )
        suivant_button_v4.click()
        print("suivant_button_v4 clicked")

        time.sleep(10)
        
        # Avez-vous déjà souscrit un crédit professionnel ?
        souscrit_un_credit_professionnel_non = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[23]/div[2]/div[1]/div[2]/a'
        )
        souscrit_un_credit_professionnel_non.click()
        print("souscrit_un_credit_professionnel_non clicked")

        time.sleep(10)

        try:
            suivant_button_v5 = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
            )
            suivant_button_v5.click()
            print("suivant_button_v5 clicked")
        except Exception as e:
            print('error suivant_button_v5 : ' + str(e))

        time.sleep(10)

        # Comment estimez-vous vos connaissances en financement professionnel ?
        connaissances_financement_professionnel_reduites = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[24]/div[3]/div[1]/div[1]/a'
        )
        connaissances_financement_professionnel_reduites.click()
        print("connaissances_financement_professionnel_reduites clicked")

        time.sleep(10)

        try:
            suivant_button_v6 = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
            )
            suivant_button_v6.click()
            print("suivant_button_v6 clicked")
        except Exception as e:
            print('error suivant_button_v6 : ' + str(e))

        time.sleep(10)

        # Vos coordonnées
        # CIVILITÉ
        civilite_select = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[27]/div[2]/div[1]/select/option[2]'
        )
        civilite_select.click()
        print("civilite_select clicked")

        time.sleep(10)

        # NOM
        nom_input = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[27]/div[2]/div[2]/input'
        )
        nom_input.clear()
        nom_input.send_keys('')
        print("nom_input inserted")

        time.sleep(10)

        # PRÉNOM
        prenom_input = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[27]/div[2]/div[3]/input'
        )
        prenom_input.clear()
        prenom_input.send_keys('')
        print("prenom_input inserted")

        time.sleep(10)

        # DATE DE NAISSANCE (JJ/MM/AAAA)
        date_de_naissance_jour = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[27]/div[2]/div[4]/input[1]'
        )
        date_de_naissance_jour.clear()
        date_de_naissance_jour.send_keys("")
        print("date_de_naissance_jour inserted")

        time.sleep(10)

        date_de_naissance_mois = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[27]/div[2]/div[4]/input[2]'
        )
        date_de_naissance_mois.clear()
        date_de_naissance_mois.send_keys("")
        print("date_de_naissance_mois inserted")

        time.sleep(10)

        date_de_naissance_annee = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[27]/div[2]/div[4]/input[3]'
        )
        date_de_naissance_annee.clear()
        date_de_naissance_annee.send_keys("")
        print("date_de_naissance_annee inserted")

        time.sleep(10)

        try:
            suivant_button_v7 = browser.find_element_by_xpath(
                "/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]"
            )
            suivant_button_v7.click()
            print("suivant_button_v7 inserted")
        except Exception as e:
            print("error suivant_button_v7 : " + str(e))

        time.sleep(10)

        # POUR QUE NOUS PUISSIONS ÉTUDIER VOTRE DEMANDE, MERCI DE RENSEIGNER VOTRE NUMÉRO DE TÉLÉPHONE.
        # TÉLÉPHONE / MOBILE
        telephone_mobile_input = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[28]/div[3]/div[1]/input'
        )
        telephone_mobile_input.clear()
        telephone_mobile_input.send_keys("")
        print("telephone_mobile_input inserted")

        time.sleep(10)

        # coocher la case "Je confirme mandater, gratuitement et sans aucun engagement de ma part,
        # Meilleurtaux pour effectuer ma demande de pré-étude de financement"
        case_a_cocher_pour_mandater_meilleur_taux = browser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/form/div[1]/div[28]/div[3]/div[2]/p/input[2]'
        )
        case_a_cocher_pour_mandater_meilleur_taux.click()
        print("case_a_cocher_pour_mandater_meilleur_taux clicked")

        time.sleep(10)

        try:
            suivant_button_v8 = browser.find_element_by_xpath(
                '/html/body/div[6]/div[2]/form/div[1]/div[30]/a[2]'
            )
            suivant_button_v8.click()
            print("suivant_button_v8 clicked")
        except Exception as e:
            print('error suivant_button_v8 : ' + str(e))

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
