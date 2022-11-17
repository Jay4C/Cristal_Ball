import FreeCAD, Part, Drawing, math, Mesh

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
