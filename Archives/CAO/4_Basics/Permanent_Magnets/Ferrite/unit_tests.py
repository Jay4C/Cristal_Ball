import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# Function for creating each disc magnet
def draw_disc(de, h, filename):
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

        file.write("De = " + de + "\n")

        file.write('h = ' + h + '\n')

        file.write("""
cylinder_1 = Part.makeCylinder(De/2, h)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Ferrite\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each ring magnet
def draw_ring(D1, D2, h):
    filename = "part_p_m_r_1D" + D1.replace(".", "_") + "_2D" + D2.replace(".", "_") + "_" + h.replace(".", "_") + "h"

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

        file.write("D1 = " + D1 + "\n")

        file.write("D2 = " + D2 + "\n")

        file.write('h = ' + h + '\n')

        file.write("""
cylinder_1 = Part.makeCylinder(D1/2, h)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(D2/2, h)
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Ferrite\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each cuboide magnet
def draw_cuboide(l, w, h):
    filename = "part_p_m_co_l" + l.replace(".", "_") + "_w" + w.replace(".", "_") + "_" + h.replace(".", "_") + "h"

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

        file.write("l = " + l + "\n")

        file.write("w = " + w + "\n")

        file.write('h = ' + h + '\n')

        file.write("""
box_1 = Part.makeBox(l, w, h)

Part.show(box_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Ferrite\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsPermanentMagnetsForDiskMagnets(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-8.0-x-2.0-mm-y30-ferrite-adherence-150-g
    def test_part_p_m_d_8mm_2mm_30y(self):
        draw_disc("8", "2", "part_p_m_d_8mm_2mm_30y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-10.2-x-4.0-mm-hf-24/16-ferrite
    def test_part_p_m_d_10_2mm_4mm_24_16hf(self):
        draw_disc("10.2", "4", "part_p_m_d_10_2mm_4mm_24_16hf")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-20.0-x-1.5-mm-y30-ferrite-adherence-200-g
    def test_part_p_m_d_20mm_1_5mm_30y(self):
        draw_disc("20", "1.5", "part_p_m_d_20mm_1_5mm_30y")

    # ok
    # https://www.aimant-boutique.fr/aimants-en-ferrite/disques-magnetiques/2973/disque-magnetique-en-ferrite-oe-12-7-x-3-0-mm-hf-24/16
    def test_part_p_m_d_12_7mm_3mm_24_16hf(self):
        draw_disc("12.7", "3", "part_p_m_d_12_7mm_3mm_24_16hf")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-15.0-x-3.0-mm-y30-ferrite-adherence-300-g
    def test_part_p_m_d_15mm_3mm_30y(self):
        draw_disc("15", "3", "part_p_m_d_15mm_3mm_30y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-10.0-x-7.0-mm-y35-ferrite-adh-350-g
    def test_part_p_m_d_10mm_7mm_35y(self):
        draw_disc("10", "7", "part_p_m_d_10mm_7mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-10.0-x-3.0-mm-y30-ferrite-adherence-250-g
    def test_part_p_m_d_10mm_3mm_30y(self):
        draw_disc("10", "3", "part_p_m_d_10mm_3mm_30y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-25.0-x-3.0-mm-hf-8/22-ferrite
    def test_part_p_m_d_25mm_3mm_35y(self):
        draw_disc("25", "3", "part_p_m_d_25mm_3mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-10.0-x-10.0-mm-y35-ferrite-adherence-400-g
    def test_part_p_m_d_10mm_10mm_35y(self):
        draw_disc("10", "10", "part_p_m_d_10mm_10mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-14.0-x-8.0-mm-y30-ferrite-adherence-450-g
    def test_part_p_m_d_14mm_8mm_30y(self):
        draw_disc("14", "8", "part_p_m_d_14mm_8mm_30y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-25.0-x-5.0-mm-y35-ferrite-adherence-900-g
    def test_part_p_m_d_25mm_5mm_35y(self):
        draw_disc("25", "5", "part_p_m_d_25mm_5mm_35y")

    # ok
    # https://www.aimant-boutique.fr/stock-restant/2897/cylindre-magnetique-oe-9-7-x-14-0-mm-ferrite-hf-28/26-anisotrope
    def test_part_p_m_d_9_7mm_14mm_28_26hf(self):
        draw_disc("9.7", "14", "part_p_m_d_25mm_5mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-15.0-x-5.0-mm-y35-ferrite-adherence-550-g
    def test_part_p_m_d_15mm_5mm_35y(self):
        draw_disc("15", "5", "part_p_m_d_15mm_14mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-20.0-x-6.0-mm-y30-ferrite-adherence-800-g
    def test_part_p_m_d_20mm_5mm_30y(self):
        draw_disc("20", "6", "part_p_m_d_20mm_5mm_30y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-25-x-8-mm-ferrite-y35-adherence-1.3-kg
    def test_part_p_m_d_25mm_8mm_35y(self):
        draw_disc("25", "8", "part_p_m_d_25mm_8mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-15.0-x-10.0-mm-y35-ferrite-adherence-750-g
    def test_part_p_m_d_15mm_10mm_35y(self):
        draw_disc("15", "10", "part_p_m_d_15mm_10mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-30.0-x-4.0-mm-y35-ferrite-adherence-800-g
    def test_part_p_m_d_30mm_4mm_35y(self):
        draw_disc("30", "4", "part_p_m_d_30mm_4mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-30.0-x-5.0-mm-hf-8/22-ferrite
    def test_part_p_m_d_30mm_5mm_y30bh(self):
        draw_disc("30", "5", "part_p_m_d_30mm_5mm_y30bh")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-36.0-x-6.5-mm-hf-24/16-ferrite
    def test_part_p_m_d_36mm_6_5mm_24_16hf(self):
        draw_disc("36", "6.5", "part_p_m_d_36mm_6_5mm_24_16hf")

    # ok
    # https://www.aimant-boutique.fr/aimants-en-ferrite/disques-magnetiques/2484/disque-magnetique-oe-27-0-x-15-0-mm-hf26/22-ferrite-offre
    def test_part_p_m_d_27mm_15mm_26_22hf(self):
        draw_disc("27", "15", "part_p_m_d_27mm_15mm_26_22hf")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-20.0-x-20.0-mm-y35-ferrite-adherence-1.7-kg
    def test_part_p_m_d_20mm_20mm_35y(self):
        draw_disc("20", "20", "part_p_m_d_20mm_20mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-26.0-x-13.0-mm-hf-24/16-ferrite
    def test_part_p_m_d_26mm_13mm_24_16hf(self):
        draw_disc("26", "13", "part_p_m_d_26mm_13mm_24_16hf")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-25.0-x-15.0-mm-y35-ferrite-adh-2.3-kg
    def test_part_p_m_d_25mm_15mm_35y(self):
        draw_disc("25", "15", "part_p_m_d_25mm_15mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-magnetique-29.25-x-10.5-mm-y35-ferrite-adh-2.5-kg
    def test_part_p_m_d_29_25mm_10_5mm_35y(self):
        draw_disc("29.25", "10.5", "part_p_m_d_29_25mm_10_5mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-25.0-x-20.0-mm-y35-ferrite
    def test_part_p_m_d_25mm_20mm_35y(self):
        draw_disc("25", "20", "part_p_m_d_25mm_20mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-50.0-x-10.0-mm-y30-ferrite-adherence-3-kg
    def test_part_p_m_d_50mm_10mm_30y(self):
        draw_disc("50", "10", "part_p_m_d_50mm_10mm_30y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-magnetique-50.0-x-15.0-mm-y35-ferrite-adh-4.1-kg
    def test_part_p_m_d_50mm_15mm_35y(self):
        draw_disc("50", "15", "part_p_m_d_50mm_15mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-40.0-x-20.0-mm-y35-ferrite-adherence-4.7-kg
    def test_part_p_m_d_40mm_20mm_35y(self):
        draw_disc("40", "20", "part_p_m_d_40mm_20mm_35y")

    # ok
    # https://www.aimant-boutique.fr/ferrite/disques-aimantes/disque-100.0-x-15.0-mm-y35-ferrite-adherence-11-kg
    def test_part_p_m_d_100mm_15mm_35y(self):
        draw_disc("100", "15", "part_p_m_d_100mm_15mm_35y")

    # ok
    # https://www.aimant-boutique.fr/aimants-en-ferrite/disques-magnetiques/2315/60-disques-magnetiques-oe-30-x-3-mm-ferrite-dure-hf28/16-vente
    def test_part_p_m_d_30mm_3mm_28_16hf(self):
        draw_disc("30", "3", "part_p_m_d_30mm_3mm_28_16hf")


class UnitTestsPermanentMagnetsForRings(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-11.0-x-2.7-x-4.5-mm-y35-ferrite-adherence-350-g
    def test_part_p_m_r_1D8_2D2_7_4_5h(self):
        draw_ring("11", "2.7", "4.5")

    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-20.0-x-6.0-x-5.0-mm-y35-ferrite-adh-750-g
    def test_part_p_m_r_1D20_2D6_5h(self):
        draw_ring("20", "6", "5")

    # ok
    # https://www.aimant-boutique.fr/aimants-en-ferrite/anneaux-magnetiques/1918/anneau-magnetique-oe-20-0-x-10-0-x-6-0-mm-y35-ferrite-adherence-780-g
    def test_part_p_m_r_1D20_2D10_6h(self):
        draw_ring("20", "10", "6")

    # ok
    # https://www.aimant-boutique.fr/aimants-en-ferrite/anneaux-magnetiques/2957/anneau-magnetique-oe-30-0-x-10-0-x-10-0-mm-y35-ferrite
    def test_part_p_m_r_1D30_2D10_10h(self):
        draw_ring("30", "10", "10")

    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-40.0-x-20.0-x-10.0-mm-y35-ferrite-adherence-2-kg
    def test_part_p_m_r_1D40_2D20_10h(self):
        draw_ring("40", "20", "10")

    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-140.0-x-60.0-x-20.0-mm-y30-ferrite
    def test_part_p_m_r_1D140_2D60_20h(self):
        draw_ring("140", "60", "20")

    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-45.0-x-22.0-x-9.0-mm-hf-24/16-ferrite
    def test_part_p_m_r_1D45_2D22_9h(self):
        draw_ring("45", "22", "9")


class UnitTestsPermanentMagnetsForCuboides(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/ferrite/parallelepipedes-aimantes/cuboide-7.0-x-7.0-x-4.0-mm-y35-ferrite
    def test_part_p_m_co_l7_w7_4h(self):
        draw_cuboide("7", "7", "4")


if __name__ == '__main__':
    unittest.main()
