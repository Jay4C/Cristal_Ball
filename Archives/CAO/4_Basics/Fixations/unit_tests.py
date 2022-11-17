import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# Function for creating each vis
def draw_vis(d, e, l, k, matter):
    filename = "part_vis_" + matter + "_" + d.replace(".", "_") + "d_" + e.replace(".", "_") + "e_" + l.replace(".", "_") + "l_" \
               + k.replace(".", "_") + "k"

    print("test_" + filename)

    if os.path.exists(filename + ".py"):
        os.remove(filename + ".py")
    else:
        print("The file does not exist")

    # Writing to file
    with open(filename + ".py", "w") as file:
        # Writing data to a file
        file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

""")

        file.write('DOC_NAME = "' + filename + '" \n\n')

        file.write("""
def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * (-0.5)
""")

        file.write("d = " + d + "\n")

        file.write('e = ' + e + '\n')

        file.write('l = ' + l + '\n')

        file.write('k = ' + k + '\n')

        file.write("""

cylinder_1 = Part.makeCylinder(e/2, l + k)

cylinder_2 = Part.makeCylinder(d/2, l)

cylinder_3 = Part.makeCylinder(e/2, l)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/' + filename + '.stl" \n')

        file.write("""Mesh.export(__objs__, stl_file)

setview()
""")

        file.close()

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(460, 750))

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(70, 670))

    time.sleep(3)

    pywinauto.keyboard.send_keys(
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Fixations\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each rondelle
def draw_rondelle(d, D, s, matter):
    filename = "part_rondelle_" + matter + "_" + d.replace(".", "_") + "d_" + D.replace(".", "_") + "D_" + s.replace(".", "_") + "s"

    print("test_" + filename)

    if os.path.exists(filename + ".py"):
        os.remove(filename + ".py")
    else:
        print("The file does not exist")

    # Writing to file
    with open(filename + ".py", "w") as file:
        # Writing data to a file
        file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

""")

        file.write('DOC_NAME = "' + filename + '" \n\n')

        file.write("""
def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * (-0.5)
""")

        file.write("d = " + d + "\n")

        file.write('D = ' + D + '\n')

        file.write('s = ' + s + '\n')

        file.write("""

cylinder_1 = Part.makeCylinder(D/2, s)

cylinder_2 = Part.makeCylinder(d/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/' + filename + '.stl" \n')

        file.write("""Mesh.export(__objs__, stl_file)

setview()
""")

        file.close()

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(460, 750))

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(70, 670))

    time.sleep(3)

    pywinauto.keyboard.send_keys(
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Fixations\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each ecrou
def draw_ecrou(d, e, m, matter):
    filename = "part_ecrou_" + matter + "_" + d.replace(".", "_") + "d_" + e.replace(".", "_") + "e_" + m.replace(".", "_") + "m"

    print("test_" + filename)

    if os.path.exists(filename + ".py"):
        os.remove(filename + ".py")
    else:
        print("The file does not exist")

    # Writing to file
    with open(filename + ".py", "w") as file:
        # Writing data to a file
        file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

""")

        file.write('DOC_NAME = "' + filename + '" \n\n')

        file.write("""
def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * (-0.5)
""")

        file.write("d = " + d + "\n")

        file.write('e = ' + e + '\n')

        file.write('m = ' + m + '\n')

        file.write("""

cylinder_1 = Part.makeCylinder(e/2, m)

cylinder_2 = Part.makeCylinder(d/2, m)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/' + filename + '.stl" \n')

        file.write("""Mesh.export(__objs__, stl_file)

setview()
""")

        file.close()

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(460, 750))

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(70, 670))

    time.sleep(3)

    pywinauto.keyboard.send_keys(
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Fixations\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each tige filetee
def draw_tige_filetee(d, matter):
    filename = "part_tige_filetee_" + matter + "_" + d.replace(".", "_") + "d"

    print("test_" + filename)

    if os.path.exists(filename + ".py"):
        os.remove(filename + ".py")
    else:
        print("The file does not exist")

    # Writing to file
    with open(filename + ".py", "w") as file:
        # Writing data to a file
        file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

""")

        file.write('DOC_NAME = "' + filename + '" \n\n')

        file.write("""
def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * (-0.5)
""")

        file.write("d = " + d + "\n")

        file.write("""

cylinder_1 = Part.makeCylinder(d/2, 1000)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/' + filename + '.stl" \n')

        file.write("""Mesh.export(__objs__, stl_file)

setview()
""")

        file.close()

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(460, 750))

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(70, 670))

    time.sleep(3)

    pywinauto.keyboard.send_keys(
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Fixations\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsBasicPartsForFixationsForVis(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m10x150-inox-a2-ef-din-933.html
    def test_part_vis_inox_10d_18_9e_150l_6_4k(self):
        draw_vis("10", "18.9", "150", "6.4", "inox")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m6x120-inox-a2-ef-din-933.html
    def test_part_vis_inox_6d_11_05e_120l_4k(self):
        draw_vis("6", "11.05", "120", "4", "inox")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m6x30-inox-a2-ef-din-933.html
    def test_part_vis_inox_6d_11_05e_30l_4k(self):
        draw_vis("6", "11.05", "30", "4", "inox")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m6x90-inox-a2-ef-din-933.html
    def test_part_vis_inox_6d_11_05e_90l_4k(self):
        draw_vis("6", "11.05", "90", "4", "inox")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m10x100-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_10d_18_9e_100l_6_4k(self):
        draw_vis("10", "18.9", "100", "6.4", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m20x100-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_20d_33_53e_100l_12_5k(self):
        draw_vis("20", "33.53", "100", "12.5", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m30x100-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_30d_50_85e_100l_18_7k(self):
        draw_vis("30", "50.85", "100", "18.7", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m8x100-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_8d_14_38e_100l_5_3k(self):
        draw_vis("8", "14.38", "100", "5.3", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m8x70-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_8d_14_38e_70l_5_3k(self):
        draw_vis("8", "14.38", "70", "5.3", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m5x10-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_5d_8_79e_10l_3_5k(self):
        draw_vis("5", "8.79", "10", "3.5", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m8x110-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_8d_14_38e_110l_5_3k(self):
        draw_vis("8", "14.38", "110", "5.3", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m22x100-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_22d_35_72e_100l_14k(self):
        draw_vis("22", "35.72", "100", "14", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m22x70-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_22d_35_72e_70l_14k(self):
        draw_vis("22", "35.72", "70", "14", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m6x90-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_6d_11_05e_90l_4k(self):
        draw_vis("6", "11.05", "90", "4", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m6x70-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_6d_11_05e_70l_4k(self):
        draw_vis("6", "11.05", "70", "4", "metal")

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m22x60-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_22d_35_72e_60l_14k(self):
        draw_vis("22", "35.72", "60", "14", "metal")


class UnitTestsBasicPartsForFixationsForRondelle(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/visserie-nylon/rondelle-plate-nylon-naturel-pa6-6-din-125/rondelle-10-5x20x2-nylon-blanc-din-125.html
    def test_part_rondelle_nylon_10_5d_20D_2s(self):
        draw_rondelle("10.5", "20", "2", "nylon")

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/inox/rondelle-z-inox-a2-nfe-25513/rondelle-z-0-6-inox-a2.html
    def test_part_rondelle_inox_6_4d_12D_1_2s(self):
        draw_rondelle("6.4", "12", "1.2", "inox")

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-30-z-blanc-nfe-25513.html
    def test_part_rondelle_metal_31d_52D_4s(self):
        draw_rondelle("31", "52", "4", "metal")

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-22-z-blanc-nfe-25513.html
    def test_part_rondelle_metal_23d_40D_3s(self):
        draw_rondelle("23", "40", "3", "metal")


class UnitTestsBasicPartsForFixationsForEcrou(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-inox-a2-din-985/ecrou-nylstop-m10-inox-a2-din-985.html
    def test_part_ecrou_inox_10d_18_9e_10m(self):
        draw_ecrou("10", "18.9", "10", "inox")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-inox-a2-din-934/ecrou-hu-m6-inox-a2-din-934.html
    def test_part_ecrou_inox_6d_11_05e_5m(self):
        draw_ecrou("6", "11.05", "5", "inox")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m10-brut-din-934.html
    def test_part_ecrou_metal_10d_18_9e_8m(self):
        draw_ecrou("10", "18.9", "8", "metal")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m20-brut-din-934.html
    def test_part_ecrou_metal_20d_32_95e_16m(self):
        draw_ecrou("20", "32.95", "16", "metal")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m30-brut-din-934.html
    def test_part_ecrou_metal_30d_50_85e_30m(self):
        draw_ecrou("30", "50.85", "30", "metal")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m8-brut-din-934.html
    def test_part_ecrou_metal_8d_14_38e_6_5m(self):
        draw_ecrou("8", "14.38", "6.5", "metal")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m5-brut-din-934.html
    def test_part_ecrou_metal_5d_8_79e_4m(self):
        draw_ecrou("5", "8.79", "4", "metal")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m22-brut-din-934.html
    def test_part_ecrou_metal_22d_36e_18m(self):
        draw_ecrou("22", "36", "18", "metal")

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m6-brut-din-934.html
    def test_part_ecrou_metal_6d_11_05e_5m(self):
        draw_ecrou("6", "11.05", "5", "metal")


class UnitTestsBasicPartsForFixationsForTigeFiletee(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m3-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_acier_3d(self):
        draw_tige_filetee("3", "acier")

    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m20-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_acier_20d(self):
        draw_tige_filetee("20", "acier")


if __name__ == '__main__':
    unittest.main()
