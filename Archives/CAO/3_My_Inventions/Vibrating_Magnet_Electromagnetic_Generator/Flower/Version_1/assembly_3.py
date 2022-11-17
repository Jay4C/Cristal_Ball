import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_3"


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

# EPS = tolerance to use to cut the parts
EPS = 5/100

E_between_coils = 5 * (1 + EPS)
D_exterieur_coil = 40 * (1 + EPS)
h_support = 2.2 * (1 + EPS)
number_of_satellites = 8
k = 5.25
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 10 * (1 + EPS)
E = 3 * (1 + EPS)
degre = 45

h_magnet = 2
EPS_1 = 0.3
h_support_coil = 1.2 + EPS_1
h_ecrou_10m = 8
l_vis = 100
number_of_magnets = int(round((l_vis - h_support*2 - h_support_coil*2 - h_ecrou_10m*2)/h_magnet))

# Insertion part_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_support").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_support").ShapeColor = (0.50,0.40,0.30)

# Insertion part_support_coil_40de
b = 0
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support_coil_40de.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_support_coil_40de").Placement = App.Placement(App.Vector(0, 0, h_support), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_support_coil_40de").ShapeColor = (0.50,0.50,0.50)
b += 1

# Insertion part_support_coil_40de
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support_coil_40de.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_support_coil_40de00" + str(b)).Placement = App.Placement(App.Vector(0, 0, h_support + h_support_coil + h_magnet*number_of_magnets), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_support_coil_40de00" + str(b)).ShapeColor = (0.50,0.50,0.50)
b += 1

# Insertion the part_support_coil_40de
degre = 45
for i1 in range(1, int(360/degre) + 1):
    file = "part_support_coil_40de"

    radius = De/2 - Dp/2 - E
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = h_support
    color = (0.50,0.50,0.50)

    if b == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= b < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(b)))
    elif 10 <= b < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(b)))
    elif 100 <= b < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(b)))

    b += 1

# Insertion the part_vis_metal_10d_18_9e_100l_6_4k
k_vis = 6.4
filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/part_vis_metal_10d_18_9e_100l_6_4k.stl"
file = "part_vis_metal_10d_18_9e_100l_6_4k"
Mesh.insert(filename, DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0, 0, -k_vis), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = (0.60,0.50,0.60)

# Insertion the part_vis_metal_10d_18_9e_100l_6_4k
degre = 45
for i1 in range(1, int(360/degre) + 1):
    radius = De/2 - Dp/2 - E
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -k_vis
    color = (0.60,0.50,0.60)

    if i1 == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= i1 < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i1)))
    elif 10 <= i1 < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i1)))
    elif 100 <= i1 < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(i1)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(i1)))

# Insertion the part_p_m_r_1D15_2D10_2h_n
a = 0
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_support + h_support_coil + h_magnet*i
    color = (0.90,0.00,0.00)

    filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/part_p_m_r_1D15_2D10_2h_n.stl"
    file = "part_p_m_r_1D15_2D10_2h_n"

    if a == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= a < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(a)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(a)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(i)))
    elif 10 <= a < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(a)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(a)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(i)))
    elif 100 <= a < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(a)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(a)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(a)))

    a += 1

# Insertion the part_p_m_r_1D15_2D10_2h_n
degre = 45
for i in range(number_of_magnets, number_of_magnets*2):
    for i1 in range(1, int(360/degre) + 1):
        radius = De/2 - Dp/2 - E
        alpha=(i1*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = h_support + h_support_coil + h_magnet*(i - number_of_magnets)
        color = (0.90,0.00,0.00)

        filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/part_p_m_r_1D15_2D10_2h_n.stl"
        file = "part_p_m_r_1D15_2D10_2h_n"

        if a == 0:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
        if 1 <= a < 10:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(a)).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(a)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(a)))
        elif 10 <= a < 100:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(a)).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(a)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(a)))
        elif 100 <= a < 1000:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file + str(a)).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file + str(a)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(a)))

        a += 1

# Insertion the part_support_coil_40de
degre = 45
for i1 in range(1, int(360/degre) + 1):
    file = "part_support_coil_40de"

    radius = De/2 - Dp/2 - E
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = h_support + h_support_coil + h_magnet*number_of_magnets
    color = (0.50,0.50,0.50)

    if b == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= b < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(b)))
    elif 10 <= b < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(b)))
    elif 100 <= b < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/" + file + ".stl",DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(b)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(b)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(b)))

    b += 1

# Insertion the part_ecrou_metal_10d_18_9e_8m
c = 0
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/part_ecrou_metal_10d_18_9e_8m.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_ecrou_metal_10d_18_9e_8m").Placement = App.Placement(App.Vector(0, 0, h_support + h_support_coil + h_magnet*number_of_magnets + h_support_coil), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_ecrou_metal_10d_18_9e_8m").ShapeColor = (0.10,0.90,0.00)
c += 1

Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/part_ecrou_metal_10d_18_9e_8m.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_ecrou_metal_10d_18_9e_8m00" + str(c)).Placement = App.Placement(App.Vector(0, 0, h_support + h_support_coil + h_magnet*number_of_magnets + h_support_coil + h_ecrou_10m + h_support), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_ecrou_metal_10d_18_9e_8m00" + str(c)).ShapeColor = (0.10,0.90,0.00)
c += 1

# Insertion the part_ecrou_metal_10d_18_9e_8m
degre = 45
for i1 in range(1, int(360/degre) + 1):
    file = "part_ecrou_metal_10d_18_9e_8m"
    filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/part_ecrou_metal_10d_18_9e_8m.stl"
    radius = De/2 - Dp/2 - E
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = h_support + h_support_coil + h_magnet*number_of_magnets + h_support_coil
    color = (0.10,0.90,0.00)

    if c == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= c < 10:
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

# Insertion the part_ecrou_metal_10d_18_9e_8m
degre = 45
for i1 in range(1, int(360/degre) + 1):
    file = "part_ecrou_metal_10d_18_9e_8m"
    filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/part_ecrou_metal_10d_18_9e_8m.stl"
    radius = De/2 - Dp/2 - E
    alpha=(i1*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = h_support + h_support_coil + h_magnet*number_of_magnets + h_support_coil + h_ecrou_10m + h_support
    color = (0.10,0.90,0.00)

    if c == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= c < 10:
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

# Insertion part_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("part_support001").Placement = App.Placement(App.Vector(0, 0, h_support + h_support_coil + h_magnet*number_of_magnets + h_support_coil + h_ecrou_10m), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("part_support001").ShapeColor = (0.50,0.40,0.30)

setview()

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/1/' + file + str(i) + '.png',1117,388,'Current')
