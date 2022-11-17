import unittest
import os.path


class DSN(unittest.TestCase):
    def test_dsn_sans_individu_avec_president_avec_valeur(self):
        print("test_dsn_sans_individu_avec_president_avec_valeur")

        file = "../dsn_sans_individu.dsn"

        if os.path.exists(file):
            print('oui')
            os.remove(file)
        else:
            print('non')

        try:
            with open("../dsn_sans_individu.dsn", mode='a', encoding='latin-1') as f:
                # bloc S10.G00.00 - Envoi (1,1)
                f.write("S10.G00.00.001,'Logiciel maison'\n")  # Nom du logiciel utilisé / S10.G00.00.001 / 1
                f.write("S10.G00.00.002,'Logiciel maison'\n")  # Nom de l'éditeur / S10.G00.00.002 / 2
                f.write("S10.G00.00.003,'1'\n")  # Numéro de version du logiciel utilisé / S10.G00.00.003 / 3
                # f.write("S10.G00.00.004,'néant'\n")  # Code de conformité en pré-contrôle / S10.G00.00.004 / 4
                f.write("S10.G00.00.005,'02'\n")  # Code envoi du fichier d'essai ou réel / S10.G00.00.005 / 5
                f.write("S10.G00.00.006,'P20V01'\n")  # Numéro de version de la norme utilisée / S10.G00.00.006 / 6
                f.write("S10.G00.00.007,'01'\n")  # Point de dépôt / S10.G00.00.007 / 7
                f.write("S10.G00.00.008,'02'\n")  # Type de l'envoi / S10.G00.00.008 / 8

                # bloc S10.G00.01 - Emetteur (1,1)
                f.write("S10.G00.01.001,''\n")  # Siren de l'émetteur de l'envoi / S10.G00.01.001 / 9
                f.write("S10.G00.01.002,'00014'\n")  # Nic de l'émetteur de l'envoi / S10.G00.01.002 / 10
                f.write("S10.G00.01.003,''\n")  # Nom ou raison sociale de l'émetteur / S10.G00.01.003 / 11
                f.write("S10.G00.01.004,''\n")  # Numéro, extension, nature et libellé de la voie / S10.G00.01.004 / 12
                f.write("S10.G00.01.005,''\n")  # Code postal / S10.G00.01.005 / 13
                f.write("S10.G00.01.006,''\n")  # Localité / S10.G00.01.006 / 14
                # f.write("S10.G00.01.007,''\n")  # Code pays / S10.G00.01.007 / 15
                # f.write("S10.G00.01.008,''\n")  # Code de distribution à l'étranger / S10.G00.01.008 / 16
                f.write("S10.G00.01.009,''\n")  # Complément de la localisation de la construction / S10.G00.01.009 / 17
                # f.write("S10.G00.01.010,'néant'\n")  # Service de distribution, complément de localisation de la voie S10.G00.01.010 / 18

                # bloc S10.G00.02 - Contact Emetteur (1,1)
                f.write("S10.G00.02.001,'01'\n")  # Code civilité / S10.G00.02.001 / 19
                f.write("S10.G00.02.002,''\n")  # Nom et prénom de la personne à contacter S10.G00.02.002 / 20
                f.write("S10.G00.02.004,''\n")  # Adresse mél du contact émetteur S10.G00.02.004 / 21
                f.write("S10.G00.02.005,''\n")  # Adresse téléphonique S10.G00.02.005 / 22
                # f.write("S10.G00.02.006,'0000000000'\n")  # Adresse fax S10.G00.02.006 / 23

                # bloc S20.G00.05 - Déclaration
                f.write("S20.G00.05.001,'01'\n")  # Nature de la déclaration S20.G00.05.001 / 24
                f.write("S20.G00.05.002,'02'\n")  # Type de la déclaration S20.G00.05.002 / 25
                f.write("S20.G00.05.003,'11'\n")  # Numéro de fraction de déclaration S20.G00.05.003 / 26
                f.write("S20.G00.05.004,'0'\n")  # Numéro d'ordre de la déclaration S20.G00.05.004 / 27
                f.write("S20.G00.05.005,'01052020'\n")  # Date du mois principal déclaré S20.G00.05.005 / 28
                # f.write("S20.G00.05.006,'000000000'\n")  # Identifiant de la déclaration annulée ou remplacée S20.G00.05.006
                f.write("S20.G00.05.007,'12062020'\n")  # Date de constitution du fichier S20.G00.05.007 / 29
                f.write("S20.G00.05.008,'01'\n")  # Champ de la déclaration S20.G00.05.008 / 30
                f.write("S20.G00.05.009,'ROME M1301'\n")  # Identifiant métier S20.G00.05.009 / 31
                f.write("S20.G00.05.010,'01'\n")  # Devise de la déclaration S20.G00.05.010 / 32
                # f.write("S20.G00.05.011,''\n")  # Nature de l’événement déclencheur du signalement S20.G00.05.011

                # bloc S20.G00.07 - Contact chez le déclaré (0,*)
                f.write("S20.G00.07.001,''\n")  # Nom et prénom du contact S20.G00.07.001 / 33
                f.write("S20.G00.07.002,''\n")  # Adresse téléphonique S20.G00.07.002 / 34
                f.write("S20.G00.07.003,''\n")  # Adresse mél du contact S20.G00.07.003 / 35
                f.write("S20.G00.07.004,'07'\n")  # Type S20.G00.07.004 / 36

                # bloc S20.G00.08 - Identifiant de l’organisme destinataire de la déclaration « Absence de rattachement pour le mois principal déclaré » (0,*)
                f.write("S20.G00.08.001,'88'\n")  # Code caisse S20.G00.08.001 / 37

                # bloc S21.G00.06 - Entreprise (1,1)
                f.write("S21.G00.06.001,'883632556'\n")  # SIREN S21.G00.06.001 / 38
                f.write("S21.G00.06.002,'00014'\n")  # NIC du siège S21.G00.06.002 / 39
                f.write("S21.G00.06.003,'4675Z'\n")  # Code APEN S21.G00.06.003 / 40
                f.write("S21.G00.06.004,'31 Avenue de Segur'\n")  # Numéro, extension, nature et libellé de la voie S21.G00.06.004 / 41
                f.write("S21.G00.06.005,'75007'\n")  # Code postal S21.G00.06.005 / 42
                f.write("S21.G00.06.006,'Paris'\n")  # Localité S21.G00.06.006 / 43
                f.write("S21.G00.06.007,'ABC LIV Segur'\n")  # Complément de la localisation de la construction S21.G00.06.007 / 44
                # f.write("S21.G00.06.008,'néant'\n")  # Service de distribution, complément de localisation de la voie S21.G00.06.008 / 45
                f.write("S21.G00.06.009,'1'\n")  # Effectif moyen de l'entreprise au 31 décembre S21.G00.06.009 / 46
                # f.write("S21.G00.06.010,'FR'\n")  # Code pays S21.G00.06.010 / 47
                # f.write("S21.G00.06.011,'néant'\n")  # Code de distribution à l'étranger S21.G00.06.011 / 48
                # f.write("S21.G00.06.012,'01'\n")  # Implantation de l'entreprise S21.G00.06.012 / 49

                # bloc S21.G00.11 - Etablissement (1,1)
                f.write("S21.G00.11.001,'00014'\n")  # NIC S21.G00.11.001 / 50
                f.write("S21.G00.11.002,'4675Z'\n")  # Code APET S21.G00.11.002 / 51
                f.write("S21.G00.11.003,'31 Avenue de Segur'\n")  # Numéro, extension, nature et libellé de la voie S21.G00.11.003 / 52
                f.write("S21.G00.11.004,'75007'\n")  # Code postal S21.G00.11.004 / 53
                f.write("S21.G00.11.005,'Paris'\n")  # Localité S21.G00.11.005 / 54
                f.write("S21.G00.11.006,'ABC LIV Segur'\n")  # Complément de la localisation de la construction S21.G00.11.006 / 55
                # f.write("S21.G00.11.007,'néant'\n")  # Service de distribution, complément de localisation de la voie S21.G00.11.007 / 56
                f.write("S21.G00.11.008,'1'\n")  # Effectif de fin de période déclarée de l'établissement S21.G00.11.008 / 57
                f.write("S21.G00.11.009,'01'\n")  # Type de rémunération soumise à contributions d'Assurance chômage pour expatriés S21.G00.11.009 / 58
                # f.write("S21.G00.11.015,'FR'\n")  # Code pays S21.G00.11.015 / 59
                # f.write("S21.G00.11.016,'néant'\n")  # Code de distribution à l'étranger S21.G00.11.016 / 60
                f.write("S21.G00.11.017,'01'\n")  # Nature juridique de l'employeur S21.G00.11.017 / 61
                #f.write("S21.G00.11.019,'30062020'\n")  # Date d'effet de l'adhésion au dispositif TESE/CEA S21.G00.11.019 / 62
                #f.write("S21.G00.11.020,'30062020'\n")  # Date d'effet de la sortie du dispositif TESE/CEA S21.G00.11.020 / 63

                # bloc S21.G00.15 - Adhésion Prévoyance (0,*)
                # f.write("S21.G00.15.001,'néant'\n")  # Référence du contrat de Prévoyance S21.G00.15.001 / 64
                # f.write("S21.G00.15.002,'P0012'\n")  # Code organisme de Prévoyance S21.G00.15.002 / 65
                # f.write("S21.G00.15.003,''\n")  # Code délégataire de gestion S21.G00.15.003 / 66
                # f.write("S21.G00.15.004,'02'\n")  # Personnel couvert S21.G00.15.004 / 67
                # f.write("S21.G00.15.005,'néant'\n")  # Identifiant technique Adhésion S21.G00.15.005 / 68

                # bloc S21.G00.16 - Changements destinataire Adhésion Prévoyance (0,*)
                # f.write("S21.G00.16.001,'31052020'\n")  # Date de la modification S21.G00.16.001 / 69
                # f.write("S21.G00.16.002,'néant'\n")  # Ancien Code organisme de Prévoyance S21.G00.16.002 / 70
                # f.write("S21.G00.16.003,'néant'\n")  # Ancien Code délégataire de gestion S21.G00.16.003 / 71

                # bloc S21.G00.20 - Versement organisme de protection sociale (0,*)
                # f.write("S21.G00.20.001,''\n")  # Identifiant Organisme de Protection Sociale S21.G00.20.001 / 72
                # f.write("S21.G00.20.002,''\n")  # Entité d'affectation des opérations S21.G00.20.002 / 73
                # f.write("S21.G00.20.003,''\n")  # BIC S21.G00.20.003 / 74
                # f.write("S21.G00.20.004,''\n")  # IBAN S21.G00.20.004 / 75
                # f.write("S21.G00.20.005,'00.00'\n")  # Montant du versement S21.G00.20.005 / 76
                # f.write("S21.G00.20.006,''\n")  # Date de début de période de rattachement S21.G00.20.006 / 77
                # f.write("S21.G00.20.007,''\n")  # Date de fin de période de rattachement S21.G00.20.007 / 78
                # f.write("S21.G00.20.008,'néant'\n")  # Code délégataire de gestion S21.G00.20.008 / 79
                # f.write("S21.G00.20.010,'05'\n")  # Mode de paiement S21.G00.20.010 / 80
                # f.write("S21.G00.20.011,'16062020'\n")  # Date de paiement S21.G00.20.011 / 81
                # f.write("S21.G00.20.012,'88363255600014'\n")  # SIRET Payeur S21.G00.20.012 / 82

                # bloc S21.G00.22 - Bordereau de cotisation due (0,*)
                # f.write("S21.G00.22.001,''\n")  # Identifiant Organisme de Protection Sociale S21.G00.22.001 / 83
                # f.write("S21.G00.22.002,''\n")  # Entité d'affectation des opérations S21.G00.22.002 / 84
                # f.write("S21.G00.22.003,'26052020'\n")  # Date de début de période de rattachement S21.G00.22.003 / 85
                # f.write("S21.G00.22.004,'31052020'\n")  # Date de fin de période de rattachement S21.G00.22.004 / 86
                # f.write("S21.G00.22.005,'00.00'\n")  # Montant total de cotisations S21.G00.22.005 / 87

                # bloc S21.G00.23 - Cotisation agrégée (0,*)
                # f.write("S21.G00.23.001,'100'\n")  # Code de cotisation S21.G00.23.001 / 88
                # f.write("S21.G00.23.002,'921'\n")  # Qualifiant d'assiette S21.G00.23.002 / 89
                # f.write("S21.G00.23.003,'00.00'\n")  # Taux de cotisation S21.G00.23.003 / 90
                # f.write("S21.G00.23.004,'00.00'\n")  # Montant d'assiette S21.G00.23.004 / 91
                # f.write("S21.G00.23.005,'00.00'\n")  # Montant de cotisation S21.G00.23.005 / 92
                # f.write("S21.G00.23.006,'75107'\n")  # Code INSEE commune S21.G00.23.006 / 93

                # bloc S21.G00.30 - Individu (0,*)
                # f.write("S21.G00.30.001,''\n")  # Numéro d'inscription au répertoire S21.G00.30.001 / 94
                # f.write("S21.G00.30.002,''\n")  # Nom de famille S21.G00.30.002 / 95
                # f.write("S21.G00.30.003,''\n")  # Nom d'usage S21.G00.30.003 / 96
                # f.write("S21.G00.30.004,''\n")  # Prénoms S21.G00.30.004 / 97
                # f.write("S21.G00.30.005,'01'\n")  # Sexe S21.G00.30.005 / 98
                # f.write("S21.G00.30.006,''\n")  # Date de naissance S21.G00.30.006 / 99
                # f.write("S21.G00.30.007,''\n")  # Lieu de naissance S21.G00.30.007 / 100
                # f.write("S21.G00.30.008,''\n")  # Numéro, extension, nature et libellé de la voie S21.G00.30.008 / 101
                # f.write("S21.G00.30.009,''\n")  # Code postal S21.G00.30.009 / 102
                # f.write("S21.G00.30.010,''\n")  # Localité S21.G00.30.010 / 103
                # f.write("S21.G00.30.011,'FR'\n")  # Code pays S21.G00.30.011 / 104
                # f.write("S21.G00.30.012,'néant'\n")  # Code de distribution à l'étranger S21.G00.30.012 / 105
                # f.write("S21.G00.30.013,'01'\n")  # Codification UE S21.G00.30.013 / 106
                # f.write("S21.G00.30.014,'98'\n")  # Code département de naissance S21.G00.30.014 / 107
                # f.write("S21.G00.30.015,'FR'\n")  # Code pays de naissance S21.G00.30.015 / 108
                # f.write("S21.G00.30.016,'Etage 1 - Appartement 6 - Digicode 15B25'\n")  # Complément de la localisation de la construction S21.G00.30.016 / 109
                # f.write("S21.G00.30.017,'néant'\n")  # Service de distribution, complément de localisation de la voie S21.G00.30.017 / 110
                # f.write("S21.G00.30.018,''\n")  # Adresse mél S21.G00.30.018 / 111
                # f.write("S21.G00.30.019,'1'\n")  # Matricule de l'individu dans l'entreprise S21.G00.30.019 / 112
                # f.write("S21.G00.30.020,'néant'\n")  # Numéro technique temporaire S21.G00.30.020 / 113
                # f.write("S21.G00.30.021,'0'\n")  # Nombre d'enfants à charge S21.G00.30.021 / 114
                # f.write("S21.G00.30.022,'néant'\n")  # Statut à l'étranger au sens fiscal S21.G00.30.022 / 115
                # f.write("S21.G00.30.023,'01'\n")  # Cumul emploi retraite S21.G00.30.023 / 116
                # f.write("S21.G00.30.024,'07'\n")  # Niveau de formation le plus élevé obtenu par l'individu S21.G00.30.024 / 117

                # bloc S21.G00.31 - Changements Individu (0,*)
                # f.write("S21.G00.31.001,'néant'\n")  # Date de la modification S21.G00.31.001 / 118
                # f.write("S21.G00.31.008,'néant'\n")  # Ancien NIR S21.G00.31.008 / 119
                # f.write("S21.G00.31.009,'néant'\n")  # Ancien Nom de famille S21.G00.31.009 / 120
                # f.write("S21.G00.31.010,'néant'\n")  # Anciens Prénoms S21.G00.31.010 / 121
                # f.write("S21.G00.31.011,'néant'\n")  # Ancienne Date de naissance S21.G00.31.011 / 122

                # bloc S21.G00.34 - Pénibilité (0,*)
                # f.write("S21.G00.34.001,'99'\n")  # Facteur d'exposition S21.G00.34.001 / 123
                # f.write("S21.G00.34.002,'néant'\n")  # Numéro du contrat S21.G00.34.002 / 124
                # f.write("S21.G00.34.003,'2020'\n")  # Année de rattachement S21.G00.34.003 / 125

                # bloc S21.G00.40 - Contrat (contrat de travail, convention, mandat) (1,*)
                # f.write("S21.G00.40.001,'26052020'\n")  # Date de début du contrat S21.G00.40.001 / 126
                # f.write("S21.G00.40.002,'03'\n")  # Statut du salarié (conventionnel) S21.G00.40.002 / 127
                # f.write("S21.G00.40.003,'01'\n")  # Code statut catégoriel Retraite Complémentaire obligatoire S21.G00.40.003 / 128
                # f.write("S21.G00.40.004,'233c'\n")  # Code profession et catégorie socioprofessionnelle (PCS-ESE) S21.G00.40.004 / 129
                # f.write("S21.G00.40.005,'06'\n")  # Code complément PCS-ESE (pour la fonction publique : référentiels NEH, NET et grade de la NNE) S21.G00.40.005 / 130
                # f.write("S21.G00.40.006,'Président'\n")  # Libellé de l'emploi S21.G00.40.006 / 131
                # f.write("S21.G00.40.007,'80'\n")  # Nature du contrat S21.G00.40.007 / 132
                # f.write("S21.G00.40.008,'99'\n")  # Dispositif de politique publique et conventionnel S21.G00.40.008 / 133
                # f.write("S21.G00.40.009,'néant'\n")  # Numéro du contrat S21.G00.40.009 / 134
                # f.write("S21.G00.40.010,'néant'\n")  # Date de fin prévisionnelle du contrat S21.G00.40.010 / 135
                # f.write("S21.G00.40.011,'99'\n")  # Unité de mesure de la quotité de travail S21.G00.40.011 / 136
                # f.write("S21.G00.40.012,'néant'\n")  # Quotité de travail de référence de l'entreprise pour la catégorie de salarié S21.G00.40.012 / 137
                # f.write("S21.G00.40.013,'néant'\n")  # Quotité de travail du contrat S21.G00.40.013 / 138
                # f.write("S21.G00.40.014,'99'\n")  # Modalité d'exercice du temps de travail S21.G00.40.014 / 139
                # f.write("S21.G00.40.016,'99'\n")  # Complément de base au régime obligatoire S21.G00.40.016 / 140
                # f.write("S21.G00.40.017,'9999'\n")  # Code convention collective applicable S21.G00.40.017 / 141
                # f.write("S21.G00.40.018,'200'\n")  # Code régime de base risque maladie S21.G00.40.018 / 142
                # f.write("S21.G00.40.019,''\n")  # Identifiant du lieu de travail S21.G00.40.019 / 143
                # f.write("S21.G00.40.020,'200'\n")  # Code régime de base risque vieillesse S21.G00.40.020 / 144
                # f.write("S21.G00.40.021,'néant'\n")  # Motif de recours S21.G00.40.021 / 145
                # f.write("S21.G00.40.022,'néant'\n")  # Code caisse professionnelle de congés payés S21.G00.40.022 / 146
                # f.write("S21.G00.40.023,'néant'\n")  # Taux de déduction forfaitaire spécifique pour frais professionnels S21.G00.40.023 / 147
                # f.write("S21.G00.40.024,'99'\n")  # Travailleur à l'étranger au sens du code de la Sécurité Sociale S21.G00.40.024 / 148
                # f.write("S21.G00.40.025,'néant'\n")  # Motif d'exclusion DSN S21.G00.40.025 / 149
                # f.write("S21.G00.40.026,'99'\n")  # Statut d'emploi du salarié S21.G00.40.026 / 150
                # f.write("S21.G00.40.027,'néant'\n")  # Code affectation Assurance chômage S21.G00.40.027 / 151
                # f.write("S21.G00.40.028,'néant'\n")  # Numéro interne employeur public S21.G00.40.028 / 152
                # f.write("S21.G00.40.029,'néant'\n")  # Type de gestion de l’Assurance chômage S21.G00.40.029 / 153
                # f.write("S21.G00.40.030,'néant'\n")  # Date d'adhésion S21.G00.40.030 / 154
                # f.write("S21.G00.40.031,''\n")  # Date de dénonciation S21.G00.40.031
                # f.write("S21.G00.40.032,'néant'\n")  # Date d’effet de la convention de gestion S21.G00.40.032 / 155
                # f.write("S21.G00.40.033,'néant'\n")  # Numéro de convention de gestion S21.G00.40.033 / 156
                # f.write("S21.G00.40.035,'505'\n")  # Code délégataire du risque maladie S21.G00.40.035 / 157
                # f.write("S21.G00.40.036,'01'\n")  # Code emplois multiples S21.G00.40.036 / 158
                # f.write("S21.G00.40.037,'01'\n")  # Code employeurs multiples S21.G00.40.037 / 159
                # f.write("S21.G00.40.038,'néant'\n")  # Code métier S21.G00.40.038 / 160
                # f.write("S21.G00.40.039,'200'\n")  # Code régime de base risque accident du travail S21.G00.40.039 / 161
                # f.write("S21.G00.40.040,'999ZZ'\n")  # Code risque accident du travail S21.G00.40.040 / 162
                # f.write("S21.G00.40.041,'néant'\n")  # Positionnement dans la convention collective S21.G00.40.041 / 163
                # f.write("S21.G00.40.042,'01'\n")  # Code statut catégoriel APECITA S21.G00.40.042 / 164
                # f.write("S21.G00.40.043,'néant'\n")  # Taux de cotisation accident du travail S21.G00.40.043 / 165
                # f.write("S21.G00.40.044,'néant'\n")  # Salarié à temps partiel cotisant à temps plein S21.G00.40.044 / 166
                # f.write("S21.G00.40.045,'néant'\n")  # Rémunération au pourboire S21.G00.40.045 / 167
                # f.write("S21.G00.40.046,''\n")  # Identifiant de l’établissement utilisateur S21.G00.40.046 / 168
                # f.write("S21.G00.40.048,'néant'\n")  # Numéro de label « Prestataire de services du spectacle vivant » S21.G00.40.048 / 169
                # f.write("S21.G00.40.049,'néant'\n")  # Numéro de licence entrepreneur spectacle S21.G00.40.049 / 170
                # f.write("S21.G00.40.050,'néant'\n")  # Numéro objet spectacle S21.G00.40.050 / 171
                # f.write("S21.G00.40.051,'néant'\n")  # Statut organisateur spectacle S21.G00.40.051 / 172
                # f.write("S21.G00.40.052,'0000'\n")  # [FP] Code complément PCS-ESE pour la fonction publique d'Etat (emploi de la NNE) S21.G00.40.052 / 173
                # f.write("S21.G00.40.053,'néant'\n")  # [FP] Nature du poste S21.G00.40.053 / 174
                # f.write("S21.G00.40.054,'néant'\n")  # [FP] Quotité de travail de référence de l'entreprise pour la catégorie de salarié dans l’hypothèse d’un poste à temps complet S21.G00.40.054 / 175
                # f.write("S21.G00.40.055,'néant'\n")  # Taux de travail à temps partiel S21.G00.40.055 / 176
                # f.write("S21.G00.40.056,'néant'\n")  # Code catégorie de service S21.G00.40.056 / 177
                # f.write("S21.G00.40.057,'néant'\n")  # [FP] Indice brut S21.G00.40.057 / 178
                # f.write("S21.G00.40.058,'néant'\n")  # [FP] Indice majoré S21.G00.40.058 / 179
                # f.write("S21.G00.40.059,'néant'\n")  # [FP] Nouvelle bonification indiciaire (NBI) S21.G00.40.059 / 180
                # f.write("S21.G00.40.060,'néant'\n")  # [FP] Indice brut d'origine S21.G00.40.060 / 181
                # f.write("S21.G00.40.061,'néant'\n")  # [FP] Indice brut de cotisation dans un emploi supérieur (article 15) S21.G00.40.061 / 182
                # f.write("S21.G00.40.062,'néant'\n")  # [FP] Ancien employeur public S21.G00.40.062 / 183
                # f.write("S21.G00.40.063,'néant'\n")  # [FP] Indice brut d’origine ancien salarié employeur public S21.G00.40.063 / 184
                # f.write("S21.G00.40.064,'néant'\n")  # [FP] Indice brut d’origine sapeur-pompier professionnel (SPP) S21.G00.40.064 / 185
                # f.write("S21.G00.40.065,'néant'\n")  # [FP] Maintien du traitement d'origine d'un contractuel titulaire S21.G00.40.065 / 186
                # f.write("S21.G00.40.066,'néant'\n")  # [FP] Type de détachement S21.G00.40.066 / 187
                # f.write("S21.G00.40.067,'néant'\n")  # Genre de navigation S21.G00.40.067 / 188
                # f.write("S21.G00.40.068,'néant'\n")  # Taux de service actif S21.G00.40.068 / 189
                # f.write("S21.G00.40.069,'néant'\n")  # Niveau de Rémunération S21.G00.40.069 / 190
                # f.write("S21.G00.40.070,'néant'\n")  # Echelon S21.G00.40.070 / 191
                # f.write("S21.G00.40.071,'néant'\n")  # Coefficient hiérarchique S21.G00.40.071 / 192
                # f.write("S21.G00.40.072,'néant'\n")  # Statut BOETH S21.G00.40.072 / 193
                # f.write("S21.G00.40.073,'99'\n")  # Complément de dispositif de politique publique S21.G00.40.073 / 194
                # f.write("S21.G00.40.074,'néant'\n")  # Cas de mise à disposition externe d'un individu de l'établissement S21.G00.40.074 / 195
                # f.write("S21.G00.40.075,'néant'\n")  # Catégorie de classement finale S21.G00.40.075 / 196
                # f.write("S21.G00.40.076,'néant'\n")  # Identifiant du contrat d'engagement maritime S21.G00.40.076 / 197
                # f.write("S21.G00.40.077,'néant'\n")  # Collège (CNIEG) S21.G00.40.077 / 198
                # f.write("S21.G00.40.078,'néant'\n")  # Forme d'aménagement du temps de travail dans le cadre de l'activité partielle S21.G00.40.078 / 199

                # bloc S21.G00.41 - Changements Contrat (0,*)
                # f.write("S21.G00.41.001,'néant'\n")  # Date de la modification S21.G00.41.001 / 200
                # f.write("S21.G00.41.002,'néant'\n")  # Ancien Statut du salarié (conventionnel) S21.G00.41.002 / 201
                # f.write("S21.G00.41.003,'néant'\n")  # Ancien Code statut catégoriel Retraite Complémentaire obligatoire S21.G00.41.003 / 202
                # f.write("S21.G00.41.004,'néant'\n")  # Ancienne Nature du contrat S21.G00.41.004 / 203
                # f.write("S21.G00.41.005,'néant'\n")  # Ancien dispositif de politique publique et conventionnel S21.G00.41.005 / 204
                # f.write("S21.G00.41.006,'néant'\n")  # Ancienne Unité de mesure de la quotité de travail S21.G00.41.006 / 205
                # f.write("S21.G00.41.007,'néant'\n")  # Ancienne Quotité de travail du contrat S21.G00.41.007 / 206
                # f.write("S21.G00.41.008,'néant'\n")  # Ancienne Modalité d'exercice du temps de travail S21.G00.41.008 / 207
                # f.write("S21.G00.41.010,'néant'\n")  # Ancien Complément de base au régime obligatoire S21.G00.41.010 / 208
                # f.write("S21.G00.41.011,'néant'\n")  # Ancien Code convention collective applicable S21.G00.41.011 / 209
                # f.write("S21.G00.41.012,'néant'\n")  # SIRET ancien établissement d'affectation S21.G00.41.012 / 210
                # f.write("S21.G00.41.013,'néant'\n")  # Ancien Identifiant du lieu de travail S21.G00.41.013 / 211
                # f.write("S21.G00.41.014,'néant'\n")  # Ancien Numéro du contrat S21.G00.41.014 / 212
                # f.write("S21.G00.41.016,'néant'\n")  # Ancien Motif de recours S21.G00.41.016 / 213
                # f.write("S21.G00.41.017,'néant'\n")  # Ancien Taux de déduction forfaitaire spécifique pour frais professionnels S21.G00.41.017 / 214
                # f.write("S21.G00.41.018,'néant'\n")  # Ancien Travailleur à l'étranger au sens du code de la Sécurité Sociale S21.G00.41.018 / 215
                # f.write("S21.G00.41.019,'néant'\n")  # Ancien Code profession et catégorie socioprofessionnelle (PCS-ESE) S21.G00.41.019 / 216
                # f.write("S21.G00.41.020,'néant'\n")  # Ancien Code complément PCS-ESE (pour la fonction publique : référentiels NEH, NET et grade de la NNE) S21.G00.41.020 / 217
                # f.write("S21.G00.41.021,'néant'\n")  # Ancienne Date de début du contrat S21.G00.41.021 / 218
                # f.write("S21.G00.41.022,'néant'\n")  # Ancienne Quotité de travail de référence de l'entreprise pour la catégorie de salarié S21.G00.41.022 / 219
                # f.write("S21.G00.41.023,'néant'\n")  # Ancien Code caisse professionnelle de congés payés S21.G00.41.023 / 220
                # f.write("S21.G00.41.024,'néant'\n")  # Ancien Code risque accident du travail S21.G00.41.024 / 221
                # f.write("S21.G00.41.025,'néant'\n")  # Ancien Code statut catégoriel APECITA S21.G00.41.025 / 222
                # f.write("S21.G00.41.027,'néant'\n")  # Ancien Salarié à temps partiel cotisant à temps plein S21.G00.41.027 / 223
                # f.write("S21.G00.41.028,'néant'\n")  # Profondeur de recalcul de la paie S21.G00.41.028 / 224
                # f.write("S21.G00.41.029,'néant'\n")  # [FP] Ancien Code complément PCS-ESE pour la fonction publique d'Etat (emploi de la NNE) S21.G00.41.029 / 225
                # f.write("S21.G00.41.030,'néant'\n")  # [FP] Ancienne Nature du poste S21.G00.41.030 / 226
                # f.write("S21.G00.41.031,'néant'\n")  # [FP] Ancienne Quotité de travail de référence de l'entreprise pour la catégorie de salarié dans l’hypothèse d’un poste à temps complet S21.G00.41.031 / 227
                # f.write("S21.G00.41.032,'néant'\n")  # Ancien Taux de travail à temps partiel S21.G00.41.032 / 228
                # f.write("S21.G00.41.033,'néant'\n")  # Ancien Code catégorie de service S21.G00.41.033 / 229
                # f.write("S21.G00.41.034,'néant'\n")  # [FP] Ancien Indice brut S21.G00.41.034 / 230
                # f.write("S21.G00.41.035,'néant'\n")  # [FP] Ancien Indice majoré S21.G00.41.035 / 231
                # f.write("S21.G00.41.036,'néant'\n")  # [FP] Ancienne Nouvelle bonification indiciaire (NBI) S21.G00.41.036 / 232
                # f.write("S21.G00.41.037,'néant'\n")  # [FP] Ancien indice brut d'origine S21.G00.41.037 / 233
                # f.write("S21.G00.41.038,'néant'\n")  # [FP] Ancien indice brut de cotisation dans un emploi supérieur (article 15) S21.G00.41.038 / 234
                # f.write("S21.G00.41.039,'néant'\n")  # [FP] Ancien ancien employeur public S21.G00.41.039 / 235
                # f.write("S21.G00.41.040,'néant'\n")  # [FP] Ancien Indice brut d’origine ancien salarié employeur public S21.G00.41.040 / 236
                # f.write("S21.G00.41.041,'néant'\n")  # [FP] Ancien indice brut d’origine sapeur-pompier professionnel (SPP) S21.G00.41.041 / 237
                # f.write("S21.G00.41.042,'néant'\n")  # [FP] Ancien maintien du traitement d'origine d'un contractuel titulaire S21.G00.41.042 / 238
                # f.write("S21.G00.41.043,'néant'\n")  # Ancien taux de service actif S21.G00.41.043 / 239
                # f.write("S21.G00.41.044,'néant'\n")  # Ancien niveau de Rémunération S21.G00.41.044 / 240
                # f.write("S21.G00.41.045,'néant'\n")  # Ancien échelon S21.G00.41.045 / 241
                # f.write("S21.G00.41.046,'néant'\n")  # Ancien coefficient hiérarchique S21.G00.41.046 / 242
                # f.write("S21.G00.41.047,'néant'\n")  # Ancien genre de navigation S21.G00.41.047 / 243
                # f.write("S21.G00.41.048,'néant'\n")  # Ancien statut BOETH S21.G00.41.048 / 244
                # f.write("S21.G00.41.049,'néant'\n")  # Ancien complément de dispositif de politique publique S21.G00.41.049 / 245
                # f.write("S21.G00.41.050,'néant'\n")  # Ancien cas de mise à disposition externe d'un individu de l'établissement S21.G00.41.050 / 246
                # f.write("S21.G00.41.051,'néant'\n")  # Ancienne catégorie de classement finale S21.G00.41.051 / 247
                # f.write("S21.G00.41.052,'néant'\n")  # Ancien code régime de base risque maladie S21.G00.41.052 / 248
                # f.write("S21.G00.41.053,'néant'\n")  # Ancien code régime de base risque vieillesse S21.G00.41.053 / 249
                # f.write("S21.G00.41.054,'néant'\n")  # Ancien identifiant du contrat d'engagement maritime S21.G00.41.054 / 250
                # f.write("S21.G00.41.055,'néant'\n")  # Ancien collège (CNIEG) S21.G00.41.055 / 251
                # f.write("S21.G00.41.056,'néant'\n")  # Ancienne forme d'aménagement du temps de travail dans le cadre de l'activité partielle S21.G00.41.056 / 252
                # f.write("S21.G00.41.057,'néant'\n")  # [FP] Ancien type de détachement S21.G00.41.057 / 253

                # bloc S21.G00.44 - Assujettissement fiscal (0,*)
                # f.write("S21.G00.44.001,'002'\n")  # Code taxe S21.G00.44.001 / 254
                # f.write("S21.G00.44.002,'00.00'\n")  # Montant S21.G00.44.002 / 255
                # f.write("S21.G00.44.003,'néant'\n")  # Millésime de rattachement S21.G00.44.003 / 256

                # bloc S21.G00.50 - Versement individu (1,*)
                # f.write("S21.G00.50.001,'néant'\n")  # Date de versement S21.G00.50.001 / 257
                # f.write("S21.G00.50.002,'00.00'\n")  # Rémunération nette fiscale S21.G00.50.002 / 258
                # f.write("S21.G00.50.003,'néant'\n")  # Numéro de versement S21.G00.50.003 / 259
                # f.write("S21.G00.50.004,'00.00'\n")  # Montant net versé S21.G00.50.004 / 260
                # f.write("S21.G00.50.006,'00.00'\n")  # Taux de prélèvement à la source S21.G00.50.006 / 261
                # f.write("S21.G00.50.007,'01'\n")  # Type du taux de prélèvement à la source S21.G00.50.007 / 262
                # f.write("S21.G00.50.008,'néant'\n")  # Identifiant du taux de prélèvement à la source S21.G00.50.008 / 263
                # f.write("S21.G00.50.009,'00.00'\n")  # Montant de prélèvement à la source S21.G00.50.009 / 264
                # f.write("S21.G00.50.011,'00.00'\n")  # Montant de la part non imposable du revenu S21.G00.50.011 / 265
                # f.write("S21.G00.50.012,'00.00'\n")  # Montant de l’abattement sur la base fiscale (non déduit de la rémunération nette fiscale) S21.G00.50.012 / 266
                # f.write("S21.G00.50.013,'00.00'\n")  # Montant soumis au PAS S21.G00.50.013 / 267

                # bloc S21.G00.51 - Rémunération (1,*)
                # f.write("S21.G00.51.001,'26052020'\n")  # Date de début de période de paie S21.G00.51.001 / 268
                # f.write("S21.G00.51.002,'31052020'\n")  # Date de fin de période de paie S21.G00.51.002 / 269
                # f.write("S21.G00.51.010,'néant'\n")  # Numéro du contrat S21.G00.51.010 / 270
                # f.write("S21.G00.51.011,'001'\n")  # Type S21.G00.51.011 / 271
                # f.write("S21.G00.51.012,'14.00'\n")  # Nombre d'heures S21.G00.51.012 / 272
                # f.write("S21.G00.51.013,'00.00'\n")  # Montant S21.G00.51.013 / 273
                # f.write("S21.G00.51.014,'néant'\n")  # [FP] Taux de rémunération de la position statutaire S21.G00.51.014 / 274
                # f.write("S21.G00.51.015,'néant'\n")  # Taux de conduite centrale nucléaire S21.G00.51.015 / 275
                # f.write("S21.G00.51.016,'néant'\n")  # Taux de majoration résidentielle S21.G00.51.016 / 276

                # bloc S21.G00.52 - Prime, gratification et indemnité (0,*)
                # f.write("S21.G00.52.001,'néant'\n")  # Type S21.G00.52.001 / 277
                # f.write("S21.G00.52.002,'00.00'\n")  # Montant S21.G00.52.002 / 278
                # f.write("S21.G00.52.003,'néant'\n")  # Date de début de la période de rattachement S21.G00.52.003 / 279
                # f.write("S21.G00.52.004,'néant'\n")  # Date de fin de la période de rattachement S21.G00.52.004 / 280
                # f.write("S21.G00.52.006,'néant'\n")  # Numéro du contrat S21.G00.52.006 / 281
                # f.write("S21.G00.52.007,'néant'\n")  # Date de versement d'origine S21.G00.52.007 / 282

                # bloc S21.G00.53 - Activité (0,*)
                # f.write("S21.G00.53.001,'01'\n")  # Type S21.G00.53.001 / 283
                # f.write("S21.G00.53.002,'3250.00'\n")  # Mesure S21.G00.53.002 / 284
                # f.write("S21.G00.53.003,'10'\n")  # Unité de mesure S21.G00.53.003 / 285

                # bloc S21.G00.54 - Autre élément de revenu brut (0,*)
                # f.write("S21.G00.54.001,'néant'\n")  # Type S21.G00.54.001 / 286
                # f.write("S21.G00.54.002,'00.00'\n")  # Montant S21.G00.54.002 / 287
                # f.write("S21.G00.54.003,'néant'\n")  # Date de début de période de rattachement S21.G00.54.003 / 288
                # f.write("S21.G00.54.004,'néant'\n")  # Date de fin de période de rattachement S21.G00.54.004 / 289

                # bloc S21.G00.55 - Composant de versement (0,*)
                # f.write("S21.G00.55.001,'00.00'\n")  # Montant versé S21.G00.55.001 / 290
                # f.write("S21.G00.55.002,'néant'\n")  # Type de population S21.G00.55.002 / 291
                # f.write("S21.G00.55.003,'néant'\n")  # Code d'affectation S21.G00.55.003 / 292
                # f.write("S21.G00.55.004,'néant'\n")  # Période d'affectation S21.G00.55.004 / 293

                # bloc S21.G00.56 - Régularisation de prélèvement à la source (0,*)
                # f.write("S21.G00.56.001,'néant'\n")  # Mois de l’erreur S21.G00.56.001 / 294
                # f.write("S21.G00.56.002,'néant'\n")  # Type d’erreur S21.G00.56.002 / 295
                # f.write("S21.G00.56.003,'néant'\n")  # Régularisation de la rémunération nette fiscale S21.G00.56.003 / 296
                # f.write("S21.G00.56.004,'néant'\n")  # Rémunération nette fiscale déclarée le mois de l’erreur S21.G00.56.004 / 297
                # f.write("S21.G00.56.005,'néant'\n")  # Régularisation du taux de prélèvement à la source S21.G00.56.005 / 298
                # f.write("S21.G00.56.006,'néant'\n")  # Taux déclaré le mois de l’erreur S21.G00.56.006 / 299
                # f.write("S21.G00.56.007,'néant'\n")  # Montant de la régularisation du prélèvement à la source S21.G00.56.007 / 300
                # f.write("S21.G00.56.008,'néant'\n")  # Régularisation du montant de la part non imposable du revenu S21.G00.56.008 / 301
                # f.write("S21.G00.56.009,'néant'\n")  # Régularisation du montant de l’abattement sur la base fiscale (non déduit de la rémunération nette fiscale) S21.G00.56.009 / 302
                # f.write("S21.G00.56.010,'néant'\n")  # Régularisation du montant soumis au PAS S21.G00.56.010 / 303

                # bloc S21.G00.60 - Arrêt de travail (0,*)
                # f.write("S21.G00.60.001,'néant'\n")  # Motif de l'arrêt S21.G00.60.001 / 304
                # f.write("S21.G00.60.002,'néant'\n")  # Date du dernier jour travaillé S21.G00.60.002 / 305
                # f.write("S21.G00.60.003,'néant'\n")  # Date de fin prévisionnelle S21.G00.60.003 / 306
                # f.write("S21.G00.60.004,''\n")  # Subrogation S21.G00.60.004
                # f.write("S21.G00.60.005,''\n")  # Date de début de subrogation S21.G00.60.005
                # f.write("S21.G00.60.006,''\n")  # Date de fin de subrogation S21.G00.60.006
                # f.write("S21.G00.60.007,''\n")  # IBAN S21.G00.60.007
                # f.write("S21.G00.60.008,''\n")  # BIC S21.G00.60.008
                # f.write("S21.G00.60.010,'néant'\n")  # Date de la reprise S21.G00.60.010 / 307
                # f.write("S21.G00.60.011,'néant'\n")  # Motif de la reprise S21.G00.60.011 / 308
                # f.write("S21.G00.60.012,''\n")  # Date de l'accident ou de la première constatation S21.G00.60.012
                # f.write("S21.G00.60.600,''\n")  # SIRET Centralisateur S21.G00.60.600

                # bloc S21.G00.62 - Fin du contrat (0,1)
                # f.write("S21.G00.62.001,'néant'\n")  # Date de fin du contrat S21.G00.62.001 / 309
                # f.write("S21.G00.62.002,'néant'\n")  # Motif de la rupture du contrat S21.G00.62.002 / 310
                # f.write("S21.G00.62.003,''\n")  # Date de notification de la rupture de contrat S21.G00.62.003
                # f.write("S21.G00.62.004,''\n")  # Date de signature de la convention de rupture S21.G00.62.004
                # f.write("S21.G00.62.005,''\n")  # Date d'engagement de la procédure de licenciement S21.G00.62.005
                # f.write("S21.G00.62.006,'néant'\n")  # Dernier jour travaillé et payé au salaire habituel S21.G00.62.006 / 311
                # f.write("S21.G00.62.008,''\n")  # Transaction en cours S21.G00.62.008
                # f.write("S21.G00.62.011,''\n")  # Nombre de mois de préavis utilisés dans le cadre du calcul CSP S21.G00.62.011
                # f.write("S21.G00.62.013,''\n")  # Montant de l'indemnité de préavis qui aurait été versée S21.G00.62.013
                # f.write("S21.G00.62.014,''\n")  # Statut particulier du salarié S21.G00.62.014
                # f.write("S21.G00.62.016,'néant'\n")  # Maintien de l’affiliation du salarié au contrat collectif S21.G00.62.016 / 312
                # f.write("S21.G00.62.017,'néant'\n")  # Modalité de déclaration de la fin du contrat d'usage S21.G00.62.017 / 313
                # f.write("S21.G00.62.018,''\n")  # Nombre de mois de préavis utilisés dans le cadre du calcul PAP S21.G00.62.018
                # f.write("S21.G00.62.019,'néant'\n")  # Solde de congés acquis et non pris (ENIM) S21.G00.62.019 / 314
                # f.write("S21.G00.62.020,''\n")  # Mois de la DSN mensuelle portant les derniers éléments déclarés dans le FCTU S21.G00.62.020

                # bloc Préavis de fin de contrat S21.G00.63
                # f.write("S21.G00.63.001,''\n")  # Type réalisation et paiement du préavis S21.G00.63.001
                # f.write("S21.G00.63.002,''\n")  # Date de début de préavis S21.G00.63.002
                # f.write("S21.G00.63.003,''\n")  # Date de fin de préavis S21.G00.63.003

                # bloc S21.G00.65 - Autre suspension de l'exécution du contrat (0,*)
                # f.write("S21.G00.65.001,'néant'\n")  # Motif de suspension S21.G00.65.001 / 315
                # f.write("S21.G00.65.002,'néant'\n")  # Date de début de la suspension S21.G00.65.002 / 316
                # f.write("S21.G00.65.003,'néant'\n")  # Date de fin de la suspension S21.G00.65.003 / 317
                # f.write("S21.G00.65.004,'néant'\n")  # [FP] Position de détachement S21.G00.65.004 / 318

                # bloc S21.G00.66 - Temps partiel Thérapeutique (0,*)
                # f.write("S21.G00.66.001,'néant'\n")  # Date de début S21.G00.66.001 / 319
                # f.write("S21.G00.66.002,'néant'\n")  # Date de fin S21.G00.66.002 / 320
                # f.write("S21.G00.66.003,'néant'\n")  # Montant S21.G00.66.003 / 321

                # bloc S21.G00.70 - Affiliation Prévoyance (0,*)
                # f.write("S21.G00.70.004,'néant'\n")  # Code option retenue par le salarié S21.G00.70.004 / 322
                # f.write("S21.G00.70.005,'néant'\n")  # Code population de rattachement S21.G00.70.005 / 323
                # f.write("S21.G00.70.007,'néant'\n")  # Nombre d’enfants à charge S21.G00.70.007 / 324
                # f.write("S21.G00.70.008,'néant'\n")  # Nombre d'adultes ayants-droit (conjoint, concubin, ...) S21.G00.70.008 / 325
                # f.write("S21.G00.70.009,'néant'\n")  # Nombre d'ayants-droit S21.G00.70.009 / 326
                # f.write("S21.G00.70.010,'néant'\n")  # Nombre d'ayants-droit autres (ascendants, collatéraux...) S21.G00.70.010 / 327
                # f.write("S21.G00.70.011,'néant'\n")  # Nombre d'enfants ayants-droit S21.G00.70.011 / 328
                # f.write("S21.G00.70.012,'néant'\n")  # Identifiant technique Affiliation S21.G00.70.012 / 329
                # f.write("S21.G00.70.013,'néant'\n")  # Identifiant technique Adhésion S21.G00.70.013 / 330
                # f.write("S21.G00.70.014,'néant'\n")  # Date de début de l’affiliation S21.G00.70.014 / 331
                # f.write("S21.G00.70.015,'néant'\n")  # Date de fin de l’affiliation S21.G00.70.015 / 332

                # bloc S21.G00.71 - Retraite complémentaire (1,*)
                # f.write("S21.G00.71.002,'néant'\n")  # Code régime Retraite Complémentaire S21.G00.71.002 / 333
                # f.write("S21.G00.71.003,'néant'\n")  # Référence adhésion employeur S21.G00.71.003 / 334

                # bloc S21.G00.72 - Affiliation à tort à un régime de retraite complémentaire (0,*)
                # f.write("S21.G00.72.001,'néant'\n")  # Code régime Retraite Complémentaire déclaré à tort S21.G00.72.001 / 335

                # bloc S21.G00.73 - Ayant-droit (0,*)
                # f.write("S21.G00.73.001,'néant'\n")  # Régime local Alsace-Moselle S21.G00.73.001 / 336
                # f.write("S21.G00.73.002,'néant'\n")  # Code option S21.G00.73.002 / 337
                # f.write("S21.G00.73.003,'néant'\n")  # Type S21.G00.73.003 / 338
                # f.write("S21.G00.73.004,'néant'\n")  # Date de début de rattachement à l'ouvrant-droit S21.G00.73.004 / 339
                # f.write("S21.G00.73.005,'néant'\n")  # Date de naissance S21.G00.73.005 / 340
                # f.write("S21.G00.73.006,'néant'\n")  # Nom de famille S21.G00.73.006 / 341
                # f.write("S21.G00.73.007,'néant'\n")  # Numéro d'inscription au répertoire S21.G00.73.007 / 342
                # f.write("S21.G00.73.008,'néant'\n")  # NIR ouvrant-droit régime de base maladie S21.G00.73.008 / 343
                # f.write("S21.G00.73.009,'néant'\n")  # Prénoms S21.G00.73.009 / 344
                # f.write("S21.G00.73.010,'néant'\n")  # Code organisme d'affiliation à l'assurance maladie S21.G00.73.010 / 345
                # f.write("S21.G00.73.011,'néant'\n")  # Date de fin de rattachement à l'ouvrant-droit S21.G00.73.011 / 346

                # bloc S21.G00.78 - Base assujettie (0,*)
                # f.write("S21.G00.78.001,'néant'\n")  # Code de base assujettie S21.G00.78.001 / 347
                # f.write("S21.G00.78.002,'néant'\n")  # Date de début de période de rattachement S21.G00.78.002 / 348
                # f.write("S21.G00.78.003,'néant'\n")  # Date de fin de période de rattachement S21.G00.78.003 / 349
                # f.write("S21.G00.78.004,'néant'\n")  # Montant S21.G00.78.004 / 350
                # f.write("S21.G00.78.005,'néant'\n")  # Identifiant technique Affiliation S21.G00.78.005 / 351
                # f.write("S21.G00.78.006,'néant'\n")  # Numéro du contrat S21.G00.78.006 / 352

                # bloc S21.G00.79 - Composant de base assujettie (0,*)
                # f.write("S21.G00.79.001,'néant'\n")  # Type de composant de base assujettie S21.G00.79.001 / 353
                # f.write("S21.G00.79.004,'néant'\n")  # Montant de composant de base assujettie S21.G00.79.004 / 354

                # bloc S21.G00.81 - Cotisation individuelle (0,*)
                # f.write("S21.G00.81.001,'néant'\n")  # Code de cotisation S21.G00.81.001 / 355
                # f.write("S21.G00.81.002,'néant'\n")  # Identifiant Organisme de Protection Sociale S21.G00.81.002 / 356
                # f.write("S21.G00.81.003,'néant'\n")  # Montant d'assiette S21.G00.81.003 / 357
                # f.write("S21.G00.81.004,'néant'\n")  # Montant de cotisation S21.G00.81.004 / 358
                # f.write("S21.G00.81.005,'néant'\n")  # Code INSEE commune S21.G00.81.005 / 359

                # bloc S21.G00.82 - Cotisation établissement (0,*)
                # f.write("S21.G00.82.001,'néant'\n")  # Valeur S21.G00.82.001 / 360
                # f.write("S21.G00.82.002,'néant'\n")  # Code de cotisation S21.G00.82.002 / 361
                # f.write("S21.G00.82.003,'néant'\n")  # Date de début de période de rattachement S21.G00.82.003 / 362
                # f.write("S21.G00.82.004,'néant'\n")  # Date de fin de période de rattachement S21.G00.82.004 / 363
                # f.write("S21.G00.82.005,'néant'\n")  # Référence réglementaire ou contractuelle S21.G00.82.005 / 364

                # bloc S21.G00.83 - Période d'affiliation à tort à un régime de retraite complémentaire (0,*)
                # f.write("S21.G00.83.001,'néant'\n")  # Date de début de période déclarée à tort S21.G00.83.001 / 365
                # f.write("S21.G00.83.002,'néant'\n")  # Date de fin de période déclarée à tort S21.G00.83.002 / 366

                # bloc S21.G00.84 - Base assujettie déclarée à tort pour un régime de retraite complémentaire (0,*)
                # f.write("S21.G00.84.001,'néant'\n")  # Code de base assujettie déclarée à tort S21.G00.84.001 / 367
                # f.write("S21.G00.84.002,'néant'\n")  # Date de début de période de rattachement de la base déclarée à tort S21.G00.84.002 / 368
                # f.write("S21.G00.84.003,'néant'\n")  # Date de fin de période de rattachement de la base déclarée à tort S21.G00.84.003 / 369
                # f.write("S21.G00.84.004,'néant'\n")  # Montant déclaré à tort S21.G00.84.004 / 370
                # f.write("S21.G00.84.005,'néant'\n")  # Numéro du contrat rattaché à la base assujettie déclarée à tort S21.G00.84.005 / 371

                # bloc S21.G00.85 - Lieu de travail ou établissement utilisateur (0,*)
                # f.write("S21.G00.85.001,'domicile'\n")  # Identifiant du lieu de travail ou de l'établissement utilisateur S21.G00.85.001 / 372
                # f.write("S21.G00.85.002,'4675Z'\n")  # Code APET S21.G00.85.002 / 373
                # f.write("S21.G00.85.003,'6 Avenue Léon Blum'\n")  # Numéro, extension, nature, libellé de voie S21.G00.85.003 / 374
                # f.write("S21.G00.85.004,'93800'\n")  # Code postal S21.G00.85.004 / 375
                # f.write("S21.G00.85.005,'Epinay-sur-Seine'\n")  # Localité S21.G00.85.005 / 376
                # f.write("S21.G00.85.006,'FR'\n")  # Code Pays S21.G00.85.006 / 377
                # f.write("S21.G00.85.007,'néant'\n")  # Code de distribution à l'étranger S21.G00.85.007 / 378
                # f.write("S21.G00.85.008,'Etage 1 - Appartement 6 - Digicode 15B25'\n")  # Complément de la localisation de la construction S21.G00.85.008 / 379
                # f.write("S21.G00.85.009,'néant'\n")  # Service de distribution, complément de localisation de la voie S21.G00.85.009 / 380
                # f.write("S21.G00.85.010,'03'\n")  # Nature juridique S21.G00.85.010 / 381
                # f.write("S21.G00.85.011,'93031'\n")  # Code INSEE commune S21.G00.85.011 / 382

                # bloc S21.G00.86 - Ancienneté (0,*)
                # f.write("S21.G00.86.001,'07'\n")  # Type S21.G00.86.001 / 383
                # f.write("S21.G00.86.002,'01'\n")  # Unité de mesure S21.G00.86.002 / 384
                # f.write("S21.G00.86.003,'18'\n")  # Valeur S21.G00.86.003 / 385
                # f.write("S21.G00.86.005,'néant'\n")  # Numéro du contrat S21.G00.86.005 / 386

                # bloc S21.G00.95 - Base assujettie déclarée à tort pour un régime de base risque maladie ou vieillesse (0,*)
                # f.write("S21.G00.95.001,'néant'\n")  # Code de base assujettie déclarée à tort S21.G00.95.001 / 387
                # f.write("S21.G00.95.002,'néant'\n")  # Date de début de période de rattachement de la base déclarée à tort S21.G00.95.002 / 388
                # f.write("S21.G00.95.003,'néant'\n")  # Date de fin de période de rattachement de la base déclarée à tort S21.G00.95.003 / 389
                # f.write("S21.G00.95.004,'néant'\n")  # Montant déclaré à tort S21.G00.95.004 / 390
                # f.write("S21.G00.95.005,'néant'\n")  # Numéro du contrat rattaché à la base assujettie déclarée à tort S21.G00.95.005 / 391

                # bloc S89.G00.32 - Bénéficiaire des honoraires (0,*)
                # f.write("S89.G00.32.001,'néant'\n")  # Profession ou qualité S89.G00.32.001 / 392
                # f.write("S89.G00.32.002,'néant'\n")  # Nom du bénéficiaire des honoraires S89.G00.32.002 / 393
                # f.write("S89.G00.32.003,'néant'\n")  # Prénom du bénéficiaire des honoraires S89.G00.32.003 / 394
                # f.write("S89.G00.32.004,'néant'\n")  # Siren du bénéficiaire des honoraires S89.G00.32.004 / 395
                # f.write("S89.G00.32.005,'néant'\n")  # Nic du bénéficiaire des honoraires S89.G00.32.005 / 396
                # f.write("S89.G00.32.006,'néant'\n")  # Raison sociale du bénéficiaire des honoraires S89.G00.32.006 / 397
                # f.write("S89.G00.32.007,'néant'\n")  # Complément de localisation de la construction S89.G00.32.007 / 398
                # f.write("S89.G00.32.008,'néant'\n")  # Numéro, extension, nature et libellé de la voie S89.G00.32.008 / 399
                # f.write("S89.G00.32.009,'néant'\n")  # Code INSEE de la commune S89.G00.32.009 / 400
                # f.write("S89.G00.32.010,'néant'\n")  # Service de distribution, complément de localisation de la voie S89.G00.32.010 / 401
                # f.write("S89.G00.32.011,'néant'\n")  # Code postal S89.G00.32.011 / 402
                # f.write("S89.G00.32.012,'néant'\n")  # Localité S89.G00.32.012 / 403
                # f.write("S89.G00.32.013,'néant'\n")  # Code pays S89.G00.32.013 / 404
                # f.write("S89.G00.32.014,'néant'\n")  # Code de distribution à l'étranger S89.G00.32.014 / 405
                # f.write("S89.G00.32.015,'néant'\n")  # Code taux réduit ou dispense de retenue à la source S89.G00.32.015 / 406
                # f.write("S89.G00.32.016,'néant'\n")  # Montant TVA droits d'auteurs S89.G00.32.016 /407
                # f.write("S89.G00.32.017,'néant'\n")  # Millésime de rattachement S89.G00.32.017 / 408

                # bloc S89.G00.33 - Avantages en nature (0,*)
                # f.write("S89.G00.33.001,'néant'\n")  # Code type avantage en nature S89.G00.33.001 / 409
                # f.write("S89.G00.33.002,'néant'\n")  # Montant avantage en nature S89.G00.33.002 / 410

                # bloc S89.G00.35 - Prise en charge des indemnités (0,*)
                # f.write("S89.G00.35.001,'néant'\n")  # Code modalité de prise en charge des indemnités S89.G00.35.001 / 411
                # f.write("S89.G00.35.002,'néant'\n")  # Montant de l'indemnité S89.G00.35.002 / 412

                # bloc S89.G00.43 - Rémunérations (0,*)
                # f.write("S89.G00.43.001,'néant'\n")  # Code type de la rémunération S89.G00.43.001 / 413
                # f.write("S89.G00.43.002,'néant'\n")  # Montant de la rémunération S89.G00.43.002 / 414

                # bloc S89.G00.87 - Actions gratuites (0,*)
                # f.write("S89.G00.87.001,'néant'\n")  # Code contexte S89.G00.87.001 / 415
                # f.write("S89.G00.87.002,'néant'\n")  # Nombre d'actions S89.G00.87.002 / 416
                # f.write("S89.G00.87.003,'néant'\n")  # Valeur unitaire de l'action S89.G00.87.003 / 417
                # f.write("S89.G00.87.004,'néant'\n")  # Fraction du gain d'acquisition de source française S89.G00.87.004 / 418
                # f.write("S89.G00.87.005,'néant'\n")  # Date d'attribution S89.G00.87.005 / 419
                # f.write("S89.G00.87.006,'néant'\n")  # Date d'acquisition définitive S89.G00.87.006 / 420
                # f.write("S89.G00.87.007,'néant'\n")  # Numéro d'inscription au répertoire S89.G00.87.007 / 421
                # f.write("S89.G00.87.008,'néant'\n")  # Numéro technique temporaire S89.G00.87.008 / 422

                # bloc S89.G00.88 - Options sur titres (stock options) (0,*)
                # f.write("S89.G00.88.001,'néant'\n")  # Code contexte S89.G00.88.001 / 423
                # f.write("S89.G00.88.002,'néant'\n")  # Nombre d'options S89.G00.88.002 / 425
                # f.write("S89.G00.88.003,'néant'\n")  # Valeur unitaire de l'action S89.G00.88.003 / 426
                # f.write("S89.G00.88.004,'néant'\n")  # Prix de souscription de l'action S89.G00.88.004 / 427
                # f.write("S89.G00.88.005,'néant'\n")  # Fraction du gain de levée d'option de source française S89.G00.88.005 / 428
                # f.write("S89.G00.88.006,'néant'\n")  # Date d'attribution S89.G00.88.006 / 429
                # f.write("S89.G00.88.007,'néant'\n")  # Date de levée de l'option S89.G00.88.007 / 430
                # f.write("S89.G00.88.008,'néant'\n")  # Numéro d'inscription au répertoire S89.G00.88.008 / 431
                # f.write("S89.G00.88.009,'néant'\n")  # Numéro technique temporaire S89.G00.88.009 / 432

                # bloc S89.G00.89 - Bons de souscription de parts de créateur d'entreprise (BSPCE) (0,*)
                # f.write("S89.G00.89.001,'néant'\n")  # Nombre de titres S89.G00.89.001 / 433
                # f.write("S89.G00.89.002,'néant'\n")  # Prix d'acquisition des titres S89.G00.89.002 / 434
                # f.write("S89.G00.89.003,'néant'\n")  # Valeur unitaire des titres au jour de l'exercice des bons S89.G00.89.003 / 435
                # f.write("S89.G00.89.004,'néant'\n")  # Fraction du gain de source française S89.G00.89.004 / 436
                # f.write("S89.G00.89.005,'néant'\n")  # Date d'acquisition des titres S89.G00.89.005 / 437
                # f.write("S89.G00.89.006,'néant'\n")  # Durée d'exercice de l'activité du bénéficiaire dans l'entreprise S89.G00.89.006 / 438
                # f.write("S89.G00.89.007,'néant'\n")  # Numéro d'inscription au répertoire S89.G00.89.007 / 439
                # f.write("S89.G00.89.008,'néant'\n")  # Numéro technique temporaire S89.G00.89.008 / 440

                # bloc S89.G00.91 - Individu non salarié (0,*)
                # f.write("S89.G00.91.001,'néant'\n")  # Numéro d'inscription au répertoire S89.G00.91.001 / 441
                # f.write("S89.G00.91.002,'néant'\n")  # Nom de famille S89.G00.91.002 / 442
                # f.write("S89.G00.91.003,'néant'\n")  # Nom d'usage S89.G00.91.003 / 443
                # f.write("S89.G00.91.004,'néant'\n")  # Prénoms S89.G00.91.004 / 444
                # f.write("S89.G00.91.005,'néant'\n")  # Sexe S89.G00.91.005 / 445
                # f.write("S89.G00.91.006,'néant'\n")  # Date de naissance S89.G00.91.006 / 446
                # f.write("S89.G00.91.007,'néant'\n")  # Lieu de naissance S89.G00.91.007 / 447
                # f.write("S89.G00.91.008,'néant'\n")  # Numéro, extension, nature et libellé de la voie S89.G00.91.008 / 448
                # f.write("S89.G00.91.009,'néant'\n")  # Code postal S89.G00.91.009 / 449
                # f.write("S89.G00.91.010,'néant'\n")  # Localité S89.G00.91.010 / 450
                # f.write("S89.G00.91.011,'néant'\n")  # Code Pays S89.G00.91.011 / 451
                # f.write("S89.G00.91.012,'néant'\n")  # Code de distribution à l'étranger S89.G00.91.012 / 452
                # f.write("S89.G00.91.013,'néant'\n")  # Complément de la localisation de la construction S89.G00.91.013 / 453
                # f.write("S89.G00.91.014,'néant'\n")  # Service de distribution, complément de localisation de la voie S89.G00.91.014 / 454
                # f.write("S89.G00.91.015,'néant'\n")  # Adresse mél S89.G00.91.015 / 455
                # f.write("S89.G00.91.016,'néant'\n")  # Matricule de l'individu dans l'entreprise S89.G00.91.016 / 456
                # f.write("S89.G00.91.017,'néant'\n")  # Statut du salarié (conventionnel) S89.G00.91.017 / 457
                # f.write("S89.G00.91.018,'néant'\n")  # Code statut catégoriel Retraite Complémentaire obligatoire S89.G00.91.018 / 458
                # f.write("S89.G00.91.019,'néant'\n")  # Code département de naissance S89.G00.91.019 / 459
                # f.write("S89.G00.91.020,'néant'\n")  # Code pays de naissance S89.G00.91.020 / 460
                # f.write("S89.G00.91.021,'néant'\n")  # Numéro technique temporaire S89.G00.91.021 / 461

                # bloc S89.G00.92 - Bases spécifiques individu non salarié (1,*)
                # f.write("S89.G00.92.001,'néant'\n")  # Type S89.G00.92.001 / 462
                # f.write("S89.G00.92.002,'néant'\n")  # Code de base spécifique S89.G00.92.002 / 463
                # f.write("S89.G00.92.003,'néant'\n")  # Montant S89.G00.92.003 / 464
                # f.write("S89.G00.92.004,'néant'\n")  # Date de début de période de rattachement S89.G00.92.004 / 465
                # f.write("S89.G00.92.005,'néant'\n")  # Date de fin de période de rattachement S89.G00.92.005 / 466
                # f.write("S89.G00.92.006,'néant'\n")  # Montant net fiscal du revenu versé S89.G00.92.006 / 467
                # f.write("S89.G00.92.007,'néant'\n")  # Taux de prélèvement à la source S89.G00.92.007 / 468
                # f.write("S89.G00.92.008,'néant'\n")  # Type du taux de prélèvement à la source S89.G00.92.008 / 469
                # f.write("S89.G00.92.009,'néant'\n")  # Identifiant du taux de prélèvement à la source S89.G00.92.009 / 470
                # f.write("S89.G00.92.010,'néant'\n")  # Montant de prélèvement à la source S89.G00.92.010 / 471
                # f.write("S89.G00.92.011,'néant'\n")  # Date de versement S89.G00.92.011 / 472
                # f.write("S89.G00.92.012,'néant'\n")  # Montant de la part non imposable du revenu S89.G00.92.012 / 473
                # f.write("S89.G00.92.013,'néant'\n")  # Montant soumis au PAS S89.G00.92.013 / 474
                # f.write("S89.G00.92.014,'néant'\n")  # Montant de l’abattement sur la base fiscale (non déduit du montant net fiscal du revenu versé) S89.G00.92.014 / 475

                # bloc S89.G00.93 - Régularisation de prélèvement à la source (0,*)
                # f.write("S89.G00.93.001,'néant'\n")  # Mois de l’erreur S89.G00.93.001 / 476
                # f.write("S89.G00.93.002,'néant'\n")  # Type d’erreur S89.G00.93.002 / 477
                # f.write("S89.G00.93.003,'néant'\n")  # Régularisation du montant net fiscal du revenu versé S89.G00.93.003 / 478
                # f.write("S89.G00.93.004,'néant'\n")  # Montant net fiscal du revenu versé du mois de l’erreur S89.G00.93.004 / 479
                # f.write("S89.G00.93.005,'néant'\n")  # Régularisation du taux de prélèvement à la source S89.G00.93.005 / 480
                # f.write("S89.G00.93.006,'néant'\n")  # Taux déclaré le mois de l’erreur S89.G00.93.006 / 481
                # f.write("S89.G00.93.007,'néant'\n")  # Montant de la régularisation du prélèvement à la source S89.G00.93.007 / 482
                # f.write("S89.G00.93.008,'néant'\n")  # Régularisation du montant de la part non imposable du revenu S89.G00.93.008 / 483
                # f.write("S89.G00.93.009,'néant'\n")  # Régularisation du montant soumis au PAS S89.G00.93.009 / 484
                # f.write("S89.G00.93.010,'néant'\n")  # Régularisation du montant de l’abattement sur la base fiscale (non déduit du montant net fiscal du revenu versé) S89.G00.93.010 / 485

                # bloc S89.G00.94 - Cotisation Individu non salarié (0,*)
                # f.write("S89.G00.94.001,'néant'\n")  # Code de cotisation S89.G00.94.001 / 486
                # f.write("S89.G00.94.002,'néant'\n")  # Montant de cotisation S89.G00.94.002 / 487

                # bloc S90.G00.90 - Total de l'envoi (1,1)
                f.write("S90.G00.90.001,'51'\n")  # Nombre total de rubriques S90.G00.90.001 / 488
                f.write("S90.G00.90.002,'1'")  # Nombre de DSN S90.G00.90.002

        finally:
            f.close()

    def test_dsn_controle_siret(self):
        print("test_dsn_controle_siret")

        try:
            with open("../dsn_controle_siret.txt", mode='a', encoding='latin-1') as f:
                f.write("")

        finally:
            f.close()


if __name__ == '__main__':
    unittest.main()
