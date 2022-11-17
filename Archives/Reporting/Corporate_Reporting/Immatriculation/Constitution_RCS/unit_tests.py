import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime as dt


class UnitTestsConstitutionRCS(unittest.TestCase):
    # ok
    def test_constitution_rcs_mercorus(self):
        print("test_constitution_rcs_mercorus")

        output = PdfFileWriter()

        # Cheque de banque
        cheque_banque = "A:\\1_Professionnel\\2_Mercorus_[En_cours_immatriculation]\\2_Archives\\1_Immatriculation" \
                        "\\2_Cheque_Banque_RCS\\Cheque_Banque_RCS.pdf"

        cheque_banque_pdf = PdfFileReader(open(cheque_banque, "rb"))

        for i in range(0, cheque_banque_pdf.getNumPages()):
            output.addPage(cheque_banque_pdf.getPage(i))

        # Attestation de délivrance de cheque de banque
        justificatif_delivrance_cheque_banque = "A:\\1_Professionnel\\2_Mercorus_[En_cours_immatriculation]" \
                                                "\\2_Archives\\1_Immatriculation\\2_Cheque_Banque_RCS" \
                                                "\\Justificatif_Delivrance_Cheque_Banque_RCS.pdf"

        justificatif_delivrance_cheque_banque_pdf = PdfFileReader(open(justificatif_delivrance_cheque_banque, "rb"))

        for i in range(0, justificatif_delivrance_cheque_banque_pdf.getNumPages()):
            output.addPage(justificatif_delivrance_cheque_banque_pdf.getPage(i))

        # Formulaire M0 SAS Cerfa 13959
        formulaire_m0_sas_cerfa_13959 = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                                        "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                                        "\\Corporate_Reporting\\E_Cerfa\\Entreprise\\13959\\Mercorus" \
                                        "\\Cerfa_13959_25_03_2021.pdf"

        formulaire_m0_sas_cerfa_13959_pdf = PdfFileReader(
            open(formulaire_m0_sas_cerfa_13959, "rb"))

        for i in range(0, formulaire_m0_sas_cerfa_13959_pdf.getNumPages()):
            output.addPage(formulaire_m0_sas_cerfa_13959_pdf.getPage(i))

        # Déclaration de non condamnation et de filiation
        declaration_non_condamnation_filiation = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                                                 "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                                                 "\\Corporate_Reporting\\Declaration_Non_Condamnation\\Mercorus" \
                                                 "\\Declaration_Non_Condamnation_23_03_2021_signed.pdf"

        declaration_non_condamnation_filiation_pdf = PdfFileReader(
            open(declaration_non_condamnation_filiation, "rb"))

        for i in range(0, declaration_non_condamnation_filiation_pdf.getNumPages()):
            output.addPage(declaration_non_condamnation_filiation_pdf.getPage(i))

        # Pièce d'identité
        piece_identite_valide_recto_verso_couleur = "A:\\2_Personnel\\2_Non_Recurrentes\\47_Mes_Identites" \
                                                    "\\Passeport_De_Jason_ALOYAU.pdf"

        piece_identite_valide_recto_verso_couleur_pdf = PdfFileReader(
            open(piece_identite_valide_recto_verso_couleur, "rb"))

        for i in range(0, piece_identite_valide_recto_verso_couleur_pdf.getNumPages()):
            output.addPage(piece_identite_valide_recto_verso_couleur_pdf.getPage(i))

        # Copie du contrat de domiciliation
        copie_contrat_domiciliation = "A:\\1_Professionnel\\2_Mercorus_[En_cours_immatriculation]\\2_Archives" \
                                      "\\1_Immatriculation\\3_Contrat_Domiciliation\\Contrat_Domiciliation_Mercorus.pdf"

        copie_contrat_domiciliation_pdf = PdfFileReader(
            open(copie_contrat_domiciliation, "rb"))

        for i in range(0, copie_contrat_domiciliation_pdf.getNumPages()):
            output.addPage(copie_contrat_domiciliation_pdf.getPage(i))

        # Liste des souscripteurs
        liste_des_souscripteurs = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                                  "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                                  "\\Corporate_Reporting\\Liste_Souscripteurs\\Mercorus" \
                                  "\\Liste_Souscripteurs_24_03_2021_signed.pdf"

        liste_des_souscripteurs_pdf = PdfFileReader(
            open(liste_des_souscripteurs, "rb"))

        for i in range(0, liste_des_souscripteurs_pdf.getNumPages()):
            output.addPage(liste_des_souscripteurs_pdf.getPage(i))

        # Déclaration des bénéficiaires effectifs
        declaration_beneficiaires_effectifs = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                                              "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                                              "\\Corporate_Reporting\\Declaration_Beneficiaires_Effectifs\\Mercorus" \
                                              "\\Declaration_Beneficiaires_Effectifs_24_03_2021_signed.pdf"

        declaration_beneficiaires_effectifs_pdf = PdfFileReader(
            open(declaration_beneficiaires_effectifs, "rb"))

        for i in range(0, declaration_beneficiaires_effectifs_pdf.getNumPages()):
            output.addPage(declaration_beneficiaires_effectifs_pdf.getPage(i))

        # Justificatif d'adresse
        justificatif_domicile_actuel_moins_3_mois = "A:\\2_Personnel\\2_Non_Recurrentes\\109_Justificatif_Adresse" \
                                                    "\\Justificatif_Adresse_Jason_ALOYAU.pdf"

        justificatif_domicile_actuel_moins_3_mois_pdf = PdfFileReader(
            open(justificatif_domicile_actuel_moins_3_mois, "rb"))

        for i in range(0, justificatif_domicile_actuel_moins_3_mois_pdf.getNumPages()):
            output.addPage(justificatif_domicile_actuel_moins_3_mois_pdf.getPage(i))

        # Attestation d'annonce légale
        attestation_annonce_legale = "A:\\1_Professionnel\\2_Mercorus_[En_cours_immatriculation]\\2_Archives" \
                                     "\\1_Immatriculation\\4_Attestation_Annonce_Legale" \
                                     "\\Attestation_Parution_Auvergnat_Paris_Mercorus.pdf"

        attestation_annonce_legale_pdf = PdfFileReader(
            open(attestation_annonce_legale, "rb"))

        for i in range(0, attestation_annonce_legale_pdf.getNumPages()):
            output.addPage(attestation_annonce_legale_pdf.getPage(i))

        # Etat des actes accomplis
        etat_actes_accomplis = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                               "\\Python__Flask__Cristal_Ball\\Test\\Service\\Archives\\Reporting" \
                               "\\Corporate_Reporting\\Etat_Actes_Accomplis\\Mercorus" \
                               "\\Etat_Actes_Accomplis_Mercorus_25_03_2021_signed.pdf"

        etat_actes_accomplis_pdf = PdfFileReader(
            open(etat_actes_accomplis, "rb"))

        for i in range(0, etat_actes_accomplis_pdf.getNumPages()):
            output.addPage(etat_actes_accomplis_pdf.getPage(i))

        # Récépissé de dépôt de capital social
        recepisse_de_depot_de_capiatl_social = "A:\\1_Professionnel\\2_Mercorus_[En_cours_immatriculation]" \
                                               "\\2_Archives\\1_Immatriculation\\5_Recepisse_Depot_Capital_Social" \
                                               "\\Recepisse_Depot_Caisse_Depots_Mercorus.pdf"

        recepisse_de_depot_de_capiatl_social_pdf = PdfFileReader(
            open(recepisse_de_depot_de_capiatl_social, "rb"))

        for i in range(0, recepisse_de_depot_de_capiatl_social_pdf.getNumPages()):
            output.addPage(recepisse_de_depot_de_capiatl_social_pdf.getPage(i))

        # Copie des statuts
        projets_statuts_complets_dates_de_moins_d_un_an = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives" \
                                                          "\\2_Outils_Numeriques\\Python__Flask__Cristal_Ball\\Test" \
                                                          "\\Service\\Archives\\Reporting\\Corporate_Reporting" \
                                                          "\\Statuts\\Mercorus" \
                                                          "\\Statuts_De_La_Societe_Mercorus_20_03_2021_signed.pdf"

        projets_statuts_complets_dates_de_moins_d_un_an_pdf = PdfFileReader(
            open(projets_statuts_complets_dates_de_moins_d_un_an, "rb"))

        for i in range(0, projets_statuts_complets_dates_de_moins_d_un_an_pdf.getNumPages()):
            output.addPage(projets_statuts_complets_dates_de_moins_d_un_an_pdf.getPage(i))

        # finally, write "output" to a real file
        output_stream = open("Mercorus\\Constitution_RCS_Mercorus_" + dt.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
