import FreeCAD, Part, Drawing, math, Mesh

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
