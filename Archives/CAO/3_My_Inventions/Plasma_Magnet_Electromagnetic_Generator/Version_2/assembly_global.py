import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global"


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

EPS = 0.3
Di_c = 40 + EPS
Dp_2 = 8

__objs__ = []

# ok
# Insertion the assembly_support
folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_2/"
file = "assembly_support"
filename = folder + file + ".stl"

color = (0.9, 0.8, 0.7)

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
# Insertion the assembly_support

# ok
# Insertion the part_p_m_r_1D40_2D20_10h
b = 0
for i in range(0, 10):
    folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
    file = "part_p_m_r_1D40_2D20_10h"
    filename = folder + file + ".stl"

    x = 0
    y = 0
    z = 2 + 10*i
    color = (0.30,0.40,0.50)

    if b == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    elif 1 <= b < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(b)))
    elif 10 <= b < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(b)))
    elif 100 <= b < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(b)))

    b += 1
# Insertion the part_p_m_r_1D40_2D20_10h

# ok
# Insertion the assembly_support
folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_2/"
file = "assembly_support"
filename = folder + file + ".stl"

color = (0.9, 0.8, 0.7)

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(1)).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)).Placement = App.Placement(App.Vector(0,0,100 + 2 + 2),App.Rotation(App.Vector(0,1,0),180))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)))
# Insertion the assembly_support

# ok
# Insertion the part_vis_metal_8d_14_38e_110l_5_3k
c = 0
color = (0.90,0.50,0.20)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_vis_metal_8d_14_38e_110l_5_3k"
filename = folder + file + ".stl"

degre = 36
for i in range(0, int(360/degre)):
    radius = Di_c/2 + EPS + Dp_2/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -5.3

    if c == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    elif 1 <= c < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(c)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(c)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(c)))
    elif 10 <= c < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(c)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(c)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(c)))
    elif 100 <= c < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(c)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(c)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(c)))

    c += 1
# Insertion the part_vis_metal_8d_14_38e_110l_5_3k

# ok
# Insertion the part_ecrou_metal_8d_14_38e_6_5m
d = 0
color = (0.90,0.10,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_8d_14_38e_6_5m"
filename = folder + file + ".stl"

degre = 36
for i in range(0, int(360/degre)):
    radius = Di_c/2 + EPS + Dp_2/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 2 + 100 + 2

    if d == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    elif 1 <= d < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(d)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(d)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(d)))
    elif 10 <= d < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(d)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(d)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(d)))
    elif 100 <= d < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(d)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(d)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(d)))

    d += 1
# Insertion the part_ecrou_metal_8d_14_38e_6_5m

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_2/assembly_global.stl"

Mesh.export(__objs__, stl_file)

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/2/' + file + str(i) + '.png',1117,388,'Current')
