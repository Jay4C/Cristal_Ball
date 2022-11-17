import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# Function for creating each full square pipe
def draw_full_square_pipe(l, h):
    filename = "part_f_s_p_" + l.replace(".", "_") + "l_" + h.replace(".", "_") + "h"

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

        file.write('h = ' + h + '\n')

        file.write("""
box_1 = Part.makeBox(l, h, h)

Part.show(box_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Pipes\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each full ring pipe
def draw_full_ring_pipe(d, h):
    filename = "part_f_r_p_" + d.replace(".", "_") + "d_" + h.replace(".", "_") + "h"

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

        file.write("r = " + str(int(d)/2) + "\n")

        file.write('h = ' + h + '\n')

        file.write("""
cylinder = Part.makeCylinder(r, h)

Part.show(cylinder)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Pipes\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each holed square pipe
def draw_holed_square_pipe(l, h, e):
    filename = "part_h_s_p_" + l.replace(".", "_") + "l_" + h.replace(".", "_") + "h_" + e.replace(".", "_") + "e"

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

        file.write('h = ' + h + '\n')

        file.write('e = ' + e + '\n')

        file.write("""
box_1 = Part.makeBox(l, h, h)

# Cut box_1 by box_2
box_2 = Part.makeBox(l, h - e*2, h - e*2)
box_2_vector = FreeCAD.Vector(0, e, e)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

Part.show(box_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Pipes\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each holed ring pipe
def draw_holed_ring_pipe(l, d, e):
    filename = "part_h_r_p_" + l.replace(".", "_") + "l_" + d.replace(".", "_") + "d_" + e.replace(".", "_") + "e"

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

        file.write('r = ' + str(int(d)/2) + '\n')

        file.write("e = " + e + "\n")

        file.write("""
cylinder_1 = Part.makeCylinder(r, l)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(r - e, l)
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Pipes\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsBasicPartsForFullSquarePipes(unittest.TestCase):
    # ok
    # https://www.commentfer.fr/fer-carre-acier/897-2655-fer-carre-plein-lamine-acier-8x8-mm-3701102707879.html#/25-longueur_en_metre-1_metre/577-section-8_x_8_mm
    def test_part_f_s_p_200l_8h(self):
        draw_full_square_pipe("200", "8")

    # ok
    # https://www.commentfer.fr/fer-carre-acier/897-2655-fer-carre-plein-lamine-acier-8x8-mm-3701102707879.html#/25-longueur_en_metre-1_metre/577-section-8_x_8_mm
    def test_part_f_s_p_100l_8h(self):
        draw_full_square_pipe("100", "8")


class UnitTestsBasicPartsForFullRingPipes(unittest.TestCase):
    # ok
    # https://www.commentfer.fr/fer-rond-acier/821-2568-rond-acier-etire-5-mm-3701102716758.html#/25-longueur_en_metre-1_metre/615-section-5_mm
    def test_part_f_r_p_5d_80h(self):
        draw_full_ring_pipe("5", "80")

    # ok
    # https://www.commentfer.fr/fer-rond-acier/825-2572-rond-acier-etire-6-mm-3701102716796.html#/25-longueur_en_metre-1_metre/616-section-6_mm
    def test_part_f_r_p_6d_100h(self):
        draw_full_ring_pipe("6", "100")


class UnitTestsBasicPartsForHoledSquarePipes(unittest.TestCase):
    # ok
    # https://www.commentfer.fr/tube-acier-carre/1802-3293-tube-carre-acier-16-x-16-3701102713443.html#/25-longueur_en_metre-1_metre/43-epaisseur-15_mm/582-section-16_x_16_mm
    def test_part_h_s_p_50l_16h_1_5e(self):
        draw_holed_square_pipe("50", "16", "1.5")


class UnitTestsBasicPartsForHoledRingPipes(unittest.TestCase):
    # ok
    # https://www.commentfer.fr/tube-acier-rond/1862-3353-tube-acier-rond-diametre-16-3701102718998.html#/25-longueur_en_metre-1_metre/43-epaisseur-15_mm/624-section-16_mm
    def test_part_h_r_p_50l_16d_1_5e(self):
        draw_holed_ring_pipe("50", "16", "1.5")


if __name__ == '__main__':
    unittest.main()
