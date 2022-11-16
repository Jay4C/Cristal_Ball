import os
import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationProtoelectronincs(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get('https://app.protoelectronique.com/fr/user-login')
        time.sleep(15)
        print("page opened")

        # Click on the "Accept" button
        accept_button = browser.find_element_by_xpath(
            '//*[@id="hs-eu-confirmation-button"]'
        )
        accept_button.click()
        time.sleep(10)
        print("accept_button clicked")

        email_input = browser.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]/div/div[1]/form/div[1]/input"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")
        time.sleep(5)
        print("email_input inserted")

        password_input = browser.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]/div/div[1]/form/div[2]/input"
        )
        password_input.clear()
        password_input.send_keys("")
        time.sleep(5)
        print("password_input inserted")

        log_in_button = browser.find_element_by_xpath(
            '//*[@id="btn_login"]'
        )
        log_in_button.click()
        time.sleep(15)
        print("log_in_button clicked")

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(5)

    #
    def test_creer_un_projet(self):
        print("test_creer_un_projet")

        # Paramètres
        designation = "stanley_meyer_vic_4"

        # Quantité de PCB
        # PCB équipés
        pcb_equipes = 1

        # Dimensions (Valeurs indiquées dans votre fichier gerber)
        x_en_mm = 250
        y_en_mm = 250

        # Spécifications
        # Matériau (1:FR4 ,
        # 2:FR4 Hi TG180 ,
        # 3:FR4 Hi IRC 600 ,
        # 4:SMI 1.0 W/m.k ,
        # 5:SMI 1.5 W/m.k ,
        # 6:SMI 2.0 W/m.k ,
        # 7:SMI 3.0 W/m.k ,
        # 8:SMI 5.0 W/m.k ,
        # 9:SMI 8.0 W/m.k ,
        # 10:POLYIMIDE rigide - TG250 ,
        # 11:CEM3 - 1.5W/m.k ,
        # 12:ROGERS 4350B)
        materiau = 12

        # Épaisseur
        # 1:0.3mm ,
        # 2:0.6mm ,
        # 3:0.8mm ,
        # 4:1.0mm ,
        # 5:1.4mm ,
        # 6:1.6mm ,
        # 7:2.0mm ,
        # 8:2.4mm
        epaisseur = 2

        # Finitions
        # 1:Or chimique (ENIG) ,
        # 2:HAL ,
        # 3:ENEPIG ,
        # 4:or electro. ,
        # 5:HAL - SN100C
        finitions = 2

        # Nombre de couches
        # 1:2 ,
        # 2:4 ,
        # 3:6,
        # 4:8
        # /html/body/div[3]/div/form/div[3]/div[4]/div[2]/select/option[1]
        nombre_de_couches = 2

        # Face CMS
        # 1:aucune ,
        # 2:TOP ,
        # 3:BOT ,
        # 4:TOP + BOT
        # /html/body/div[3]/div/form/div[3]/div[6]/div[2]/select/option[1]
        face_cms = 2

        # Épaisseur de cuivre externe fini (µ)
        # 1:35 µm ,
        # 2:70 µm ,
        # 3:105 µm ,
        # 4:140 µm ,
        # 5:210 µm
        # /html/body/div[3]/div/form/div[3]/div[7]/div[2]/select/option[1]
        epaisseur_de_cuivre_externe_fini = 2

        # Classe IPC
        # 1:Class 2 ,
        # 2:Class 3
        # /html/body/div[3]/div/form/div[3]/div[9]/div[2]/select/option[1]
        class_ipc = 2

        # Vernis
        # Vernis épargne
        # 1:sans ,
        # 2:TOP ,
        # 3:BOT ,
        # 4:TOP + BOT
        # /html/body/div[3]/div/form/div[5]/div[1]/div[2]/select/option[1]
        vernis_epargne = 2

        # Couleur du vernis
        # 1:vert ,
        # 2:noir brillant ,
        # 3:noir mat ,
        # 4:blanc ,
        # 5:rouge ,
        # 6:bleu ,
        # 7:violet ,
        # 8:jaune ,
        # 9:Transparent
        # /html/body/div[3]/div/form/div[5]/div[2]/div[2]/select/option[1]
        couleur_du_vernis = 2

        # Épargne pelable
        # 1:sans ,
        # 2:TOP ,
        # 3:BOT ,
        # 4:TOP + BOT
        # /html/body/div[3]/div/form/div[5]/div[3]/div[2]/select/option[1]
        epargne_pelable = 2

        # Marquage
        # Sérigraphie (encre)
        # 1:sans ,
        # 2:TOP ,
        # 3:BOT ,
        # 4:TOP+BOT
        # /html/body/div[3]/div/form/div[7]/div[1]/div[2]/select/option[1]
        serigraphie = 2

        # Marquage ROHS
        # 1:sans ,
        # 2:sérigraphie TOP ,
        # 3:sérigraphie BOT ,
        # 4:couche vernis TOP ,
        # 5:couche vernis BOT ,
        # 6:couche cuivre TOP ,
        # 7:couche cuivre BOT
        # /html/body/div[3]/div/form/div[7]/div[3]/div[2]/select/option[7]
        marquage_rohs = 2

        # Marquage UL
        # 1:sans ,
        # 2:sérigraphie TOP ,
        # 3:sérigraphie BOT ,
        # 4:couche vernis TOP ,
        # 5:couche vernis BOT ,
        # 6:couche cuivre TOP
        # 7:couche cuivre BOT
        # /html/body/div[3]/div/form/div[7]/div[4]/div[2]/select/option[7]
        marquage_ul = 2

        # Marquage Date
        # 1:sans ,
        # 2:sérigraphie TOP ,
        # 3:sérigraphie BOT ,
        # 4:couche vernis TOP ,
        # 5:couche vernis BOT ,
        # 6:couche cuivre TOP
        # 7:couche cuivre BOT
        # /html/body/div[3]/div/form/div[7]/div[5]/div[2]/select/option[7]
        marquage_date = 2

        # Options spécifiques
        # Espace entre pistes
        # 1:> 0.075 mm ,
        # 2:> 0.10 mm ,
        # 3:> 0.15 mm ,
        # 4:> 0.20 mm
        # /html/body/div[3]/div/form/div[9]/div[1]/div[2]/select/option[1]
        espace_entre_pistes = 2

        # Taille min. des perçages
        # 1:> 0.10 mm ,
        # 2:> 0.20 mm
        # /html/body/div[3]/div/form/div[9]/div[2]/div[2]/select/option[1]
        taille_minimale_des_percages = 2

        # Trous borgnes
        # 1:non ,
        # 2:oui
        # /html/body/div[3]/div/form/div[9]/div[3]/div[2]/select/option[1]
        trous_borgnes = 2

        # Via croisé
        # 1:non ,
        # 2:oui
        # /html/body/div[3]/div/form/div[9]/div[4]/div[2]/select/option[1]
        via_croise = 2

        # Via enterré
        # 1:non ,
        # 2:oui
        # /html/body/div[3]/div/form/div[9]/div[5]/div[2]/select/option[1]
        via_enterre = 2

        # Contrôle d'impédance
        # 1:non,
        # 2:oui
        # /html/body/div[3]/div/form/div[9]/div[6]/div[2]/select/option[1]
        controle_impedance = 2

        # Métallisation tranche
        # 1:non,
        # 2:oui
        # /html/body/div[3]/div/form/div[9]/div[7]/div[2]/select/option[1]
        metallisation_tranche = 2

        # Press-fit
        # 1:Choix obligatoire ,
        # 2:non ,
        # 3:oui
        press_fit = 2

        # Via Fill
        # 1:sans ,
        # 2:Via Fill ,
        # 3:Via in pad - IPC-4761 Type VII
        # /html/body/div[3]/div/form/div[9]/div[10]/div[2]/select/option[1]
        via_fill = 2

        # Biseau
        # 1:sans ,
        # 2:TOP ,
        # 3:BOT ,
        # 4:TOP & BOT
        # /html/body/div[3]/div/form/div[9]/div[11]/div[2]/select/option[1]
        biseau = 2

        # Trous fraisés
        # 1:sans ,
        # 2:TOP ,
        # 3:BOT ,
        # 4:TOP & BOT
        # /html/body/div[3]/div/form/div[9]/div[12]/div[2]/select/option[1]
        trous_fraises = 2

        # Coupe métallographique
        # 1:non ,
        # 2:oui
        # /html/body/div[3]/div/form/div[9]/div[14]/div[2]/select/option[1]
        coupe_metallographique = 2

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()
        print("browser.maximize_window()")

        time.sleep(5)

        # open
        browser.get('https://app.protoelectronique.com/fr/user-login')
        time.sleep(15)
        print("page opened")

        # Click on the "Accept" button
        accept_button = browser.find_element_by_xpath(
            '//*[@id="hs-eu-confirmation-button"]'
        )
        accept_button.click()
        time.sleep(10)
        print("accept_button clicked")

        email_input = browser.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]/div/div[1]/form/div[1]/input"
        )
        email_input.clear()
        email_input.send_keys(".@outlook.fr")
        time.sleep(5)
        print("email_input inserted")

        password_input = browser.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]/div/div[1]/form/div[2]/input"
        )
        password_input.clear()
        password_input.send_keys("")
        time.sleep(5)
        print("password_input inserted")

        log_in_button = browser.find_element_by_xpath(
            '//*[@id="btn_login"]'
        )
        log_in_button.click()
        time.sleep(15)
        print("log_in_button clicked")

        # Click on the "Créer un nouveau projet" button
        creer_un_nouveau_projet_button = browser.find_element_by_xpath(
            '//*[@id="btn_dashboard_create_project"]'
        )
        creer_un_nouveau_projet_button.click()
        time.sleep(15)
        print("creer_un_nouveau_projet_button clicked")

        # Nom du projet
        # Insert the "Désignation" input
        designation_input = browser.find_element_by_xpath(
            '//*[@id="js_modal_project_create_project_name"]'
        )
        designation_input.send_keys(designation)
        time.sleep(10)
        print("designation_input inserted")

        # Quantité de cartes
        # PCB équipés
        pcb_equipes_input = browser.find_element_by_xpath(
            '//*[@id="js_modal_project_create_nb_cards_equiped"]'
        )
        pcb_equipes_input.clear()
        pcb_equipes_input.send_keys(pcb_equipes)
        time.sleep(10)
        print("PCB équipés : " + str(pcb_equipes))

        # Click on the "Passer à la configuration du PCB" button
        passer_a_la_configuration_du_pcb_button = browser.find_element_by_xpath(
            '//*[@id="btn-go-to-pcb-config"]'
        )
        passer_a_la_configuration_du_pcb_button.click()
        time.sleep(15)
        print("passer_a_la_configuration_du_pcb_button clicked")

        # Dimensions (Valeurs indiquées dans votre fichier gerber)
        # X (en mm)
        x_en_mm_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[1]/div[1]/input'
        )
        x_en_mm_input.clear()
        x_en_mm_input.send_keys(x_en_mm)
        time.sleep(10)
        print("x_en_mm_input inserted")

        # Y (en mm)
        y_en_mm_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[1]/div[2]/input'
        )
        y_en_mm_input.clear()
        y_en_mm_input.send_keys(y_en_mm)
        time.sleep(10)
        print("y_en_mm_input inserted")

        # Spécifications
        # Matériau
        materiau_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[3]/div[1]/div[2]/select/option[' + str(materiau) + ']'
        )
        materiau_input.click()
        time.sleep(10)
        print("materiau_input.click()")

        # Épaisseur
        epaisseur_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[3]/div[2]/div[2]/select/option[' + str(epaisseur) + ']'
        )
        epaisseur_input.click()
        time.sleep(10)
        print("epaisseur_input.click()")

        # Finitions
        finitions_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[3]/div[3]/div[2]/select/option[' + str(finitions) + ']'
        )
        finitions_input.click()
        time.sleep(10)
        print("finitions_input.click()")

        # Nombre de couches
        nombre_de_couches_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[3]/div[4]/div[2]/select/option[' + str(nombre_de_couches) + ']'
        )
        nombre_de_couches_input.click()
        time.sleep(10)
        print("nombre_de_couches_input.click()")

        # Face CMS
        face_cms_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[3]/div[6]/div[2]/select/option[' + str(face_cms) + ']'
        )
        face_cms_input.click()
        time.sleep(10)
        print("face_cms_input.click()")

        # Épaisseur de cuivre externe fini (µ)
        _input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[3]/div[7]/div[2]/select/option['
            + str(epaisseur_de_cuivre_externe_fini) + ']'
        )
        _input.click()
        time.sleep(10)
        print(".click()")

        # Classe IPC
        class_ipc_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[3]/div[9]/div[2]/select/option[' + str(class_ipc) + ']'
        )
        class_ipc_input.click()
        time.sleep(10)
        print("class_ipc_input.click()")

        # Vernis
        # Vernis épargne
        vernis_epargne_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[5]/div[1]/div[2]/select/option[' + str(vernis_epargne) + ']'
        )
        vernis_epargne_input.click()
        time.sleep(10)
        print("vernis_epargne_input.click()")

        # Couleur du vernis
        couleur_du_vernis_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[5]/div[2]/div[2]/select/option[' + str(couleur_du_vernis) + ']'
        )
        couleur_du_vernis_input.click()
        time.sleep(10)
        print("couleur_du_vernis_input.click()")

        # Épargne pelable
        epargne_pelable_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[5]/div[3]/div[2]/select/option[' + str(epargne_pelable) + ']'
        )
        epargne_pelable_input.click()
        time.sleep(10)
        print("couleur_du_vernis_input.click()")

        # Marquage
        # Sérigraphie (encre)
        serigraphie_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[7]/div[1]/div[2]/select/option[' + str(serigraphie) + ']'
        )
        serigraphie_input.click()
        time.sleep(10)
        print("serigraphie_input.click()")

        # Marquage ROHS
        marquage_rohs_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[7]/div[3]/div[2]/select/option[' + str(marquage_rohs) + ']'
        )
        marquage_rohs_input.click()
        time.sleep(10)
        print("marquage_rohs_input.click()")

        # Marquage UL
        marquage_ul_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[7]/div[4]/div[2]/select/option[' + str(marquage_ul) + ']'
        )
        marquage_ul_input.click()
        time.sleep(10)
        print("marquage_ul_input.click()")

        # Marquage Date
        marquage_date_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[7]/div[5]/div[2]/select/option[' + str(marquage_date) + ']'
        )
        marquage_date_input.click()
        time.sleep(10)
        print("marquage_date_input.click()")

        # Options spécifiques
        # Espace entre pistes
        espace_entre_pistes_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[1]/div[2]/select/option[' + str(espace_entre_pistes) + ']'
        )
        espace_entre_pistes_input.click()
        time.sleep(10)
        print("espace_entre_pistes_input.click()")

        # Taille min. des perçages
        taille_minimale_des_percages_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[2]/div[2]/select/option[' + str(taille_minimale_des_percages) + ']'
        )
        taille_minimale_des_percages_input.click()
        time.sleep(10)
        print("taille_minimale_des_percages_input.click()")

        # Trous borgnes
        trous_borgnes_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[3]/div[2]/select/option[' + str(trous_borgnes) + ']'
        )
        trous_borgnes_input.click()
        time.sleep(10)
        print("trous_borgnes_input.click()")

        # Via croisé
        via_croise_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[4]/div[2]/select/option[' + str(via_croise) + ']'
        )
        via_croise_input.click()
        time.sleep(10)
        print("via_croise_input.click()")

        # Via enterré
        via_enterre_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[5]/div[2]/select/option[' + str(via_enterre) + ']'
        )
        via_enterre_input.click()
        time.sleep(10)
        print("via_enterre_input.click()")

        # Contrôle d'impédance
        controle_impedance_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[6]/div[2]/select/option[' + str(controle_impedance) + ']'
        )
        controle_impedance_input.click()
        time.sleep(10)
        print("controle_impedance_input.click()")

        # Métallisation tranche
        metallisation_tranche_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[7]/div[2]/select/option[' + str(metallisation_tranche) + ']'
        )
        metallisation_tranche_input.click()
        time.sleep(10)
        print("metallisation_tranche_input.click()")

        # Press-fit
        press_fit_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[8]/div[2]/select/option[' + str(press_fit) + ']'
        )
        press_fit_input.click()
        time.sleep(10)
        print("press_fit_input.click()")

        # Via Fill
        via_fill_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[10]/div[2]/select/option[' + str(via_fill) + ']'
        )
        via_fill_input.click()
        time.sleep(10)
        print("via_fill_input.click()")

        # Biseau
        biseau_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[11]/div[2]/select/option[' + str(biseau) + ']'
        )
        biseau_input.click()
        time.sleep(10)
        print("biseau_input.click()")

        # Trous fraisés
        trous_fraises_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[12]/div[2]/select/option[' + str(trous_fraises) + ']'
        )
        trous_fraises_input.click()
        time.sleep(10)
        print("trous_fraises_input.click()")

        # Coupe métallographique
        coupe_metallographique_input = browser.find_element_by_xpath(
            '/html/body/div[3]/div/form/div[9]/div[14]/div[2]/select/option[' + str(coupe_metallographique) + ']'
        )
        coupe_metallographique_input.click()
        time.sleep(10)
        print("coupe_metallographique_input.click()")

        # Click on the "Aller au choix des composants" button
        aller_au_choix_des_composants_button = browser.find_element_by_xpath(
            '//*[@id="btn-go-to-components"]'
        )
        aller_au_choix_des_composants_button.click()
        time.sleep(15)
        print("aller_au_choix_des_composants_button clicked")

        # Click on the "importer_une_bom_button" button
        importer_une_bom_button = browser.find_element_by_xpath(
            '//*[@id="btn-go-to-bom-import"]'
        )
        importer_une_bom_button.click()
        time.sleep(15)
        print("importer_une_bom_button clicked")

        # Click on the "Envoyer un fichier" button
        envoyer_un_fichier_button = browser.find_element_by_xpath(
            '//*[@id="file_upload"]'
        )
        envoyer_un_fichier_button.click()
        time.sleep(15)
        print("envoyer_un_fichier_button clicked")

        # Click on the "Parcourir" button
        parcourir_input = browser.find_element_by_xpath(
            '//*[@id="js_import_bom_file_input"]'
        )
        parcourir_input.send_keys("A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques\\"
                                  "EDA_Brevet_US_5_149_407_Water_Electrolyzer\\"
                                  "EDA_Brevet_US_5_149_407_Water_Electrolyzer.csv")
        time.sleep(15)
        print("parcourir_input file uploaded")

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")
        time.sleep(15)


if __name__ == '__main__':
    unittest.main()
