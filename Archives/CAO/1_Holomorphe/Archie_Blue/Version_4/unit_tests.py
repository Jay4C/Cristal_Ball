import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsArchieBlueHydrogenGeneratorVersion4ForParts(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-inox-a2-din-985/ecrou-nylstop-m10-inox-a2-din-985.html
    def test_part_ecrou_10m(self):
        print("test_part_ecrou_10m")

        if os.path.exists("part_ecrou_10m.py"):
            os.remove("part_ecrou_10m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_10m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_10m"


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

cylinder_1 = Part.makeCylinder(18.90/2, 10)

cylinder_2 = Part.makeCylinder(5, 10)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_10m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_ecrou_10m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_10m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_ecrou_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m10x200-inox-a2-ef-din-933.html
    def test_part_vis_metal_m10_200l(self):
        print("test_part_vis_metal_m10_200l")

        if os.path.exists("part_vis_metal_m10_200l.py"):
            os.remove("part_vis_metal_m10_200l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m10_200l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m10_200l"


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

d1 = 10
e = 18.90
L = 200
k = 6.40

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

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m10_200l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_vis_metal_m10_200l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m10_200l_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_vis_metal_m10_200l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m10x150-inox-a2-ef-din-933.html
    def test_part_vis_metal_m10_150l(self):
        print("test_part_vis_metal_m10_150l")

        if os.path.exists("part_vis_metal_m10_150l.py"):
            os.remove("part_vis_metal_m10_150l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m10_150l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m10_150l"


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

d1 = 10
L = 150
k = 6.40
e = 18.90

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

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m10_150l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_vis_metal_m10_150l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m10_150l_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_vis_metal_m10_150l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/inox-a2/th-inox-a2-filetage-total-din-933/th-m10x30-inox-a2-ef-din-933.html
    def test_part_vis_metal_m10_30l(self):
        print("test_part_vis_metal_m10_30l")

        if os.path.exists("part_vis_metal_m10_30l.py"):
            os.remove("part_vis_metal_m10_30l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m10_30l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m10_30l"


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

d1 = 10
L = 30
k = 6.40
e = 18.90

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

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_vis_metal_m10_30l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_vis_metal_m10_30l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m10_30l_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_vis_metal_m10_30l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/visserie-nylon/rondelle-plate-nylon-naturel-pa6-6-din-125/rondelle-10-5x20x2-nylon-blanc-din-125.html
    def test_part_rondelle_10m(self):
        print("test_part_rondelle_10m")

        if os.path.exists("part_rondelle_10m.py"):
            os.remove("part_rondelle_10m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_10m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_10m"


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

d1 = 10.5
d2 = 20
s = 2

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_10m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_rondelle_10m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_10m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue'
            '\\\\Version_4\\\\part_rondelle_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.plexiglas-shop.com/fr/produits/plexiglas-xt/ro0a070gt.html?force_sid=hdhbk391d16to9fcfpc6scnai7
    def test_part_tank_d200_170l(self):
        print("test_part_tank_d200_170l")

        if os.path.exists("part_tank_d200_170l.py"):
            os.remove("part_tank_d200_170l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tank_d200_170l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tank_d200_170l"


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

# Diametre maximal du tank
diametre_maximal = 200

cylinder_1 = Part.makeCylinder(diametre_maximal/2, diametre_maximal - 30)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 3, diametre_maximal - 30)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_tank_d200_170l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_tank_d200_170l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_tank_d200_170l'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_tank_d200_170l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.laserboost.com/stainless-steel/
    def test_part_capacitor_plate(self):
        print("test_part_capacitor_plate")

        if os.path.exists("part_capacitor_plate.py"):
            os.remove("part_capacitor_plate.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_capacitor_plate.py", "w") as file:
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

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

epaisseur = 1

# Diametre maximal du tank
diametre_maximal_tank = 200

# Diametre maximal du capacitor plate
diametre_maximal_capacitor_plate = diametre_maximal_tank - 3*2 - 5*2

cylinder_1 = Part.makeCylinder(diametre_maximal_capacitor_plate/2, epaisseur)

cylinder_2 = Part.makeCylinder(5, epaisseur)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for supporting the capacitor plate
degre = 0
radius = diametre_maximal_capacitor_plate/2
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(16.50, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes and the cathodes
degre = 90
radius = diametre_maximal_capacitor_plate/2 - 5 - 5
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(5, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for supporting the capacitor plate
degre = 180
radius = diametre_maximal_capacitor_plate/2
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(16.50, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for supporting the capacitor plate
degre = 270
radius = diametre_maximal_capacitor_plate/2
alpha=(degre*math.pi)/180
hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
hole = Part.makeCylinder(16.50, epaisseur)
hole.translate(hole_vector)
cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 30
for i in range(int(360/degre)):
    radius = diametre_maximal_capacitor_plate/2 - 5 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, epaisseur)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 90
for i in range(int(360/degre)):
    radius = 20
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, epaisseur)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 30
for i in range(int(360/degre)):
    for i_1 in range(2, 4):
        radius = 20 * i_1
        alpha=(i*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(5, epaisseur)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_capacitor_plate").getObject("Shape"))

step_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_capacitor_plate.step"

ImportGui.export(__objs__, step_file)

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_capacitor_plate.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_capacitor_plate.dxf"

importDXF.export(__objs__, dxf_file)

del __objs__

setview()

# Generate PNG files
file = 'part_capacitor_plate_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_capacitor_plate.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/materiaux/materiaux-sls/materiau-plastique/
    def test_part_bottom_support_capacitor_plate(self):
        print("test_part_bottom_support_capacitor_plate")

        if os.path.exists("part_bottom_support_capacitor_plate.py"):
            os.remove("part_bottom_support_capacitor_plate.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_bottom_support_capacitor_plate.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math, importDXF

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

# EPS= tolerance to use to cut the parts
EPS = 0.30
EPS_C = EPS * -0.5

e = 3 + EPS
d1 = 10 + EPS

# Diametre maximal du tank
diametre_maximal_tank = 200

# Diametre maximal
diametre_maximal = diametre_maximal_tank - 3*2 - 5*2

cylinder_1 = Part.makeCylinder(diametre_maximal/2, e)

cylinder_2 = Part.makeCylinder(d1/2, e)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the capacitor plates
degre = 30
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 5 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d1/2, e)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 90
for i in range(int(360/degre)):
    radius = 20
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d1/2, e)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for letting the gas mixture to go out
degre = 30
for i in range(int(360/degre)):
    for i_1 in range(2, 4):
        radius = 20 * i_1
        alpha=(i*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(d1/2, e)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_bottom_support_capacitor_plate").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_bottom_support_capacitor_plate.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_bottom_support_capacitor_plate_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_bottom_support_capacitor_plate.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-manchons-a-visser-laiton-f-12-x-17-pour-tube-en-cuivre-65815253.html
    def test_part_manchon_a_visser_12_17_f(self):
        print("test_part_manchon_a_visser_12_17_f")

        if os.path.exists("part_manchon_a_visser_12_17_f.py"):
            os.remove("part_manchon_a_visser_12_17_f.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_manchon_a_visser_12_17_f.py", "w") as file:
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

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_manchon_a_visser_12_17_f.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_manchon_a_visser_12_17_f_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_manchon_a_visser_12_17_f.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-mamelons-a-visser-laiton-m-12-x-17-pour-tube-en-cuivre-65814231.html
    def test_part_manchon_a_visser_12_17_m(self):
        print("test_part_manchon_a_visser_12_17_m")

        if os.path.exists("part_manchon_a_visser_12_17_m.py"):
            os.remove("part_manchon_a_visser_12_17_m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_manchon_a_visser_12_17_m.py", "w") as file:
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

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_manchon_a_visser_12_17_m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_manchon_a_visser_12_17_m_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_manchon_a_visser_12_17_m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/materiaux/materiaux-sls/materiau-plastique/
    def test_part_bottom_support(self):
        print("test_part_bottom_support")

        if os.path.exists("part_bottom_support.py"):
            os.remove("part_bottom_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_bottom_support.py", "w") as file:
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

e = 70

e1 = e - 5

d_vis = 10

d_m_tank = 200

d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + d_vis*2 + (e - e1)*2

cylinder_1 = Part.makeCylinder(d_m_b_s/2, e)

cylinder_2 = Part.makeCylinder((d_m_tank + 0.1*2)/2 , e1)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, e - e1)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(d_m_b_s/2, e1)

cylinder_4 = Part.makeCylinder((d_m_tank + (e - e1)*2)/2, e1)

# cylinder_4 cut by cylinder_3
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_3 cut by cylinder_1
cylinder_3_vector = FreeCAD.Vector(0, 0, e - e1)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degre = 15
for i in range(int(360/degre)):
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 0
    hole_vector = FreeCAD.Vector(x, y, z)
    hole = Part.makeCylinder(5, 6)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_bottom_support").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_bottom_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_bottom_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_bottom_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/materiaux/materiaux-sls/materiau-plastique/
    def test_part_top_support(self):
        print("test_part_top_support")

        if os.path.exists("part_top_support.py"):
            os.remove("part_top_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_top_support.py", "w") as file:
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
EPS = 0.10
EPS_C = EPS * -0.5

e = 70

e1 = e - 5

d_vis = 10

d_m_tank = 200

d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + d_vis*2 + (e - e1)*2

cylinder_1 = Part.makeCylinder(d_m_b_s/2, e)

cylinder_2 = Part.makeCylinder((d_m_tank + 0.1*2)/2 , e1)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, e - e1)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(d_m_b_s/2, e1)

cylinder_4 = Part.makeCylinder((d_m_tank + (e - e1)*2)/2, e1)

# cylinder_4 cut by cylinder_3
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_3 cut by cylinder_1
cylinder_3_vector = FreeCAD.Vector(0, 0, e - e1)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degre = 15
for i in range(int(360/degre)):
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis/2, 6)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anode and the cathode
degre = 180
for i in range(int(360/degre)):
    radius = d_m_tank/2 - 3 - 5 - 5 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d_vis/2, 6)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the input and the output
degres = [90, 270]
for degre in degres:
    radius = d_m_tank/4
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(16.5/2, 6)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_support").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_top_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_top_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\part_top_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsArchieBlueHydrogenGeneratorVersion4ForAssemblies(unittest.TestCase):
    # ok
    def test_assembly_bottom(self):
        print("test_assembly_bottom")

        if os.path.exists("assembly_bottom.py"):
            os.remove("assembly_bottom.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_bottom.py", "w") as file:
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

__objs__=[]

# For placing part_bottom_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_bottom_support.stl", "assembly_bottom")
FreeCAD.getDocument("assembly_bottom").getObject("part_bottom_support").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_bottom").getObject("part_bottom_support").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument("assembly_bottom").getObject("part_bottom_support"))

# For placing part_tank_d200_170l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_tank_d200_170l.stl", "assembly_bottom")
FreeCAD.getDocument("assembly_bottom").getObject("part_tank_d200_170l").Placement = App.Placement(App.Vector(0, 0, 5), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_bottom").getObject("part_tank_d200_170l").ShapeColor = (0.90,6.00,0.30)
__objs__.append(FreeCAD.getDocument("assembly_bottom").getObject("part_tank_d200_170l"))

e = 70
e1 = e - 5
d_vis = 10
d_m_tank = 200
d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + d_vis*2 + (e - e1)*2
s_rondelle_10m = 2
degre = 15
number_of_holes = int(360/degre)

# Insertion part_rondelle_10m
for i1 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_rondelle_10m"
    
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -s_rondelle_10m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion part_rondelle_10m
for i1 in range(number_of_holes, number_of_holes*2):
    doc = "assembly_bottom"
    file = "part_rondelle_10m"
    
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 5
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion part_ecrou_10m
for i2 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_ecrou_10m"
    
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 7
    color = (0.30,0.30,0.30)

    if i2 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# Insertion part_ecrou_10m
for i2 in range(number_of_holes, number_of_holes*2):
    doc = "assembly_bottom"
    file = "part_ecrou_10m"
    
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 150
    color = (0.30,0.30,0.30)

    if i2 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# For placing the part_vis_metal_m10_200l
k = 6.40
for i3 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_vis_metal_m10_200l"
    
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i3*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - 2 - k
    color = (0.30,0.70,0.70)

    if i3 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i3)))

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/assembly_bottom.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_bottom_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\assembly_bottom.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_top(self):
        print("test_assembly_top")

        if os.path.exists("assembly_top.py"):
            os.remove("assembly_top.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_top.py", "w") as file:
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

__objs__=[]

# For placing the part_top_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_top_support.stl", "assembly_top")
FreeCAD.getDocument("assembly_top").getObject("part_top_support").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument("assembly_top").getObject("part_top_support").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument("assembly_top").getObject("part_top_support"))

e = 70
e1 = e - 5
d_vis = 10
d_m_tank = 200
d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + d_vis*2 + (e - e1)*2
s_rondelle_10m = 2
degre = 15
number_of_holes = int(360/degre)
h_ecrou_10m = 10

# Insertion the part_rondelle_10m
for i1 in range(0, number_of_holes):
    doc = "assembly_top"
    file = "part_rondelle_10m"
    
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -s_rondelle_10m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion the part_rondelle_10m
degre1 = 180
for i1 in range(number_of_holes, number_of_holes+2):
    doc = "assembly_top"
    file = "part_rondelle_10m"
    
    radius = d_m_tank/2 - 3 - 5 - 5 - 5
    alpha=(i1*degre1*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -s_rondelle_10m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion the part_ecrou_10m
for i2 in range(0, number_of_holes):
    doc = "assembly_top"
    file = "part_ecrou_10m"
    
    radius = d_m_b_s/2 - 5 - 5
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_10m - h_ecrou_10m
    color = (0.90,0.90,0.00)

    if i2 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

degre1 = 180
for i2 in range(number_of_holes, number_of_holes+2):
    doc = "assembly_top"
    file = "part_ecrou_10m"
    
    radius = d_m_tank/2 - 3 - 5 - 5 - 5
    alpha=(i2*degre1*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_10m - h_ecrou_10m
    color = (0.90,0.90,0.00)

    if i2 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# Insertion the part_manchon_a_visser_12_17_f
degres = [90, 270]
i3 = 0
for degre3 in degres:
    doc = "assembly_top"
    file = "part_manchon_a_visser_12_17_f"
    
    radius = d_m_tank/4
    alpha=(degre3*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e - e1)
    color = (0.90,0.00,0.90)

    if i3 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i3)))
    
    i3 += 1

