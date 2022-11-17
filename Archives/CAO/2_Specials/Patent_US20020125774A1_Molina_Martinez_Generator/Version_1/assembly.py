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

# insertion part_stator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_stator.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_stator").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_stator").ShapeColor = (0.50,0.50,0.50)
FreeCADGui.getDocument("assembly").getObject("part_stator").Transparency = 70

# insertion part_rotor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_rotor.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rotor").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rotor").ShapeColor = (0.10,0.20,0.30)

# insertion part_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_support").Placement = App.Placement(App.Vector(0, 0, -1), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_support").ShapeColor = (0.30,0.60,0.90)
FreeCADGui.getDocument("assembly").getObject("part_support").Transparency = 80

number_of_steps = 123

# insertion part_stator
for i in range(0, number_of_steps):
    location = (i+1)
    
    if i < 9:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_stator.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_stator00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_stator00" + str(i+1)).ShapeColor = (0.50,0.50,0.50)
        FreeCADGui.getDocument("assembly").getObject("part_stator00" + str(i+1)).Transparency = 70
    elif i < 99:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_stator.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_stator0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_stator0" + str(i+1)).ShapeColor = (0.50,0.50,0.50)
        FreeCADGui.getDocument("assembly").getObject("part_stator0" + str(i+1)).Transparency = 70
    else:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_stator.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_stator" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_stator" + str(i+1)).ShapeColor = (0.50,0.50,0.50)
        FreeCADGui.getDocument("assembly").getObject("part_stator" + str(i+1)).Transparency = 70
        
# insertion part_rotor
for i in range(0, number_of_steps):
    location = (i+1)
    
    if i < 9:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_rotor.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rotor00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rotor00" + str(i+1)).ShapeColor = (0.10,0.20,0.30)
    elif i < 99:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_rotor.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rotor0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rotor0" + str(i+1)).ShapeColor = (0.10,0.20,0.30)
    else:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_rotor.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rotor" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rotor" + str(i+1)).ShapeColor = (0.10,0.20,0.30)

# insertion part_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/part_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_support001").Placement = App.Placement(App.Vector(0, 0, number_of_steps+1), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_support001").ShapeColor = (0.30,0.60,0.90)
FreeCADGui.getDocument("assembly").getObject("part_support001").Transparency = 80

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_support001"))

# append part_stator
for i in range(0, number_of_steps):
    if i < 9:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator00" + str(i+1)))
    elif i < 99:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator0" + str(i+1)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_stator" + str(i+1)))

# append part_rotor
for i in range(0, number_of_steps):
    if i < 9:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor00" + str(i+1)))
    elif i < 99:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor0" + str(i+1)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_rotor" + str(i+1)))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US20020125774A1_Molina_Martinez_Generator/Version_1/assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US20020125774A1/' + file + str(i) + '.png',1117,388,'Current')
