import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1Parts(unittest.TestCase):
    # ok
    # https://www.france-poulies.com/paliers/5370-palier-alesage-o20-aplique-2-trous.html
    def test_part_palier(self):
        print("test_part_palier")

        if os.path.exists("part_palier.py"):
            os.remove("part_palier.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_palier.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palier"


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

# part_palier
x = 127
y = 38
z = 65
part_palier = Part.makeBox(x, y, z)

trou_arbre = Part.makeCylinder(20/2, y)

# Cut part_palier by trou_arbre
# rotation trou_arbre
axe_x = FreeCAD.Vector(1, 0, 0)
trou_arbre_vector = FreeCAD.Vector(0, 0, 0)
trou_arbre.rotate(trou_arbre_vector, axe_x, 90)

# translation trou_arbre
trou_arbre_vector = FreeCAD.Vector(x/2, 38, 33.3)
trou_arbre.translate(trou_arbre_vector)

part_palier = part_palier.cut(trou_arbre)

# Cut part_palier by trou_vis
trou_vis = Part.makeCylinder(13/2, 65)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector((127-95)/2, 38/2, 0)
trou_vis.translate(trou_vis_vector)

part_palier = part_palier.cut(trou_vis)

# translation trou_vis
trou_vis_vector = FreeCAD.Vector(95, 0, 0)
trou_vis.translate(trou_vis_vector)

part_palier = part_palier.cut(trou_vis)

Part.show(part_palier)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_palier").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palier.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_palier_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_palier.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.gensetcomponents.com/fr/Alternateur-Mecc-Alte-ECP3-2S/4-triphase-105-KVA-LTP-1800-rpm-60-Hz-avec-AVR
    def test_part_alternateur(self):
        print("test_part_alternateur")

        if os.path.exists("part_alternateur.py"):
            os.remove("part_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_alternateur"


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

h_tube = 50
K = 14
B = 58
C = 305
D1 = 23
A1 = 220

# part_alternateur
x = 277
y = 454
z = 317
part_alternateur = Part.makeBox(x, y, z)

# arbre
D = 35
E = 55
arbre = Part.makeCylinder(D/2, E)

# rotation arbre moteur
axe_x = FreeCAD.Vector(1, 0, 0)
arbre_vector = FreeCAD.Vector(0, 0, 0)
arbre.rotate(arbre_vector, axe_x, 90)

# translation arbre moteur
arbre_vector = FreeCAD.Vector(x/2, 0, 132)
arbre.translate(arbre_vector)
part_alternateur = part_alternateur.fuse(arbre)

# Cut part_alternateur by box_1
box_1 = Part.makeBox(h_tube,y,z - 20)
# translation box_1 for the first cut
box_1_vector = FreeCAD.Vector(0, 0, 20)
box_1.translate(box_1_vector)
part_alternateur = part_alternateur.cut(box_1)
# translation box_1 for the second cut
box_1_vector = FreeCAD.Vector(x - h_tube, 0, 0)
box_1.translate(box_1_vector)
part_alternateur = part_alternateur.cut(box_1)

# Cut part_alternateur by cylinder_1
cylinder_1 = Part.makeCylinder(K/2, 20)
# translation cylinder_1 for the first cut
cylinder_1_vector = FreeCAD.Vector((x - A1)/2, B, 0)
cylinder_1.translate(cylinder_1_vector)
part_alternateur = part_alternateur.cut(cylinder_1)
# translation cylinder_1 for the second cut
cylinder_1_vector = FreeCAD.Vector(0, C, 0)
cylinder_1.translate(cylinder_1_vector)
part_alternateur = part_alternateur.cut(cylinder_1)
# translation cylinder_1 for the third cut
cylinder_1_vector = FreeCAD.Vector(0, D1, 0)
cylinder_1.translate(cylinder_1_vector)
part_alternateur = part_alternateur.cut(cylinder_1)
# translation cylinder_1 for the fourth cut
cylinder_1_vector = FreeCAD.Vector(A1, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_alternateur = part_alternateur.cut(cylinder_1)
# translation cylinder_1 for the fifth cut
cylinder_1_vector = FreeCAD.Vector(0, -D1, 0)
cylinder_1.translate(cylinder_1_vector)
part_alternateur = part_alternateur.cut(cylinder_1)
# translation cylinder_1 for the sixth cut
cylinder_1_vector = FreeCAD.Vector(0, -C, 0)
cylinder_1.translate(cylinder_1_vector)
part_alternateur = part_alternateur.cut(cylinder_1)

Part.show(part_alternateur)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_alternateur").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_alternateur.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_alternateur_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.em-distribution.fr/moteur-monophase-230v/1929-moteur-electrique-monophase-almo-mmp-b14-18-kw-1500-tr-min-ha-90-230v.html
    def test_part_moteur_electrique(self):
        print("test_part_moteur_electrique")

        if os.path.exists("part_moteur_electrique.py"):
            os.remove("part_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moteur_electrique"


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

# part_moteur_electrique
A = 140
C = 56
B = 125
K = 10
AB = 175
L = 367
AD = 150
H = 90
h_tube = 50

# arbre
D = 24
E = 50

part_moteur_electrique = Part.makeBox(AB, (L - E), AD + H)

arbre = Part.makeCylinder(D/2, E)

# rotation arbre moteur
axe_x = FreeCAD.Vector(1, 0, 0)
arbre_vector = FreeCAD.Vector(0, 0, 0)
arbre.rotate(arbre_vector, axe_x, 90)

# translation arbre moteur
arbre_vector = FreeCAD.Vector(AB/2, 0, H)
arbre.translate(arbre_vector)
part_moteur_electrique = part_moteur_electrique.fuse(arbre)

# Cut part_moteur_electrique by box_1
box_1 = Part.makeBox(h_tube,(L - E),AD + H - 20)
# translation box_1 for the first cut
box_1_vector = FreeCAD.Vector(0, 0, 20)
box_1.translate(box_1_vector)
part_moteur_electrique = part_moteur_electrique.cut(box_1)
# translation box_1 for the second cut
box_1_vector = FreeCAD.Vector(AB - h_tube, 0, 0)
box_1.translate(box_1_vector)
part_moteur_electrique = part_moteur_electrique.cut(box_1)

# Cut part_moteur_electrique by cylinder_1
cylinder_1 = Part.makeCylinder(K/2, 20)
# translation cylinder_1 for the first cut
cylinder_1_vector = FreeCAD.Vector((AB - A)/2, C, 0)
cylinder_1.translate(cylinder_1_vector)
part_moteur_electrique = part_moteur_electrique.cut(cylinder_1)
# translation cylinder_1 for the second cut
cylinder_1_vector = FreeCAD.Vector(0, B, 0)
cylinder_1.translate(cylinder_1_vector)
part_moteur_electrique = part_moteur_electrique.cut(cylinder_1)
# translation cylinder_1 for the third cut
cylinder_1_vector = FreeCAD.Vector(A, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_moteur_electrique = part_moteur_electrique.cut(cylinder_1)
# translation cylinder_1 for the fourth cut
cylinder_1_vector = FreeCAD.Vector(0, -B, 0)
cylinder_1.translate(cylinder_1_vector)
part_moteur_electrique = part_moteur_electrique.cut(cylinder_1)

Part.show(part_moteur_electrique)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moteur_electrique").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moteur_electrique.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moteur_electrique_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71588-moyeu-amovible-ma1008-20-4014486251906.html
    def test_part_moyeu_amovible_volant_inertie(self):
        print("test_part_moyeu_amovible_volant_inertie")

        if os.path.exists("part_moyeu_amovible_volant_inertie.py"):
            os.remove("part_moyeu_amovible_volant_inertie.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moyeu_amovible_volant_inertie.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_volant_inertie"


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

# part_moyeu_amovible_volant_inertie
De = 35
L = 22.2
part_moyeu_amovible_volant_inertie = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(20/2, L)

# Cut part_moyeu_amovible_volant_inertie by cylinder_1
part_moyeu_amovible_volant_inertie = part_moyeu_amovible_volant_inertie.cut(cylinder_1)

Part.show(part_moyeu_amovible_volant_inertie)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_volant_inertie").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_volant_inertie.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moyeu_amovible_volant_inertie_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_moyeu_amovible_volant_inertie.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/73952-poulie-trapezoidale-moyeu-amovible-spz50-1ma-4014486249682.html
    def test_part_poulie_volant_inertie(self):
        print("test_part_poulie_volant_inertie")

        if os.path.exists("part_poulie_volant_inertie.py"):
            os.remove("part_poulie_volant_inertie.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_poulie_volant_inertie.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_volant_inertie"


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

# part_poulie_volant_inertie
De = 54
L = 22.2
part_poulie_volant_inertie = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(35/2, L)

# Cut part_poulie_volant_inertie by cylinder_1
part_poulie_volant_inertie = part_poulie_volant_inertie.cut(cylinder_1)

Part.show(part_poulie_volant_inertie)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_volant_inertie").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_volant_inertie.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_poulie_volant_inertie_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_poulie_volant_inertie.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71660-moyeu-amovible-ma1610-35-4014486252538.html
    def test_part_moyeu_amovible_alternateur(self):
        print("test_part_moyeu_amovible_alternateur")

        if os.path.exists("part_moyeu_amovible_alternateur.py"):
            os.remove("part_moyeu_amovible_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moyeu_amovible_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_alternateur"


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

# part_moyeu_amovible_alternateur
De = 57
L = 25.4
part_moyeu_amovible_alternateur = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(35/2, L)

# Cut part_moyeu_amovible_alternateur by cylinder_1
part_moyeu_amovible_alternateur = part_moyeu_amovible_alternateur.cut(cylinder_1)

Part.show(part_moyeu_amovible_alternateur)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_alternateur").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_alternateur.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moyeu_amovible_alternateur_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_moyeu_amovible_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/73975-poulie-trapezoidale-moyeu-amovible-spz85-2ma-4014486249910.html
    def test_part_poulie_alternateur(self):
        print("test_part_poulie_alternateur")

        if os.path.exists("part_poulie_alternateur.py"):
            os.remove("part_poulie_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_poulie_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_alternateur"


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

# part_poulie_alternateur
De = 89
L = 25.4
part_poulie_alternateur = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(57/2, L)

# Cut part_poulie_alternateur by cylinder_1
part_poulie_alternateur = part_poulie_alternateur.cut(cylinder_1)

Part.show(part_poulie_alternateur)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_alternateur").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_alternateur.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_poulie_alternateur_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_poulie_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/moyeu-amovible/71703-moyeu-amovible-ma2517-24-4014486252163.html
    def test_part_moyeu_amovible_moteur_electrique(self):
        print("test_part_moyeu_amovible_moteur_electrique")

        if os.path.exists("part_moyeu_amovible_moteur_electrique.py"):
            os.remove("part_moyeu_amovible_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_moyeu_amovible_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_moyeu_amovible_moteur_electrique"


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

# part_moyeu_amovible_moteur_electrique
De = 85.5
L = 44.45
part_moyeu_amovible_moteur_electrique = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(24/2, L)

# Cut part_moyeu_amovible_moteur_electrique by cylinder_1
part_moyeu_amovible_moteur_electrique = part_moyeu_amovible_moteur_electrique.cut(cylinder_1)

Part.show(part_moyeu_amovible_moteur_electrique)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_moyeu_amovible_moteur_electrique").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_moteur_electrique.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_moyeu_amovible_moteur_electrique_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_moyeu_amovible_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.123courroies.com/profil-z-10x6-spz-10x8/74122-poulie-trapezoidale-moyeu-amovible-spz500-2ma-4014486251364.html
    def test_part_poulie_moteur_electrique(self):
        print("test_part_poulie_moteur_electrique")

        if os.path.exists("part_poulie_moteur_electrique.py"):
            os.remove("part_poulie_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_poulie_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_poulie_moteur_electrique"


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

# part_poulie_moteur_electrique
De = 504
L = 44.45
part_poulie_moteur_electrique = Part.makeCylinder(De/2, L)

cylinder_1 = Part.makeCylinder(85.5/2, L)

# Cut part_poulie_moteur_electrique by cylinder_1
part_poulie_moteur_electrique = part_poulie_moteur_electrique.cut(cylinder_1)

Part.show(part_poulie_moteur_electrique)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_poulie_moteur_electrique").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_moteur_electrique.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_poulie_moteur_electrique_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_poulie_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m20-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m20_1000l(self):
        print("test_part_tige_filetee_m20_1000l")

        if os.path.exists("part_tige_filetee_m20_1000l.py"):
            os.remove("part_tige_filetee_m20_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tige_filetee_m20_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "tige_filetee_m20_1000l"


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

# tige_filetee_m20_1000l
tige_filetee_m20_1000l = Part.makeCylinder(20/2, 1000)

Part.show(tige_filetee_m20_1000l)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("tige_filetee_m20_1000l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_tige_filetee_m20_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'tige_filetee_m20_1000l_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_tige_filetee_m20_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m20-z-blanc-din-985.html
    def test_part_ecrou_20m(self):
        print("test_part_ecrou_20m")

        if os.path.exists("part_ecrou_20m.py"):
            os.remove("part_ecrou_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_20m.py", "w") as file:
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
h = 20

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_20m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_20m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_ecrou_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-20-z-blanc-nfe-25513.html
    def test_part_rondelle_20m(self):
        print("test_part_rondelle_20m")

        if os.path.exists("part_rondelle_20m.py"):
            os.remove("part_rondelle_20m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_20m.py", "w") as file:
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

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_20m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_rondelle_20m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_support_masselotte(self):
        print("test_part_support_masselotte")

        if os.path.exists("part_support_masselotte.py"):
            os.remove("part_support_masselotte.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support_masselotte.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_masselotte"


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

length = 1200
width = 70
thickness = 20

box_1 = Part.makeBox(length, width, thickness)

cylinder_1 = Part.makeCylinder(20/2, 20)

# box_1 cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(600, 35, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_support_masselotte").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_support_masselotte.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_support_masselotte_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_support_masselotte.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_masselotte(self):
        print("test_part_masselotte")

        if os.path.exists("part_masselotte.py"):
            os.remove("part_masselotte.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_masselotte.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_masselotte"


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

length = 200
width = 70
thickness = 20

box_1 = Part.makeBox(length, width, thickness)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_masselotte").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_masselotte_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_masselotte.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.mypalletsonline.com/fr/palette-occasion-1000x1200/197-palette-bois-1000-x-1200-recycle-demi-lourde-3s.html
    def test_part_palette(self):
        print("test_part_palette")

        if os.path.exists("part_palette.py"):
            os.remove("part_palette.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_palette.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_palette"


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

length = 1200
width = 1000
thickness = 100

part_palette = Part.makeBox(length, width, thickness)

Part.show(part_palette)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_palette").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palette.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_palette_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_palette.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m10x120-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m10_120l(self):
        print("test_part_vis_metal_m10_120l")

        if os.path.exists("part_vis_metal_m10_120l.py"):
            os.remove("part_vis_metal_m10_120l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m10_120l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m10_120l"


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
L = 120
k = 6.4
e = 18.9

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

__objs__.append(FreeCAD.getDocument("part_vis_metal_m10_120l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m10_120l_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_vis_metal_m10_120l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m10-z-blanc-din-985.html
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

d1 = 10
e = 18.9
h = 10

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_10m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_10m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\part_ecrou_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-10-z-blanc-nfe-25513.html
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

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_10m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO'
            '\\\\2_Specials\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_rondelle_10m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m12x120-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m12_120l(self):
        print("test_part_vis_metal_m12_120l")

        if os.path.exists("part_vis_metal_m12_120l.py"):
            os.remove("part_vis_metal_m12_120l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m12_120l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m12_120l"


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
L = 120
k = 7.5
e = 21.1

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

__objs__.append(FreeCAD.getDocument("part_vis_metal_m12_120l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m12_120l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m12_120l_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_vis_metal_m12_120l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m10x140-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m10_140l(self):
        print("test_part_vis_metal_m10_140l")

        if os.path.exists("part_vis_metal_m10_140l.py"):
            os.remove("part_vis_metal_m10_140l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m10_140l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m10_140l"


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
L = 140
k = 6.4
e = 18.9

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

__objs__.append(FreeCAD.getDocument("part_vis_metal_m10_140l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_140l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m10_140l_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_vis_metal_m10_140l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m12x140-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m12_140l(self):
        print("test_part_vis_metal_m12_140l")

        if os.path.exists("part_vis_metal_m12_140l.py"):
            os.remove("part_vis_metal_m12_140l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m12_140l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m12_140l"


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
L = 140
k = 7.5
e = 21.1

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

__objs__.append(FreeCAD.getDocument("part_vis_metal_m12_140l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m12_140l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m12_140l_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_vis_metal_m12_140l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m12-z-blanc-din-985.html
    def test_part_ecrou_12m(self):
        print("test_part_ecrou_12m")

        if os.path.exists("part_ecrou_12m.py"):
            os.remove("part_ecrou_12m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_12m.py", "w") as file:
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
e = 21.1
h = 12

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_12m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_12m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_12m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_ecrou_12m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-12-z-blanc-nfe-25513.html
    def test_part_rondelle_12m(self):
        print("test_part_rondelle_12m")

        if os.path.exists("part_rondelle_12m.py"):
            os.remove("part_rondelle_12m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_12m.py", "w") as file:
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

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_12m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO'
            '\\\\2_Specials\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_rondelle_12m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/quincaillerie/quincaillerie-du-meuble/roue-et-roulette/roulette-de-meuble/roulette-pivotante-a-frein-a-tige-filetee-diam-75-mm-82629508.html#:~:text=Tableau%20de%20caract%C3%A9ristiques%20du%20produit%20%20%20Couleur,%20%20Polypropyl%C3%A8ne%20%2024%20more%20rows%20
    def test_part_roulette_pivotante(self):
        print("test_part_roulette_pivotante")

        if os.path.exists("part_roulette_pivotante.py"):
            os.remove("part_roulette_pivotante.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_roulette_pivotante.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_roulette_pivotante"


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

d1 = 121.5
d_vis_m10 = 10
L = 99
d2_rondelle_m10 = 20
d3 = d2_rondelle_m10 + 3*2
L3 = L - 3

cylinder_1 = Part.makeCylinder(d1/2, L)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(d_vis_m10/2, L)
cylinder_1 = cylinder_1.cut(cylinder_2)

# Cut cylinder_1 by cylinder_3
cylinder_3 = Part.makeCylinder(d3/2, L3)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_roulette_pivotante").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_roulette_pivotante.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_roulette_pivotante_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO'
            '\\\\2_Specials\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_roulette_pivotante.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m14x100-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m14_100l(self):
        print("test_part_vis_metal_m14_100l")

        if os.path.exists("part_vis_metal_m14_100l.py"):
            os.remove("part_vis_metal_m14_100l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_vis_metal_m14_100l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m14_100l"


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

d1 = 14
L = 100
k = 8.8
e = 24.49

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

__objs__.append(FreeCAD.getDocument("part_vis_metal_m14_100l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_vis_metal_m14_100l_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_vis_metal_m14_100l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m14-z-blanc-din-985.html
    def test_part_ecrou_14m(self):
        print("test_part_ecrou_14m")

        if os.path.exists("part_ecrou_14m.py"):
            os.remove("part_ecrou_14m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_14m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_14m"


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

d1 = 14
e = 24.49
h = 14

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_14m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_ecrou_14m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_ecrou_14m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-14-z-blanc-nfe-25513.html
    def test_part_rondelle_14m(self):
        print("test_part_rondelle_14m")

        if os.path.exists("part_rondelle_14m.py"):
            os.remove("part_rondelle_14m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_14m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_14m"


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

d1 = 15
d2 = 27
s = 2.5

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_rondelle_14m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_rondelle_14m_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO'
            '\\\\2_Specials\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\part_rondelle_14m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1Assemblies(unittest.TestCase):
    # ok
    def test_assembly_slice_flywheel(self):
        print("test_assembly_slice_flywheel")

        if os.path.exists("assembly_slice_flywheel.py"):
            os.remove("assembly_slice_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_slice_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_slice_flywheel"


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

# part_support_masselotte
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_support_masselotte.stl","assembly_slice_flywheel")
FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_masselotte
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_slice_flywheel")
FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte").Placement = App.Placement(App.Vector(1000,0,-25),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(1, 10):
    x = 1000
    y = -i * 20
    z = -25

    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(10, 20):
    x = 1000
    y = 90 + 20 * (i-10)
    z = -25

    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(20, 30):
    x = 0
    y = -20 * (i - 20)
    z = -25

    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_masselotte
for i in range(30, 40):
    x = 0
    y = 90 + 20 * (i-30)
    z = -25

    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_slice_flywheel")
    FreeCADGui.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
    FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

setview()

# Export assembly_slice_flywheel
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_support_masselotte"))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte"))

for i in range(1, 10):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte00" + str(i)))

for i in range(10, 20):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))

for i in range(20, 30):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))

for i in range(30, 40):
    __objs__.append(FreeCAD.getDocument("assembly_slice_flywheel").getObject("part_masselotte0" + str(i)))

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_slice_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_slice_flywheel_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\assembly_slice_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_flywheel(self):
        print("test_assembly_flywheel")

        if os.path.exists("assembly_flywheel.py"):
            os.remove("assembly_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel"


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

# part_tige_filetee_m20_1000l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_tige_filetee_m20_1000l.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.40,0.20,0.10)
FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(600,35,-(1000-20)/2),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(600,35,20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(600,35,-3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(600,35,20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(600,35,- 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# For moteur electrique

# part_poulie_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie").Placement = App.Placement(App.Vector(600,35,510 - 22.2 - 10 - 20 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie").Placement = App.Placement(App.Vector(600,35,510 - 22.2 - 10 - 20 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m002").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m003").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 22.2 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10 - 20 - 3 - 22.2 - 3),App.Rotation(App.Vector(0,0,1),0))

# For alternateur

# part_poulie_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001").Placement = App.Placement(App.Vector(600,35,-512.2 + 22.2 + 10 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_volant_inertie.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m004").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m004").Placement = App.Placement(App.Vector(600,35,-490 + 10),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m005").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m005").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2 + 3),App.Rotation(App.Vector(0,0,1),0))

# For moteur electrique

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m006").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 22.2 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# part_palier
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palier.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_palier").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel").getObject("part_palier").Placement = App.Placement(App.Vector(600 - 127/2,35 + 65/2,510 - 38 - 10 - 20 - 3 - 22.2 - 3 - 20),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m007").Placement = App.Placement(App.Vector(600,35,510 - 3 - 10 - 20 - 3 - 22.2 - 3 - 20 - 38),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m006").Placement = App.Placement(App.Vector(600,35,510 - 20 - 10 - 20 - 3 - 22.2 - 3 - 20 - 38 - 3),App.Rotation(App.Vector(0,0,1),0))

# For alternateur

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m008").Placement = App.Placement(App.Vector(600,35,-490 + 10 + 20 + 3 + 22.2 + 3 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_palier
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palier.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_palier001").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel").getObject("part_palier001").Placement = App.Placement(App.Vector(600 - 127/2,35 + 65/2,-490 + 10 + 20 + 3 + 22.2 + 3 + 20 + 3),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m009").Placement = App.Placement(App.Vector(600,35,-(490 - 10 - 20 - 3 - 22.2 - 3 - 20 - 3 - 38)),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m007").Placement = App.Placement(App.Vector(600,35,-(490 - 10 - 20 - 3 - 22.2 - 3 - 20 -3 - 38 - 3)),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_flywheel
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m002"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m003"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m003"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_poulie_volant_inertie001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_moyeu_amovible_volant_inertie001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m004"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m004"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m005"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m005"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m006"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_palier"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m007"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m006"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m008"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_palier001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m009"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m007"))

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel.stl")

del __objs__

# Generate PNG files
file = 'assembly_flywheel_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_moteur_electrique(self):
        print("test_assembly_moteur_electrique")

        if os.path.exists("assembly_moteur_electrique.py"):
            os.remove("assembly_moteur_electrique.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_moteur_electrique.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_moteur_electrique"


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

# Export assembly_moteur_electrique
__objs__=[]

# part_moteur_electrique
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moteur_electrique.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_moteur_electrique").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moteur_electrique").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moteur_electrique"))

# part_poulie_moteur_electrique
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_moteur_electrique.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_poulie_moteur_electrique").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_poulie_moteur_electrique").Placement = App.Placement(App.Vector(175/2,-(50-44.45),90),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_poulie_moteur_electrique"))

# part_moyeu_amovible_moteur_electrique
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_moteur_electrique.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_moyeu_amovible_moteur_electrique").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moyeu_amovible_moteur_electrique").Placement = App.Placement(App.Vector(175/2,-(50-44.45),90),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_moyeu_amovible_moteur_electrique"))

AB = 175
A = 140
B = 125
C = 56
y1 = AB/2 - A/2

# part_rondelle_10m

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(y1,C,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m001").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(y1,C + B,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m002").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(y1 + A,C + B,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_moteur_electrique")
FreeCADGui.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m003").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(y1 + A,C,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_moteur_electrique").getObject("part_rondelle_10m003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_moteur_electrique.stl")

del __objs__

# Generate PNG files
file = 'assembly_moteur_electrique_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\assembly_moteur_electrique.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_alternateur(self):
        print("test_assembly_alternateur")

        if os.path.exists("assembly_alternateur.py"):
            os.remove("assembly_alternateur.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_alternateur.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_alternateur"


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

# Export assembly_alternateur
__objs__=[]

# part_alternateur
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_alternateur.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_alternateur").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_alternateur").getObject("part_alternateur").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_alternateur"))

# part_poulie_alternateur
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_alternateur.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_poulie_alternateur").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_alternateur").getObject("part_poulie_alternateur").Placement = App.Placement(App.Vector(277/2,0,132),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_poulie_alternateur"))

# part_moyeu_amovible_alternateur
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_alternateur.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_moyeu_amovible_alternateur").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_alternateur").getObject("part_moyeu_amovible_alternateur").Placement = App.Placement(App.Vector(277/2,0,132),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_moyeu_amovible_alternateur"))

AB = 277
A = 220
B = 58
C = 305
D = 23
y1 = AB/2 - A/2

# part_rondelle_14m

# part_rondelle_14m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_rondelle_14m").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m").Placement = App.Placement(App.Vector(y1,B,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m"))

# part_rondelle_14m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_rondelle_14m001").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m001").Placement = App.Placement(App.Vector(y1,B + C + D,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m001"))

# part_rondelle_14m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_rondelle_14m002").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m002").Placement = App.Placement(App.Vector(y1 + A,B,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m002"))

# part_rondelle_14m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_alternateur")
FreeCADGui.getDocument("assembly_alternateur").getObject("part_rondelle_14m003").ShapeColor = (0.5,0.7,0.9)
FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m003").Placement = App.Placement(App.Vector(y1 + A,B + C + D,20),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_alternateur").getObject("part_rondelle_14m003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_alternateur.stl")

del __objs__

# Generate PNG files
file = 'assembly_alternateur_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\assembly_alternateur.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_socle(self):
        print("test_assembly_socle")

        if os.path.exists("assembly_socle.py"):
            os.remove("assembly_socle.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_socle.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_socle"


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

# part_palette
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palette.stl","assembly_socle")
FreeCADGui.getDocument("assembly_socle").getObject("part_palette").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_socle").getObject("part_palette").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

height_alternateur = 317
number_of_masselottes_per_slice_flywheel_per_block = 10
radius_flywheel = 500
maximal_radius_masselotte_compiled = round(math.sqrt(math.pow(radius_flywheel, 2) + math.pow(number_of_masselottes_per_slice_flywheel_per_block*20 + 35, 2)))
number_of_masselottes_for_moteur_electrique = 8

# For palier - 1
i1 = round((maximal_radius_masselotte_compiled + height_alternateur)/20)

# part_masselotte
for i in range(0, i1 - 1):
    x = (1200 - 200)/2
    y = 10 + 20 + 3 + 22.2 + 3 + 20 + 3
    z = 100 + i * 20
    
    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte").ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    else:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# For palier - 2

i2 = i1 * 2

for i in range(i1 - 1, i2 - 2):
    x = (1200 - 200)/2
    y = 1000 - (70 + 10 + 20 + 3 + 22.2 + 3 + 20)
    z = 100 + (i - (i1 - 1)) * 20
    
    if i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# For fixing the motor
for i in range(i2 - 2, i2 + number_of_masselottes_for_moteur_electrique):
    x = 10 + 175 + 12.5
    y = 1000 - 367 - 70
    z = 100 + (i - (i2 - 2)) * 20
    
    if i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

for i in range(i2 + number_of_masselottes_for_moteur_electrique, i2 + number_of_masselottes_for_moteur_electrique*2 + 2):
    x = 10 + 175 + 12.5
    y = 1000 - 70*3
    z = 100 + (i - (i2 + number_of_masselottes_for_moteur_electrique)) * 20
    
    if i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_masselotte.stl","assembly_socle")
        FreeCADGui.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).ShapeColor = (0.90,0.80,0.70)
        FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_socle
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_palette"))

# For palier - 1
for i in range(0, i1 - 1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte"))
    elif 1 <= i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))

# For palier - 2
for i in range(i1 - 1, i2 - 2):
    if i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)))
    elif 10 <= i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))
    elif 100 <= i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)))

# For fixing the motor
for i in range(i2 - 2, i2 + number_of_masselottes_for_moteur_electrique):
    if i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)))
    elif 10 <= i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))
    elif 100 <= i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)))

for i in range(i2 + number_of_masselottes_for_moteur_electrique, i2 + number_of_masselottes_for_moteur_electrique*2 + 2):
    if i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte00" + str(i)))
    elif 10 <= i < 100:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte0" + str(i)))
    elif 100 <= i < 1000:
        __objs__.append(FreeCAD.getDocument("assembly_socle").getObject("part_masselotte" + str(i)))

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle.stl")

del __objs__

# Generate PNG files
file = 'assembly_socle_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\assembly_socle.py"{)}.read{(}{)}{)}'
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
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

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

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# assembly_socle
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_socle").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_global").getObject("assembly_socle").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))

height_alternateur = 317
number_of_masselottes_per_slice_flywheel_per_block = 10
radius_flywheel = 500
maximal_radius_masselotte_compiled = round(math.sqrt(math.pow(radius_flywheel, 2) + math.pow(number_of_masselottes_per_slice_flywheel_per_block*20 + 35, 2)))
total_number_of_masselotte_compiled = round((maximal_radius_masselotte_compiled + height_alternateur)/20) - 1

# assembly_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_flywheel").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global").getObject("assembly_flywheel").Placement = App.Placement(App.Vector(0,490,70 + 100 + total_number_of_masselotte_compiled*20 - 2.5),App.Rotation(FreeCAD.Vector(1,0,0), -90))

# assembly_alternateur
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_alternateur.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_alternateur").ShapeColor = (0.50,0.40,0.30)
FreeCAD.getDocument("assembly_global").getObject("assembly_alternateur").Placement = App.Placement(App.Vector(1200 - 277 - 10,10 + 20 + 3 + 24,100),App.Rotation(App.Vector(1,0,0),0))

# assembly_moteur_electrique
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_moteur_electrique.stl","assembly_global")
FreeCADGui.getDocument("assembly_global").getObject("assembly_moteur_electrique").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_global").getObject("assembly_moteur_electrique").Placement = App.Placement(App.Vector(10 + 200 + 175,1000 - 50 - 20,100 + 200),App.Rotation(App.Vector(0,0,1),180))

setview()

# Export assembly_alternateur
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_socle"))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_flywheel"))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_alternateur"))
__objs__.append(FreeCAD.getDocument("assembly_global").getObject("assembly_moteur_electrique"))

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\assembly_global.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_plant(self):
        print("test_assembly_plant")

        if os.path.exists("assembly_plant.py"):
            os.remove("assembly_plant.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_plant.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_plant"


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

# assembly_global
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global.stl","assembly_plant")
FreeCADGui.getDocument("assembly_plant").getObject("assembly_global").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_plant").getObject("assembly_global").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))

setview()

# Export assembly_plant
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_plant").getObject("assembly_global"))

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_plant.stl")

del __objs__

# Generate PNG files
file = 'assembly_plant_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1\\\\assembly_plant.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_roulette_pivotante(self):
        print("test_assembly_roulette_pivotante")

        if os.path.exists("assembly_roulette_pivotante.py"):
            os.remove("assembly_roulette_pivotante.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_roulette_pivotante.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_roulette_pivotante"


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

L = 99
L3 = L - 3
s_rondelle_10m = 2
k_vis_m10 = 6.4

# Export assembly_roulette_pivotante
__objs__ = []

# part_roulette_pivotante
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_roulette_pivotante.stl","assembly_roulette_pivotante")
FreeCADGui.getDocument("assembly_roulette_pivotante").getObject("part_roulette_pivotante").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_roulette_pivotante").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_roulette_pivotante"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_roulette_pivotante")
FreeCADGui.getDocument("assembly_roulette_pivotante").getObject("part_rondelle_10m").ShapeColor = (0.30,0.50,0.70)
FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(0,0,L),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_rondelle_10m"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_roulette_pivotante")
FreeCADGui.getDocument("assembly_roulette_pivotante").getObject("part_rondelle_10m001").ShapeColor = (0.30,0.50,0.70)
FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(0,0,L3 - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_rondelle_10m001"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_roulette_pivotante")
FreeCADGui.getDocument("assembly_roulette_pivotante").getObject("part_vis_metal_m10_120l").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector(0,0,L3 - s_rondelle_10m - k_vis_m10),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_vis_metal_m10_120l"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_roulette_pivotante")
FreeCADGui.getDocument("assembly_roulette_pivotante").getObject("part_ecrou_10m").ShapeColor = (0.80,0.60,0.40)
FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(0,0,L + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante").getObject("part_ecrou_10m"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl")

del __objs__

# Generate PNG files
file = 'assembly_roulette_pivotante_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\assembly_roulette_pivotante.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_roulette_pivotante_2v(self):
        print("test_assembly_roulette_pivotante_2v")

        if os.path.exists("assembly_roulette_pivotante_2v.py"):
            os.remove("assembly_roulette_pivotante_2v.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_roulette_pivotante_2v.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_roulette_pivotante_2v"


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

L = 99
L3 = L - 3
s_rondelle_10m = 2
k_vis_m10 = 6.4

# Export assembly_roulette_pivotante_2v
__objs__ = []

# part_roulette_pivotante
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_roulette_pivotante.stl","assembly_roulette_pivotante_2v")
FreeCADGui.getDocument("assembly_roulette_pivotante_2v").getObject("part_roulette_pivotante").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_roulette_pivotante").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_roulette_pivotante"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_roulette_pivotante_2v")
FreeCADGui.getDocument("assembly_roulette_pivotante_2v").getObject("part_rondelle_10m").ShapeColor = (0.30,0.50,0.70)
FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(0,0,L),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_rondelle_10m"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_roulette_pivotante_2v")
FreeCADGui.getDocument("assembly_roulette_pivotante_2v").getObject("part_rondelle_10m001").ShapeColor = (0.30,0.50,0.70)
FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(0,0,L3 - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_rondelle_10m001"))

# part_vis_metal_m10_140l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_140l.stl","assembly_roulette_pivotante_2v")
FreeCADGui.getDocument("assembly_roulette_pivotante_2v").getObject("part_vis_metal_m10_140l").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_vis_metal_m10_140l").Placement = App.Placement(App.Vector(0,0,L3 - s_rondelle_10m - k_vis_m10),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_vis_metal_m10_140l"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_roulette_pivotante_2v")
FreeCADGui.getDocument("assembly_roulette_pivotante_2v").getObject("part_ecrou_10m").ShapeColor = (0.80,0.60,0.40)
FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(0,0,L + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_roulette_pivotante_2v").getObject("part_ecrou_10m"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante_2v.stl")

del __objs__

# Generate PNG files
file = 'assembly_roulette_pivotante_2v_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\assembly_roulette_pivotante_2v.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1PartsSteelBoxTubeForFlywheel(unittest.TestCase):
    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_the_rotor_flywheel(self):
        print("test_part_steel_box_tube_for_the_rotor_flywheel")

        if os.path.exists("part_steel_box_tube_for_the_rotor_flywheel.py"):
            os.remove("part_steel_box_tube_for_the_rotor_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_the_rotor_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_the_rotor_flywheel"


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

# part_steel_box_tube_for_the_rotor_flywheel
h = 50
l = 50
L = 1000
e = 3
part_steel_box_tube_for_the_rotor_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_the_rotor_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_the_rotor_flywheel = part_steel_box_tube_for_the_rotor_flywheel.cut(box_1)

# Cut part_steel_box_tube_for_the_rotor_flywheel by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h/4, h, (2*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_the_rotor_flywheel = part_steel_box_tube_for_the_rotor_flywheel.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(0, 0, (6*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_the_rotor_flywheel = part_steel_box_tube_for_the_rotor_flywheel.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector((L-h/2), 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_the_rotor_flywheel = part_steel_box_tube_for_the_rotor_flywheel.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector(0, 0, -(6*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_the_rotor_flywheel = part_steel_box_tube_for_the_rotor_flywheel.cut(cylinder_1)

# Cut part_steel_box_tube_for_the_rotor_flywheel by cylinder_2
cylinder_2 = Part.makeCylinder(20/2, 50)
# translation cylinder_2 for the first hole
cylinder_2_vector = FreeCAD.Vector(L/2, h/2, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_the_rotor_flywheel = part_steel_box_tube_for_the_rotor_flywheel.cut(cylinder_2)

Part.show(part_steel_box_tube_for_the_rotor_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_the_rotor_flywheel").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_the_rotor_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_the_rotor_flywheel_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_the_rotor_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_ground_flywheel(self):
        print("test_part_steel_box_tube_for_support_ground_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_ground_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_ground_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_ground_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_ground_flywheel"


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

# part_steel_box_tube_for_support_ground_flywheel
h = 50
l = 50
L = 500
e = 3
part_steel_box_tube_for_support_ground_flywheel = Part.makeBox(L, h, l)

# part_steel_box_tube_for_support_palier_flywheel
Lspf = 50*2 + 20*2 + 127
Ltspf = (L - Lspf)/2 + h/2

# Cut part_steel_box_tube_for_support_ground_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(box_1)

# Cut part_steel_box_tube_for_support_ground_flywheel by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, h)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h/2, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(L-h, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_1)

# Cut part_steel_box_tube_for_support_ground_flywheel by cylinder_2
cylinder_2 = Part.makeCylinder(10/2, h)
# translation cylinder_2 for the first hole
cylinder_2_vector = FreeCAD.Vector(Ltspf, (2*h)/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_2)
# translation cylinder_2 for the second hole
cylinder_2_vector = FreeCAD.Vector(0, (6*h)/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_2)
# translation cylinder_2 for the third hole
cylinder_2_vector = FreeCAD.Vector(Lspf - h, 0, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_2)
# translation cylinder_2 for the fourth hole
cylinder_2_vector = FreeCAD.Vector(0, -(6*h)/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_2)

# Cut part_steel_box_tube_for_support_ground_flywheel by cylinder_3
cylinder_3 = Part.makeCylinder(10/2, h)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_3_vector = FreeCAD.Vector(0, 0, 0)
cylinder_3.rotate(cylinder_3_vector, axe_x, 90)
# translation cylinder_3 for the first hole
cylinder_3_vector = FreeCAD.Vector(L/2, h, (2*h)/10)
cylinder_3.translate(cylinder_3_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_3)
# translation cylinder_3 for the second hole
cylinder_3_vector = FreeCAD.Vector(0, 0, (6*h)/10)
cylinder_3.translate(cylinder_3_vector)
part_steel_box_tube_for_support_ground_flywheel = part_steel_box_tube_for_support_ground_flywheel.cut(cylinder_3)

Part.show(part_steel_box_tube_for_support_ground_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_ground_flywheel").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_ground_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_ground_flywheel_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_ground_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_palier_flywheel(self):
        print("test_part_steel_box_tube_for_support_palier_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_palier_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_palier_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_palier_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_palier_flywheel"


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

# part_palier
L1 = 127
J = 95
e1 = 20

# part_steel_box_tube_for_support_palier_flywheel
h = 50
l = 50
L = 50*2 + 20*2 + L1
e = 3
part_steel_box_tube_for_support_palier_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_palier_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_palier_flywheel = part_steel_box_tube_for_support_palier_flywheel.cut(box_1)

# Cut part_steel_box_tube_for_support_palier_flywheel by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h/2, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_palier_flywheel = part_steel_box_tube_for_support_palier_flywheel.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(L-h, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_palier_flywheel = part_steel_box_tube_for_support_palier_flywheel.cut(cylinder_1)

# Cut part_steel_box_tube_for_support_palier_flywheel by cylinder_2
cylinder_2 = Part.makeCylinder(13/2, 50)
# translation cylinder_2 for the first hole
cylinder_2_vector = FreeCAD.Vector(h + e1 + (L1-J)/2, h/2, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_palier_flywheel = part_steel_box_tube_for_support_palier_flywheel.cut(cylinder_2)
# translation cylinder_2 for the second hole
cylinder_2_vector = FreeCAD.Vector(J, 0, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_palier_flywheel = part_steel_box_tube_for_support_palier_flywheel.cut(cylinder_2)

Part.show(part_steel_box_tube_for_support_palier_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_palier_flywheel").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_palier_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_palier_flywheel_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_palier_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_elevator_flywheel(self):
        print("test_part_steel_box_tube_for_support_elevator_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_elevator_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_elevator_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_elevator_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_elevator_flywheel"


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

L_flywheel = 1000
h_tube = 50
number_of_weights = 1
h_ecrou = 10
s_rondelle_10m = 2

# part_steel_box_tube_for_support_elevator_flywheel
h = 50
l = 50
L_elevator = math.sqrt(math.pow(L_flywheel/2,2) + math.pow(h_tube/2 + number_of_weights*(h_tube/2) + h_ecrou + s_rondelle_10m + h_tube,2))+ 50*3
e = 3
part_steel_box_tube_for_support_elevator_flywheel = Part.makeBox(L_elevator, h, l)

# Cut part_steel_box_tube_for_support_elevator_flywheel by box_1
box_1 = Part.makeBox(L_elevator, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_elevator_flywheel = part_steel_box_tube_for_support_elevator_flywheel.cut(box_1)

# Cut part_steel_box_tube_for_support_elevator_flywheel by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, h)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector((2*h)/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_elevator_flywheel = part_steel_box_tube_for_support_elevator_flywheel.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_elevator_flywheel = part_steel_box_tube_for_support_elevator_flywheel.cut(cylinder_1)

# Cut part_steel_box_tube_for_support_elevator_flywheel by cylinder_2
cylinder_2 = Part.makeCylinder(10/2, h)
# rotation cylinder_2
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_2_vector = FreeCAD.Vector(0, 0, 0)
cylinder_2.rotate(cylinder_2_vector, axe_x, 90)
# translation cylinder_2 for the third hole
cylinder_2_vector = FreeCAD.Vector(L_elevator-h/2, h, h/2)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_elevator_flywheel = part_steel_box_tube_for_support_elevator_flywheel.cut(cylinder_2)

Part.show(part_steel_box_tube_for_support_elevator_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_elevator_flywheel").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_elevator_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_elevator_flywheel_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_elevator_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_flywheel(self):
        print("test_part_steel_box_tube_for_support_link_flywheel")

        if os.path.exists("part_steel_box_tube_for_support_link_flywheel.py"):
            os.remove("part_steel_box_tube_for_support_link_flywheel.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_flywheel.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_flywheel"


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

L_flywheel = 1000
s_rondelle_20m = 3
h_ecrou = 20
L_moyeu_amovible_volant_inertie = 22.2
h1_palier = 38

# part_steel_box_tube_for_support_link_flywheel
h = 50
l = 50
L = (L_flywheel/2 + 10 - 38 - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou)*2 + h1_palier
e = 3
part_steel_box_tube_for_support_link_flywheel = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_flywheel by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_flywheel = part_steel_box_tube_for_support_link_flywheel.cut(box_1)

# Cut part_steel_box_tube_for_support_link_flywheel by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, h)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector((2*h)/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_flywheel = part_steel_box_tube_for_support_link_flywheel.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_flywheel = part_steel_box_tube_for_support_link_flywheel.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector(L - ((8*h)/10)*2, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_flywheel = part_steel_box_tube_for_support_link_flywheel.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_flywheel = part_steel_box_tube_for_support_link_flywheel.cut(cylinder_1)

Part.show(part_steel_box_tube_for_support_link_flywheel)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_flywheel").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_flywheel.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_link_flywheel_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_link_flywheel.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2239-8441-fer-carre-acier-sur-mesure.html#/586-section-25_x_25_mm
    def test_part_steel_box_for_weight(self):
        print("test_part_steel_box_for_weight")

        if os.path.exists("part_steel_box_for_weight.py"):
            os.remove("part_steel_box_for_weight.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_for_weight.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_weight"


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

# part_steel_box_for_weight
h = 25
l = 25
L = 500
part_steel_box_for_weight = Part.makeBox(L, h, l)

h_tube_flywheel = 50

# Cut part_steel_box_for_weight by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, h)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(L/2 - h_tube_flywheel/2 + (2*h_tube_flywheel)/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_for_weight = part_steel_box_for_weight.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector((6*h_tube_flywheel)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_for_weight = part_steel_box_for_weight.cut(cylinder_1)

Part.show(part_steel_box_for_weight)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_weight").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_for_weight.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_for_weight_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_for_weight.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1PartsSteelBoxTubeForMotor(unittest.TestCase):
    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_horizontal_motor(self):
        print("test_part_steel_box_tube_for_support_horizontal_motor")

        if os.path.exists("part_steel_box_tube_for_support_horizontal_motor.py"):
            os.remove("part_steel_box_tube_for_support_horizontal_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_horizontal_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_horizontal_motor"


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

# part_steel_box_tube_for_support_horizontal_motor
h = 50
l = 50
L = 367
E = 50
e = 3

part_steel_box_tube_for_support_horizontal_motor = Part.makeBox(L-E, h, l)

# Cut part_steel_box_tube_for_support_horizontal_motor by box_1
box_1 = Part.makeBox(L-E, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_horizontal_motor = part_steel_box_tube_for_support_horizontal_motor.cut(box_1)

# Cut part_steel_box_tube_for_support_horizontal_motor by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector((2*h)/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor = part_steel_box_tube_for_support_horizontal_motor.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor = part_steel_box_tube_for_support_horizontal_motor.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector((L-E)-2*((8*h)/10), 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor = part_steel_box_tube_for_support_horizontal_motor.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor = part_steel_box_tube_for_support_horizontal_motor.cut(cylinder_1)

Part.show(part_steel_box_tube_for_support_horizontal_motor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_horizontal_motor").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_motor.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_horizontal_motor_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_horizontal_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_horizontal_motor_2(self):
        print("test_part_steel_box_tube_for_support_horizontal_motor_2")

        if os.path.exists("part_steel_box_tube_for_support_horizontal_motor_2.py"):
            os.remove("part_steel_box_tube_for_support_horizontal_motor_2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_horizontal_motor_2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_horizontal_motor_2"


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

# part_steel_box_tube_for_support_horizontal_motor_2
h = 50
l = 50
L = 367
E = 50
e = 3
part_steel_box_tube_for_support_horizontal_motor_2 = Part.makeBox(L - E, h, l)

# Cut part_steel_box_tube_for_support_horizontal_motor_2 by box_1
box_1 = Part.makeBox(L - E, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(box_1)

# Cut part_steel_box_tube_for_support_horizontal_motor_2 by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector((2*h)/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_1)
# translation cylinder_1 for the second hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_1)
# translation cylinder_1 for the second hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector((L - E) - 2*(8*h/10), 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_1)
# translation cylinder_1 for the second hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector(6*h/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_1)

# Cut part_steel_box_tube_for_support_horizontal_motor_2 by cylinder_2
cylinder_2 = Part.makeCylinder(10/2, 50)
# translation cylinder_2 for the first hole
cylinder_2_vector = FreeCAD.Vector((3*h)/2, 2*h/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_2)
# translation cylinder_2 for the second hole
cylinder_2_vector = FreeCAD.Vector(0, 6*h/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_2)
# translation cylinder_2 for the third hole
cylinder_2_vector = FreeCAD.Vector((L - E) - 2*(3*h/2), 0, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_2)
# translation cylinder_2 for the fourth hole
cylinder_2_vector = FreeCAD.Vector(0, -6*h/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_2)

# Cut part_steel_box_tube_for_support_horizontal_motor_2 by cylinder_3
cylinder_3 = Part.makeCylinder(10/2, 50)
# translation cylinder_3 for the first hole
cylinder_3_vector = FreeCAD.Vector((L - E)/2, h/2, 0)
cylinder_3.translate(cylinder_3_vector)
part_steel_box_tube_for_support_horizontal_motor_2 = part_steel_box_tube_for_support_horizontal_motor_2.cut(cylinder_3)

Part.show(part_steel_box_tube_for_support_horizontal_motor_2)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_horizontal_motor_2").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_motor_2.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_horizontal_motor_2_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_horizontal_motor_2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_vertical_motor(self):
        print("test_part_steel_box_tube_for_support_vertical_motor")

        if os.path.exists("part_steel_box_tube_for_support_vertical_motor.py"):
            os.remove("part_steel_box_tube_for_support_vertical_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_vertical_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_vertical_motor"


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

# part_steel_box_tube_for_support_vertical_motor
h = 50
l = 50
L = 50*2 + 50*3
e = 3
part_steel_box_tube_for_support_vertical_motor = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_vertical_motor by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_vertical_motor = part_steel_box_tube_for_support_vertical_motor.cut(box_1)

# Cut part_steel_box_tube_for_support_vertical_motor by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h/2, h, (2*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_motor = part_steel_box_tube_for_support_vertical_motor.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(0, 0, (6*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_motor = part_steel_box_tube_for_support_vertical_motor.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector(L-h, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_motor = part_steel_box_tube_for_support_vertical_motor.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector(0, 0, -(6*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_motor = part_steel_box_tube_for_support_vertical_motor.cut(cylinder_1)

Part.show(part_steel_box_tube_for_support_vertical_motor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_vertical_motor").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_motor.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_vertical_motor_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_vertical_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_motor(self):
        print("test_part_steel_box_tube_for_support_link_motor")

        if os.path.exists("part_steel_box_tube_for_support_link_motor.py"):
            os.remove("part_steel_box_tube_for_support_link_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_motor"


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

# part_steel_box_tube_for_support_link_motor
h = 50
l = 50
L = 175
e = 3
part_steel_box_tube_for_support_link_motor = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_motor by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_motor = part_steel_box_tube_for_support_link_motor.cut(box_1)

# Cut part_steel_box_tube_for_support_link_motor by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(2*h/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_motor = part_steel_box_tube_for_support_link_motor.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(6*h/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_motor = part_steel_box_tube_for_support_link_motor.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector(L - 2*(8*h/10), 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_motor = part_steel_box_tube_for_support_link_motor.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector(6*h/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_motor = part_steel_box_tube_for_support_link_motor.cut(cylinder_1)

# Cut part_steel_box_tube_for_support_link_motor by cylinder_2
cylinder_2 = Part.makeCylinder(10/2, 50)
# rotation cylinder_2
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_2_vector = FreeCAD.Vector(0, 0, 0)
cylinder_2.rotate(cylinder_2_vector, axe_x, 90)
# translation cylinder_2 for the first hole
cylinder_2_vector = FreeCAD.Vector(L/2, h, h/2)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_link_motor = part_steel_box_tube_for_support_link_motor.cut(cylinder_2)

Part.show(part_steel_box_tube_for_support_link_motor)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_motor").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_link_motor_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_link_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_motor_2(self):
        print("test_part_steel_box_tube_for_support_link_motor_2")

        if os.path.exists("part_steel_box_tube_for_support_link_motor_2.py"):
            os.remove("part_steel_box_tube_for_support_link_motor_2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_motor_2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_motor_2"


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

# part_steel_box_tube_for_support_link_motor_2
h = 50
l = 50
L = 175
e = 3
part_steel_box_tube_for_support_link_motor_2 = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_motor_2 by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_motor_2 = part_steel_box_tube_for_support_link_motor_2.cut(box_1)

# Cut part_steel_box_tube_for_support_link_motor_2 by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h/2, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_motor_2 = part_steel_box_tube_for_support_link_motor_2.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(L-h, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_motor_2 = part_steel_box_tube_for_support_link_motor_2.cut(cylinder_1)

Part.show(part_steel_box_tube_for_support_link_motor_2)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_motor_2").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor_2.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_link_motor_2_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_link_motor_2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1PartsSteelBoxTubeForGenerator(unittest.TestCase):
    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_horizontal_generator(self):
        print("test_part_steel_box_tube_for_support_horizontal_generator")

        if os.path.exists("part_steel_box_tube_for_support_horizontal_generator.py"):
            os.remove("part_steel_box_tube_for_support_horizontal_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_horizontal_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_horizontal_generator"


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

# part_steel_box_tube_for_support_horizontal_generator
h = 50
l = 50
L = 454
e = 3
part_steel_box_tube_for_support_horizontal_generator = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_horizontal_generator by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_horizontal_generator = part_steel_box_tube_for_support_horizontal_generator.cut(box_1)

# Cut part_steel_box_tube_for_support_horizontal_generator by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector((2*h)/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator = part_steel_box_tube_for_support_horizontal_generator.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator = part_steel_box_tube_for_support_horizontal_generator.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector(L-2*((8*h)/10), 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator = part_steel_box_tube_for_support_horizontal_generator.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator = part_steel_box_tube_for_support_horizontal_generator.cut(cylinder_1)

Part.show(part_steel_box_tube_for_support_horizontal_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_horizontal_generator").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_horizontal_generator_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_horizontal_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_horizontal_generator_2(self):
        print("test_part_steel_box_tube_for_support_horizontal_generator_2")

        if os.path.exists("part_steel_box_tube_for_support_horizontal_generator_2.py"):
            os.remove("part_steel_box_tube_for_support_horizontal_generator_2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_horizontal_generator_2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_horizontal_generator_2"


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

# part_steel_box_tube_for_support_horizontal_generator_2
h = 50
l = 50
L = 454
e = 3
part_steel_box_tube_for_support_horizontal_generator_2 = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_horizontal_generator_2 by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(box_1)

# Cut part_steel_box_tube_for_support_horizontal_generator_2 by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector((2*h)/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_1)
# translation cylinder_1 for the second hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector((6*h)/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_1)
# translation cylinder_1 for the second hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector(L - 2*(8*h/10), 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_1)
# translation cylinder_1 for the second hole for axe_x 90
cylinder_1_vector = FreeCAD.Vector(6*h/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_1)

# Cut part_steel_box_tube_for_support_horizontal_generator_2 by cylinder_2
cylinder_2 = Part.makeCylinder(10/2, 50)
# translation cylinder_2 for the first hole
cylinder_2_vector = FreeCAD.Vector((3*h)/2, 2*h/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_2)
# translation cylinder_2 for the second hole
cylinder_2_vector = FreeCAD.Vector(0, 6*h/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_2)
# translation cylinder_2 for the third hole
cylinder_2_vector = FreeCAD.Vector(L - 2*(3*h/2), 0, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_2)
# translation cylinder_2 for the fourth hole
cylinder_2_vector = FreeCAD.Vector(0, -6*h/10, 0)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_2)

# Cut part_steel_box_tube_for_support_horizontal_generator_2 by cylinder_3
cylinder_3 = Part.makeCylinder(10/2, 50)
# translation cylinder_3 for the first hole
cylinder_3_vector = FreeCAD.Vector(L/2, h/2, 0)
cylinder_3.translate(cylinder_3_vector)
part_steel_box_tube_for_support_horizontal_generator_2 = part_steel_box_tube_for_support_horizontal_generator_2.cut(cylinder_3)

Part.show(part_steel_box_tube_for_support_horizontal_generator_2)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_horizontal_generator_2").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_generator_2.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_horizontal_generator_2_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_horizontal_generator_2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_vertical_generator(self):
        print("test_part_steel_box_tube_for_support_vertical_generator")

        if os.path.exists("part_steel_box_tube_for_support_vertical_generator.py"):
            os.remove("part_steel_box_tube_for_support_vertical_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_vertical_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_vertical_generator"


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

# part_steel_box_tube_for_support_vertical_generator
h = 50
l = 50
L = 50*2 + 50*3
e = 3
part_steel_box_tube_for_support_vertical_generator = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_vertical_generator by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_vertical_generator = part_steel_box_tube_for_support_vertical_generator.cut(box_1)

# Cut part_steel_box_tube_for_support_vertical_generator by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h/2, h, (2*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_generator = part_steel_box_tube_for_support_vertical_generator.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(0, 0, (6*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_generator = part_steel_box_tube_for_support_vertical_generator.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector(L-h, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_generator = part_steel_box_tube_for_support_vertical_generator.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector(0, 0, -(6*h)/10)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_vertical_generator = part_steel_box_tube_for_support_vertical_generator.cut(cylinder_1)

Part.show(part_steel_box_tube_for_support_vertical_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_vertical_generator").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_vertical_generator_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_vertical_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_generator(self):
        print("test_part_steel_box_tube_for_support_link_generator")

        if os.path.exists("part_steel_box_tube_for_support_link_generator.py"):
            os.remove("part_steel_box_tube_for_support_link_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_generator"


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

# part_steel_box_tube_for_support_link_generator
h = 50
l = 50
L = 277
e = 3
part_steel_box_tube_for_support_link_generator = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_generator by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(box_1)

# Cut part_steel_box_tube_for_support_link_generator by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(2*h/10, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(6*h/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(cylinder_1)
# translation cylinder_1 for the third hole
cylinder_1_vector = FreeCAD.Vector(L - 2*(8*h/10), 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(cylinder_1)
# translation cylinder_1 for the fourth hole
cylinder_1_vector = FreeCAD.Vector(6*h/10, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(cylinder_1)

# Cut part_steel_box_tube_for_support_link_generator by cylinder_2
cylinder_2 = Part.makeCylinder(10/2, 50)
# rotation cylinder_2
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_2_vector = FreeCAD.Vector(0, 0, 0)
cylinder_2.rotate(cylinder_2_vector, axe_x, 90)
# translation cylinder_2 for the first hole
cylinder_2_vector = FreeCAD.Vector(L/2, h, h/2)
cylinder_2.translate(cylinder_2_vector)
part_steel_box_tube_for_support_link_generator = part_steel_box_tube_for_support_link_generator.cut(cylinder_2)

Part.show(part_steel_box_tube_for_support_link_generator)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_generator").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_generator.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_link_generator_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_link_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.commentfer.fr/acier-sur-mesure/2212-8346-tube-carre-acier-sur-mesure.html#/47-epaisseur-3_mm/591-section-50_x_50_mm
    def test_part_steel_box_tube_for_support_link_generator_2(self):
        print("test_part_steel_box_tube_for_support_link_generator_2")

        if os.path.exists("part_steel_box_tube_for_support_link_generator_2.py"):
            os.remove("part_steel_box_tube_for_support_link_generator_2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_steel_box_tube_for_support_link_generator_2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_tube_for_support_link_generator_2"


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

# part_steel_box_tube_for_support_link_generator_2
h = 50
l = 50
L = 277
e = 3
part_steel_box_tube_for_support_link_generator_2 = Part.makeBox(L, h, l)

# Cut part_steel_box_tube_for_support_link_generator_2 by box_1
box_1 = Part.makeBox(L, h - e*2, l - e*2)
box_1_vector = FreeCAD.Vector(0, e, e)
box_1.translate(box_1_vector)
part_steel_box_tube_for_support_link_generator_2 = part_steel_box_tube_for_support_link_generator_2.cut(box_1)

# Cut part_steel_box_tube_for_support_link_generator_2 by cylinder_1
cylinder_1 = Part.makeCylinder(10/2, 50)
# rotation cylinder_1
axe_x = FreeCAD.Vector(1, 0, 0)
cylinder_1_vector = FreeCAD.Vector(0, 0, 0)
cylinder_1.rotate(cylinder_1_vector, axe_x, 90)
# translation cylinder_1 for the first hole
cylinder_1_vector = FreeCAD.Vector(h/2, h, h/2)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_generator_2 = part_steel_box_tube_for_support_link_generator_2.cut(cylinder_1)
# translation cylinder_1 for the second hole
cylinder_1_vector = FreeCAD.Vector(L-h, 0, 0)
cylinder_1.translate(cylinder_1_vector)
part_steel_box_tube_for_support_link_generator_2 = part_steel_box_tube_for_support_link_generator_2.cut(cylinder_1)

Part.show(part_steel_box_tube_for_support_link_generator_2)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_tube_for_support_link_generator_2").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_generator_2.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_tube_for_support_link_generator_2_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine'
            '\\\\Version_1\\\\part_steel_box_tube_for_support_link_generator_2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1AssembliesWithSteelBoxTubesForFlywheel(unittest.TestCase):
    # ok
    def test_assembly_slice_flywheel_with_steel_box_tubes(self):
        print("test_assembly_slice_flywheel_with_steel_box_tubes")

        if os.path.exists("assembly_slice_flywheel_with_steel_box_tubes.py"):
            os.remove("assembly_slice_flywheel_with_steel_box_tubes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_slice_flywheel_with_steel_box_tubes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_slice_flywheel_with_steel_box_tubes"


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

# Export assembly_slice_flywheel_with_steel_box_tubes
__objs__ = []
h = 50
L_rotor = 1000
s = 2
k = 6.4
h_ecrou = 10

# part_steel_box_tube_for_the_rotor_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_the_rotor_flywheel.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_tube_for_the_rotor_flywheel").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_tube_for_the_rotor_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_tube_for_the_rotor_flywheel"))

# Block 1
# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(h/4,-s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector(h/4,-s-k,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(h/4,-s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m001"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector(h/4,-s-k,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m002").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(h/4,h,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m002"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m003").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(h/4,h,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m003"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(h/4,h + s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(h/4,h + s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m001"))

# part_steel_box_for_weight
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_for_weight.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight").Placement = App.Placement(App.Vector(0,h + s + h_ecrou,500/2 + 25),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m004").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m004"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m005").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m005"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25 + s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m002"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25 + s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m003"))

# Block 2
# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m006").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector(L_rotor-h/4,h,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m006"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(L_rotor-h/4,h+s+k,(2*h)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m007").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector(L_rotor-h/4,h,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m007"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(L_rotor-h/4,h+s+k,(8*h)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m008").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector(L_rotor-h/4,-s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m008"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m009").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector(L_rotor-h/4,-s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m009"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m004").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m004"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m005").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m005"))

# part_steel_box_for_weight
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_for_weight.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight001").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight001").Placement = App.Placement(App.Vector(L_rotor-25,-s-h_ecrou-25,500/2 + 25),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight001"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m010").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m010"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m011").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m011"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m006").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s-h_ecrou,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m006"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m007").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s-h_ecrou,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m007"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_slice_flywheel_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_slice_flywheel_with_steel_box_tubes_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_slice_flywheel_with_steel_box_tubes.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_flywheel_with_steel_box_tubes(self):
        print('test_assembly_flywheel_with_steel_box_tubes')

        if os.path.exists("assembly_flywheel_with_steel_box_tubes.py"):
            os.remove("assembly_flywheel_with_steel_box_tubes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_flywheel_with_steel_box_tubes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel_with_steel_box_tubes"


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

h_flywheel = 50
L_flywheel = 1000
s_rondelle_20m = 3
h_ecrou = 20
L_moyeu_amovible_volant_inertie = 22.2

# Export assembly_flywheel_with_steel_box_tubes
__objs__ = []

# assembly_slice_flywheel_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_slice_flywheel_with_steel_box_tubes.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("assembly_slice_flywheel_with_steel_box_tubes").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("assembly_slice_flywheel_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("assembly_slice_flywheel_with_steel_box_tubes"))

# part_tige_filetee_m20_1000l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_tige_filetee_m20_1000l.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.40,0.20,0.10)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-(L_flywheel-h_flywheel)/2),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_tige_filetee_m20_1000l"))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,h_flywheel),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m"))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-s_rondelle_20m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m001"))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,h_flywheel + s_rondelle_20m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m"))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,- s_rondelle_20m - h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m001"))

# For moteur electrique

# part_poulie_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - L_moyeu_amovible_volant_inertie - 10 - h_ecrou - s_rondelle_20m + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie"))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - L_moyeu_amovible_volant_inertie - 10 - h_ecrou - s_rondelle_20m + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m002").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - s_rondelle_20m - 10 - h_ecrou + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m002"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - h_ecrou - 10 + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m002"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m003").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - s_rondelle_20m - 10 - h_ecrou - L_moyeu_amovible_volant_inertie - s_rondelle_20m + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m003"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - s_rondelle_20m - 10 - h_ecrou - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m003"))

# For alternateur

# part_poulie_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 -12.2 + L_moyeu_amovible_volant_inertie + 10 + h_ecrou + s_rondelle_20m + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie001"))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie001"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m004").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m004"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m004").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m004"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m005").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m005"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m005").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m005"))

# For moteur electrique

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m006").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 + 10 - s_rondelle_20m - 10 - h_ecrou - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m006"))

# part_palier
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palier.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier").Placement = App.Placement(App.Vector(L_flywheel/2 - 127/2,h_flywheel/2 + 65/2,L_flywheel/2 + 10 - 38 - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m007").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 + 10 - s_rondelle_20m - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou - 38),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m007"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m006").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 + 10 - h_ecrou - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou - 38 - s_rondelle_20m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m006"))

# For alternateur

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m008").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m008"))

# part_palier
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palier.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier001").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier001").Placement = App.Placement(App.Vector(L_flywheel/2 - 127/2,h_flywheel/2 + 65/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 + s_rondelle_20m - s_rondelle_20m - 0.5),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier001"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m009").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 + s_rondelle_20m + 38 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m009"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m007").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 + s_rondelle_20m + 38 + s_rondelle_20m - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m007"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_flywheel_with_steel_box_tubes_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_flywheel_with_steel_box_tubes.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_half_socle_with_steel_box_tubes(self):
        print('test_assembly_half_socle_with_steel_box_tubes')

        if os.path.exists("assembly_half_socle_with_steel_box_tubes.py"):
            os.remove("assembly_half_socle_with_steel_box_tubes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_half_socle_with_steel_box_tubes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_half_socle_with_steel_box_tubes"


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

L_flywheel = 1000
number_of_weights = 1
h_ecrou_10m = 10
s_rondelle_10m = 2
s_rondelle_12m = 2.5

h_tube = 50
L_ground = 500
L_elevator = math.sqrt(math.pow(L_flywheel/2,2) + math.pow(h_tube/2 + number_of_weights*(h_tube/2) + h_ecrou_10m + s_rondelle_10m + h_tube,2))+ 50*3

# part_palier
L1 = 127
J = 95
e1 = 20
z_palier = 65

# part_steel_box_tube_for_support_palier_flywheel
Lspf = 50*2 + 20*2 + L1
Ltspf = (L_ground - Lspf)/2 + h_tube/2

k_vis_10m = 6.4

L_roulette_pivotante = 99

# Export assembly_half_socle_with_steel_box_tubes
__objs__ = []

# part_steel_box_tube_for_support_ground_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_ground_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_ground_flywheel").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_ground_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_ground_flywheel"))

# part_steel_box_tube_for_support_elevator_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_elevator_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel").Placement = App.Placement(App.Vector(Ltspf + h_tube/2,-2*h_tube,0),App.Rotation(App.Vector(0,1,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel"))

# part_steel_box_tube_for_support_elevator_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_elevator_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel001").Placement = App.Placement(App.Vector(Ltspf + h_tube/2 + Lspf - h_tube,-2*h_tube,0),App.Rotation(App.Vector(0,1,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel001"))

# part_steel_box_tube_for_support_palier_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_palier_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_palier_flywheel").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_palier_flywheel").Placement = App.Placement(App.Vector(Ltspf - h_tube/2,-h_tube,L_elevator - h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_palier_flywheel"))

# part_rondelle_10m for ground - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m"))

# part_rondelle_10m for ground - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m001"))

# part_rondelle_10m for ground - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m002"))

# part_rondelle_10m for ground - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m003"))

# part_rondelle_10m for ground - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m004").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m004"))

# part_rondelle_10m for ground - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m005").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m005"))

# part_rondelle_10m for ground - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m006").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector(Ltspf,s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m006"))

# part_rondelle_10m for ground - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m007").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector(Ltspf,s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m007"))

# part_rondelle_10m for ground - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m008").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m008"))

# part_rondelle_10m for ground - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m009").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m009"))

# part_rondelle_10m for elevator_1 - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m010").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m010"))

# part_rondelle_10m for elevator_1 - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m011").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m011"))

# part_rondelle_10m for elevator_2 - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m012").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m012"))

# part_rondelle_10m for elevator_2 - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m013").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m013"))

# part_rondelle_10m for elevator_1 - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m014").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m014").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m014"))

# part_rondelle_10m for elevator_2 - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m015").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m015").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m015"))

# part_rondelle_10m for palier - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m016").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m016").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m016"))

# part_rondelle_10m for palier - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m017").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m017").Placement = App.Placement(App.Vector(Ltspf,s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m017"))

# part_rondelle_12m for palier - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m"))

# part_rondelle_12m for palier - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m001").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m001").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m001"))

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector(Ltspf,k_vis_10m + s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector(Ltspf,k_vis_10m + s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,k_vis_10m + s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,k_vis_10m + s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003"))

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector(Ltspf,k_vis_10m + s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,k_vis_10m + s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,- s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,- s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l007"))

# part_vis_metal_m12_140l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m12_140l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l"))

# part_vis_metal_m12_140l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m12_140l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l001").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l001").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l001"))

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube - s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube - s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube - s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube - s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m003"))

# part_ecrou_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m004").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m004").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube - s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m004"))

# part_ecrou_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m005").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m005").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube - s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m005"))

# part_rondelle_12m for palier - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m002").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m002").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator + z_palier),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m002"))

# part_rondelle_12m for palier - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m003").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m003").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator + z_palier),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m003"))

# part_ecrou_12m for palier - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m").ShapeColor = (0.75,0.50,0.25)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator + z_palier + s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m"))

# part_ecrou_12m for palier - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m001").ShapeColor = (0.75,0.50,0.25)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m001").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator + z_palier + s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m001"))

# part_ecrou_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m006").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m006").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,h_tube + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m006"))

# part_ecrou_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m007").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m007").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,h_tube + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m007"))

# assembly_roulette_pivotante - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante").ShapeColor = (0.30,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,-L_roulette_pivotante - s_rondelle_10m - k_vis_10m - s_rondelle_10m*3 + 0.5),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante"))

# assembly_roulette_pivotante - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante001").ShapeColor = (0.30,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante001").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,-L_roulette_pivotante - s_rondelle_10m - k_vis_10m - s_rondelle_10m*3 + 0.5),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante001"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_half_socle_with_steel_box_tubes_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_half_socle_with_steel_box_tubes.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_complete_socle_with_steel_box_tubes(self):
        print("test_assembly_complete_socle_with_steel_box_tubes")

        if os.path.exists("assembly_complete_socle_with_steel_box_tubes.py"):
            os.remove("assembly_complete_socle_with_steel_box_tubes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_complete_socle_with_steel_box_tubes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_complete_socle_with_steel_box_tubes"


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

L_flywheel = 1000
s_rondelle_20m = 3
s_rondelle_10m = 2
h_ecrou = 20
L_moyeu_amovible_volant_inertie = 22.2
h1_palier = 38

h_tube = 50
L_ground = 500
L_link = (L_flywheel/2 + 10 - 38 - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou)*2 + h1_palier

# Export assembly_complete_socle_with_steel_box_tubes
__objs__ = []

# assembly_half_socle_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes").ShapeColor = (0.25,0.75,1.0)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes"))

# part_steel_box_tube_for_support_link_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_flywheel.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_link_flywheel").ShapeColor = (0.2,0.5,0.8)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_link_flywheel").Placement = App.Placement(App.Vector(L_ground/2 - h_tube/2,-L_link,h_tube),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_link_flywheel"))

# assembly_half_socle_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes001").ShapeColor = (0.25,0.75,1.0)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes001").Placement = App.Placement(App.Vector(L_ground,-L_link,0),App.Rotation(App.Vector(0,0,1),180))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes001"))

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (2*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (8*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m003"))

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (2*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (8*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_complete_socle_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_complete_socle_with_steel_box_tubes_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_complete_socle_with_steel_box_tubes.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_flywheel_global_with_steel_box_tubes(self):
        print("test_assembly_flywheel_global_with_steel_box_tubes")

        if os.path.exists("assembly_flywheel_global_with_steel_box_tubes.py"):
            os.remove("assembly_flywheel_global_with_steel_box_tubes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_flywheel_global_with_steel_box_tubes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel_global_with_steel_box_tubes"


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

h_tube = 50
number_of_weights = 1
h_ecrou_10m = 10
s_rondelle_10m = 2

L_flywheel = 1000
s_rondelle_20m = 3
h_ecrou_20m = 20
L_moyeu_amovible_volant_inertie = 22.2
h1_palier = 38

L_ground = 500
L_link = (L_flywheel/2 + 10 - h1_palier - 10 - h_ecrou_20m - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou_20m)*2 + h1_palier
L_elevator = math.sqrt(math.pow(L_flywheel/2,2) + math.pow(h_tube/2 + number_of_weights*(h_tube/2) + h_ecrou_10m + s_rondelle_10m + h_tube,2))+ 50*3
h_palier = 65
d_vis = 13

# Export assembly_flywheel_global_with_steel_box_tubes
__objs__ = []

# assembly_complete_socle_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_complete_socle_with_steel_box_tubes.stl","assembly_flywheel_global_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_complete_socle_with_steel_box_tubes").ShapeColor = (0.25,0.75,1.0)
FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_complete_socle_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_complete_socle_with_steel_box_tubes"))

# assembly_flywheel_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_with_steel_box_tubes.stl","assembly_flywheel_global_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_flywheel_with_steel_box_tubes").ShapeColor = (0.2,0.5,0.8)
FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_flywheel_with_steel_box_tubes").Placement = App.Placement(App.Vector(-L_ground/2,-L_link/2 + h1_palier - d_vis,L_elevator + (h_palier - h_tube)/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_flywheel_with_steel_box_tubes"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_global_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_flywheel_global_with_steel_box_tubes_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_flywheel_global_with_steel_box_tubes.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1AssembliesWithSteelBoxTubesForMotor(unittest.TestCase):
    # ok
    def test_assembly_half_socle_with_steel_box_tubes_for_motor(self):
        print("test_assembly_half_socle_with_steel_box_tubes_for_motor")

        if os.path.exists("assembly_half_socle_with_steel_box_tubes_for_motor.py"):
            os.remove("assembly_half_socle_with_steel_box_tubes_for_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_half_socle_with_steel_box_tubes_for_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_half_socle_with_steel_box_tubes_for_motor"


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

L_support_horizontal_motor = 367
E_support_horizontal_motor = 50
L_support_vertical_motor = 50*2 + 50*3
h_tube = 50
s_rondelle_10m = 2
k_vis_10m = 6.4
h_ecrou_10m = 10

# Export assembly_half_socle_with_steel_box_tubes_for_motor
__objs__ = []

# part_steel_box_tube_for_support_horizontal_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_motor.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_horizontal_motor").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_horizontal_motor").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_horizontal_motor"))

# part_steel_box_tube_for_support_vertical_motor - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_motor.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_vertical_motor").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_vertical_motor").Placement = App.Placement(App.Vector(0,-h_tube,h_tube),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_vertical_motor"))

# part_steel_box_tube_for_support_vertical_motor - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_motor.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_vertical_motor001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_vertical_motor001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - h_tube,-h_tube,h_tube),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_vertical_motor001"))

# part_steel_box_tube_for_support_horizontal_motor_2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_motor_2.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_horizontal_motor_2").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_horizontal_motor_2").Placement = App.Placement(App.Vector(0,0,-L_support_vertical_motor + h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_horizontal_motor_2"))

# part_rondelle_10m

# for_support_horizontal_motor

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007"))

# for_support_horizontal_motor_2

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m014").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m014").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,-h_tube,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m014"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m015").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m015").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,-h_tube,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m015"))

# part_rondelle_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m016").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m016").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_motor - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m016"))

# part_rondelle_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m017").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m017").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_motor - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m017"))

# part_rondelle_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m018").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m018").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_motor - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m018"))

# part_rondelle_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m019").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m019").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_motor - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m019"))

# part_rondelle_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m020").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m020").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,h_tube/2,-(L_support_vertical_motor - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m020"))

# part_vis_metal_m10_120l

# for_support_horizontal_motor

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003"))

# for_support_horizontal_motor_2

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_motor - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007"))

# part_ecrou_10m

# for_support_horizontal_motor

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003"))

# for_support_horizontal_motor_2

# part_ecrou_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m004").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m004").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_motor - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m004"))

# part_ecrou_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m005").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m005").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_motor - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m005"))

# part_ecrou_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m006").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m006").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_motor - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m006"))

# part_ecrou_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m007").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m007").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_motor - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m007"))

# part_ecrou_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m008").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m008").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_motor - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m008"))

# part_ecrou_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m009").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m009").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_motor - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m009"))

# part_ecrou_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m010").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m010").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_motor - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m010"))

# part_ecrou_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m011").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m011").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_motor - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m011"))

# part_ecrou_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m012").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m012").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,h_tube/2,-(L_support_vertical_motor - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m012"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_motor.stl")

del __objs__

# Generate PNG files
file = 'assembly_half_socle_with_steel_box_tubes_for_motor_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_half_socle_with_steel_box_tubes_for_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_socle_with_steel_box_tubes_for_motor(self):
        print("test_assembly_socle_with_steel_box_tubes_for_motor")

        if os.path.exists("assembly_socle_with_steel_box_tubes_for_motor.py"):
            os.remove("assembly_socle_with_steel_box_tubes_for_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_socle_with_steel_box_tubes_for_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_socle_with_steel_box_tubes_for_motor"


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

L_support_vertical_motor = 50*2 + 50*3
h_tube = 50
L_support_horizontal_motor = 367
E_support_horizontal_motor = 50
L_support_link_motor = 175
k_vis_10m = 6.4
L_roulette_pivotante = 99
h_ecrou_10m = 10

# Export assembly_socle_with_steel_box_tubes_for_motor
__objs__ = []

# assembly_half_socle_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor"))

# part_steel_box_tube_for_support_link_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor").ShapeColor = (0.70,0.50,0.20)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor").Placement = App.Placement(App.Vector(h_tube,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor"))

# part_steel_box_tube_for_support_link_motor_2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor_2.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor_2").ShapeColor = (0.70,0.30,0.10)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor_2").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2 - h_tube/2,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor_2"))

# part_steel_box_tube_for_support_link_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor001").ShapeColor = (0.70,0.50,0.20)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - 2*h_tube,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor001"))

# assembly_half_socle_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor),L_support_link_motor,0),App.Rotation(App.Vector(0,0,1),180))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor001"))

# part_rondelle_10m

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,h_tube/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007"))

# part_rondelle_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,L_support_link_motor - h_tube/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008"))

# part_rondelle_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009"))

# part_rondelle_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010"))

# part_rondelle_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011"))

# part_rondelle_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) -(3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012"))

# part_rondelle_10m - 14
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013"))

# part_ecrou_10m

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").ShapeColor = (0.33,0.22,0.11)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").ShapeColor = (0.33,0.22,0.11)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001"))

# part_vis_metal_m10_120l

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003"))

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007"))

# assembly_roulette_pivotante

# assembly_roulette_pivotante - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante"))

# assembly_roulette_pivotante - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante001").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante001"))

# assembly_roulette_pivotante_2v - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante_2v.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,h_tube/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v"))

# assembly_roulette_pivotante_2v - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante_2v.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v001").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,L_support_link_motor - h_tube/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v001"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle_with_steel_box_tubes_for_motor.stl")

del __objs__

# Generate PNG files
file = 'assembly_socle_with_steel_box_tubes_for_motor_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_socle_with_steel_box_tubes_for_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_global_with_steel_box_tubes_for_motor(self):
        print("test_assembly_global_with_steel_box_tubes_for_motor")

        if os.path.exists("assembly_global_with_steel_box_tubes_for_motor.py"):
            os.remove("assembly_global_with_steel_box_tubes_for_motor.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_global_with_steel_box_tubes_for_motor.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_with_steel_box_tubes_for_motor"


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

h_tube = 50
L_support_horizontal_motor = 367
E_support_horizontal_motor = 50
s_rondelle_10m = 2

# Export assembly_global_with_steel_box_tubes_for_motor
__objs__ = []

# assembly_socle_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle_with_steel_box_tubes_for_motor.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_socle_with_steel_box_tubes_for_motor").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_socle_with_steel_box_tubes_for_motor").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_socle_with_steel_box_tubes_for_motor"))

# assembly_moteur_electrique
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_moteur_electrique.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_moteur_electrique").ShapeColor = (0.30,0.20,0.10)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_moteur_electrique").Placement = App.Placement(App.Vector(L_support_horizontal_motor - E_support_horizontal_motor,0,h_tube),App.Rotation(App.Vector(0,0,1),90))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_moteur_electrique"))

# motor
A = 140
AB = 175
B = 125
C = 56
E = 50
L = 367
K = 10
y1 = (AB - A)/2
x1 = L - B - C - E

h_ecrou_10m = 10
k_vis_10m = 6.4

# part_rondelle_10m

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(x1 + B,y1,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(x1,y1 + A,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(x1 + B,y1 + A,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003"))

# part_ecrou_10m

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(x1 + B,y1,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(x1,y1 + A,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(x1 + B,y1 + A,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003"))

# part_vis_metal_m10_120l

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector(x1,y1,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector(x1 + B,y1,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(x1,y1 + A,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(x1 + B,y1 + A,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_motor.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_with_steel_box_tubes_for_motor_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_global_with_steel_box_tubes_for_motor.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1AssembliesWithSteelBoxTubesForGenerator(unittest.TestCase):
    # ok
    def test_assembly_half_socle_with_steel_box_tubes_for_generator(self):
        print("test_assembly_half_socle_with_steel_box_tubes_for_generator")

        if os.path.exists("assembly_half_socle_with_steel_box_tubes_for_generator.py"):
            os.remove("assembly_half_socle_with_steel_box_tubes_for_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_half_socle_with_steel_box_tubes_for_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_half_socle_with_steel_box_tubes_for_generator"


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

L_support_horizontal_generator = 454
L_support_vertical_generator = 50*2 + 50*3
h_tube = 50

# Export assembly_half_socle_with_steel_box_tubes_for_generator
__objs__ = []

# part_steel_box_tube_for_support_horizontal_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_generator.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator"))

# part_steel_box_tube_for_support_vertical_generator - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_generator.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator").Placement = App.Placement(App.Vector(0,-h_tube,h_tube),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator"))

# part_steel_box_tube_for_support_vertical_generator - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_generator.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator001").Placement = App.Placement(App.Vector(L_support_horizontal_generator - h_tube,-h_tube,h_tube),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator001"))

# part_steel_box_tube_for_support_horizontal_generator_2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_generator_2.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator_2").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator_2").Placement = App.Placement(App.Vector(0,0,-L_support_vertical_generator + h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator_2"))

# part_rondelle_10m

# for_support_horizontal_generator

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007"))

# for_support_horizontal_generator_2

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m014").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m014").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m014"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m015").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m015").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m015"))

# part_rondelle_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m016").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m016").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m016"))

# part_rondelle_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m017").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m017").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m017"))

# part_rondelle_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m018").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m018").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m018"))

# part_rondelle_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m019").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m019").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m019"))

# part_rondelle_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m020").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m020").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,h_tube/2,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m020"))

# part_vis_metal_m10_120l

# for_support_horizontal_generator

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003"))

# for_support_horizontal_motor_2

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007"))

# part_ecrou_10m

# for_support_horizontal_generator

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m002").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m003").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m003"))

# for_support_horizontal_generator_2

# part_ecrou_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m004").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m004").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m004"))

# part_ecrou_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m005").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m005").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m005"))

# part_ecrou_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m006").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m006").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m006"))

# part_ecrou_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m007").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m007").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m007"))

# part_ecrou_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m008").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m008").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m008"))

# part_ecrou_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m009").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m009").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m009"))

# part_ecrou_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m010").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m010").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m010"))

# part_ecrou_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m011").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m011").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m011"))

# part_ecrou_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m012").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m012").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,h_tube/2,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m012"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_generator.stl")

del __objs__

# Generate PNG files
file = 'assembly_half_socle_with_steel_box_tubes_for_generator_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_half_socle_with_steel_box_tubes_for_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_socle_with_steel_box_tubes_for_generator(self):
        print("test_assembly_socle_with_steel_box_tubes_for_generator")

        if os.path.exists("assembly_socle_with_steel_box_tubes_for_generator.py"):
            os.remove("assembly_socle_with_steel_box_tubes_for_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_socle_with_steel_box_tubes_for_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_socle_with_steel_box_tubes_for_generator"


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

L_support_vertical_generator = 50*2 + 50*3
h_tube = 50
L_support_horizontal_generator = 454
L_support_link_generator = 277

# Export assembly_socle_with_steel_box_tubes_for_generator
__objs__ = []

# assembly_half_socle_with_steel_box_tubes_for_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_generator.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_half_socle_with_steel_box_tubes_for_generator").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_half_socle_with_steel_box_tubes_for_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_half_socle_with_steel_box_tubes_for_generator"))

# part_steel_box_tube_for_support_link_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_generator.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator").ShapeColor = (0.70,0.50,0.20)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator").Placement = App.Placement(App.Vector(h_tube,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator"))

# part_steel_box_tube_for_support_link_generator_2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_generator_2.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator_2").ShapeColor = (0.70,0.30,0.10)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator_2").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2 - h_tube/2,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator_2"))

# part_steel_box_tube_for_support_link_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_generator.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator001").ShapeColor = (0.70,0.50,0.20)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator001").Placement = App.Placement(App.Vector(L_support_horizontal_generator - 2*h_tube,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_link_generator001"))

# assembly_half_socle_with_steel_box_tubes_for_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_generator.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_half_socle_with_steel_box_tubes_for_generator001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_half_socle_with_steel_box_tubes_for_generator001").Placement = App.Placement(App.Vector(L_support_horizontal_generator,L_support_link_generator,0),App.Rotation(App.Vector(0,0,1),180))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_half_socle_with_steel_box_tubes_for_generator001"))

# part_rondelle_10m

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator/2,-(L_support_vertical_generator - 2*h_tube) - h_tube),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,L_support_link_generator/2,-(L_support_vertical_generator - 2*h_tube) - h_tube),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator/2,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator - (8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator - (2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,h_tube/2,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007"))

# part_rondelle_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,L_support_link_generator - h_tube/2,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008"))

# part_rondelle_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009"))

# part_rondelle_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010"))

# part_rondelle_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,L_support_link_generator - (2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011"))

# part_rondelle_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector(L_support_horizontal_generator -(3*h_tube)/2,L_support_link_generator - (8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012"))

# part_rondelle_10m - 14
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,L_support_link_generator/2,-L_support_vertical_generator - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013"))

# part_ecrou_10m

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m").ShapeColor = (0.33,0.22,0.11)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator/2,-(L_support_vertical_generator - 2*h_tube) - h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001").ShapeColor = (0.33,0.22,0.11)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,L_support_link_generator/2,-(L_support_vertical_generator - 2*h_tube) - h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001"))

# part_vis_metal_m10_120l

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator - (8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003"))

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator - (2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,L_support_link_generator - (8*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,L_support_link_generator - (2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_generator - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007"))

# assembly_roulette_pivotante

# assembly_roulette_pivotante - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_generator/2,-L_support_vertical_generator - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante"))

# assembly_roulette_pivotante - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante001").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante001").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,L_support_link_generator/2,-L_support_vertical_generator - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante001"))

# assembly_roulette_pivotante_2v - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante_2v.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante_2v").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante_2v").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,h_tube/2,-L_support_vertical_generator - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante_2v"))

# assembly_roulette_pivotante_2v - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante_2v.stl","assembly_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante_2v001").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante_2v001").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,L_support_link_generator - h_tube/2,-L_support_vertical_generator - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_generator").getObject("assembly_roulette_pivotante_2v001"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle_with_steel_box_tubes_for_generator.stl")

del __objs__

# Generate PNG files
file = 'assembly_socle_with_steel_box_tubes_for_generator_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_socle_with_steel_box_tubes_for_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_global_with_steel_box_tubes_for_generator(self):
        print("test_assembly_global_with_steel_box_tubes_for_generator")

        if os.path.exists("assembly_global_with_steel_box_tubes_for_generator.py"):
            os.remove("assembly_global_with_steel_box_tubes_for_generator.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_global_with_steel_box_tubes_for_generator.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_with_steel_box_tubes_for_generator"


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

h_tube = 50
L_support_horizontal2_generator = 454

# Export assembly_global_with_steel_box_tubes_for_generator
__objs__ = []

# assembly_socle_with_steel_box_tubes_for_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle_with_steel_box_tubes_for_generator.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_socle_with_steel_box_tubes_for_generator").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_socle_with_steel_box_tubes_for_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_socle_with_steel_box_tubes_for_generator"))

# assembly_alternateur
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_alternateur.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_alternateur").ShapeColor = (0.30,0.20,0.10)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_alternateur").Placement = App.Placement(App.Vector(L_support_horizontal2_generator,0,h_tube),App.Rotation(App.Vector(0,0,1),90))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_alternateur"))

# generator
A1 = 220
AB = 277
B = 58
C = 305
D = 23
E = 50
K = 14
A = 454
x1 = A - B - C - D
y1 = (AB - A1)/2

h_ecrou_14m = 14
k_vis_14m = 8.8
s_rondelle_14m = 2.5

# part_rondelle_14m

# part_rondelle_14m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m"))

# part_rondelle_14m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m001").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m001").Placement = App.Placement(App.Vector(x1 + C + D,y1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m001"))

# part_rondelle_14m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m002").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m002").Placement = App.Placement(App.Vector(x1,y1 + A1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m002"))

# part_rondelle_14m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m003").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m003").Placement = App.Placement(App.Vector(x1 + C + D,y1 + A1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m003"))

# part_ecrou_14m

# part_ecrou_14m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m"))

# part_ecrou_14m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m001").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m001").Placement = App.Placement(App.Vector(x1 + C + D,y1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m001"))

# part_ecrou_14m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m002").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m002").Placement = App.Placement(App.Vector(x1,y1 + A1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m002"))

# part_ecrou_14m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m003").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m003").Placement = App.Placement(App.Vector(x1 + C + D,y1 + A1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m003"))

# part_vis_metal_m14_100l

# part_vis_metal_m14_100l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l").Placement = App.Placement(App.Vector(x1,y1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l"))

# part_vis_metal_m14_100l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l001").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l001").Placement = App.Placement(App.Vector(x1 + C + D,y1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l001"))

# part_vis_metal_m14_100l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l002").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l002").Placement = App.Placement(App.Vector(x1,y1 + A1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l002"))

# part_vis_metal_m14_100l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l003").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l003").Placement = App.Placement(App.Vector(x1 + C + D,y1 + A1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_generator.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_with_steel_box_tubes_for_generator_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_global_with_steel_box_tubes_for_generator.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


# ok
class UnitTestsChasCampbellGravitationalEngineVersion1AssembliesWithSteelBoxTubesForGravitationalEngine(unittest.TestCase):
    # ok
    def test_assembly_global_gravitational_engine_with_steel_box_tubes(self):
        print("test_assembly_global_gravitational_engine_with_steel_box_tubes")

        if os.path.exists("assembly_global_gravitational_engine_with_steel_box_tubes.py"):
            os.remove("assembly_global_gravitational_engine_with_steel_box_tubes.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_global_gravitational_engine_with_steel_box_tubes.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_gravitational_engine_with_steel_box_tubes"


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

L_flywheel = 1000
L_support_vertical_motor = 50*2 + 50*3
L_support_vertical_generator = 50*2 + 50*3
h_tube = 50
L_roulette_pivotante = 99
s_rondelle_10m = 2
h_ecrou_10m = 10
h_ecrou_20m = 20
h_moyeu_amovible_volant_inertie = 22.2

# Export assembly_global_gravitational_engine_with_steel_box_tubes
__objs__ = []

# assembly_global_with_steel_box_tubes_for_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_generator.stl","assembly_global_gravitational_engine_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_generator").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_generator").Placement = App.Placement(App.Vector(-L_flywheel/2 + h_tube*6,-(3*L_flywheel)/2 + h_tube*4,L_support_vertical_generator/2 + h_tube/2 + s_rondelle_10m + L_roulette_pivotante - 1),App.Rotation(App.Vector(0,0,1),90))
__objs__.append(FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_generator"))

# assembly_global_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_motor.stl","assembly_global_gravitational_engine_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_motor").ShapeColor = (0.30,0.20,0.10)
FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_motor").Placement = App.Placement(App.Vector(-L_flywheel/2,L_flywheel/2 - h_ecrou_20m - h_moyeu_amovible_volant_inertie - h_tube,L_support_vertical_motor/2 + h_tube/2 + s_rondelle_10m + L_roulette_pivotante - 1),App.Rotation(App.Vector(0,0,1),-90))
__objs__.append(FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_motor"))

# assembly_flywheel_global_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_global_with_steel_box_tubes.stl","assembly_global_gravitational_engine_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_flywheel_global_with_steel_box_tubes").ShapeColor = (0.80,0.60,0.40)
FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_flywheel_global_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_flywheel_global_with_steel_box_tubes"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_gravitational_engine_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_gravitational_engine_with_steel_box_tubes_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Chas_Campbell_Gravitational_Engine\\\\Version_1'
            '\\\\assembly_global_gravitational_engine_with_steel_box_tubes.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