# Insertion the part_manchon_a_visser_12_17_m
degres = [90, 270]
i4 = 0
for degre3 in degres:
    doc = "assembly_top"
    file = "part_manchon_a_visser_12_17_m"
    
    radius = d_m_tank/4
    alpha=(degre3*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -11
    color = (0.10,0.10,0.90)

    if i4 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i4 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i4)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i4)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i4)))
    elif 10 <= i4 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i4)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i4)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i4)))
    elif 100 <= i4 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i4)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i4)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i4)))
    
    i4 += 1

degres = [90]
for degre3 in degres:
    doc = "assembly_top"
    file = "part_manchon_a_visser_12_17_m"
    
    radius = d_m_tank/4
    alpha=(degre3*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 5 + 18 - 8
    color = (0.10,0.10,0.90)

    if i4 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i4 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i4)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i4)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i4)))
    elif 10 <= i4 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i4)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i4)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i4)))
    elif 100 <= i4 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i4)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i4)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i4)))
    
    i4 += 1

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/assembly_top.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_top_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\assembly_top.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_capacitors(self):
        print("test_assembly_capacitors")

        if os.path.exists("assembly_capacitors.py"):
            os.remove("assembly_capacitors.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_capacitors.py", "w") as file:
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

__objs__ = []

# Diametre maximal du tank
diametre_maximal_tank = 200

