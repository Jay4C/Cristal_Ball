import FreeCAD, Part, Drawing, math, Mesh, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rotor_laser_cutting"


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
EPS_C = EPS * (-0.5)

maximal_diameter = 100

maximal_heigth = 15

# part_rotor_laser_cutting
part_rotor_laser_cutting = Part.makeCylinder(maximal_diameter/2, maximal_heigth)

# part_rotor_laser_cutting cut by cylinder_1
cylinder_1 = Part.makeCylinder(5, maximal_heigth)
part_rotor_laser_cutting = part_rotor_laser_cutting.cut(cylinder_1)

# holes for fixing the magnets
degre = 30
for i in range(int(360/degre)):
    radius = maximal_diameter/2 - 12.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor_laser_cutting = part_rotor_laser_cutting.cut(hole)

# holes for the cooling
degre = 90
for i in range(int(360/degre)):
    radius = 5 + 12.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor_laser_cutting = part_rotor_laser_cutting.cut(hole)

# holes for the cooling
degres = [1*45, 3*45, 5*45, 7*45]
for degre in degres:
    radius = math.sqrt(2*math.pow(16.25,2))
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(7.5, maximal_heigth)
    hole.translate(hole_vector)
    part_rotor_laser_cutting = part_rotor_laser_cutting.cut(hole)

Part.show(part_rotor_laser_cutting)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_rotor_laser_cutting").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20150188400A1_Magnetic_Flywheel_Induction_EMG_aka_Hatem_Motor/Version_1/part_rotor_laser_cutting.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20150188400A1_Magnetic_Flywheel_Induction_EMG_aka_Hatem_Motor/Version_1/part_rotor_laser_cutting.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_rotor_laser_cutting_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20150188400A1/' + file + str(i) + '.png',1117,388,'Current')
