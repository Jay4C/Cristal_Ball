import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_capacitors"


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

# Diametre maximal du tank
diametre_maximal_tank = 200

# Diametre maximal
diametre_maximal = diametre_maximal_tank - 3*2 - 5*2

# EPS= tolerance to use to cut the parts
EPS = 0.30
EPS_C = EPS * -0.5

e = 3 + EPS
d1 = 10 + EPS

s_rondelle_10m = 2
h_ecrou_10m = 8
e_capacitor_plate = 1

l_vis_150 = 150
number_of_capacitors = int((l_vis_150 - e - s_rondelle_10m*2 - h_ecrou_10m)/(e_capacitor_plate + s_rondelle_10m))

# For placing the part_bottom_support_capacitor_plate
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/part_bottom_support_capacitor_plate.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate").ShapeColor = (0.30,0.60,0.90)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("part_bottom_support_capacitor_plate"))

# Insertion the part_rondelle_nylon_10m
degre = 90
for i1 in range(0, 4):
    file = "part_rondelle_nylon_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -s_rondelle_10m
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_10m
degre = 90
for i1 in range(4, 8):
    file = "part_rondelle_nylon_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_inox_10m
degre = 90
for i1 in range(0, 4):
    file = "part_ecrou_inox_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = e + s_rondelle_10m
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# For placing the part_vis_inox_m10_200l
k = 6.40
degre = 180
for i3 in range(0, 2):
    file = "part_vis_inox_m10_200l"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(i3*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_10m - k
    color = (0.30,0.30,0.60)

    if i3 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)))

# For placing the part_vis_inox_m10_150l
k = 6.40
degres = [90, 270]
i3 = 0
for degre in degres:
    file = "part_vis_inox_m10_150l"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - s_rondelle_10m - k
    color = (0.30,0.60,0.60)

    if i3 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i3 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i3)))
    elif 10 <= i3 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i3)))
    elif 100 <= i3 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i3)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i3)))

    i3 += 1

# Insertion the part_rondelle_nylon_10m
degre = 0
for i1 in range(8, number_of_capacitors + 4):
    file = "part_rondelle_nylon_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (8))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_10m
degre = 90
for i1 in range(number_of_capacitors + 4, number_of_capacitors*2):
    file = "part_rondelle_nylon_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (number_of_capacitors + 4))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_10m
degre = 180
for i1 in range(number_of_capacitors*2, number_of_capacitors*3 - 4):
    file = "part_rondelle_nylon_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (number_of_capacitors*2))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_rondelle_nylon_10m
degre = 270
for i1 in range(number_of_capacitors*3 - 4, number_of_capacitors*4 - 8):
    file = "part_rondelle_nylon_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(i1 - (number_of_capacitors*3 - 4))
    color = (0.90,0.00,0.00)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_inox_10m
degre = 90
for i1 in range(4, 8):
    file = "part_ecrou_inox_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(number_of_capacitors - 4) - e_capacitor_plate
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_capacitor_plate
for i1 in range(0, number_of_capacitors - 5):
    file = "part_capacitor_plate"

    x = 0
    y = 0
    z = (e + s_rondelle_10m + h_ecrou_10m + s_rondelle_10m) + (s_rondelle_10m + e_capacitor_plate)*i1
    color = (0.50,0.50,0.00)

    angle_rotation = 0

    if i1 == 0 or i1 % 2 == 0:
        angle_rotation = 90
    else:
        angle_rotation = -90

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),angle_rotation))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_ecrou_inox_10m
degre = 90
for i1 in range(8, 12):
    file = "part_ecrou_inox_10m"

    radius = diametre_maximal/2 - 5 - 5
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = (e + s_rondelle_10m + h_ecrou_10m) + (s_rondelle_10m + e_capacitor_plate)*(number_of_capacitors - 4) - e_capacitor_plate + h_ecrou_10m
    color = (0.40,0.50,0.40)

    if i1 == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_6/" + DOC_NAME + ".stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = DOC_NAME + '_'
# Ombr�
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/6/' + file + str(i) + '.png',1117,388,'Current')
