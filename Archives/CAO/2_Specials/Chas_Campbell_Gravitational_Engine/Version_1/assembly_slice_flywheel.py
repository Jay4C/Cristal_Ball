import FreeCAD, Part, Drawing, math, Mesh

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
