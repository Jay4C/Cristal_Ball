import unittest
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime as dt


class UnitTestsConstruction(unittest.TestCase):
    def test_permis_construire(self):
        print("test_permis_construire")

        output = PdfFileWriter()

        # Récépissé de dépôt d’une demande de permis de construire ou de permis d’aménager
        depot_demande_permis_construire = ""

        depot_demande_permis_construire_pdf = PdfFileReader(
            open(depot_demande_permis_construire, "rb")
        )

        for i in range(0, depot_demande_permis_construire_pdf.getNumPages()):
            output.addPage(depot_demande_permis_construire_pdf.getPage(i))

        # 1) Pièces obligatoires pour tous les dossiers :
        #
        # PC1 : Un plan de situation
        pc1_plan_de_situation = ""

        pc1_plan_de_situation_pdf = PdfFileReader(open(pc1_plan_de_situation, "rb"))

        for j in range(0, 6):
            for i in range(0, pc1_plan_de_situation_pdf.getNumPages()):
                output.addPage(pc1_plan_de_situation_pdf.getPage(i))

        # PC2 : Un plan de masse
        pc2_plan_de_masse = ""

        pc2_plan_de_masse_pdf = PdfFileReader(open(pc2_plan_de_masse, "rb"))

        for j in range(0, 6):
            for i in range(0, pc2_plan_de_masse_pdf.getNumPages()):
                output.addPage(pc2_plan_de_masse_pdf.getPage(i))

        # PC3 : Un plan en coupe
        pc3_plan_de_coupe = ""

        pc3_plan_de_coupe_pdf = PdfFileReader(open(pc3_plan_de_coupe, "rb"))

        for j in range(0, 6):
            for i in range(0, pc3_plan_de_coupe_pdf.getNumPages()):
                output.addPage(pc3_plan_de_coupe_pdf.getPage(i))

        # PC4 : Une notice
        pc4_notice = ""

        pc4_notice_pdf = PdfFileReader(open(pc4_notice, "rb"))

        for i in range(0, pc4_notice_pdf.getNumPages()):
            output.addPage(pc4_notice_pdf.getPage(i))

        # PC5 : Un plan des façades et des toitures
        pc5_plan_facades_toitures = ""

        pc5_plan_facades_toitures_pdf = PdfFileReader(open(pc5_plan_facades_toitures, "rb"))

        for i in range(0, pc5_plan_facades_toitures_pdf.getNumPages()):
            output.addPage(pc5_plan_facades_toitures_pdf.getPage(i))

        # PC6 : Un document graphique
        pc6_document_graphique = ""

        pc6_document_graphique_pdf = PdfFileReader(open(pc6_document_graphique, "rb"))

        for i in range(0, pc6_document_graphique_pdf.getNumPages()):
            output.addPage(pc6_document_graphique_pdf.getPage(i))

        # PC7 : Une photographie permettant de situer le terrain dans l’environnement proche
        pc7_photographie = ""

        pc7_photographie_pdf = PdfFileReader(open(pc7_photographie, "rb"))

        for i in range(0, pc7_photographie_pdf.getNumPages()):
            output.addPage(pc7_photographie_pdf.getPage(i))

        # PC8 : Une photographie permettant de situer le terrain dans le paysage lointain
        pc8_photographie = ""

        pc8_photographie_pdf = PdfFileReader(open(pc8_photographie, "rb"))

        for i in range(0, pc8_photographie_pdf.getNumPages()):
            output.addPage(pc8_photographie_pdf.getPage(i))

        # Si votre projet est soumis à l’obligation de réaliser une étude d’impact :
        #
        # PC11 : L’étude d’impact ou la décision de dispense d’une telle étude
        pc11_etude_impact = ""

        pc11_etude_impact_pdf = PdfFileReader(open(pc11_etude_impact, "rb"))

        for i in range(0, pc11_etude_impact_pdf.getNumPages()):
            output.addPage(pc11_etude_impact_pdf.getPage(i))

        # PC11-1 : L’étude d’impact actualisée ainsi que les avis de l’autorité environnementale, des collectivités
        # territoriales et leurs groupements intéressés par le projet
        pc11_1_etude_impact_actualisee = ""

        pc11_1_etude_impact_actualisee_pdf = PdfFileReader(open(pc11_1_etude_impact_actualisee, "rb"))

        for i in range(0, pc11_1_etude_impact_actualisee_pdf.getNumPages()):
            output.addPage(pc11_1_etude_impact_actualisee_pdf.getPage(i))

        # Si votre projet est susceptible d’affecter de manière significative un site Natura 2000 :
        #
        # PC11-2 : Le dossier d’évaluation des incidences prévu à l’art. R. 414-23 du code de l’environnement
        # ou l’étude d’impact en tenant lieu [Art. R. 431-16 c) du code de l’urbanisme]
        pc11_2_dossier_evaluation_incidences = ""

        pc11_2_dossier_evaluation_incidences_pdf = PdfFileReader(open(pc11_2_dossier_evaluation_incidences, "rb"))

        for i in range(0, pc11_2_dossier_evaluation_incidences_pdf.getNumPages()):
            output.addPage(pc11_2_dossier_evaluation_incidences_pdf.getPage(i))

        # Si votre projet est accompagné de la réalisation ou de la réhabilitation d’une installation d’assainissement
        # non collectif:
        #
        # PC11-3 : L’attestation de conformité du projet d’installation [Art. R. 431-16 d) du code de l’urbanisme]
        pc11_3_attestation_conformite_projet_installation = ""

        pc11_3_attestation_conformite_projet_installation_pdf = PdfFileReader(
            open(pc11_3_attestation_conformite_projet_installation, "rb")
        )

        for i in range(0, pc11_3_attestation_conformite_projet_installation_pdf.getNumPages()):
            output.addPage(pc11_3_attestation_conformite_projet_installation_pdf.getPage(i))

        # Si votre projet se situe dans une zone où un plan de prévention des risques impose la réalisation
        # d’une étude :
        #
        # PC13 : L’attestation de l’architecte ou de l’expert certifiant que l’étude a été réalisée et que le
        # projet la prend en compte [Art. R. 431-16 f) du code de l’urbanisme]
        pc13_attestation_architecte = ""

        pc13_attestation_architecte_pdf = PdfFileReader(
            open(pc13_attestation_architecte, "rb")
        )

        for i in range(0, pc13_attestation_architecte_pdf.getNumPages()):
            output.addPage(pc13_attestation_architecte_pdf.getPage(i))

        # Si votre projet nécessite un agrément :
        #
        # PC14 : La copie de l’agrément [Art. R. 431-16 g) du code de l’urbanisme]
        pc14_copie_agrement = ""

        pc14_copie_agrement_pdf = PdfFileReader(
            open(pc14_copie_agrement, "rb")
        )

        for i in range(0, pc14_copie_agrement_pdf.getNumPages()):
            output.addPage(pc14_copie_agrement_pdf.getPage(i))

        # Si votre projet se situe en commune littorale dans un espace remarquable ou dans un milieu à préserver :
        #
        # PC15. Une notice précisant l’activité économique qui doit être exercée dans le bâtiment [Art.
        # R. 431-16 h) du code de l’urbanisme]
        pc15_notice_activite_economique_batiment = ""

        pc15_notice_activite_economique_batiment_pdf = PdfFileReader(
            open(pc15_notice_activite_economique_batiment, "rb")
        )

        for i in range(0, pc15_notice_activite_economique_batiment_pdf.getNumPages()):
            output.addPage(pc15_notice_activite_economique_batiment_pdf.getPage(i))

        # Si votre projet nécessite une étude de sécurité publique :
        #
        # PC16 : L’étude de sécurité [Art. R. 431-16 i) du code de l’urbanisme]
        pc16_etude_securite = ""

        pc16_etude_securite_pdf = PdfFileReader(
            open(pc16_etude_securite, "rb")
        )

        for i in range(0, pc16_etude_securite_pdf.getNumPages()):
            output.addPage(pc16_etude_securite_pdf.getPage(i))

        # Si votre projet est tenu de respecter la réglementation thermique :
        #
        # PC16-1 : Le formulaire attestant la prise en compte de la réglementation thermique et, le cas
        # échéant, la réalisation de l’étude de faisabilité relative aux approvisionnements en énergie,
        # prévu par les articles R. 111-20-1 et R. 111-20-2 du code de la construction et de l’habitation
        # [Art. R. 431-16 j) du code de l’urbanisme]
        pc16_1_formulaire_reglementation_thermique = ""

        pc16_1_formulaire_reglementation_thermique_pdf = PdfFileReader(
            open(pc16_1_formulaire_reglementation_thermique, "rb")
        )

        for i in range(0, pc16_1_formulaire_reglementation_thermique_pdf.getNumPages()):
            output.addPage(pc16_1_formulaire_reglementation_thermique_pdf.getPage(i))

        # Si votre projet est situé à proximité d’une canalisation de transport dans une zone de dangers :
        #
        # PC16-2 : L’analyse de compatibilité du projet avec la canalisation du point de vue de la sécurité
        # des personnes, prévue à l’art. R. 555-31 du code de l’environnement [Art. R. 431-16 k) du code
        # de l’urbanisme]
        pc16_2_analyse_compatibilite_projet_canalisation_securite_personnes = ""

        pc16_2_analyse_compatibilite_projet_canalisation_securite_personnes_pdf = PdfFileReader(
            open(pc16_2_analyse_compatibilite_projet_canalisation_securite_personnes, "rb")
        )

        for i in range(0, pc16_2_analyse_compatibilite_projet_canalisation_securite_personnes_pdf.getNumPages()):
            output.addPage(pc16_2_analyse_compatibilite_projet_canalisation_securite_personnes_pdf.getPage(i))

        # Si votre projet fait l’objet d’une concertation :
        #
        # PC16-4 : Le bilan de la concertation et le document conclusif [Art. R. 431-16 m) du code de
        # l’urbanisme]
        pc16_4_bilan_concertation_document_conclusif = ""

        pc16_4_bilan_concertation_document_conclusif_pdf = PdfFileReader(
            open(pc16_4_bilan_concertation_document_conclusif, "rb")
        )

        for i in range(0, pc16_4_bilan_concertation_document_conclusif_pdf.getNumPages()):
            output.addPage(pc16_4_bilan_concertation_document_conclusif_pdf.getPage(i))

        # Si votre projet se situe sur un terrain ayant accueilli une installation classée mise à l’arrêt définitif
        # et régulièrement réhabilitée pour permettre l’usage défini dans les conditions prévues aux articles
        # L. 512-6-1, L. 512-7-6 et L. 512-12-1 du code de l’environnement, et lorsqu’un usage différent est envisagé:
        #
        # PC16-5 : Une attestation établie par un bureau d’études certifié dans le domaine des sites et
        # sols pollués, ou équivalent, garantissant que les mesures de gestion de la pollution au regard
        # du nouvel usage du terrain projeté ont été prise en compte dans la conception du projet. [Art.
        # R. 431-16 n) du code de l’urbanisme]
        pc16_5_attestation_bureau_etudes_n = ""

        pc16_5_attestation_bureau_etudes_n_pdf = PdfFileReader(
            open(pc16_5_attestation_bureau_etudes_n, "rb")
        )

        for i in range(0, pc16_5_attestation_bureau_etudes_n_pdf.getNumPages()):
            output.addPage(pc16_5_attestation_bureau_etudes_n_pdf.getPage(i))

        # Si votre projet se situe dans un secteur d’information sur les sols, et si la construction projetée
        # n’est pas dans le périmètre
        # d’un lotissement autorisé ayant déjà fait l’objet d’une demande comportant une attestation garantissant
        # la réalisation
        # d’une étude des sols :
        #
        # PC16-6 : Une attestation établie par un bureau d’études certifié dans le domaine des sites et
        # sols pollués, ou équivalent, garantissant que les mesures de gestion de la pollution au regard
        # du nouvel usage du terrain projeté ont été prise en compte dans la conception du projet. [Art.
        # R.431-16 o) du code de l’urbanisme]
        pc16_6_attestation_bureau_etudes_o = ""

        pc16_6_attestation_bureau_etudes_o_pdf = PdfFileReader(
            open(pc16_6_attestation_bureau_etudes_o, "rb")
        )

        for i in range(0, pc16_6_attestation_bureau_etudes_o_pdf.getNumPages()):
            output.addPage(pc16_6_attestation_bureau_etudes_o_pdf.getPage(i))

        # Si votre projet déroge à certaines règles de construction et met en œuvre une solution d’effet équivalent :
        #
        # PC 16-7 : L’attestation montrant le caractère équivalent des résultats obtenus par les moyens
        # mis en œuvre, ainsi que leur caractère innovant [Art. 5 de l’ordonnance n° 2018-937 du 30
        # octobre 2018 visant à faciliter la réalisation de projets de construction et à favoriser l’innovation]
        pc16_7_attestation_caractere_equivalent_resultats = ""

        pc16_7_attestation_caractere_equivalent_resultats_pdf = PdfFileReader(
            open(pc16_7_attestation_caractere_equivalent_resultats, "rb")
        )

        for i in range(0, pc16_7_attestation_caractere_equivalent_resultats_pdf.getNumPages()):
            output.addPage(pc16_7_attestation_caractere_equivalent_resultats_pdf.getPage(i))

        # Si votre projet nécessite un défrichement :
        #
        # PC24 : La copie de la lettre du préfet qui vous fait savoir que votre demande d’autorisation
        # de défrichement est complète, si le défrichement est ou non soumis à reconnaissance de la
        # situation et de l’état des terrains et si la demande doit ou non faire l’objet d’une enquête publique
        # [Art. R. 431-19 du code de l’urbanisme]
        pc24_copie_lettre_prefet_autorisation_defrichement = ""

        pc24_copie_lettre_prefet_autorisation_defrichement_pdf = PdfFileReader(
            open(pc24_copie_lettre_prefet_autorisation_defrichement, "rb")
        )

        for i in range(0, pc24_copie_lettre_prefet_autorisation_defrichement_pdf.getNumPages()):
            output.addPage(pc24_copie_lettre_prefet_autorisation_defrichement_pdf.getPage(i))

        # Si votre projet porte sur une installation classée pour la protection de l’environnement :
        #
        # PC25 : Une justification du dépôt de la demande d’enregistrement ou de déclaration au titre
        # de la législation relative aux Installations Classées pour la Protection de l’Environnement [Art.
        # R. 431-20 du code de l’urbanisme]
        pc25_justification_depot_demande_icpe = ""

        pc25_justification_depot_demande_icpe_pdf = PdfFileReader(
            open(pc25_justification_depot_demande_icpe, "rb")
        )

        for i in range(0, pc25_justification_depot_demande_icpe_pdf.getNumPages()):
            output.addPage(pc25_justification_depot_demande_icpe_pdf.getPage(i))

        # Si le terrain ne peut comporter les emplacements de stationnement imposés par le document d’urbanisme :
        #
        # PC34 : Le plan de situation du terrain sur lequel sont réalisées les aires de stationnement
        # et le plan des constructions et aménagements correspondants [Art. R. 431-26 a) du code de
        # l’urbanisme]
        pc34_plan_situation_terrainaires_stationnement = ""

        pc34_plan_situation_terrainaires_stationnement_pdf = PdfFileReader(
            open(pc34_plan_situation_terrainaires_stationnement, "rb")
        )

        for i in range(0, pc34_plan_situation_terrainaires_stationnement_pdf.getNumPages()):
            output.addPage(pc34_plan_situation_terrainaires_stationnement_pdf.getPage(i))

        # ou
        # PC35. La promesse synallagmatique de concession ou d’acquisition [Art. R. 431-26 b) du
        # code de l’urbanisme]
        pc35_promesse_synallagmatique_concession_ou_acquisition = ""

        pc35_promesse_synallagmatique_concession_ou_acquisition_pdf = PdfFileReader(
            open(pc35_promesse_synallagmatique_concession_ou_acquisition, "rb")
        )

        for i in range(0, pc35_promesse_synallagmatique_concession_ou_acquisition_pdf.getNumPages()):
            output.addPage(pc35_promesse_synallagmatique_concession_ou_acquisition_pdf.getPage(i))

        # Si vous demandez une ou plusieurs dérogations aux règles constructives au titre de l’article L. 151-29-1,
        # L. 152-5 et L. 152-6 du code de l’urbanisme :
        #
        # PC40-3 : Une note précisant la nature de la ou des dérogations demandées justifiant du respect
        # des objectifs et des conditions fixées aux articles L . 151-29-1, L. 152-5 et L. 152-6 du code de
        # l’urbanisme pour chacune des dérogations demandées. [Art. R. 431-31-2 du code de l’urbanisme]
        pc40_3_note_nature_derogations = ""

        pc40_3_note_nature_derogations_pdf = PdfFileReader(
            open(pc40_3_note_nature_derogations, "rb")
        )

        for i in range(0, pc40_3_note_nature_derogations_pdf.getNumPages()):
            output.addPage(pc40_3_note_nature_derogations_pdf.getPage(i))

        # Finally, write "output" to a real file
        output_stream = open("Permis_Construire\\depot_permis_construire_"
                             + dt.today().strftime('%d_%m_%Y')
                             + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_icpe_declaration(self):
        print("test_icpe_declaration")

        output = PdfFileWriter()

        # Les coordonnées du déclarant
        coordonnees_declarant = ""

        coordonnees_declarant_pdf = PdfFileReader(open(coordonnees_declarant, "rb"))

        for i in range(0, coordonnees_declarant_pdf.getNumPages()):
            output.addPage(coordonnees_declarant_pdf.getPage(i))

        # L’emplacement sur lequel l’installation doit être réalisée
        emplacement_installation = ""

        emplacement_installation_pdf = PdfFileReader(open(emplacement_installation, "rb"))

        for i in range(0, emplacement_installation_pdf.getNumPages()):
            output.addPage(emplacement_installation_pdf.getPage(i))

        # Plan d’ensemble
        plan_ensemble = ""

        plan_ensemble_pdf = PdfFileReader(open(plan_ensemble, "rb"))

        for i in range(0, plan_ensemble_pdf.getNumPages()):
            output.addPage(plan_ensemble_pdf.getPage(i))

        # Plan cadastral
        plan_cadastral = ""

        plan_cadastral_pdf = PdfFileReader(open(plan_cadastral, "rb"))

        for i in range(0, plan_cadastral_pdf.getNumPages()):
            output.addPage(plan_cadastral_pdf.getPage(i))

        # La nature et le volume des activités que le déclarant se propose d'exercer ainsi que la ou les rubriques de
        # la nomenclature dans lesquelles l'installation doit être rangée
        nature_volume_activites = ""

        nature_volume_activites_pdf = PdfFileReader(open(nature_volume_activites, "rb"))

        for i in range(0, nature_volume_activites_pdf.getNumPages()):
            output.addPage(nature_volume_activites_pdf.getPage(i))

        # Une présentation générale du mode et des conditions d'utilisation, d'épuration et d'évacuation des eaux
        # résiduaires et des émanations de toute nature ainsi que de gestion des déchets de l'exploitation sont
        # précisés ;
        presentation_generale_mode_gestion_dechets = ""

        presentation_generale_mode_gestion_dechets_pdf = PdfFileReader(open(presentation_generale_mode_gestion_dechets,
                                                                            "rb"))

        for i in range(0, presentation_generale_mode_gestion_dechets_pdf.getNumPages()):
            output.addPage(presentation_generale_mode_gestion_dechets_pdf.getPage(i))

        # Une présentation générale des dispositions prévues en cas de sinistre
        presentation_generale_dispositions_sinistre = ""

        presentation_generale_dispositions_sinistre_pdf = PdfFileReader(
            open(presentation_generale_dispositions_sinistre, "rb"))

        for i in range(0, presentation_generale_dispositions_sinistre_pdf.getNumPages()):
            output.addPage(presentation_generale_dispositions_sinistre_pdf.getPage(i))

        # Un dossier d’évaluation des incidences Natura 2000, si l’installation figure sur les listes mentionnées au
        # III de l’article L.414-4 du code de l’environnement.
        dossier_evaluation_incidences_natura_2000 = ""

        dossier_evaluation_incidences_natura_2000_pdf = PdfFileReader(open(dossier_evaluation_incidences_natura_2000,
                                                                           "rb"))

        for i in range(0, dossier_evaluation_incidences_natura_2000_pdf.getNumPages()):
            output.addPage(dossier_evaluation_incidences_natura_2000_pdf.getPage(i))

        # En référence à l’article L.512-8 du code de l’environnement, la déclaration inclut les installations,
        # ouvrages, travaux et activités (dits « IOTA ») relevant du II de l'article L. 214-3 (soit IOATA relevant
        # de la déclaration) projetés par le pétitionnaire que leur connexité rend nécessaires à l'installation classée
        # ou dont la proximité est de nature à en modifier notablement les dangers ou inconvénients.
        iota = ""

        iota_pdf = PdfFileReader(open(iota, "rb"))

        for i in range(0, iota_pdf.getNumPages()):
            output.addPage(iota_pdf.getPage(i))

        # Déclaration initiale d'une installation classée relevant du régime de la déclaration.
        declaration_initiale_icpe_regime_declaration = ""

        declaration_initiale_icpe_regime_declaration_pdf = PdfFileReader(
            open(declaration_initiale_icpe_regime_declaration, "rb")
        )

        for i in range(0, declaration_initiale_icpe_regime_declaration_pdf.getNumPages()):
            output.addPage(declaration_initiale_icpe_regime_declaration_pdf.getPage(i))

        # Finally, write "output" to a real file
        output_stream = open("ICPE\\depot_declaration_initiale_icpe_declaration_"
                             + dt.today().strftime('%d_%m_%Y')
                             + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()

    def test_grtgaz_expression_besoin(self):
        print("test_grtgaz_expression_besoin")

        output = PdfFileWriter()

        # Un plan de situation à l’échelle adaptée, une vue aérienne (plan type Google map), etc. …
        # pour localiser l’implantation du site envisagé.
        plan_situation = ""

        plan_situation_pdf = PdfFileReader(open(plan_situation, "rb"))

        for i in range(0, plan_situation_pdf.getNumPages()):
            output.addPage(plan_situation_pdf.getPage(i))

        # Schéma du process du projet
        schema_process_projet = ""

        schema_process_projet_pdf = PdfFileReader(open(schema_process_projet, "rb"))

        for i in range(0, schema_process_projet_pdf.getNumPages()):
            output.addPage(schema_process_projet_pdf.getPage(i))

        # Schéma des installations du projet
        schema_installations_projet = ""

        schema_installations_projet_pdf = PdfFileReader(open(schema_installations_projet, "rb"))

        for i in range(0, schema_installations_projet_pdf.getNumPages()):
            output.addPage(schema_installations_projet_pdf.getPage(i))

        # Expression du besoin
        expression_du_besoin = ""

        expression_du_besoin_pdf = PdfFileReader(open(expression_du_besoin, "rb"))

        for i in range(0, expression_du_besoin_pdf.getNumPages()):
            output.addPage(expression_du_besoin_pdf.getPage(i))

        # Finally, write "output" to a real file
        output_stream = open("Grtgaz\\depot_expression_besoin_"
                             + dt.today().strftime('%d_%m_%Y')
                             + ".pdf", "wb")
        output.write(output_stream)
        output_stream.close()


if __name__ == '__main__':
    unittest.main()
