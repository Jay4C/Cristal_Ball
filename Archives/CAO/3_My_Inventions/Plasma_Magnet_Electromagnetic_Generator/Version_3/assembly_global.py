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
Di_c = 140 + EPS
Dp_2 = 6 + EPS

__objs__ = []

# ok
# Insertion the assembly_support
folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_3/"
file = "assembly_support"
filename = folder + file + ".stl"

color = (0.9, 0.8, 0.7)

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
# Insertion the assembly_support

# ok
# Insertion the part_p_m_r_1D140_2D60_20h
color = (0.70, 0.80, 0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D140_2D60_20h"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,2 + 20*0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(1)).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)).Placement = App.Placement(App.Vector(0,0,2 + 20*1),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)))

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(2)).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(2)).Placement = App.Placement(App.Vector(0,0,2 + 20*2),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(2)))
# Insertion the part_p_m_r_1D140_2D60_20h

# ok
# Insertion the assembly_support
folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_3/"
file = "assembly_support"
filename = folder + file + ".stl"

color = (0.9, 0.8, 0.7)

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(1)).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)).Placement = App.Placement(App.Vector(0,0,60 + 2 + 2),App.Rotation(App.Vector(0,1,0),180))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)))
# Insertion the assembly_support

# ok
# Insertion the part_vis_metal_6d_11_05e_70l_4k
c = 0
color = (0.90,0.50,0.20)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_vis_metal_6d_11_05e_70l_4k"
filename = folder + file + ".stl"

degre = 10
for i in range(0, int(360/degre)):
    radius = Di_c/2 + EPS + Dp_2/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -4

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
# Insertion the part_vis_metal_6d_11_05e_70l_4k

# ok
# Insertion the part_ecrou_metal_6d_11_05e_5m
d = 0
color = (0.90,0.10,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_6d_11_05e_5m"
filename = folder + file + ".stl"

degre = 10
for i in range(0, int(360/degre)):
    radius = Di_c/2 + EPS + Dp_2/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 2 + 60 + 2

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
# Insertion the part_ecrou_metal_6d_11_05e_5m

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_3/assembly_global.stl"

Mesh.export(__objs__, stl_file)

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')
