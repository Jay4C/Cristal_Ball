import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_shaft"


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

assembly = "assembly_shaft"

r_tube = 159/2
e_tube = 4
h_rondelle_30m = 4
h_ecrou_30m = 30*0.8
e_support = 5
h_palier_4_fixation_support = 38.1
h_palier_2_fixation_ossature = 48
h_poulie_generator = 25.4
L_tube = 1000 - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_poulie_generator + h_rondelle_30m + h_ecrou_30m) - (e_support + h_palier_4_fixation_support + h_rondelle_30m + h_ecrou_30m + h_rondelle_30m + h_palier_2_fixation_ossature + h_rondelle_30m + h_ecrou_30m)

Start_assembly_magnet = (1000 - L_tube)/2 + h_rondelle_30m + h_ecrou_30m
h_disc = 5
h_magnet = 20
h_assembly_magnet = h_disc + h_magnet + 2

# part_tige_filetee_m30_1000l
part_tige_filetee_m30_1000l_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_tige_filetee_m30_1000l.stl"
Mesh.insert(part_tige_filetee_m30_1000l_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_tige_filetee_m30_1000l").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m30_1000l").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_magnet
color = (0.70, 0.70, 0.70)
i2 = round((L_tube - 2*h_rondelle_30m - 2*h_ecrou_30m)/h_assembly_magnet)
title = 'assembly_magnet'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + title + ".stl"
for i in range(0, i2):
    x = 0
    y = 0
    z = Start_assembly_magnet + i * h_assembly_magnet

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

# part_tube
x = 0
y = 0
z = Start_assembly_magnet - h_rondelle_30m - h_ecrou_30m
color = (0.45, 0.99, 0.05)
part_tube_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_tube.stl"
Mesh.insert(part_tube_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_tube").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_tube").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
x = 0
y = 0
z = Start_assembly_magnet - h_rondelle_30m
color = (0.45, 0.05, 0.95)
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_30m
x = 0
y = 0
z = Start_assembly_magnet - h_rondelle_30m - h_ecrou_30m
color = (0.45, 0.55, 0.65)
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_30m
color = (0.45, 0.05, 0.95)
x = 0
y = 0
z = Start_assembly_magnet + i2 * h_assembly_magnet
part_rondelle_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_rondelle_30m.stl"
Mesh.insert(part_rondelle_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_rondelle_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_30m
color = (0.45, 0.55, 0.65)
x = 0
y = 0
z = Start_assembly_magnet + i2 * h_assembly_magnet + h_rondelle_30m
part_ecrou_30m_stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_ecrou_30m.stl"
Mesh.insert(part_ecrou_30m_stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject("part_ecrou_30m001").ShapeColor = color
FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export
__objs__ = []

__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tige_filetee_m30_1000l"))

title = "assembly_magnet"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

# part_tube
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_tube"))

# part_rondelle_30m
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m"))

# part_ecrou_30m
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m"))

# part_rondelle_30m001
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_rondelle_30m001"))

# part_ecrou_30m001
__objs__.append(FreeCAD.getDocument(assembly).getObject("part_ecrou_30m001"))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/" + assembly + ".stl")

del __objs__

# Generate PNG files
file = 'C:\\Users\\Jason\\Documents\\Devs\\Cristal_Ball\\Archives\\CAO\\HG\\Version_3\\Png\\' + assembly + '_'
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
