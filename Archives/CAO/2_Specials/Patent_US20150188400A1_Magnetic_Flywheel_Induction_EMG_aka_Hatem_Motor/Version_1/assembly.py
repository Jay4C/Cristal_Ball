import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly"


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

# insertion part_rotor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20150188400A1_Magnetic_Flywheel_Induction_EMG_aka_Hatem_Motor/Version_1/part_rotor.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rotor").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rotor").ShapeColor = (0.30,0.20,0.10)
FreeCADGui.getDocument("assembly").getObject("part_rotor").Transparency = 40

# insertion part_magnet for fixing the magnets
degre = 30
for i in range(int(360/degre)):
    axe_x = FreeCAD.Vector(1, 0, 0)    
    axe_y = FreeCAD.Vector(0, 1, 0)
    axe_z = FreeCAD.Vector(0, 0, 1)
    
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20150188400A1_Magnetic_Flywheel_Induction_EMG_aka_Hatem_Motor/Version_1/part_magnet.stl", "assembly")
    radius = maximal_diameter/2 + 3
    alpha=(i*degre*math.pi)/180
    magnet_vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 7.5)
    rotation_magnet_vector = App.Rotation(alpha*(360/(2*math.pi)) - 90, 0, 90)
    
    if i < 1:
        FreeCAD.getDocument("assembly").getObject("part_magnet").Placement = App.Placement(magnet_vector, rotation_magnet_vector)
        FreeCADGui.getDocument("assembly").getObject("part_magnet").ShapeColor = (0.50,0.50,0.50)
    elif i >= 1 and i < 10:
        FreeCAD.getDocument("assembly").getObject("part_magnet00" + str(i)).Placement = App.Placement(magnet_vector, rotation_magnet_vector)
        FreeCADGui.getDocument("assembly").getObject("part_magnet00" + str(i)).ShapeColor = (0.50,0.50,0.50)
    else:
        FreeCAD.getDocument("assembly").getObject("part_magnet0" + str(i)).Placement = App.Placement(magnet_vector, rotation_magnet_vector)
        FreeCADGui.getDocument("assembly").getObject("part_magnet0" + str(i)).ShapeColor = (0.50,0.50,0.50)
        
setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor"))

for i1 in range(int(360/degre)):
    if i1 < 1:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_magnet"))
    elif i1 >=1 and i1 < 10:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_magnet00" + str(i1)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_magnet0" + str(i1)))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20150188400A1_Magnetic_Flywheel_Induction_EMG_aka_Hatem_Motor/Version_1/assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_'
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
        