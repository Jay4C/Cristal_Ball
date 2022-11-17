import FreeCAD, Part, Drawing, math, Mesh

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
