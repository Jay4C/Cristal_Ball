import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# Function for creating each disc magnet
def draw_disc(de, h, type):
    filename = "part_p_m_d_de" + de.replace(".", "_") + "_" + h.replace(".", "_") + "h_" + type

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

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Neodyme\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each ring magnet
def draw_ring(D1, D2, h, type):
    filename = "part_p_m_r_1D" + D1.replace(".", "_") + "_2D" + D2.replace(".", "_") + "_" + h.replace(".", "_") + "h_" + type

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

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Neodyme\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each cuboide magnet
def draw_cuboide(l, w, h, type):
    filename = "part_p_m_co_l" + l.replace(".", "_") + "_w" + w.replace(".", "_") + "_" + h.replace(".", "_") + "h_" + type

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

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Neodyme\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each cube magnet
def draw_cube(l, type):
    filename = "part_p_m_c_" + l.replace(".", "_") + "l_" + type

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

        file.write("""
box_1 = Part.makeBox(l, l, l)

Part.show(box_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Neodyme\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each cylinder magnet
def draw_cylinder(d, h, type):
    filename = "part_p_m_cy_d" + d.replace(".", "_") + "_" + h.replace(".", "_") + "h_" + type

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

        file.write("h = " + h + "\n")

        file.write("""
cylinder_1 = Part.makeCylinder(d/2, h)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Neodyme\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each cylinder magnet
def draw_cone(d1, d2, h, type):
    filename = "part_p_m_cone_1D" + d1.replace(".", "_") + "_2D" + d2.replace(".", "_") + "_" + h.replace(".", "_") + "h_" + type

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

        file.write("d1 = " + d1 + "\n")

        file.write("d2 = " + d2 + "\n")

        file.write("h = " + h + "\n")

        file.write("""
cone = Part.makeCone(d1/2, d2/2, h)

Part.show(cone)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Neodyme\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


# Function for creating each sphere magnet
def draw_sphere(d1, type):
    filename = "part_p_m_sphere_" + d1.replace(".", "_") + "_1D_" + type

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

        file.write("d1 = " + d1 + "\n")

        file.write("""
sphere = Part.makeSphere(d1/2)

Part.show(sphere)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/' + filename + '.stl" \n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\4_Basics\\\\Permanent_Magnets\\\\Neodyme\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsPermanentMagnetsForDisk(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/aimants-en-neodyme/disques-magnetiques-1.0-x-1.0-mm-n45-nickel-adherence-25-g
    def test_part_p_m_d_de8_2h_n(self):
        draw_disc("1", "1", "n")


class UnitTestsPermanentMagnetsForRings(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/neodyme/anneaux-aimantes/anneau-6.0-x-2.0-x-2.0-mm-n45-dore-adherence-650-g
    def test_part_p_m_r_1D6_2D2_2h_n(self):
        draw_ring("6", "2", "2", "n")

    # ok
    # https://www.aimant-boutique.fr/neodyme/anneaux-aimantes/anneau-20.0-x-10.0-x-6.0-mm-n44-nickele-adherence-7-kg
    def test_part_p_m_r_1D20_2D10_6h_n(self):
        draw_ring("20", "10", "6", "n")

    # ok
    # https://www.aimant-boutique.fr/neodyme/anneaux-aimantes/anneau-15.0-x-10.0-x-2.0-mm-n40-nickele-adherence-800-g
    def test_part_p_m_r_1D15_2D10_2h_n(self):
        draw_ring("15", "10", "2", "n")

    # ok
    # https://www.aimant-boutique.fr/neodyme/anneaux-aimantes/anneau-18.0-x-10.0-x-4.0-mm-n40-nickele-adherence-2.5-kg
    def test_part_p_m_r_1D18_2D10_4h_n(self):
        draw_ring("18", "10", "4", "n")

    # ok
    # https://www.aimant-boutique.fr/neodyme/anneaux-aimantes/anneau-15.0-x-8.0-x-6.0-mm-n42-nickele-adherence-5-kg
    def test_part_p_m_r_1D15_2D8_6h_n(self):
        draw_ring("15", "8", "6", "n")


class UnitTestsPermanentMagnetsForCuboides(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/neodyme/parallelepipedes-aimantes/cuboide-5.0-x-3.0-x-2.0-mm-n52-dore-adherence-550-g
    def test_part_p_m_co_l5_w3_2h_n(self):
        draw_cuboide("5", "3", "2", "n")


class UnitTestsPermanentMagnetsForCubes(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/neodyme/cubes-aimantes/cube-2.0-x-2.0-x-2.0-mm-n45-nickele-adherence-100-g
    def test_part_p_m_c_2l_n(self):
        draw_cube("2", "n")

    # ok
    # https://www.aimant-boutique.fr/neodyme/cubes-aimantes/cube-8.0-x-8.0-x-8.0-mm-n40-nickele-adherence-4-kg
    def test_part_p_m_c_8l_n(self):
        draw_cube("8", "n")


class UnitTestsPermanentMagnetsForCylinders(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/aimants-en-neodyme/cylindre-magnetiques/2431/cylindre-magnetique-oe-2-0-x-4-0-mm-n45-nickel-adherence-280-g
    def test_part_p_m_cy_d2_4h_n(self):
        draw_cylinder("2", "4", "n")


class UnitTestsPermanentMagnetsForCones(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/neodyme/cones-aimantes/cone-15.08.0-x-6.0-mm-n42-nickele-adherence-5-kg
    def test_part_p_m_cone_1D15_2D8_6h_n(self):
        draw_cone("15", "8", "6", "n")


class UnitTestsPermanentMagnetsForSpheres(unittest.TestCase):
    # ok
    # https://www.aimant-boutique.fr/neodyme/spheres-aimantees/sphere-3.0-mm-nickele-n40-adherence-130-g
    def test_part_p_m_sphere_3_1D_n(self):
        draw_sphere("3", "n")


if __name__ == '__main__':
    unittest.main()
