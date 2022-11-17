import FreeCAD, Part, Mesh, math, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support"


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
EPS = 5/100

E_between_coils = 5 * (1 + EPS)
D_exterieur_coil = 40 * (1 + EPS)
h_support = 1
number_of_satellites = 8
k = 5.25
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 10 * (1 + EPS)
E = 3 * (1 + EPS)

cylinder_1 = Part.makeCylinder(De/2, h_support)

# cylinder_1 cut by cylinder_2
cylinder_2 = Part.makeCylinder(Dp/2, h_support)
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_1 cut by hole in several times
degre = 15
for i in range(int(360/degre)):
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(Dp/2, h_support)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cylinder_1 cut by hole in several times
degre = 120
for i in range(int(360/degre)):
    radius = (De/2 - Dp/2 - E)/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(Dp*2, h_support)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')