# Diametre maximal
diametre_maximal = diametre_maximal_tank - 3*2 - 5*2

# EPS= tolerance to use to cut the parts
EPS = 0.30
EPS_C = EPS * -0.5

e = 3 + EPS
d1 = 10 + EPS

s_rondelle_10m = 2
h_ecrou_10m = 10
e_capacitor_plate = 1

l_vis_150 = 150
number_of_capacitors = int((l_vis_150 - e - s_rondelle_10m*2 - h_ecrou_10m)/(e_capacitor_plate + s_rondelle_10m))

# For placing the part_bottom_support_capacitor_plate
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/part_bottom_support_capacitor_plate.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate"))

# Insertion the part_rondelle_10m
degre = 90
for i1 in range(0, 4):
    file = "part_rondelle_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -s_rondelle_10m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_10m
degre = 90
for i1 in range(4, 8):
    file = "part_rondelle_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_10m
degre = 90
for i1 in range(0, 4):
    file = "part_ecrou_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e + s_rondelle_10m
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# For placing the part_vis_metal_m10_200l
k = 6.40
degre = 180
for i3 in range(0, 2):
    file = "part_vis_metal_m10_200l"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(i3*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_10m - k
    color = (0.30,0.30,0.60)

    if i3 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)))

# For placing the part_vis_metal_m10_150l
k = 6.40
degres = [90, 270]
i3 = 0
for degre in degres:
    file = "part_vis_metal_m10_150l"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_10m - k
    color = (0.30,0.60,0.60)

    if i3 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)))
        
    i3 += 1

