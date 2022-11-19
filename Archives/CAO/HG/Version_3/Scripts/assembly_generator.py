import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_generator"


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

assembly = "assembly_generator"

# Parameters
h_rondelle_30m = 4
h_ecrou_30m = 30*0.8
h_ecrou_12m = 12*0.8
k_vis_12m = 7.5
k_vis_20m = 12.5
h_rondelle_20m = 3
h_ecrou_20m = 16
h_rondelle_12m = 2.5
e_support = 5
h_palier_4_fixation_support = 38.1
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator/2 + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)
h1 = (L_tube - 170)/2

# assembly_shaft
color = (0.10, 0.20, 0.30)
assembly_shaft_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_shaft.stl"
Mesh.insert(assembly_shaft_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_shaft").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_shaft").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_support
x = 0
y = 0
z = (1000 - L_tube)/2 + h1 + 1
color = (0.20, 0.40, 0.60)
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,1,0),180))

# assembly_support
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube - h1 + 5 + 2
color = (0.20, 0.40, 0.60)
assembly_support_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_support.stl"
Mesh.insert(assembly_support_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_support001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_support001").Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),15*4))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m + 2
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_palier_2_fixation_ossature
x = -165/2
y = 84/2
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_4_fixation_support - h_rondelle_30m
color = (0.50, 0.90, 0.40)
part_palier_2_fixation_ossature_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_palier_2_fixation_ossature.stl"
Mesh.insert(part_palier_2_fixation_ossature_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_2_fixation_ossature").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_4_fixation_support - h_rondelle_30m - h_rondelle_30m
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_30m
x = 0
y = 0
z = (1000 - L_tube)/2 - 5 - h_palier_4_fixation_support - h_rondelle_30m - h_ecrou_30m - h_rondelle_30m - h_palier_4_fixation_support - h_rondelle_30m - h_rondelle_30m - h_ecrou_30m
color = (0.40, 0.30, 0.00)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m002").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m002").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_palier_2_fixation_ossature
x = -165/2
y = 84/2
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m
color = (0.50, 0.90, 0.40)
part_palier_2_fixation_ossature_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_palier_2_fixation_ossature.stl"
Mesh.insert(part_palier_2_fixation_ossature_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_palier_2_fixation_ossature001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),90))

# part_rondelle_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m + h_palier_2_fixation_ossature
color = (0.90, 0.50, 0.40)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m003").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m003").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# part_ecrou_30m
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + 3 + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m
color = (0.40, 0.30, 0.00)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# assembly_poulie
x = 0
y = 0
z = - h_palier_2_fixation_ossature - h_rondelle_30m - h_ecrou_30m - 8
color = (0.40, 0.40, 0.40)
assembly_poulie_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_poulie.stl"
Mesh.insert(assembly_poulie_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_poulie").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_poulie").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),0))

# assembly_poulie
x = 0
y = 0
z = (1000 - L_tube)/2 + L_tube + h1 + h_ecrou_30m
color = (0.40, 0.40, 0.40)
assembly_poulie_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/assembly_poulie.stl"
Mesh.insert(assembly_poulie_stl_file, assembly)
FreeCADGui.getDocument(assembly).getObject("assembly_poulie001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("assembly_poulie001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(1,0,0),180))

# part_vis_metal_m20_200l
# radius for fixing the device
d_tube = 159
d_nut = 36
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

color = (0.10, 0.50, 0.90)
title = 'part_vis_metal_m20_200l'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [60*1, 60*3, 60*5]
i1 = 0
for degre in degres:
    i = i1
    radius = r_f_d
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = (1000 - L_tube)/2 + h1 + 1 - k_vis_20m - h_rondelle_20m - 5

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
    
    i1 += 1

# part_ecrou_20m
# radius for fixing the device
d_tube = 159
d_nut = 36
r_f_d = (d_tube + 5*2 + 2*2 + d_nut)/2

color = (0.00, 0.00, 0.90)
title = 'part_ecrou_20m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
degres = [60*1, 60*3, 60*5]
i2 = 0
for degre in degres:
    i = i2
    radius = r_f_d
    alpha = (degre*math.pi)/180
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    z = (1000 - L_tube)/2 + h1 + 200 - h_ecrou_20m + 1

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
    
    i2 += 1

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_shaft"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_support001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_palier_2_fixation_ossature001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m002"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_poulie"))

__objs__.append(FreeCAD.getDocument(assembly).getObject("assembly_poulie001"))

title = "part_vis_metal_m20_200l"
for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_20m"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Cristal_Ball\\Archives\\CAO\\HG\\Version_3\\Png\\assembly_generator_'
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
