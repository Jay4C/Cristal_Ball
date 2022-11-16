import unittest
import time
import warnings
from selenium import webdriver

annee = "Annee_2021"
exercice = "2_Exercice_01_01_2021__31_12_2021"
votre_reference = "Exercice2021"
date_debut_exercice = "01/01/2021"
date_fin_exercice = "31/12/2021"


class UnitTestsWebAutomationInfogreffe(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page_for_dsn_test")

        url = 'https://www.infogreffe.fr/formalites-entreprise/depot-des-comptes.html'

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        email = ""
        password = ""

        url = 'https://www.infogreffe.fr'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on "Refuser tout" button
        refuser_tout_button = browser.find_element_by_xpath(
            '//*[@id="refusercookies_label"]'
        )
        refuser_tout_button.click()

        time.sleep(5)

        # Click on "Se connecter" button
        se_connecter_button = browser.find_element_by_xpath(
            '//*[@id="btn-connect"]'
        )
        se_connecter_button.click()

        time.sleep(5)

        # Insert "Mail"
        mail_input = browser.find_element_by_xpath(
            '//*[@id="username"]'
        )
        mail_input.clear()
        mail_input.send_keys(email)

        time.sleep(5)

        # Insert "Mot de passe"
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="password"]'
        )
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys(password)

        time.sleep(5)

        # Click on "Connexion" button
        connexion_button = browser.find_element_by_xpath(
            '/html/body/div/div/div[1]/div/div/div/div/form/div/div[4]/div[2]/button'
        )
        connexion_button.click()

        time.sleep(5)

    # ok
    def test_deposer_comptes_annuels_holomorphe(self):
        print("test_deposer_comptes_annuels_holomorphe")

        email = ""
        password = ""

        # Informations entreprise
        siren = "883632556"
        folder_exercice = "A:\\1_Professionnel\\1_Holomorphe\\1_Administration" \
                            "\\2_Gestion_Declarations_Administratives\\1_Recurrentes\\5_Infogreffe" \
                            "\\4_Approbation_Comptes_Sociaux\\" + exercice
        folder_screenshot = folder_exercice + "\\Screenshot"
        bilan_file = folder_exercice + "Bilan_Compte_Resultat_" + annee + "_HOLOMORPHE.pdf"
        inventaire_file = folder_exercice + "Inventaire_" + annee + "_HOLOMORPHE.pdf"
        p_v_a_c_annuels_file = folder_exercice + "P_V_A_C_Annuels_" + annee + "_HOLOMORPHE.pdf"
        attestation_conformite_file = folder_exercice + "Conformite_Comptables_" + annee + "_HOLOMORPHE.pdf"
        declaration_confidentialite_comptes_annuels_file = folder_exercice \
                                                           + "Declaration_Confidentialite_Comptes_Annuels_" \
                                                           + annee \
                                                           + "_HOLOMORPHE.pdf"
        rapport_de_gestion_file = folder_exercice + "Rapport_Gestion_" + annee + "_HOLOMORPHE.pdf"

        url = 'https://www.infogreffe.fr'

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='..\\..\\geckodriver.exe',
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)
        print('browser.get(url)')

        time.sleep(15)

        # Click on "Refuser tout" button
        refuser_tout_button = browser.find_element_by_xpath(
            '//*[@id="refusercookies_label"]'
        )
        refuser_tout_button.click()

        time.sleep(5)

        # Click on "Se connecter" button
        se_connecter_button = browser.find_element_by_xpath(
            '//*[@id="btn-connect"]'
        )
        se_connecter_button.click()

        time.sleep(5)

        # Insert "Mail"
        mail_input = browser.find_element_by_xpath(
            '//*[@id="username"]'
        )
        mail_input.clear()
        mail_input.send_keys(email)

        time.sleep(5)

        # Insert "Mot de passe"
        mot_de_passe_input = browser.find_element_by_xpath(
            '//*[@id="password"]'
        )
        mot_de_passe_input.clear()
        mot_de_passe_input.send_keys(password)

        time.sleep(5)

        # Click on "Connexion" button
        connexion_button = browser.find_element_by_xpath(
            '/html/body/div/div/div[1]/div/div/div/div/form/div/div[4]/div[2]/button'
        )
        connexion_button.click()

        time.sleep(10)

        i = 1

        # Screenshot
        browser.save_screenshot(folder_screenshot + "\\Page_" + str(i) + ".png")
        i += 1

        time.sleep(5)

        # Get on the "Déposer les comptes annuels" url
        url_depot_comptes_annuels = "https://www.infogreffe.fr/acces-formalite/dpca.html"
        browser.get(url_depot_comptes_annuels)
        print('browser.get(url_depot_comptes_annuels)')

        time.sleep(15)

        browser.refresh()
        print('browser.refresh()')

        time.sleep(5)

        # Insert the 'siren' input
        for a in range(1, 10):
            try:
                siren_input = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt23' + str(a) + ':numeroIdentification"]'
                )
                siren_input.clear()
                siren_input.send_keys(siren)
                print("siren_input.send_keys(siren)")
                break
            except Exception as e:
                print('error siren_input : ' + str(e))

        time.sleep(7)

        # Click on the "Rechercher" button
        for a in range(1, 10):
            try:
                rechercher_button = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt25' + str(a) + '"]'
                )
                rechercher_button.click()
                print("rechercher_button.click()")
                break
            except Exception as e:
                print('error rechercher_button : ' + str(e))

        time.sleep(10)

        # Screenshot
        browser.save_screenshot(folder_screenshot + "\\Page_" + str(i) + ".png")
        i += 1

        time.sleep(5)

        # Click on the "Etape suivante" button
        for a in range(1, 10):
            try:
                etape_suivante_1_button = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt34' + str(a) + ':etapeSuivante"]'
                )
                etape_suivante_1_button.click()
                print('etape_suivante_1_button.click()')
                break
            except Exception as e:
                print('error etape_suivante_1_button : ' + str(e))

        time.sleep(10)

        for a in range(1, 10):
            try:
                # Insert the 'Votre référence' input
                votre_reference_input = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt19' + str(a) + ':votreReference"]'
                )
                votre_reference_input.clear()
                votre_reference_input.send_keys(votre_reference)
                print("votre_reference_input.send_keys(votre_reference)")
                break
            except Exception as e:
                print('error votre_reference_input : ' + str(e))

        time.sleep(5)

        for a in range(1, 10):
            try:
                # Insert the "Date Debut Exercice" input
                date_debut_exercice_input = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt24' + str(a) + ':dateExerciceDEb_input"]'
                )
                date_debut_exercice_input.clear()
                date_debut_exercice_input.send_keys(date_debut_exercice)
                print('date_debut_exercice_input.send_keys(date_debut_exercice)')
                break
            except Exception as e:
                print('error date_debut_exercice_input : ' + str(e))

        time.sleep(5)

        for a in range(1, 10):
            try:
                # Insert the "Date Fin Exercice" input
                date_fin_exercice_input = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt25' + str(a) + ':dateExerciceFin_input"]'
                )
                date_fin_exercice_input.clear()
                date_fin_exercice_input.send_keys(date_fin_exercice)
                print('date_fin_exercice_input.send_keys(date_fin_exercice)')
                break
            except Exception as e:
                print('error date_fin_exercice_input : ' + str(e))

        time.sleep(5)

        # Click on the "associe_unique_president" checkbox
        try:
            associe_unique_president_checbox = browser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/div/div/div/span[4]/div/div/div/div[2]/span'
            )
            associe_unique_president_checbox.click()
            print("associe_unique_president_checbox.click()")
        except Exception as e:
            print('error associe_unique_president_checbox : ' + str(e))

        time.sleep(5)

        # Click on the "sans_annexe" checkbox
        try:
            sans_annexe_checkbox = browser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/div/div/div/span[5]/div/div/div/div[2]/span'
            )
            sans_annexe_checkbox.click()
            print("sans_annexe_checkbox.click()")
        except Exception as e:
            print('error sans_annexe_checkbox : ' + str(e))

        time.sleep(5)

        # Click on the "option_exercee_article_l232_25_du_code_de_commerce" checkbox
        try:
            option_exercee_article_l232_25_du_code_de_commerce_checkbox = browser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/div/div/div/span[6]/div[1]/div/div/div[2]/span'
            )
            option_exercee_article_l232_25_du_code_de_commerce_checkbox.click()
            print("option_exercee_article_l232_25_du_code_de_commerce_checkbox.click()")
        except Exception as e:
            print('error option_exercee_article_l232_25_du_code_de_commerce_checkbox : ' + str(e))

        time.sleep(5)

        # Click on the "comptes_deposes_non_rendus_publics" checkbox
        try:
            comptes_deposes_non_rendus_publics_checkbox = browser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/div/div/div/span[6]/div[2]/div/div[1]/div/div[2]'
            )
            comptes_deposes_non_rendus_publics_checkbox.click()
            print("comptes_deposes_non_rendus_publics_checkbox.click()")
        except Exception as e:
            print('error comptes_deposes_non_rendus_publics_checkbox : ' + str(e))

        time.sleep(5)

        # Click on the "accepte_les_termes" checkbox
        try:
            accepte_les_termes_checkbox = browser.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/div/div/div/span[7]/div/div/div/div[2]/span'
            )
            accepte_les_termes_checkbox.click()
            print("accepte_les_termes_checkbox.click()")
        except Exception as e:
            print('error accepte_les_termes_checkbox : ' + str(e))

        time.sleep(5)

        # Screenshot
        browser.save_screenshot(folder_screenshot + "\\Page_" + str(i) + ".png")
        i += 1

        time.sleep(5)

        # Click on the "Etape suivante" button
        for a in range(1, 10):
            try:
                etape_suivante_2_button = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt40' + str(a) + ':etapeSuivante"]'
                )
                etape_suivante_2_button.click()
                print("etape_suivante_2_button.click()")
                break
            except Exception as e:
                print('error etape_suivante_2_button : ' + str(e))

        time.sleep(10)

        # Insert the "bilan_file_upload" file upload
        for a in range(1, 10):
            try:
                bilan_file_upload = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt26' + str(a) + ':0:j_idt300_input"]'
                )
                bilan_file_upload.clear()
                bilan_file_upload.send_keys(bilan_file)
                print('bilan_file_upload.send_keys(bilan_file)')
                break
            except Exception as e:
                print('error bilan_file_upload : ' + str(e))

        time.sleep(15)

        # Insert the "inventaire_file_upload" file upload
        for a in range(1, 10):
            try:
                inventaire_file_upload = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt26' + str(a) + ':1:j_idt300_input"]'
                )
                inventaire_file_upload.clear()
                inventaire_file_upload.send_keys(inventaire_file)
                print('inventaire_file_upload.send_keys(inventaire_file)')
                break
            except Exception as e:
                print('error inventaire_file_upload : ' + str(e))

        time.sleep(15)

        # Insert the "attestation_conformite_file" file upload
        for a in range(1, 10):
            try:
                attestation_conformite_file_upload = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt26' + str(a) + ':2:j_idt300_input"]'
                )
                attestation_conformite_file_upload.clear()
                attestation_conformite_file_upload.send_keys(attestation_conformite_file)
                print('attestation_conformite_file_upload.send_keys(attestation_conformite_file)')
                break
            except Exception as e:
                print('error attestation_conformite_file_upload : ' + str(e))

        time.sleep(15)

        # Insert the "declaration_confidentialite_comptes_annuels_file_upload" file upload
        for a in range(1, 10):
            try:
                declaration_confidentialite_comptes_annuels_file_upload = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt26' + str(a) + ':3:j_idt300_input"]'
                )
                declaration_confidentialite_comptes_annuels_file_upload.clear()
                declaration_confidentialite_comptes_annuels_file_upload.send_keys(
                    declaration_confidentialite_comptes_annuels_file)
                print('declaration_confidentialite_comptes_annuels_file_upload.send_keys(declaration_confidentialite_comptes_annuels_file)')
                break
            except Exception as e:
                print('error declaration_confidentialite_comptes_annuels_file_upload : ' + str(e))

        time.sleep(15)

        # Insert the "p_v_a_c_annuels_file_upload" file upload
        for a in range(1, 10):
            try:
                p_v_a_c_annuels_file_upload = browser.find_element_by_xpath(
                    '//*[@id="formulaire:pF_0_panelPiecesFacultatifs_PAJ_DPCA:j_idt31' + str(a) + ':0:j_idt349_input"]'
                )
                p_v_a_c_annuels_file_upload.clear()
                p_v_a_c_annuels_file_upload.send_keys(p_v_a_c_annuels_file)
                print('p_v_a_c_annuels_file_upload.send_keys(p_v_a_c_annuels_file)')
                break
            except Exception as e:
                print('error p_v_a_c_annuels_file_upload : ' + str(e))

        time.sleep(15)

        # Insert the "rapport_de_gestion_file_upload" file upload
        for a in range(1, 10):
            try:
                rapport_de_gestion_file_upload = browser.find_element_by_xpath(
                    '//*[@id="formulaire:pF_0_panelPiecesFacultatifs_PAJ_DPCA:j_idt31' + str(a) + ':2:j_idt349_input"]'
                )
                rapport_de_gestion_file_upload.clear()
                rapport_de_gestion_file_upload.send_keys(rapport_de_gestion_file)
                print('.send_keys(rapport_de_gestion_file)')
                break
            except Exception as e:
                print('error : ' + str(e))

        time.sleep(15)

        # Screenshot
        browser.save_screenshot(folder_screenshot + "\\Page_" + str(i) + ".png")
        i += 1

        time.sleep(5)

        # Click on the "Etape suivante" button
        for a in range(1, 10):
            try:
                etape_suivante_3_button = browser.find_element_by_xpath(
                    '//*[@id="formulaire:j_idt41' + str(a) + ':etapeSuivante"]'
                )
                etape_suivante_3_button.click()
                print("etape_suivante_3_button.click()")
                break
            except Exception as e:
                print('error : ' + str(e))

        time.sleep(10)

        # Click on the "atteste avoir visualisé mon dépôt" checkbox
        visualiser_mon_depot_checkbox = browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/div/form/div[2]/div/div/div[3]/div/div/div[2]/span'
        )
        visualiser_mon_depot_checkbox.click()
        print("visualiser_mon_depot_checkbox.click()")

        time.sleep(10)

        # Screenshot
        browser.save_screenshot(folder_screenshot + "\\Page_" + str(i) + ".png")
        i += 1

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
