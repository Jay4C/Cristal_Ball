import FreeCAD, Part, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_equerre_assemblage_laser_cutting_v2"


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

d1 = 8.40
d2 = 16
s = 1.5
space_between_electrodes_axes = (50/2 - 4 - 4)*2

box_1 = Part.makeBox(space_between_electrodes_axes + d2, d2, s)

cylinder_1 = Part.makeCylinder(d1/2, s)
cylinder_1_vector = FreeCAD.Vector(d2/2, d2/2, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

cylinder_1_vector = FreeCAD.Vector(space_between_electrodes_axes, 0, 0)
cylinder_1.translate(cylinder_1_vector)
box_1 = box_1.cut(cylinder_1)

box_2 = Part.makeBox(space_between_electrodes_axes - d2, (d2-3)/2, s)
box_2_vector = FreeCAD.Vector(d2, 0, 0)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

box_2_vector = FreeCAD.Vector(0, (d2-3)/2 + 3, 0)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

cylinder_2 = Part.makeCylinder((d2+10)/2, s)
cylinder_3 = Part.makeCylinder(d2/2, s)
cylinder_2 = cylinder_2.cut(cylinder_3)
box_3 = Part.makeBox(d2+10, 3, s)
box_3_vector = FreeCAD.Vector(0, -1.5, 0)
box_3.translate(box_3_vector)
cylinder_2 = cylinder_2.cut(box_3)

cylinder_2_vector = FreeCAD.Vector(d2/2, d2/2, 0)
cylinder_2.translate(cylinder_2_vector)
box_1 = box_1.cut(cylinder_2)

cylinder_4 = Part.makeCylinder((d2+10)/2, s)
cylinder_4 = cylinder_4.cut(cylinder_3)
box_4 = Part.makeBox(d2+10, 3, s)
box_4_vector = FreeCAD.Vector(-d2 - 5, -1.5, 0)
box_4.translate(box_4_vector)
cylinder_4 = cylinder_4.cut(box_4)

cylinder_4_vector = FreeCAD.Vector(d2/2 + space_between_electrodes_axes, d2/2, 0)
cylinder_4.translate(cylinder_4_vector)
box_1 = box_1.cut(cylinder_4)

Part.show(box_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_equerre_assemblage_laser_cutting_v2").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Edwin_Gray_Power_Tube/Version_3/part_equerre_assemblage_laser_cutting_v2.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Edwin_Gray_Power_Tube/Version_3/part_equerre_assemblage_laser_cutting_v2.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_equerre_assemblage_laser_cutting_v2_v3_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Edwin_Gray/' + file + str(i) + '.png',1117,388,'Current')
