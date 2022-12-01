import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_device"


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

assembly = "assembly_device"

# part_support
title = "part_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_magnet_1d140_2d60_20e
color = (0.90,0.80,0.70)
i1 = 3
title = 'part_magnet_1d140_2d60_20e'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
for i in range(0, i1):
    x = 0
    y = 0
    z = 2 + i * 21

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_faraday_disc
color = (0.70,0.00,0.00)
i2 = 3
title = 'part_faraday_disc'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
for i in range(0, i2):
    x = 0
    y = 0
    z = 22 + i * 21

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_vis_metal_m6_70l
color = (0.70,0.70,0.00)
i3 = 9
title = 'part_vis_metal_m6_70l'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
for i in range(0, i3):
    k = 4
    degre = (360/i3)
    d3 = 11.05
    radius = (140 + 2*1.5 + 2*(d3/2))/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -k

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_6m
color = (0.90,0.00,0.90)
i4 = 9
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
for i in range(0, i4):
    degre = (360/i4)
    d3 = 11.05
    radius = (140 + 2*1.5 + 2*(d3/2))/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 2 + 3 * 21 + 2

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_6m
color = (0.90,0.00,0.90)
i7 = 9
i8 = 3
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
i9 = i4
for j in range(0, i8):
    for i in range(0, i7):
        degre = (360/i7)
        d3 = 11.05
        radius = (140 + 2*1.5 + 2*(d3/2))/2
        alpha=(i*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = 2 + j * 21
    
        if i9 == 0:
            Mesh.insert(stl_file,assembly)
            FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
            FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
        elif i9 >= 1 and i9 < 10:
            Mesh.insert(stl_file,assembly)
            FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i9)).ShapeColor = color
            FreeCAD.getDocument(assembly).getObject(title + "00" + str(i9)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
        elif i9 >= 10 and i9 < 100:
            Mesh.insert(stl_file,assembly)
            FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i9)).ShapeColor = color
            FreeCAD.getDocument(assembly).getObject(title + "0" + str(i9)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
        elif i9 >= 100 and i9 < 1000:
            Mesh.insert(stl_file,assembly)
            FreeCADGui.getDocument(assembly).getObject(title + str(i9)).ShapeColor = color
            FreeCAD.getDocument(assembly).getObject(title + str(i9)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
        
        i9 += 1
        
# part_support
z = 2 + 3 * 21
title = "part_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title + "001").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject(title + "001").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))

# part_vis_metal_m22_60
k = 14
z = 2 + 3 * 21 - k - 9*2
color = (0.90,0.00,0.10)
title = "part_vis_metal_m22_60l"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))

# part_vis_metal_m22_60l
k = 14
z = k + 2 + 9
color = (0.90,0.00,0.10)
title = "part_vis_metal_m22_60l"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title + "001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject(title + "001").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,1,0),180))

# part_magnet_1d45_2d22_9e
color = (0.70,0.00,0.00)
i5 = 1
title = 'part_magnet_1d45_2d22_9e'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
for i in range(0, i5):
    x = 0
    y = 0
    z = 2 + i * 9

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_magnet_1d45_2d22_9e
color = (0.70,0.00,0.00)
i6 = 2
title = 'part_magnet_1d45_2d22_9e'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
for i in range(i5, i5 + i6):
    x = 0
    y = 0
    z = (2 + 3 * 21 + 2 - 2 - 9) - (i - i5) * 9

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_22m
z = -22
title = "part_ecrou_22m"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_22m
z = 2 + 3 * 21 + 2
title = "part_ecrou_22m"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title + "001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument(assembly).getObject(title + "001").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__=[]
title = "part_support"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_magnet_1d140_2d60_20e"
for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_faraday_disc"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m6_70l"
for i in range(0, i3):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))
        
title = "part_ecrou_6m"
for i in range(0, i4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_6m"
for i in range(i4, i4 + i7):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_magnet_1d45_2d22_9e"
for i in range(0, i5):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))
        
title = "part_magnet_1d45_2d22_9e"
for i in range(i5, i5 + i6):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/3_My_Inventions/PHG/Version_1/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Cristal_Ball\\Archives\\CAO\\3_My_Inventions\\PHG\\Version_1\\Png\\assembly_device_'
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
