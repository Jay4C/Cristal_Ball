import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as dt
import os


class UnitTestsDepotsFondsCaisseDepotsConsignations(unittest.TestCase):
    def test_depots_fonds_caisse_depots_consignations_mercorus(self):
        packet = io.BytesIO()

        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFontSize(8)

        # Cocher la case (M)
        can.drawString(round(0.54 * 72), round(9.44 * 72), "X")

        # Insérer le nom et les prénoms
        can.drawString(round(1.57 * 72), round(9.47 * 72), "")

        # Cocher la case (Président)
        can.drawString(round(3.82 * 72), round(9.11 * 72), "X")

        # Insérer l'adresse personnelle à laquelle sera envoyée par courrier simple le récepissé de dépôt :
        can.drawString(round(0.7 * 72), round(8.52 * 72), " - Etage 1 Appartement 6 - 93800 Epinay-sur-Seine")

        # Insérer le numéro de téléphone (obligatoire)
        can.drawString(round(2.05 * 72), round(7.89 * 72), "")

        # Insérer l'adresse e-mail (obligatoire)
        can.drawString(round(2.22 * 72), round(7.6 * 72), "")

        # Insérer le nom de la société
        can.drawString(round(1.66 * 72), round(6.7 * 72), "MERCORUS")

        # Insérer l'adresse de la société
        can.drawString(round(1.89 * 72), round(6.38 * 72), "10 rue de Penthièvre 75008 Paris")

        # Insérer la Forme juridique
        can.drawString(round(1.6 * 72), round(6.1 * 72), "Société par actions simplifiée unipersonnelle à capital variable")

        # Insérer le Montant déposé
        can.drawString(round(1.62 * 72), round(5.78 * 72), "100,00 € (cent euros)")

        # Cocher la case (Président) pour "Je note que le récépissé de dépôt me sera adressé par courrier
        # (lettre simple) par la Caisse des Dépôts, en ma qualité de : "
        can.drawString(round(1.34 * 72), round(4.56 * 72), "X")

        # Insérer (A mon adresse suivante :)
        can.drawString(round(2.04 * 72), round(3.99 * 72), " - Etage 1 Appartement 6 - 93800 Epinay-sur-Seine")

        # Insérer (Fait à )
        can.drawString(round(1.4 * 72), round(2.68 * 72), "Epinay-sur-Seine (93800)")

        # Insérer (, le )
        can.drawString(round(5 * 72), round(2.68 * 72), dt.today().strftime('%d/%m/%Y'))

        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        # read your existing PDF
        existing_pdf = PdfFileReader(open("Depots_Fonds_CDC.pdf", "rb"))

        output = PdfFileWriter()

        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        # finally, write "output" to a real file
        output_file = "Mercorus\\Depots_Fonds_CDC_" + dt.today().strftime('%d_%m_%Y') + ".pdf"
        output_stream = open(output_file, "wb")
        output.write(output_stream)
        output_stream.close()

        try:
            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(output_file, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = round(4.64 * 72)

            y_coord = round(1.68 * 72)

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(output_file) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(x_coord) + "x" + str(y_coord) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))

    def test_dossier_depots_fonds_caisse_depots_consignations_mercorus(self):
        print("test_dossier_depots_fonds_caisse_depots_consignations_mercorus")

        output = PdfFileWriter()

        # Demande de dépôt conforme au modèle proposé
        demande_de_depot_conforme_au_modele_propose = "Mercorus\\Depots_Fonds_CDC_24_03_2021_signed.pdf"

        demande_de_depot_conforme_au_modele_propose_pdf = PdfFileReader(
            open(demande_de_depot_conforme_au_modele_propose, "rb"))

        for i in range(0, demande_de_depot_conforme_au_modele_propose_pdf.getNumPages()):
            output.addPage(demande_de_depot_conforme_au_modele_propose_pdf.getPage(i))

        # Justificatif de domicile actuel de moins de 3 mois
        justificatif_domicile_actuel_moins_3_mois = "A:\\2_Personnel\\2_Non_Recurrentes\\109_Justificatif_Adresse" \
                                                    "\\Justificatif_Adresse_Jason_ALOYAU.pdf"

        justificatif_domicile_actuel_moins_3_mois_pdf = PdfFileReader(
            open(justificatif_domicile_actuel_moins_3_mois, "rb"))

        for i in range(0, justificatif_domicile_actuel_moins_3_mois_pdf.getNumPages()):
            output.addPage(justificatif_domicile_actuel_moins_3_mois_pdf.getPage(i))

        # Projets de statuts complets datés de moins d'un an
        projets_statuts_complets_dates_de_moins_d_un_an = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives" \
                                                          "\\2_Outils_Numeriques\\Python__Flask__Cristal_Ball\\Test" \
                                                          "\\Service\\Archives\\Reporting\\Corporate_Reporting" \
                                                          "\\Statuts\\Mercorus" \
                                                          "\\Statuts_De_La_Societe_Mercorus_20_03_2021_signed.pdf"

        projets_statuts_complets_dates_de_moins_d_un_an_pdf = PdfFileReader(
            open(projets_statuts_complets_dates_de_moins_d_un_an, "rb"))
        
        for i in range(0, projets_statuts_complets_dates_de_moins_d_un_an_pdf.getNumPages()):
            output.addPage(projets_statuts_complets_dates_de_moins_d_un_an_pdf.getPage(i))

        # Pièces d’identité en cours de validité : photocopies recto verso et en couleur (passeport)
        piece_identite_valide_recto_verso_couleur = "A:\\2_Personnel\\2_Non_Recurrentes\\47_Mes_Identites" \
                                                    "\\Passeport_De_Jason_ALOYAU.pdf"

        piece_identite_valide_recto_verso_couleur_pdf = PdfFileReader(
            open(piece_identite_valide_recto_verso_couleur, "rb"))

        for i in range(0, piece_identite_valide_recto_verso_couleur_pdf.getNumPages()):
            output.addPage(piece_identite_valide_recto_verso_couleur_pdf.getPage(i))

        # Chèque(s) de banque et Justificatif(s) de délivrance d’un chèque de banque établi(s) par la banque émettrice
        cheque_banque = "A:\\1_Professionnel\\2_Mercorus_[En_cours_immatriculation]\\2_Archives\\1_Immatriculation" \
                        "\\1_Cheque_Banque_Depots_Capital\\Cheque_Banque_Depots_Capital.pdf"

        cheque_banque_pdf = PdfFileReader(open(cheque_banque, "rb"))

        for i in range(0, cheque_banque_pdf.getNumPages()):
            output.addPage(cheque_banque_pdf.getPage(i))

        justificatif_delivrance_cheque_banque = "A:\\1_Professionnel\\2_Mercorus_[En_cours_immatriculation]" \
                                                "\\2_Archives\\1_Immatriculation\\1_Cheque_Banque_Depots_Capital" \
                                                "\\Justificatif_Delivrance_Cheque_Banque.pdf"

        justificatif_delivrance_cheque_banque_pdf = PdfFileReader(open(justificatif_delivrance_cheque_banque, "rb"))

        for i in range(0, justificatif_delivrance_cheque_banque_pdf.getNumPages()):
            output.addPage(justificatif_delivrance_cheque_banque_pdf.getPage(i))

        # finally, write "output" to a real file
        output_stream = open("Mercorus\\Dossier_Depots_Fonds_CDC_" + dt.today().strftime('%d_%m_%Y') + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
