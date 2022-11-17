import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_core_8mm_8mm_200mm"


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

# part_steel_box_for_core_8mm_8mm_200mm
h = 8
l = 8
L = 200
part_steel_box_for_core_8mm_8mm_200mm = Part.makeBox(L, h, l)

Part.show(part_steel_box_for_core_8mm_8mm_200mm)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_core_8mm_8mm_200mm").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US6362718B1_Motionless_Electromagnetic_Generator/Version_1/part_steel_box_for_core_8mm_8mm_200mm.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_steel_box_for_core_8_8_200_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US6362718B1/' + file + str(i) + '.png',1117,388,'Current')
