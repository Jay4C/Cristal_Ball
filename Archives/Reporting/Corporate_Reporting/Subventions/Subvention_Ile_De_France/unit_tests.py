import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime as dt


class UnitTestsSubventionIleDeFrance(unittest.TestCase):
    def test_subvention_ile_de_france(self):
        print("test_subvention_ile_de_france")

        output = PdfFileWriter()

        # Extrait kbis de moins de 3 mois
        extrait_kbis_moins_trois_mois = ""

        extrait_kbis_moins_trois_mois_pdf = PdfFileReader(open(extrait_kbis_moins_trois_mois, "rb"))

        for i in range(0, extrait_kbis_moins_trois_mois_pdf.getNumPages()):
            output.addPage(extrait_kbis_moins_trois_mois_pdf.getPage(i))

        # Liasses fiscales complètes (bilan, compte de résultat , annexe ) des 3 derniers exercices*
        liasses_fiscale_completes_trois_derniers_exercices = ""

        liasses_fiscale_completes_trois_derniers_exercices_pdf = PdfFileReader(
            open(liasses_fiscale_completes_trois_derniers_exercices, "rb"))

        for i in range(0, liasses_fiscale_completes_trois_derniers_exercices_pdf.getNumPages()):
            output.addPage(liasses_fiscale_completes_trois_derniers_exercices_pdf.getPage(i))

        # Composition du groupe
        composition_du_groupe = ""

        composition_du_groupe_pdf = PdfFileReader(open(composition_du_groupe, "rb"))

        for i in range(0, composition_du_groupe_pdf.getNumPages()):
            output.addPage(composition_du_groupe_pdf.getPage(i))

        # Fichier de données financières de l’entreprise
        fichier_de_donnees_financieres_entreprise = ""

        fichier_de_donnees_financieres_entreprise_pdf = PdfFileReader(open(fichier_de_donnees_financieres_entreprise, "rb"))

        for i in range(0, fichier_de_donnees_financieres_entreprise_pdf.getNumPages()):
            output.addPage(fichier_de_donnees_financieres_entreprise_pdf.getPage(i))

        # Organigramme actuel de l’entreprise
        organigramme_actuel_entreprise = ""

        organigramme_actuel_entreprise_pdf = PdfFileReader(open(organigramme_actuel_entreprise, "rb"))

        for i in range(0, organigramme_actuel_entreprise_pdf.getNumPages()):
            output.addPage(organigramme_actuel_entreprise_pdf.getPage(i))

        # Organigramme actuel de l’entreprise à N+3
        organigramme_actuel_entreprise_n_plus_trois = ""

        organigramme_actuel_entreprise_n_plus_trois_pdf = PdfFileReader(open(organigramme_actuel_entreprise_n_plus_trois, "rb"))

        for i in range(0, organigramme_actuel_entreprise_n_plus_trois_pdf.getNumPages()):
            output.addPage(organigramme_actuel_entreprise_n_plus_trois_pdf.getPage(i))

        # Plan de développement sur 36 mois
        plan_developpement_trente_six_mois = ""

        plan_developpement_trente_six_mois_pdf = PdfFileReader(open(plan_developpement_trente_six_mois, "rb"))

        for i in range(0, plan_developpement_trente_six_mois_pdf.getNumPages()):
            output.addPage(plan_developpement_trente_six_mois_pdf.getPage(i))

        # Devis
        devis = ""

        devis_pdf = PdfFileReader(open(devis, "rb"))

        for i in range(0, devis_pdf.getNumPages()):
            output.addPage(devis_pdf.getPage(i))

        # Déclaration des aides perçues et à venir *
        declaration_des_aides_percues_et_a_venir = ""

        declaration_des_aides_percues_et_a_venir_pdf = PdfFileReader(open(declaration_des_aides_percues_et_a_venir, "rb"))

        for i in range(0, declaration_des_aides_percues_et_a_venir_pdf.getNumPages()):
            output.addPage(declaration_des_aides_percues_et_a_venir_pdf.getPage(i))

        # Lettre d’engagements
        lettre_engagements = ""

        lettre_engagements_pdf = PdfFileReader(open(lettre_engagements, "rb"))

        for i in range(0, lettre_engagements_pdf.getNumPages()):
            output.addPage(lettre_engagements_pdf.getPage(i))

        # Charte régionale des valeurs de la République et de la laïcité, datée, signée et tamponnée*
        charte_regionale_valeurs_republique_laicite_datee_signee_tamponnee = ""

        charte_regionale_valeurs_republique_laicite_datee_signee_tamponnee_pdf = \
            PdfFileReader(open(charte_regionale_valeurs_republique_laicite_datee_signee_tamponnee, "rb"))

        for i in range(0, charte_regionale_valeurs_republique_laicite_datee_signee_tamponnee_pdf.getNumPages()):
            output.addPage(charte_regionale_valeurs_republique_laicite_datee_signee_tamponnee_pdf.getPage(i))

        # Plan d’affaires
        plan_affaires = ""

        plan_affaires_pdf = PdfFileReader(open(plan_affaires, "rb"))

        for i in range(0, plan_affaires_pdf.getNumPages()):
            output.addPage(plan_affaires_pdf.getPage(i))

        # Etudes de marché
        etudes_de_marche = ""

        etudes_de_marche_pdf = PdfFileReader(open(etudes_de_marche, "rb"))

        for i in range(0, etudes_de_marche_pdf.getNumPages()):
            output.addPage(etudes_de_marche_pdf.getPage(i))

        # Présentation du projet
        presentation_du_projet = ""

        presentation_du_projet_pdf = PdfFileReader(open(presentation_du_projet, "rb"))

        for i in range(0, presentation_du_projet_pdf.getNumPages()):
            output.addPage(presentation_du_projet_pdf.getPage(i))

        # Dossier technique
        dossier_technique = ""

        dossier_technique_pdf = PdfFileReader(open(dossier_technique, "rb"))

        for i in range(0, dossier_technique_pdf.getNumPages()):
            output.addPage(dossier_technique_pdf.getPage(i))

        # finally, write "output" to a real file
        output_stream = open("S_I_D_L\\demande_de_subvention_" + dt.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
