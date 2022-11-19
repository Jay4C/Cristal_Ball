import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard
import time


# Homopolar generator
# https://patentimages.storage.googleapis.com/0c/c9/14/0e4d740f16793e/WO1995008210A1.pdf
class UnitsTestsHGVersion3Parts(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-8-8/tige-filetee-acier-8-8-brut-din-975/tige-filetee-m30-acier-8-8-brut-din-975.html
    def test_part_tige_filetee_m30_1000l(self):
        print("test_part_tige_filetee_m30_1000l")

        if os.path.exists("Scripts\\part_tige_filetee_m30_1000l.py"):
            os.remove("Scripts\\part_tige_filetee_m30_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tige_filetee_m30_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tige_filetee_m30_1000l"


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

# part_tige_filetee_m30_1000l
d1 = 30
L = 1000
part_tige_filetee_m30_1000l = Part.makeCylinder(d1/2, L)

Part.show(part_tige_filetee_m30_1000l)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tige_filetee_m30_1000l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_tige_filetee_m30_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_tige_filetee_m30_1000l_'
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

        pywinauto.mouse.click(button="left", coords=(round(665*1.5), round(695*1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60*1.5), round(615*1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_tige_filetee_m30_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m30-brut-din-934.html
    def test_part_ecrou_30m(self):
        print("test_part_ecrou_30m")

        if os.path.exists("Scripts\\part_ecrou_30m.py"):
            os.remove("Scripts\\part_ecrou_30m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_30m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_30m"


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

d1 = 30
e = d1*1.6
h = d1*0.8

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_30m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_ecrou_30m_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_ecrou_30m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-moyenne-m/inox/rondelle-m-inox-a2-nfe-25513/rondelle-m-0-30-inox-a2.html
    def test_part_rondelle_30m(self):
        print("test_part_rondelle_30m")

        if os.path.exists("Scripts\\part_rondelle_30m.py"):
            os.remove("Scripts\\part_rondelle_30m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_30m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_30m"


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

d1 = 31
d2 = 60
s = 4

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_30m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_rondelle_30m_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_rondelle_30m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m20x300-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m20_300l(self):
        print("test_part_vis_metal_m20_300l")

        if os.path.exists("Scripts\\part_vis_metal_m20_300l.py"):
            os.remove("Scripts\\part_vis_metal_m20_300l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m20_300l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m20_300l"


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

L = 300
k = 12.5
d1 = 20
e = 33.53

cylinder_1 = Part.makeCylinder(e/2, L+k)

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
__objs__.append(FreeCAD.getDocument("part_vis_metal_m20_300l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_vis_metal_m20_300l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_vis_metal_m20_300l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m20x200-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m20_200l(self):
        print("test_part_vis_metal_m20_200l")

        if os.path.exists("Scripts\\part_vis_metal_m20_200l.py"):
            os.remove("Scripts\\part_vis_metal_m20_200l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m20_200l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m20_200l"


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

L = 200
k = 12.5
d1 = 20
e = 33.53

cylinder_1 = Part.makeCylinder(e/2, L+k)

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
__objs__.append(FreeCAD.getDocument("part_vis_metal_m20_200l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_vis_metal_m20_200l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_vis_metal_m20_200l_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_vis_metal_m20_200l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-20-z-blanc-nfe-25513.html
    def test_part_rondelle_20m(self):
        print("test_part_rondelle_20m")

        if os.path.exists("Scripts\\part_rondelle_20m.py"):
            os.remove("Scripts\\part_rondelle_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_20m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_20m"


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

d1 = 21
d2 = 36
s = 3

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_20m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_rondelle_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m20-brut-din-934.html
    def test_part_ecrou_20m(self):
        print("test_part_ecrou_20m")

        if os.path.exists("Scripts\\part_ecrou_20m.py"):
            os.remove("Scripts\\part_ecrou_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_20m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_20m"


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

d1 = 20
e = 32.95
h = 16

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_20m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_20m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_ecrou_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m12x55-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m12_55l(self):
        print("test_part_vis_metal_m12_55l")

        if os.path.exists("Scripts\\part_vis_metal_m12_55l.py"):
            os.remove("Scripts\\part_vis_metal_m12_55l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m12_55l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m12_55l"


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

L = 55
k = 7.5
d1 = 12
e = 21.1

cylinder_1 = Part.makeCylinder(e/2, L+k)

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
__objs__.append(FreeCAD.getDocument("part_vis_metal_m12_55l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_vis_metal_m12_55l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_vis_metal_m12_55l_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_vis_metal_m12_55l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-12-z-blanc-nfe-25513.html
    def test_part_rondelle_12m(self):
        print("test_part_rondelle_12m")

        if os.path.exists("Scripts\\part_rondelle_12m.py"):
            os.remove("Scripts\\part_rondelle_12m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_rondelle_12m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_12m"


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

d1 = 13
d2 = 24
s = 2.5

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_rondelle_12m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_12m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_rondelle_12m_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_rondelle_12m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m12-brut-din-934.html
    def test_part_ecrou_12m(self):
        print("test_part_ecrou_12m")

        if os.path.exists("Scripts\\part_ecrou_12m.py"):
            os.remove("Scripts\\part_ecrou_12m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_12m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_12m"


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

d1 = 12
e = d1*1.6
h = d1*0.8

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_12m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_12m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_ecrou_12m_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_ecrou_12m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.aimant-boutique.fr/ferrite/anneaux-aimantes/anneau-140.0-x-60.0-x-20.0-mm-y30-ferrite
    def test_part_magnet_1d140_2d60_20e(self):
        print("test_part_magnet_1d140_2d60_20e")

        if os.path.exists("Scripts\\part_magnet_1d140_2d60_20e.py"):
            os.remove("Scripts\\part_magnet_1d140_2d60_20e.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_magnet_1d140_2d60_20e.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_magnet_1d140_2d60_20e"


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

d1 = 60
d2 = 140
s = 20

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_magnet_1d140_2d60_20e").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_magnet_1d140_2d60_20e.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_magnet_1d140_2d60_20e_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_magnet_1d140_2d60_20e.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.laserboost.com/
    def test_part_faraday_disc(self):
        print("test_part_faraday_disc")

        if os.path.exists("Scripts\\part_faraday_disc.py"):
            os.remove("Scripts\\part_faraday_disc.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_faraday_disc.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_faraday_disc"


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

d_magnet = 140
d1 = 30.1
d2 = d_magnet + 2*2
s = 5

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_faraday_disc").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_faraday_disc.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_faraday_disc.dxf"

importDXF.export(__objs__, dxf_file)

setview()

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_faraday_disc_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_faraday_disc.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/
    def test_part_support_magnet(self):
        print("test_part_support_magnet")

        if os.path.exists("Scripts\\part_support_magnet.py"):
            os.remove("Scripts\\part_support_magnet.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_support_magnet.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_magnet"


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

d_magnet = 140

d_exterieur = d_magnet + 2*2
d_interieur = d_magnet
d_arbre = 30.1
h_support_global = 5
h_support_magnet = 3

# Cylinder_1
cylinder_1 = Part.makeCylinder(d_exterieur/2, h_support_global)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(d_arbre/2, h_support_global)
cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for emptying the part
degre = 72
for i in range(int(360/degre)):
    radius = d_interieur/2 - 3 - (d_arbre + 10)/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder((d_arbre + 10)/2, h_support_global)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cylinder_3
cylinder_3 = Part.makeCylinder(d_interieur/2, h_support_magnet)
cylinder_3_vector = FreeCAD.Vector(0, 0, h_support_global - h_support_magnet)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support_magnet").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_support_magnet.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_support_magnet.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/
    def test_part_support_generator(self):
        print("test_part_support_generator")

        if os.path.exists("Scripts\\part_support_generator.py"):
            os.remove("Scripts\\part_support_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_support_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_generator"


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

# tube diameter
d_tube = 159

# nut diameter for screw 20
d_nut = 36

# main diameter
d1 = d_tube + 5*2 + 2*2 + d_nut*2 + 2*2

h_rondelle_30m = 4
h_ecrou_30m = 30*0.8
e_support = 5
h_palier_4_fixation_support = 38.1
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator/2 + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)

# maximum length
h1 = (L_tube - 170)/2

# hole length
h2 = h1 - 5

# inner diameter for fixing the tube
d_inner_tube = d_tube

# radius for fixing the device
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

# screw diameter
d_vis = 20

d3 = d1

d4 = d_tube + 5*2

d_ecrou_30m = 30*1.6 + 5*2

d_arbre = d_ecrou_30m

# part_palier_4_fixations dimensions
r_f_p = 100/2

d_vis_palier = 12.1

# Cylinder_1
cylinder_1 = Part.makeCylinder(d1/2, h1)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(d_inner_tube/2, h2)
cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the device
degre = 15
for i in range(int(360/degre)):
    radius = r_f_d
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cylinder_3
cylinder_3 = Part.makeCylinder(d3/2, h2)

# Cut cylinder_3 by cylinder_4
cylinder_4 = Part.makeCylinder(d4/2, h2)
cylinder_3 = cylinder_3.cut(cylinder_4)

# Cut cylinder_1 by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 5)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# Cut cylinder_1 by cylinder_5
cylinder_5 = Part.makeCylinder(d_arbre/2, h1)
cylinder_1 = cylinder_1.cut(cylinder_5)

# Cut cylinder_1 by trou_vis for fixing the part_palier_4_fixations
for degre in [45, 45*3, 45*5, 45*7]:
    radius = r_f_p
    alpha = (degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis_palier/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cut the holes for emptying the part
degre = 20
for i1 in range(0, 8):
    for i2 in range(int(360/degre)):
        d_hole = 20
        z_hole = (d_hole + 5) * ( i1 + 1)
        axe_y = FreeCAD.Vector(0, 1, 0)
        axe_z = FreeCAD.Vector(0, 0, 1)
        radius_screw = 0
        alpha=(i2*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius_screw*math.cos(alpha), radius_screw*math.sin(alpha), z_hole)
        hole = Part.makeCylinder(d_hole/2, d1, hole_vector, axe_y)
        hole.rotate(hole_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support_generator").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_support_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_support_generator_'

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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_support_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://i0.wp.com/3transmissions.eu/wp-content/uploads/2021/04/accouplements_rigides_fendus_ks.png?ssl=1
    def test_part_accouplement_rigide_mecanique(self):
        print("test_part_accouplement_rigide_mecanique")

        if os.path.exists("Scripts\\part_accouplement_rigide_mecanique.py"):
            os.remove("Scripts\\part_accouplement_rigide_mecanique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_accouplement_rigide_mecanique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh
    
    DOC = FreeCAD.activeDocument()
    
    DOC_NAME = "part_accouplement_rigide_mecanique"
    
    
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
    
    # part_accouplement_rigide_mecanique
    R = 57.7
    L = 83
    Di = 30
    part_accouplement_rigide_mecanique = Part.makeCylinder(R/2, L)
    
    cylinder_1 = Part.makeCylinder(Di/2, L)
    
    # Cut part_accouplement_rigide_mecanique by cylinder_1
    part_accouplement_rigide_mecanique = part_accouplement_rigide_mecanique.cut(cylinder_1)
    
    Part.show(part_accouplement_rigide_mecanique)
    
    DOC.recompute()
    
    __objs__ = []
    
    __objs__.append(FreeCAD.getDocument("part_accouplement_rigide_mecanique").getObject("Shape"))
    
    stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_accouplement_rigide_mecanique.stl"
    
    Mesh.export(__objs__, stl_file)
    
    setview()
    
    # Generate PNG files
    file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_accouplement_rigide_mecanique_'
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

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_accouplement_rigide_mecanique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://lemetal.fr/tube-rond-acier-noir/326-tube-rond-o-159-x-4-creux-acier-noir.html#/longueur_en_centimetre-100
    def test_part_tube(self):
        print("test_part_tube")

        if os.path.exists("Scripts\\part_tube.py"):
            os.remove("Scripts\\part_tube.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tube.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tube"


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

# part_tube
r_tube = 159/2
e_tube = 4
h_rondelle_30m = 4
h_ecrou_30m = 30*0.8
e_support = 5
h_palier_4_fixation_support = 38.1
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L = 1000 - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator/2 + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)

print(L)

part_tube = Part.makeCylinder(r_tube, L)

cylinder_1 = Part.makeCylinder(r_tube - e_tube, L)

part_tube = part_tube.cut(cylinder_1)

Part.show(part_tube)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tube").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_tube.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_tube_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_tube.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123roulement.com/paliers-UCFC206
    def test_part_palier_4_fixations_support(self):
        print("test_part_palier_4_fixations_support")

        if os.path.exists("Scripts\\part_palier_4_fixations_support.py"):
            os.remove("Scripts\\part_palier_4_fixations_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_palier_4_fixations_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier_4_fixations_support"


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

# part_palier_4_fixations_support
A = 125
B = 38.1
part_palier_4_fixations_support = Part.makeCylinder(A/2, B)

# Cut part_palier_4_fixations_support by trou_arbre
Da = 30
trou_arbre = Part.makeCylinder(Da/2, B)
part_palier_4_fixations_support = part_palier_4_fixations_support.cut(trou_arbre)

# Cut part_palier_4_fixations_support by trou_vis
degres = [45*1, 45*3, 45*5, 45*7]
P = 100
D_vis = 12
for degre in degres:
    radius = P/2
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(D_vis/2, B)
    hole.translate(hole_vector)
    part_palier_4_fixations_support = part_palier_4_fixations_support.cut(hole)

Part.show(part_palier_4_fixations_support)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier_4_fixations_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_palier_4_fixations_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_palier_4_fixations_support_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_palier_4_fixations_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123roulement.com/paliers-UCP206-D1#lg=1&slide=0
    def test_part_palier_2_fixation_ossature(self):
        print("test_part_palier_2_fixation_ossature")

        if os.path.exists("Scripts\\part_palier_2_fixation_ossature.py"):
            os.remove("Scripts\\part_palier_2_fixation_ossature.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_palier_2_fixation_ossature.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier_2_fixation_ossature"


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

# part_palier_2_fixation_ossature
x = 165
y = 48
z = 84
part_palier_2_fixation_ossature = Part.makeBox(x, y, z)

Da = 30
trou_arbre = Part.makeCylinder(Da/2, y)

# Cut part_palier_2_fixation_ossature by trou_arbre
# rotation trou_arbre
axe_x = FreeCAD.Vector(1, 0, 0)
trou_arbre_vector = FreeCAD.Vector(0, 0, 0)
trou_arbre.rotate(trou_arbre_vector, axe_x, 90)

# translation trou_arbre
trou_arbre_vector = FreeCAD.Vector(x/2, y, 42.9)
trou_arbre.translate(trou_arbre_vector)

part_palier_2_fixation_ossature = part_palier_2_fixation_ossature.cut(trou_arbre)

# Cut part_palier_2_fixation_ossature by trou_vis
D_vis = 17
trou_vis = Part.makeCylinder(D_vis/2, z)

# translation trou_vis
E = 121
A = 165
trou_vis_vector = FreeCAD.Vector((A - E)/2, y/2, 0)
trou_vis.translate(trou_vis_vector)

part_palier_2_fixation_ossature = part_palier_2_fixation_ossature.cut(trou_vis)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector(E, 0, 0)
trou_vis.translate(trou_vis_vector)

part_palier_2_fixation_ossature = part_palier_2_fixation_ossature.cut(trou_vis)

Part.show(part_palier_2_fixation_ossature)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier_2_fixation_ossature").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_palier_2_fixation_ossature.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_palier_2_fixation_ossature_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_palier_2_fixation_ossature.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71618-moyeu-amovible-ma1210-30-4014486252361.html
    def test_part_moyeu_amovible_generator(self):
        print("test_part_moyeu_amovible_generator")

        if os.path.exists("Scripts\\part_moyeu_amovible_generator.py"):
            os.remove("Scripts\\part_moyeu_amovible_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_moyeu_amovible_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_generator"


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

# part_moyeu_amovible_generator
De = 47.5
L = 25.4
Di = 30
part_moyeu_amovible_generator = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(Di/2, L)

# Cut part_moyeu_amovible_generator by cylinder_1
part_moyeu_amovible_generator = part_moyeu_amovible_generator.cut(cylinder_1)

Part.show(part_moyeu_amovible_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_generator").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_moyeu_amovible_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_moyeu_amovible_generator_'
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

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_moyeu_amovible_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/73970-poulie-trapezoidale-moyeu-amovible-spz80-1ma-4014486249866.html
    def test_part_poulie_generator(self):
        print("test_part_poulie_generator")

        if os.path.exists("Scripts\\part_poulie_generator.py"):
            os.remove("Scripts\\part_poulie_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_poulie_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_generator"


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

# part_poulie_generator
De = 84
L = 25.4
Di = 47.5
part_poulie_generator = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(Di/2, L)

# Cut part_poulie_generator by cylinder_1
part_poulie_generator = part_poulie_generator.cut(cylinder_1)

Part.show(part_poulie_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_generator").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_poulie_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\part_poulie_generator_'
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

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_poulie_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m30x70-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m30_70l(self):
        print("test_part_vis_metal_m30_70l")

        if os.path.exists("Scripts\\part_vis_metal_m30_70l.py"):
            os.remove("Scripts\\part_vis_metal_m30_70l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m30_70l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m30_70l"


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

# Dimensions
L = 70
k = 18.7
d1 = 30
e = 50.85

cylinder_1 = Part.makeCylinder(e/2, L+k)

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
__objs__.append(FreeCAD.getDocument("part_vis_metal_m30_70l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_vis_metal_m30_70l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\HG\\\\Version_3\\\\Png\\\\part_vis_metal_m30_70l_'
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
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\part_vis_metal_m30_70l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsHGVersion3Assemblies(unittest.TestCase):
    # ok
    def test_assembly_magnet(self):
        print("test_assembly_magnet")

        if os.path.exists("Scripts\\assembly_magnet.py"):
            os.remove("Scripts\\assembly_magnet.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_magnet.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_magnet"


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

assembly = "assembly_magnet"

h_magnet = 20
h_faraday_disc = 5

# part_faraday_disc
color = (0.90, 0.80, 0.70)
x = 0
y = 0
z = 0
title = 'part_faraday_disc'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_magnet_1d140_2d60_20e
color = (0.10, 0.80, 0.10)
x = 0
y = 0
z = 5
title = 'part_magnet_1d140_2d60_20e'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_support_magnet
color = (0.20, 0.40, 0.00)
x = 0
y = 0
z = h_faraday_disc + h_magnet + 2
title = 'part_support_magnet'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,1,0),180))

setview()

# Export
__objs__ = []

title = "part_faraday_disc"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_magnet_1d140_2d60_20e"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_support_magnet"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\' + assembly + '_'
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

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\assembly_magnet.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_shaft(self):
        print("test_assembly_shaft")

        if os.path.exists("Scripts\\assembly_shaft.py"):
            os.remove("Scripts\\assembly_shaft.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_shaft.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_shaft"


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

assembly = "assembly_shaft"

r_tube = 159/2
e_tube = 4
h_rondelle_30m = 4
h_ecrou_30m = 30*0.8
e_support = 5
h_palier_4_fixation_support = 38.1
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)

Start_assembly_magnet = (1000 - L_tube)/2 + h_rondelle_30m + h_ecrou_30m
h_disc = 5
h_magnet = 20
h_assembly_magnet = h_disc + h_magnet + 2

# part_tige_filetee_m30_1000l
part_tige_filetee_m30_1000l_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_tige_filetee_m30_1000l.stl"
Mesh.insert(part_tige_filetee_m30_1000l_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_tige_filetee_m30_1000l").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m30_1000l").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_magnet
color = (0.70, 0.70, 0.70)
i2 = round((L_tube - 2*h_rondelle_30m - 2*h_ecrou_30m)/h_assembly_magnet)
title = 'assembly_magnet'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
for i in range(0, i2):
    x = 0
    y = 0
    z = Start_assembly_magnet + i * h_assembly_magnet

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_tube
x = 0
y = 0
z = Start_assembly_magnet - h_rondelle_30m - h_ecrou_30m
color = (0.45, 0.99, 0.05)
part_tube_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_tube.stl"
Mesh.insert(part_tube_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_tube").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_tube").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
x = 0
y = 0
z = Start_assembly_magnet - h_rondelle_30m
color = (0.45, 0.05, 0.95)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_30m
x = 0
y = 0
z = Start_assembly_magnet - h_rondelle_30m - h_ecrou_30m
color = (0.45, 0.55, 0.65)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
color = (0.45, 0.05, 0.95)
x = 0
y = 0
z = Start_assembly_magnet + i2 * h_assembly_magnet
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_30m
color = (0.45, 0.55, 0.65)
x = 0
y = 0
z = Start_assembly_magnet + i2 * h_assembly_magnet + h_rondelle_30m
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m30_1000l"))

title = "assembly_magnet"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

# part_tube
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tube"))

# part_rondelle_30m
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

# part_ecrou_30m
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m"))

# part_rondelle_30m001
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001"))

# part_ecrou_30m001
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\' + assembly + '_'
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

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\assembly_shaft.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_support(self):
        print("test_assembly_support")

        if os.path.exists("Scripts\\assembly_support.py"):
            os.remove("Scripts\\assembly_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support"


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

assembly = "assembly_support"

# Parameters
h_rondelle_30m = 4
h_ecrou_30m = 30*0.8
h_ecrou_12m = 12*0.8
k_vis_12m = 7.5
h_rondelle_12m = 2.5
e_support = 5
h_palier_4_fixation_support = 38.1
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator/2 + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)

h1 = (L_tube - 170)/2

# part_support_generator
x = 0
y = 0
z = 0
color = (0.10, 0.20, 0.30)
part_support_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_support_generator.stl"
Mesh.insert(part_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_support_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_support_generator").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_palier_4_fixations_support
x = 0
y = 0
z = h1
color = (0.20, 0.40, 0.60)
part_palier_4_fixations_support_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_palier_4_fixations_support.stl"
Mesh.insert(part_palier_4_fixations_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_4_fixations_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_4_fixations_support").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))    

# part_rondelle_30m
x = 0
y = 0
z = h1 + h_palier_4_fixation_support
color = (0.40, 0.60, 0.80)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_30m
x = 0
y = 0
z = h1 + h_palier_4_fixation_support + h_rondelle_30m
color = (0.60, 0.80, 0.90)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_12m
color = (0.70, 0.70, 0.70)
title = 'part_rondelle_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [45*1, 45*3, 45*5, 45*7]
i1 = 0
for degre in degres:
    i = i1
    radius = 100/2
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = h1 + h_palier_4_fixation_support

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1
    
# part_rondelle_12m
color = (0.70, 0.70, 0.70)
title = 'part_rondelle_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [45*1, 45*3, 45*5, 45*7]
for degre in degres:
    i = i1
    radius = 100/2
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = h1 - 5 - h_rondelle_12m

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1    

# part_ecrou_12m
color = (0.10, 0.20, 0.30)
title = 'part_ecrou_12m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [45*1, 45*3, 45*5, 45*7]
i2 = 0
for degre in degres:
    i = i2
    radius = 100/2
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = h1 + h_palier_4_fixation_support + h_rondelle_12m

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i2 += 1
    
# part_vis_metal_m12_55l
color = (0.20, 0.30, 0.70)
title = 'part_vis_metal_m12_55l'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [45*1, 45*3, 45*5, 45*7]
i3 = 0
for degre in degres:
    i = i3
    radius = 100/2
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = h1 - 5 - h_rondelle_12m - k_vis_12m

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i3 += 1

# part_rondelle_20m

# radius for fixing the device
d_tube = 159
d_nut = 36
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

color = (0.10, 0.50, 0.90)
title = 'part_rondelle_20m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [120*1, 120*2, 120*3]
i4 = 0
for degre in degres:
    i = i4
    radius = r_f_d
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = 5

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i4 += 1

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_support_generator"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_4_fixations_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m"))

title = "part_rondelle_12m"
for i in range(0, i1*2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_12m"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m12_55l"
for i in range(0, i3):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_rondelle_20m"
for i in range(0, i4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\' + assembly + '_'
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

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\assembly_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_poulie(self):
        print("test_assembly_poulie")

        if os.path.exists("Scripts\\assembly_poulie.py"):
            os.remove("Scripts\\assembly_poulie.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_poulie.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_poulie"


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

assembly = "assembly_poulie"

# Parameters
h_rondelle_30m = 4
h_poulie_generator = 25.4
k_vis_metal_30m_70l = 18.7

# part_moyeu_amovible_generator
color = (0.10, 0.20, 0.30)
part_moyeu_amovible_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_moyeu_amovible_generator.stl"
Mesh.insert(part_moyeu_amovible_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_moyeu_amovible_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_poulie_generator
color = (0.30, 0.60, 0.90)
part_poulie_generator_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_poulie_generator.stl"
Mesh.insert(part_poulie_generator_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_poulie_generator").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_poulie_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
x = 0
y = 0
z = h_poulie_generator
color = (0.10, 0.00, 0.00)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
x = 0
y = 0
z = - h_rondelle_30m
color = (0.10, 0.00, 0.00)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_vis_metal_m30_70l
x = 0
y = 0
z = - h_rondelle_30m - k_vis_metal_30m_70l
color = (0.10, 0.90, 0.90)
part_vis_metal_m30_70l_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_vis_metal_m30_70l.stl"
Mesh.insert(part_vis_metal_m30_70l_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_vis_metal_m30_70l").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_vis_metal_m30_70l").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_accouplement_rigide_mecanique
x = 0
y = 0
z = h_poulie_generator + h_rondelle_30m
color = (0.20, 0.70, 0.90)
part_accouplement_rigide_mecanique_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_accouplement_rigide_mecanique.stl"
Mesh.insert(part_accouplement_rigide_mecanique_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_accouplement_rigide_mecanique").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_accouplement_rigide_mecanique").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_moyeu_amovible_generator"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_poulie_generator"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_vis_metal_m30_70l"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_accouplement_rigide_mecanique"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\assembly_poulie.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_generator(self):
        print("test_assembly_generator")

        if os.path.exists("Scripts\\assembly_generator.py"):
            os.remove("Scripts\\assembly_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_generator"


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

assembly = "assembly_generator"

# Parameters
h_rondelle_30m = 4
h_ecrou_30m = 30*0.8
h_ecrou_12m = 12*0.8
k_vis_12m = 7.5
k_vis_20m = 12.5
h_rondelle_20m = 3
h_ecrou_20m = 16
h_rondelle_12m = 2.5
e_support = 5
h_palier_4_fixation_support = 38.1
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator/2 + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)
h1 = (L_tube - 170)/2

# assembly_shaft
color = (0.10, 0.20, 0.30)
assembly_shaft_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_shaft.stl"
Mesh.insert(assembly_shaft_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_shaft").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_shaft").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_support
x = 0
y = 0
z = (1000 - L_tube)/2 + h1 + 1
color = (0.20, 0.40, 0.60)
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,1,0),180))

# assembly_support
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube - h1 + 5 + 2
color = (0.20, 0.40, 0.60)
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support001").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),15*4))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m + 2
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_palier_2_fixation_ossature
x = -165/2
y = 84/2
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_4_fixation_support - h_rondelle_30m
color = (0.50, 0.90, 0.40)
part_palier_2_fixation_ossature_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_palier_2_fixation_ossature.stl"
Mesh.insert(part_palier_2_fixation_ossature_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_2_fixation_ossature").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_4_fixation_support - h_rondelle_30m - h_rondelle_30m
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_4_fixation_support - h_rondelle_30m - h_rondelle_30m - h_ecrou_30m
color = (0.40, 0.30, 0.00)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m002").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_palier_2_fixation_ossature
x = -165/2
y = 84/2
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m
color = (0.50, 0.90, 0.40)
part_palier_2_fixation_ossature_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_palier_2_fixation_ossature.stl"
Mesh.insert(part_palier_2_fixation_ossature_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_2_fixation_ossature001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m + h_palier_2_fixation_ossature
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m003").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m
color = (0.40, 0.30, 0.00)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# assembly_poulie
x = 0
y = 0
z = - h_palier_2_fixation_ossature - h_rondelle_30m - h_ecrou_30m - 8
color = (0.40, 0.40, 0.40)
assembly_poulie_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_poulie.stl"
Mesh.insert(assembly_poulie_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_poulie").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_poulie").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# assembly_poulie
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h1 + h_ecrou_30m
color = (0.40, 0.40, 0.40)
assembly_poulie_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_poulie.stl"
Mesh.insert(assembly_poulie_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_poulie001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_poulie001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),180))

# part_vis_metal_m20_200l
# radius for fixing the device
d_tube = 159
d_nut = 36
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

color = (0.10, 0.50, 0.90)
title = 'part_vis_metal_m20_200l'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [60*1, 60*3, 60*5]
i1 = 0
for degre in degres:
    i = i1
    radius = r_f_d
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = (1000 - L_tube)/2 + h1 + 1 - k_vis_20m - h_rondelle_20m - 5

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i1 += 1

# part_ecrou_20m
# radius for fixing the device
d_tube = 159
d_nut = 36
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

color = (0.00, 0.00, 0.90)
title = 'part_ecrou_20m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [60*1, 60*3, 60*5]
i2 = 0
for degre in degres:
    i = i2
    radius = r_f_d
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = (1000 - L_tube)/2 + h1 + 200 - h_ecrou_20m + 1

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    
    i2 += 1

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_shaft"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m002"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_poulie"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_poulie001"))

title = "part_vis_metal_m20_200l"
for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_20m"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Png\\\\assembly_generator_'
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

        pywinauto.mouse.click(button="left", coords=(round(690 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\HG\\\\Version_3\\\\Scripts\\\\assembly_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
