import unittest
import os


class UnitTestsFilesTreatement(unittest.TestCase):
    # ok
    def test_replace_srings_in_from_one_file(sel):
        print("test_replace_srings_in_from_one_file")

        file_path = "A:\\2_Personnel\\1_Recurrentes\\70_Mon_Compte_Github\\Python-Macros-For-FreeCAD" \
                    "\\Chas_Campbell_Gravitational_Engine\\Version_1\\part_ecrou_10m.py"

        # read input file
        fin = open(file_path, "rt")

        # read file contents to string
        data = fin.read()

        # replace all occurrences of the required string
        new_data = data.replace("'A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + ", '')\
            .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/", "")\
            .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_2/", "")\
            .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/", "")

        # close the input file
        fin.close()

        # open the input file in write mode
        fin = open(file_path, "wt")

        # overrite the input file with the resulting data
        fin.write(new_data)

        # close the file
        fin.close()

    # ok
    def test_replace_srings_in_from_all_file_in_one_folder(sel):
        print("test_replace_srings_in_from_all_file_in_one_folder")

        folder = "A:\\2_Personnel\\1_Recurrentes\\70_Mon_Compte_Github\\Python-Macros-For-FreeCAD" \
                 "\\Chas_Campbell_Gravitational_Engine\\Version_1"

        files = os.listdir(folder)

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(folder, file)

                fin = open(file_path, "rt")

                data = fin.read()

                new_data = data.replace("'A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + ", '')\
                    .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/", "")\
                    .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_2/", "")\
                    .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/", "")\
                    .replace("A:\\\\", "").replace("1_Professionnel", "").replace("1_Holomorphe", "")\
                    .replace("2_Archives", "").replace("2_Outils_Numeriques", "").replace("My_Tools", "")\
                    .replace("Test", "").replace("Service", "").replace("Archives", "").replace("CAO", "")\
                    .replace("2_Specials", "").replace("Chas_Campbell_Gravitational_Engine", "")\
                    .replace("Version_1", "").replace("\\\\", "").replace("            ''", "")

                fin.close()

                fin = open(file_path, "wt")

                fin.write(new_data)

                fin.close()

    # ok
    def test_replace_srings_in_from_all_file_in_many_folders(sel):
        print("test_replace_srings_in_from_all_file_in_many_folders")

        folders = [
            "A:\\2_Personnel\\1_Recurrentes\\70_Mon_Compte_Github\\Python-Macros-For-FreeCAD\\Transmutator\\Version_1"
        ]

        for folder in folders:
            files = os.listdir(folder)

            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(folder, file)

                    fin = open(file_path, "rt")

                    data = fin.read()

                    new_data = data.replace("'A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + ", '') \
                        .replace("'A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/Transmutator/' + ", '') \
                        .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Transmutator/Version_1/", "")\
                        .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/", "")\
                        .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/", "")\
                        .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_2/", "")\
                        .replace("A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/", "") \
                        .replace("A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Transmutator\\\\Version_1\\\\", "")\
                        .replace("A:\\\\", "").replace("1_Professionnel", "").replace("1_Holomorphe", "")\
                        .replace("2_Archives", "").replace("2_Outils_Numeriques", "").replace("My_Tools", "")\
                        .replace("Test", "").replace("Service", "").replace("Archives", "").replace("CAO", "")\
                        .replace("2_Specials", "").replace("Chas_Campbell_Gravitational_Engine", "")\
                        .replace("Version_1", "").replace("Version_2", "").replace("Version_3", "").replace("\\\\", "")

                    fin.close()

                    fin = open(file_path, "wt")

                    fin.write(new_data)

                    fin.close()

    # ok
    def test_remove_files_from_many_folders(sel):
        print("test_remove_files_from_many_folders")

        folders = [
            "A:\\2_Personnel\\1_Recurrentes\\70_Mon_Compte_Github\\Python-Macros-For-FreeCAD\\Transmutator\\Version_1"
        ]

        for folder in folders:
            files = os.listdir(folder)

            for file in files:
                if file.endswith(".stl") or file.endswith(".dxf"):
                    file_path = os.path.join(folder, file)
                    os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
