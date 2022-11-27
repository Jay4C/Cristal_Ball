import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_bottom"


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

__objs__ = []

# For placing part_bottom_support
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_bottom_support.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_bottom_support").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support"))

# For placing part_tank_d60_150l
Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/part_tank_d60_150l.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_tank_d60_150l").Placement = App.Placement(App.Vector(0, 0, 5), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_tank_d60_150l").ShapeColor = (0.90,6.00,0.30)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_tank_d60_150l"))

l_tank = 150
l_vis_6m = 90
e = l_tank - 100
e1 = e - 5
d_vis = 6
e_vis_6m = 11.05
d_m_tank = 60
d_m_b_s = d_m_tank + 0.1*2 + (e - e1)*2 + 1.5*2 + (e - e1)*2 + e_vis_6m*2 + (e - e1)*2
s_rondelle_nylon_6m = 1.6
degre = 30
number_of_holes = int(360/degre)

# Insertion part_rondelle_nylon_6m
for i1 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_rondelle_nylon_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e - 5 - s_rondelle_nylon_6m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion part_rondelle_nylon_6m
for i1 in range(number_of_holes, number_of_holes*2):
    doc = "assembly_bottom"
    file = "part_rondelle_nylon_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i1)))

# Insertion part_ecrou_inox_6m
for i2 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_ecrou_inox_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e + s_rondelle_nylon_6m
    color = (0.30,0.30,0.30)

    if i2 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# Insertion part_ecrou_inox_6m
for i2 in range(number_of_holes, number_of_holes*2):
    doc = "assembly_bottom"
    file = "part_ecrou_inox_6m"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i2*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e + s_rondelle_nylon_6m + s_rondelle_nylon_6m*10
    color = (0.30,0.30,0.30)

    if i2 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i2 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i2)))
    elif 10 <= i2 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i2)))
    elif 100 <= i2 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i2)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i2)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i2)))

# For placing the part_vis_metal_inox_m6_90l
k = 4
for i3 in range(0, number_of_holes):
    doc = "assembly_bottom"
    file = "part_vis_metal_inox_m6_90l"

    radius = d_m_b_s/2 - (e - e1)*2
    alpha=(i3*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e - 5 - k - s_rondelle_nylon_6m
    color = (0.30,0.70,0.70)

    if i3 == 0:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/" + file + ".stl",doc)
        FreeCADGui.getDocument(doc).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(doc).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(doc).getObject(file + str(i3)))

setview()

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/Stl/assembly_bottom.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Cristal_Ball\\Archives\\CAO\\1_Holomorphe\\Archie_Blue\\Version_5\\Png\\assembly_bottom_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage(file + str(i) + '.png',1117,388,'Current')