# Insertion the part_rondelle_10m
degre = 0
for i1 in range(8, number_of_capacitors + 4):
    file = "part_rondelle_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (8))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_10m
degre = 90
for i1 in range(number_of_capacitors + 4, number_of_capacitors*2):
    file = "part_rondelle_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (number_of_capacitors + 4))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_10m
degre = 180
for i1 in range(number_of_capacitors*2, number_of_capacitors*3 - 4):
    file = "part_rondelle_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (number_of_capacitors*2))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_10m
degre = 270
for i1 in range(number_of_capacitors*3 - 4, number_of_capacitors*4 - 8):
    file = "part_rondelle_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (number_of_capacitors*3 - 4))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_10m
degre = 90
for i1 in range(4, 8):
    file = "part_ecrou_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(number_of_capacitors - 4) - e_capacitor_plate
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_capacitor_plate
for i1 in range(0, number_of_capacitors - 5):
    file = "part_capacitor_plate"
    
    x = 0
    y = 0
    z = (e + s_rondelle_10m + h_ecrou_10m + s_rondelle_10m) + (s_rondelle_10m + e_capacitor_plate)*i1
    color = (0.50,0.50,0.00)
    
    angle_rotation = 0
    
    if i1 == 0 or i1 % 2 == 0:
        angle_rotation = 90
    else:
        angle_rotation = -90

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_10m
degre = 90
for i1 in range(8, 12):
    file = "part_ecrou_10m"
    
    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(number_of_capacitors - 4) - e_capacitor_plate + h_ecrou_10m
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + DOC_NAME + ".stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\assembly_capacitors.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_global(self):
        print("test_assembly_global")

        if os.path.exists("assembly_global.py"):
            os.remove("assembly_global.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_global.py", "w") as file:
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
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/assembly_bottom.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_bottom").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_bottom").ShapeColor = (0.30,0.60,0.90)
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_bottom").Transparency = 50
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_bottom"))

# For placing the assembly_top
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/assembly_top.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_top").Placement = App.Placement(App.Vector(0, 0, 170 + 10), App.Rotation(App.Vector(0,1,0), 180))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_top").ShapeColor = (0.60,0.90,0.30)
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_top").Transparency = 50
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_top"))

# For placing the assembly_capacitors
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/assembly_capacitors.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_capacitors").Placement = App.Placement(App.Vector(0, 0, 10*2), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_capacitors").ShapeColor = (0.90,0.30,0.60)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_capacitors"))

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_4/" + DOC_NAME + ".stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/4/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\1_Holomorphe\\\\Archie_Blue\\\\Version_4\\\\assembly_global.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
