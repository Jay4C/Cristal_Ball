import unittest
import csv
import xlsxwriter


class UnitTestsManagement(unittest.TestCase):
    def test_modify_ganttproject_from_csv_file_to_validate_some_tasks(self):
        print('test_modify_ganttproject_from_csv_file')

        try:
            date_de_debut = "30/06/20"
            date_de_fin = "30/06/20"
            avancee = "100"
            couleur = "#cc00cc"

            min = 17956
            max = 18024

            lines = list()

            with open('Activites_Annee_2020_v1.csv', 'r', encoding="utf8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    lines.append(dict(row))

                    if (min <= int(dict(row)["ID"]) <= max):
                        print("raw row : " + str(dict(row)))

                        lines.remove(dict(row))

                        line = {
                            "ID": dict(row)["ID"],
                            "Nom": dict(row)["Nom"]
                            .replace("Copie_", "")
                            .replace("_[Outil_Non_Operationnel]", "")
                            .replace("_[Pagination]", "")
                            .replace("_[Cryptage]", "")
                            .replace("_[Balisage]", "")
                            .replace("_[Retour_Information]", "")
                            .replace("_[Localisation]", "")
                            .replace("_[Robot]", "")
                            .replace("_[Robot_et_Parsing]", "")
                            .replace("_[Url_Fixe]", "")
                            .replace("_[Paginations]", "")
                            .replace("_[Non_Operationnel]", ""),
                            "Date de début": date_de_debut,
                            "Date de fin": date_de_fin,
                            "Durée": dict(row)["Durée"],
                            "Avancée": avancee,
                            "Coût": dict(row)["Coût"],
                            "Responsable": dict(row)["Responsable"],
                            "Prédécesseurs": dict(row)["Prédécesseurs"],
                            "Numéro hiérarchique": dict(row)["Numéro hiérarchique"],
                            "Ressources": dict(row)["Ressources"],
                            "Assignments": dict(row)["Assignments"],
                            "Nouvelle tâche": couleur,
                            "Lien internet": dict(row)["Lien internet"],
                            "Notes": dict(row)["Notes"]
                        }

                        print("new row : " + str(line))

                        lines.append(line)

            with open('mycsv.csv', 'w', newline='', encoding="utf8") as file:
                fieldnames = [
                    "ID",
                    "Nom",
                    "Date de début",
                    "Date de fin",
                    "Durée",
                    "Avancée",
                    "Coût",
                    "Responsable",
                    "Prédécesseurs",
                    "Numéro hiérarchique",
                    "Ressources",
                    "Assignments",
                    "Nouvelle tâche",
                    "Lien internet",
                    "Notes"
                ]

                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(lines)

        except Exception as e:
            print("error : " + str(e))

    def test_display_topics_for_grap_bilderberg_from_csv_file(self):
        print("test_display_topics_for_grap_bilderberg_from_csv_file")

        try:
            with open('Activites_Annee_2020_v1.csv', 'r', encoding="utf8") as file:
                reader = csv.DictReader(file)

                min = 70176
                max = 70642

                for row in reader:
                    if (min <= int(dict(row)["ID"]) <= max):
                        print(dict(row)["Nom"])

        except Exception as e:
            print("error : " + str(e))

    def test_modify_ganttproject_from_csv_file(self):
        print('test_modify_ganttproject_from_csv_file')

        try:
            date_de_debut = "10/10/20"
            date_de_fin = "10/10/20"
            avancee = "0"
            couleur = "#000000"

            min = 28726
            max = 28730

            lines = list()

            with open('Global_Management_v3_2020_2.csv', 'r', encoding="utf8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    lines.append(dict(row))

                    if (min <= int(dict(row)["ID"]) <= max):
                        print("raw row : " + str(dict(row)))

                        lines.remove(dict(row))

                        line = {
                            "ID": dict(row)["ID"],
                            "Nom": dict(row)["Nom"]
                            .replace("Copie_", "")
                            .replace("_[Outil_Non_Operationnel]", "")
                            .replace("_[Pagination]", "")
                            .replace("_[Cryptage]", "")
                            .replace("_[Balisage]", "")
                            .replace("_[Retour_Information]", "")
                            .replace("_[Localisation]", "")
                            .replace("_[Robot]", "")
                            .replace("_[Robot_et_Parsing]", "")
                            .replace("_[Url_Fixe]", "")
                            .replace("_[Paginations]", "")
                            .replace("_[Non_Operationnel]", ""),
                            "Date de début": date_de_debut, #dict(row)["Date de début"],
                            "Date de fin": date_de_fin, #dict(row)["Date de fin"],
                            "Durée": dict(row)["Durée"],
                            "Avancée": avancee, #dict(row)["Avancée"],
                            "Coût": dict(row)["Coût"],
                            "Responsable": dict(row)["Responsable"],
                            "Prédécesseurs": dict(row)["Prédécesseurs"],
                            "Numéro hiérarchique": dict(row)["Numéro hiérarchique"],
                            "Ressources": dict(row)["Ressources"],
                            "Assignments": dict(row)["Assignments"],
                            "Nouvelle tâche": couleur, #dict(row)["Nouvelle tâche"],
                            "Lien internet": dict(row)["Lien internet"],
                            "Notes": dict(row)["Notes"]
                        }

                        print("new row : " + str(line))

                        lines.append(line)

            with open('Global_Management_v3_2020_3.csv', 'w', newline='', encoding="utf8") as file:
                fieldnames = [
                    "ID",
                    "Nom",
                    "Date de début",
                    "Date de fin",
                    "Durée",
                    "Avancée",
                    "Coût",
                    "Responsable",
                    "Prédécesseurs",
                    "Numéro hiérarchique",
                    "Ressources",
                    "Assignments",
                    "Nouvelle tâche",
                    "Lien internet",
                    "Notes"
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(lines)

        except Exception as e:
            print("error : " + str(e))

    def test_extract_comments_from_ganttproject_from_csv_file_to_excel(self):
        print('test_extract_comments_from_ganttproject_from_csv_file_to_excel')

        try:
            filename = "dsn_info_urls.xlsx"

            workbook = xlsxwriter.Workbook(filename)

            worksheet = workbook.add_worksheet('Data')

            worksheet.write(0, 0, 'url')

            min = 1

            max = 3

            with open('Management_3.csv', 'r', encoding="utf8") as file:
                reader = csv.DictReader(file)

                i = 1

                for row in reader:
                    if (min <= int(dict(row)["ID"]) <= max):
                        print('"' + str(dict(row)["Notes"]) + '",')

                        worksheet.write(i, 0, '"' + str(dict(row)["Notes"]) + '",')

                        i += 1

            workbook.close()
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
