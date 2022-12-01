import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsArchieBlueHydrogenGeneratorVersion5ForParts(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-inox-a2-din-934/ecrou-hu-m6-inox-a2-din-934.html
    def test_part_ecrou_inox_6m(self):
        print("test_part_ecrou_inox_6m")

        if os.path.exists("Scripts\\part_ecrou_inox_6m.py"):
            os.remove("Scripts\\part_ecrou_inox_6m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_inox_6m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_inox_6m"


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

# Parameters
d1 = 6
m = 5
e = 11.05
s = 10

cylinder_1 = Part.makeCylinder(e/2, m)

cylinder_2 = Part.makeCylinder(d1/2, m)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_inox_6m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_ecrou_inox_6m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_ecrou_inox_6m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_ecrou_inox_6m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.plexiglas-shop.com/fr/produits/plexiglas-xt/ro0a070gt.html?force_sid=hdhbk391d16to9fcfpc6scnai7
    def test_part_tank_d60_150l(self):
        print("test_part_tank_d60_150l")

        if os.path.exists("Scripts\\part_tank_d60_150l.py"):
            os.remove("Scripts\\part_tank_d60_150l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tank_d60_150l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tank_d60_150l"


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

# EPS = tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# Diametres du tank
diametre_exterieur = 60
diametre_interieur = 54

# Hauteur maximale du tank
hauteur_maximale = 150

cylinder_1 = Part.makeCylinder(diametre_exterieur/2, hauteur_maximale)

cylinder_2 = Part.makeCylinder(diametre_interieur/2, hauteur_maximale)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_tank_d60_150l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_tank_d60_150l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_tank_d60_150l_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_tank_d60_150l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m6x120-inox-a2-ef-din-933.html
    def test_part_vis_metal_inox_m6_120l(self):
        print("test_part_vis_metal_inox_m6_120l")

        if os.path.exists("Scripts\\part_vis_metal_inox_m6_120l.py"):
            os.remove("Scripts\\part_vis_metal_inox_m6_120l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_inox_m6_120l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_inox_m6_120l"


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

d1 = 6
e = 11.05
L = 120
k = 4

cylinder_1 = Part.makeCylinder(e/2, L + k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_vis_metal_inox_m6_120l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_vis_metal_inox_m6_120l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_vis_metal_inox_m6_120l_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_vis_metal_inox_m6_120l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m6x90-inox-a2-ef-din-933.html
    def test_part_vis_metal_inox_m6_90l(self):
        print("test_part_vis_metal_inox_m6_90l")

        if os.path.exists("Scripts\\part_vis_metal_inox_m6_90l.py"):
            os.remove("Scripts\\part_vis_metal_inox_m6_90l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_inox_m6_90l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_inox_m6_90l"


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

d1 = 6
e = 11.05
L = 90
k = 4

cylinder_1 = Part.makeCylinder(e/2, L + k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_vis_metal_inox_m6_90l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_vis_metal_inox_m6_90l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_vis_metal_inox_m6_90l_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_vis_metal_inox_m6_90l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/visserie-nylon/rondelle-plate-nylon-naturel-pa6-6-din-125/rondelle-6-4x12x1-6-nylon-blanc-din-125.html
    def test_part_rondelle_nylon_6m(self):
        print("test_part_rondelle_nylon_6m")

        if os.path.exists("Scripts\\part_rondelle_nylon_6m.py"):
            os.remove("Scripts\\part_rondelle_nylon_6m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_nylon_6m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_nylon_6m"


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

d1 = 6.4
d2 = 12
s = 1.6

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_nylon_6m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_rondelle_nylon_6m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_rondelle_nylon_6m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_rondelle_nylon_6m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.laserboost.com/stainless-steel/
    def test_part_capacitor_plate(self):
        print("test_part_capacitor_plate")

        if os.path.exists("Scripts\\part_capacitor_plate.py"):
            os.remove("Scripts\\part_capacitor_plate.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_capacitor_plate.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh, ImportGui, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_capacitor_plate"


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

e = 1
d_vis = 6
d_fixing = d_vis + e*3.5
epaisseur = 1

# Diametre exterieur du tank
diametre_exterieur_tank = 50

# Diametre interieur du tank
diametre_interieur_tank = 44

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_interieur_tank - (e+1)*2

cylinder_1 = Part.makeCylinder(diametre_maximal_capacitor_plate/2, epaisseur)

# cylinder_1 cut by cylinder_2
cylinder_2 = Part.makeCylinder(d_vis/2, epaisseur)
cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for supporting the capacitor plate
degre = 0
radius = diametre_maximal_capacitor_plate/2 - e - d_vis/2
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(d_fixing/2, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes and the cathodes
degre = 90
radius = diametre_maximal_capacitor_plate/2 - e - d_vis/2
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(d_vis/2, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for supporting the capacitor plate
degre = 180
radius = diametre_maximal_capacitor_plate/2 - e - d_vis/2
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(d_fixing/2, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for supporting the capacitor plate
degre = 270
radius = diametre_maximal_capacitor_plate/2 - e - d_vis/2
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(d_fixing/2, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_capacitor_plate").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_capacitor_plate.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_capacitor_plate.dxf"

importDXF.export(__objs__, dxf_file)

del __objs__

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_capacitor_plate_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_capacitor_plate.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/materiaux/materiaux-sls/materiau-plastique/
    def test_part_bottom_support_capacitor_plate(self):
        print("test_part_bottom_support_capacitor_plate")

        if os.path.exists("Scripts\\part_bottom_support_capacitor_plate.py"):
            os.remove("Scripts\\part_bottom_support_capacitor_plate.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_bottom_support_capacitor_plate.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, math, Mesh, ImportGui, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support_capacitor_plate"


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

e = 1
d_vis = 6
d_fixing = d_vis + e*2
epaisseur = 3

# Diametre exterieur du tank
diametre_exterieur_tank = 50

# Diametre interieur du tank
diametre_interieur_tank = 44

# Diametre maximal du bottom capacitor plate
diametre_maximal_bottom_capacitor_plate = diametre_interieur_tank - (e+1)*2

cylinder_1 = Part.makeCylinder(diametre_maximal_bottom_capacitor_plate/2, epaisseur)

cylinder_2 = Part.makeCylinder(d_vis, epaisseur)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the capacitor plates
degre = 45
for i in range(int(360/degre)):
    radius = diametre_maximal_bottom_capacitor_plate/2 - e - d_vis/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis/2, epaisseur)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_bottom_support_capacitor_plate").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_bottom_support_capacitor_plate.stl"

Mesh.export(__objs__, stl_file)

del __objs__

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_bottom_support_capacitor_plate_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_bottom_support_capacitor_plate.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/manchon-laiton-femelle-8-13-84494635.html
    def test_part_manchon_8_13_f(self):
        print("test_part_manchon_8_13_f")

        if os.path.exists("Scripts\\part_manchon_8_13_f.py"):
            os.remove("Scripts\\part_manchon_8_13_f.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_manchon_8_13_f.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_manchon_8_13_f"


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

diametre_interieur = 14

diametre_exterieur = diametre_interieur + 2*2

hauteur_maximale = 18

cylinder_1 = Part.makeCylinder(diametre_exterieur/2, hauteur_maximale)

cylinder_2 = Part.makeCylinder(diametre_interieur/2, hauteur_maximale)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_manchon_8_13_f").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_manchon_8_13_f.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_manchon_8_13_f_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_manchon_8_13_f.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-mamelons-a-visser-laiton-m-8-x-13-pour-tube-en-cuivre-65814203.html
    def test_part_mamelon_a_visser_8_13_m(self):
        print("test_part_mamelon_a_visser_8_13_m")

        if os.path.exists("Scripts\\part_mamelon_a_visser_8_13_m.py"):
            os.remove("Scripts\\part_mamelon_a_visser_8_13_m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_mamelon_a_visser_8_13_m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_mamelon_a_visser_8_13_m"


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
EPS_C = EPS * -0.5

diametre_exterieur = 14

diametre_interieur = 8

diametre_exterieur_maximal = 18

hauteur_maximale = 14

cylinder_1 = Part.makeCylinder(diametre_exterieur_maximal/2, hauteur_maximale)

cylinder_2 = Part.makeCylinder(diametre_interieur/2, hauteur_maximale)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_exterieur_maximal/2, (hauteur_maximale - 3)/2)

cylinder_4 = Part.makeCylinder(diametre_exterieur/2, (hauteur_maximale - 3)/2)

cylinder_3 = cylinder_3.cut(cylinder_4)

cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_3_vector = FreeCAD.Vector(0, 0, (hauteur_maximale - 3)/2 + 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_mamelon_a_visser_8_13_m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_mamelon_a_visser_8_13_m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_mamelon_a_visser_8_13_m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_mamelon_a_visser_8_13_m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/materiaux/materiaux-sls/materiau-plastique/
    def test_part_bottom_support(self):
        print("test_part_bottom_support")

        if os.path.exists("Scripts\\part_bottom_support.py"):
            os.remove("Scripts\\part_bottom_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_bottom_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support"


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
EPS = 0.3
EPS_C = EPS * -0.5

l_tank = 150

l_vis_6m = 90

e = l_tank - 100

e1 = e - 5

d_vis_6m = 6 + EPS

e_vis_6m = 11.05

d_m_tank = 60

d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + e_vis_6m*2 + (e - e1)*2

cylinder_1 = Part.makeCylinder(d_m_b_s/2, e)

cylinder_2 = Part.makeCylinder((d_m_tank + 0.1*2)/2 , e1)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, e - e1)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(d_m_b_s/2, e1 - 5)

cylinder_4 = Part.makeCylinder((d_m_tank + (e - e1)*2)/2, e1 - 5)

# cylinder_4 cut by cylinder_3
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_3 cut by cylinder_1
cylinder_3_vector = FreeCAD.Vector(0, 0, e - e1)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degre = 30
for i in range(int(360/degre)):
    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 0
    hole_vector = FreeCAD.Vector(x, y, z)
    hole = Part.makeCylinder(d_vis_6m/2, e)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_bottom_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_bottom_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_bottom_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_bottom_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/materiaux/materiaux-sls/materiau-plastique/
    def test_part_top_support(self):
        print("test_part_top_support")

        if os.path.exists("Scripts\\part_top_support.py"):
            os.remove("Scripts\\part_top_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_top_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support"


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
EPS = 0.3
EPS_C = EPS * -0.5

l_tank = 150

l_vis_6m = 90

e = l_tank - 100

e1 = e - 5

d_vis_6m = 6 + EPS

e_vis_6m = 11.05

d_m_tank = 60

d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + e_vis_6m*2 + (e - e1)*2

cylinder_1 = Part.makeCylinder(d_m_b_s/2, e)

cylinder_2 = Part.makeCylinder((d_m_tank + 0.1*2)/2 , e - 3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(d_m_b_s/2, e1)

cylinder_4 = Part.makeCylinder((d_m_tank + (e - e1)*2)/2, e1)

# cylinder_4 cut by cylinder_3
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 0)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# cylinder_1 cut by cylinder_5 for the input of water and the output of gas
cylinder_5 = Part.makeCylinder(14/2, e)
cylinder_1 = cylinder_1.cut(cylinder_5)

# holes for fixing the tank
degre = 30
for i in range(int(360/degre)):
    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 0
    hole_vector = FreeCAD.Vector(x, y, z)
    hole = Part.makeCylinder(d_vis_6m/2, e)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Diametre interieur du tank
diametre_interieur_tank = 44

e_c_p = 1

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_interieur_tank - (e_c_p+1)*2

# holes for fixing the bottom capacitor plate 
degre = 180
for i in range(int(360/degre)):
    radius = diametre_maximal_capacitor_plate/2 - e_c_p - d_vis_6m/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 0
    hole_vector = FreeCAD.Vector(x, y, z)
    hole = Part.makeCylinder(d_vis_6m/2, e)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_top_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_top_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_top_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsArchieBlueHydrogenGeneratorVersion5ForAssemblies(unittest.TestCase):
    # ok
    def test_assembly_bottom(self):
        print("test_assembly_bottom")

        if os.path.exists("Scripts\\assembly_bottom.py"):
            os.remove("Scripts\\assembly_bottom.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_bottom.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_bottom"


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

__objs__ = []

# For placing part_bottom_support
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_bottom_support.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_bottom_support").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support"))

# For placing part_tank_d60_150l
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_tank_d60_150l.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_tank_d60_150l").Placement = App.Placement(App.Vector(0, 0, 5), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_tank_d60_150l").ShapeColor = (0.90,6.00,0.30)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_tank_d60_150l"))

l_tank = 150
l_vis_6m = 90
e = l_tank - 100
e1 = e - 5
d_vis = 6
e_vis_6m = 11.05
d_m_tank = 60
d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + e_vis_6m*2 + (e - e1)*2
s_rondelle_nylon_6m = 1.6
degre = 30
number_of_holes = int(360/degre)

# Insertion part_rondelle_nylon_6m
for i1 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_rondelle_nylon_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e - 5 - s_rondelle_nylon_6m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion part_rondelle_nylon_6m
for i1 in range(number_of_holes, number_of_holes*2):
    doc = "assembly_bottom"
    file = "part_rondelle_nylon_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion part_ecrou_inox_6m
for i2 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_ecrou_inox_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e + s_rondelle_nylon_6m
    color = (0.30,0.30,0.30)

    if i2 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# Insertion part_ecrou_inox_6m
for i2 in range(number_of_holes, number_of_holes*2):
    doc = "assembly_bottom"
    file = "part_ecrou_inox_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e + s_rondelle_nylon_6m + s_rondelle_nylon_6m*10
    color = (0.30,0.30,0.30)

    if i2 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# For placing the part_vis_metal_inox_m6_90l
k = 4
for i3 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_vis_metal_inox_m6_90l"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i3*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e - 5 - k - s_rondelle_nylon_6m
    color = (0.30,0.70,0.70)

    if i3 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i3)))

setview()

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/assembly_bottom.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\assembly_bottom_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\assembly_bottom.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_top(self):
        print("test_assembly_top")

        if os.path.exists("Scripts\\assembly_top.py"):
            os.remove("Scripts\\assembly_top.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_top.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_top"


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

__objs__ = []

# For placing the part_top_support
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_top_support.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_top_support").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_top_support").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_top_support"))

l_tank = 150
l_vis_6m = 90
e = l_tank - 100
e1 = e - 5
d_vis_6m = 6
e_vis_6m = 11.05
d_m_tank = 60
d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + e_vis_6m*2 + (e - e1)*2
s_rondelle_nylon_6m = 1.6
number_of_holes = int(360/degre)
h_ecrou_inox_6m = 4.6

# Diametre interieur du tank
diametre_interieur_tank = 44

e_c_p = 1

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_interieur_tank - (e_c_p+1)*2

degre = 30
# Insertion the part_rondelle_nylon_6m
for i1 in range(0, number_of_holes):
    doc = "assembly_top"
    file = "part_rondelle_nylon_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e - 5 - s_rondelle_nylon_6m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    elif 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_6m
degre1 = 180
for i1 in range(number_of_holes, number_of_holes+2):
    doc = "assembly_top"
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e_c_p - d_vis_6m/2
    alpha=(i1*degre1*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 3
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    elif 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_6m
degre1 = 180
for i1 in range(number_of_holes+2, number_of_holes+4):
    doc = "assembly_top"
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e_c_p - d_vis_6m/2
    alpha=(i1*degre1*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_nylon_6m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    elif 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion the part_ecrou_inox_6m
for i2 in range(0, number_of_holes):
    doc = "assembly_top"
    file = "part_ecrou_inox_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e - 5 - s_rondelle_nylon_6m - h_ecrou_inox_6m - 0.4
    color = (0.90,0.90,0.00)

    if i2 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    elif 1 <= i2 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

degre1 = 180
for i2 in range(number_of_holes, number_of_holes+2):
    doc = "assembly_top"
    file = "part_ecrou_inox_6m"

    radius = diametre_maximal_capacitor_plate/2 - e_c_p - d_vis_6m/2
    alpha=(i2*degre1*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_nylon_6m - h_ecrou_inox_6m - 0.4
    color = (0.90,0.90,0.00)

    if i2 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    elif 1 <= i2 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

degre1 = 180
for i2 in range(number_of_holes + 2, number_of_holes + 4):
    doc = "assembly_top"
    file = "part_ecrou_inox_6m"

    radius = diametre_maximal_capacitor_plate/2 - e_c_p - d_vis_6m/2
    alpha=(i2*degre1*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 3 + s_rondelle_nylon_6m
    color = (0.90,0.90,0.00)

    if i2 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    elif 1 <= i2 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# Insertion the part_manchon_8_13_f
doc = "assembly_top"
file = "part_manchon_8_13_f"
x = 0
y = 0
z = - 18
color = (0.90,0.00,0.90)
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(doc).getObject(file))

# Insertion the part_mamelon_a_visser_8_13_m
doc = "assembly_top"
file = "part_mamelon_a_visser_8_13_m"
x = 0
y = 0
z = - ((14 - 3)/2 - 3)
color = (0.10,0.10,0.90)
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(doc).getObject(file))

setview()

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/assembly_top.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\assembly_top_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\assembly_top.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_capacitors(self):
        print("test_assembly_capacitors")

        if os.path.exists("Scripts\\assembly_capacitors.py"):
            os.remove("Scripts\\assembly_capacitors.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_capacitors.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_capacitors"


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
EPS = 0.30
EPS_C = EPS * -0.5

__objs__ = []

# Diametre maximal du tank
diametre_maximal_tank = 50

# Diametre maximal
diametre_maximal = diametre_maximal_tank - 3*2 - 5*2

e = 3
d1 = 10 + EPS

s_rondelle_nylon_6m = 1.6
h_ecrou_nylon_6m = 4.6
h_ecrou_inox_6m = 5
e_capacitor_plate = 1
d_vis_6m = 6

e1 = 1

# Diametre interieur du tank
diametre_interieur_tank = 44

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_interieur_tank - (e1+1)*2

l_vis_60 = 60
number_of_capacitors = int((l_vis_60 - e - s_rondelle_nylon_6m*2 - h_ecrou_inox_6m)/(e_capacitor_plate + s_rondelle_nylon_6m))

# For placing the part_bottom_support_capacitor_plate
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_bottom_support_capacitor_plate.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate"))

# Insertion the part_rondelle_nylon_6m
degre = 90
for i1 in range(0, 4):
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_nylon_6m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_6m
degre = 90
for i1 in range(4, 8):
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_inox_6m
degre = 90
for i1 in range(0, 4):
    file = "part_ecrou_inox_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e + s_rondelle_nylon_6m
    color = (0.40,0.50,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# For placing the part_vis_metal_inox_m6_120l
k = 4
degre = 180
for i3 in range(0, 2):
    file = "part_vis_metal_inox_m6_120l"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(i3*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_nylon_6m - k
    color = (0.30,0.30,0.60)

    if i3 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)))

# For placing the part_vis_nylon_m6_60l
k = 3.9
degres = [90, 270]
i3 = 0
for degre in degres:
    file = "part_vis_nylon_m6_60l"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_nylon_6m - k
    color = (0.30,0.60,0.60)

    if i3 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)))

    i3 += 1

# Insertion the part_rondelle_nylon_6m
degre = 0
for i1 in range(8, number_of_capacitors + 4):
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_nylon_6m + h_ecrou_inox_6m) + (s_rondelle_nylon_6m + e_capacitor_plate)*(i1 - (8))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_6m
degre = 90
for i1 in range(number_of_capacitors + 4, number_of_capacitors*2):
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_nylon_6m + h_ecrou_inox_6m) + (s_rondelle_nylon_6m + e_capacitor_plate)*(i1 - (number_of_capacitors + 4))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_6m
degre = 180
for i1 in range(number_of_capacitors*2, number_of_capacitors*3 - 4):
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_nylon_6m + h_ecrou_inox_6m) + (s_rondelle_nylon_6m + e_capacitor_plate)*(i1 - (number_of_capacitors*2))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_6m
degre = 270
for i1 in range(number_of_capacitors*3 - 4, number_of_capacitors*4 - 8):
    file = "part_rondelle_nylon_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_nylon_6m + h_ecrou_inox_6m) + (s_rondelle_nylon_6m + e_capacitor_plate)*(i1 - (number_of_capacitors*3 - 4))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_inox_6m
degre = 90
for i1 in range(4, 8):
    file = "part_ecrou_inox_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_nylon_6m + h_ecrou_inox_6m) + (s_rondelle_nylon_6m + e_capacitor_plate)*(number_of_capacitors - 4) - e_capacitor_plate
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_capacitor_plate
for i1 in range(0, number_of_capacitors - 5):
    file = "part_capacitor_plate"

    x = 0
    y = 0
    z = (e + s_rondelle_nylon_6m + h_ecrou_inox_6m + s_rondelle_nylon_6m) + (s_rondelle_nylon_6m + e_capacitor_plate)*i1
    color = (0.50,0.50,0.00)

    angle_rotation = 0

    if i1 == 0 or i1 % 2 == 0:
        angle_rotation = 90
    else:
        angle_rotation = -90

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_inox_6m
degre = 90
for i1 in range(8, 12):
    file = "part_ecrou_inox_6m"

    radius = diametre_maximal_capacitor_plate/2 - e1 - d_vis_6m/2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_nylon_6m + h_ecrou_inox_6m) + (s_rondelle_nylon_6m + e_capacitor_plate)*(number_of_capacitors - 4) - e_capacitor_plate + h_ecrou_inox_6m
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

setview()

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + DOC_NAME + ".stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\assembly_capacitors_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\assembly_capacitors.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_global(self):
        print("test_assembly_global")

        if os.path.exists("Scripts\\assembly_global.py"):
            os.remove("Scripts\\assembly_global.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_global.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global"


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

__objs__ = []

# For placing the assembly_bottom
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/assembly_bottom.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_bottom").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_bottom").ShapeColor = (0.30,0.60,0.90)
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_bottom").Transparency = 0
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_bottom"))

# For placing the assembly_top
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/assembly_top.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_top").Placement = App.Placement(App.Vector(0, 0, 150 + 8), App.Rotation(App.Vector(0,1,0), 180))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_top").ShapeColor = (0.60,0.90,0.30)
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_top").Transparency = 0
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_top"))

# For placing the assembly_capacitors
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/assembly_capacitors.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_capacitors").Placement = App.Placement(App.Vector(0, 0, 55), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_capacitors").ShapeColor = (0.90,0.30,0.60)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_capacitors"))

setview()

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + DOC_NAME + ".stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\assembly_global_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\assembly_global.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsArchieBlueHydrogenGeneratorVersion5ForPartsTrash(unittest.TestCase):
    # ok
    # https://www.plexiglas-shop.com/fr/produits/plexiglas-xt/ro0a070gt.html?force_sid=hdhbk391d16to9fcfpc6scnai7
    def test_part_tank_d40_150l(self):
        print("test_part_tank_d40_150l")

        if os.path.exists("Scripts\\part_tank_d40_150l.py"):
            os.remove("Scripts\\part_tank_d40_150l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tank_d40_150l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

    DOC = FreeCAD.activeDocument()

    DOC_NAME = "part_tank_d40_150l"


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

    # EPS = tolerance to use to cut the parts
    EPS = 0.10
    EPS_C = EPS * -0.5

    # Diametres du tank
    diametre_exterieur = 40
    diametre_interieur = 34

    # Hauteur maximale du tank
    hauteur_maximale = 150

    cylinder_1 = Part.makeCylinder(diametre_exterieur/2, hauteur_maximale)

    cylinder_2 = Part.makeCylinder(diametre_interieur/2, hauteur_maximale)

    # cylinder_1 cut by cylinder_2
    cylinder_1 = cylinder_1.cut(cylinder_2)

    Part.show(cylinder_1)

    DOC.recompute()

    __objs__=[]

    __objs__.append(FreeCAD.getDocument("part_tank_d40_150l").getObject("Shape"))

    stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_tank_d40_150l.stl"

    Mesh.export(__objs__, stl_file)

    setview()

    # Generate PNG files
    file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_tank_d40_150l_'
    # Ombré
    Gui.runCommand('Std_DrawStyle',5)
    i = 1
    Gui.activeDocument().activeView().viewIsometric()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewFront()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewTop()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRight()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRear()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewBottom()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewLeft()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    # Filaire
    Gui.runCommand('Std_DrawStyle',2)
    i += 1
    Gui.activeDocument().activeView().viewIsometric()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewFront()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewTop()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRight()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRear()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewBottom()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewLeft()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_tank_d40_150l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.plexiglas-shop.com/fr/produits/plexiglas-xt/ro0a070gt.html?force_sid=hdhbk391d16to9fcfpc6scnai7
    def test_part_tank_d50_150l(self):
        print("test_part_tank_d50_150l")

        if os.path.exists("Scripts\\part_tank_d50_150l.py"):
            os.remove("Scripts\\part_tank_d50_150l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tank_d50_150l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

    DOC = FreeCAD.activeDocument()

    DOC_NAME = "part_tank_d50_150l"


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

    # EPS = tolerance to use to cut the parts
    EPS = 0.10
    EPS_C = EPS * -0.5

    # Diametres du tank
    diametre_exterieur = 50
    diametre_interieur = 44

    # Hauteur maximale du tank
    hauteur_maximale = 150

    cylinder_1 = Part.makeCylinder(diametre_exterieur/2, hauteur_maximale)

    cylinder_2 = Part.makeCylinder(diametre_interieur/2, hauteur_maximale)

    # cylinder_1 cut by cylinder_2
    cylinder_1 = cylinder_1.cut(cylinder_2)

    Part.show(cylinder_1)

    DOC.recompute()

    __objs__=[]

    __objs__.append(FreeCAD.getDocument("part_tank_d50_150l").getObject("Shape"))

    stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_tank_d50_150l.stl"

    Mesh.export(__objs__, stl_file)

    setview()

    # Generate PNG files
    file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_tank_d50_150l_'
    # Ombré
    Gui.runCommand('Std_DrawStyle',5)
    i = 1
    Gui.activeDocument().activeView().viewIsometric()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewFront()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewTop()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRight()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRear()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewBottom()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewLeft()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    # Filaire
    Gui.runCommand('Std_DrawStyle',2)
    i += 1
    Gui.activeDocument().activeView().viewIsometric()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewFront()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewTop()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRight()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewRear()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewBottom()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

    i += 1
    Gui.activeDocument().activeView().viewLeft()
    Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_tank_d50_150l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/visserie-nylon/tete-cylindrique-fendue-tc-din-84-nylon-pa6-6-naturel/tc-m6x60-pa6-6-blanc-din-84.html
    def test_part_vis_nylon_m6_60l(self):
        print("test_part_vis_nylon_m6_60l")

        if os.path.exists("Scripts\\part_vis_nylon_m6_60l.py"):
            os.remove("Scripts\\part_vis_nylon_m6_60l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_nylon_m6_60l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_nylon_m6_60l"


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

d1 = 6
d2 = 10
L = 60
k = 3.9

cylinder_1 = Part.makeCylinder(d2/2, L + k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(d2/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_vis_nylon_m6_60l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_vis_nylon_m6_60l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_vis_nylon_m6_60l_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_vis_nylon_m6_60l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-manchons-a-visser-laiton-f-12-x-17-pour-tube-en-cuivre-65815253.html
    def test_part_manchon_a_visser_12_17_f(self):
        print("test_part_manchon_a_visser_12_17_f")

        if os.path.exists("Scripts\\part_manchon_a_visser_12_17_f.py"):
            os.remove("Scripts\\part_manchon_a_visser_12_17_f.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_manchon_a_visser_12_17_f.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_manchon_a_visser_12_17_f"


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
EPS_C = EPS * -0.5

diametre_maximal = 22

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 18)

cylinder_2 = Part.makeCylinder(16.4/2, 18)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_manchon_a_visser_12_17_f").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_manchon_a_visser_12_17_f.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_manchon_a_visser_12_17_f_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_manchon_a_visser_12_17_f.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-mamelons-a-visser-laiton-m-12-x-17-pour-tube-en-cuivre-65814231.html
    def test_part_manchon_a_visser_12_17_m(self):
        print("test_part_manchon_a_visser_12_17_m")

        if os.path.exists("Scripts\\part_manchon_a_visser_12_17_m.py"):
            os.remove("Scripts\\part_manchon_a_visser_12_17_m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_manchon_a_visser_12_17_m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_manchon_a_visser_12_17_m"


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
EPS_C = EPS * -0.5

diametre_maximal = 19

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 19)

cylinder_2 = Part.makeCylinder(11/2, 19)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 8)

cylinder_4 = Part.makeCylinder(16/2, 8)

cylinder_3 = cylinder_3.cut(cylinder_4)

cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_3_vector = FreeCAD.Vector(0, 0, 11)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_manchon_a_visser_12_17_m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_manchon_a_visser_12_17_m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_manchon_a_visser_12_17_m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_manchon_a_visser_12_17_m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/visserie-nylon/ecrou-hu-nylon-pa6-6-naturel-din-555/ecrou-hu-m6-pa6-6-blanc-din-555.html
    def test_part_ecrou_nylon_6m(self):
        print("test_part_ecrou_nylon_6m")

        if os.path.exists("Scripts\\part_ecrou_nylon_6m.py"):
            os.remove("Scripts\\part_ecrou_nylon_6m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_nylon_6m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_nylon_6m"


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

# Parameters
d1 = 6
m = 4.6
e = 10.89
s = 10

cylinder_1 = Part.makeCylinder(e/2, m)

cylinder_2 = Part.makeCylinder(d1/2, m)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_nylon_6m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_ecrou_nylon_6m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Png\\\\part_ecrou_nylon_6m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_5\\\\Scripts\\\\part_ecrou_nylon_6m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
