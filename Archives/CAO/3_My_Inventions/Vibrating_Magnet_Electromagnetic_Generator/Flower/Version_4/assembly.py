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

__objs__ = []

# EPS = tolerance to use to cut the parts
EPS = 0.15

E_between_coils = 3 + EPS
D_exterieur_coil = 40 + EPS
h_support = 5
number_of_satellites = 10
k = 6.3
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 20 + EPS
E = 3 + EPS
k_vis_20d_100l = 12.5
h_magnet_1D40_2D20_10h = 10
l_vis_100 = 100
h_ecrou_20d_16m = 16
h_tige = 1000
h_coil = l_vis_100 - h_magnet_1D40_2D20_10h*2 - h_support*2 - h_ecrou_20d_16m + EPS
number_of_steps = int(round(h_tige/(h_support*2 + h_magnet_1D40_2D20_10h*2 + h_coil)))

# ok
# Insertion the part_support
b = 0
for i in range(0, number_of_steps + 1):
    folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_4/"
    file = "part_support"
    filename = folder + file + ".stl"

    x = 0
    y = 0
    z = (h_coil + h_magnet_1D40_2D20_10h*2 + h_support)*i
    color = (0.50,0.40,0.30)

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
# Insertion the part_support

# ok
# Insertion the part_tige_filetee_acier_20d
c = 0
color = (0.50,0.50,0.50)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_tige_filetee_acier_20d"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,-h_ecrou_20d_16m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))

c += 1

degre = 36
for i in range(0, int(360/degre)):    
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -h_ecrou_20d_16m

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
# Insertion the part_tige_filetee_acier_20d

# ok
# Insertion the part_ecrou_metal_20d_32_95e_16m
f = 0
color = (0.30,0.60,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_20d_32_95e_16m"
filename = folder + file + ".stl"

degre = 36
for i in range(0, int(360/degre)):    
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -h_ecrou_20d_16m

    if f == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= f < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)))
    elif 10 <= f < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)))
    elif 100 <= f < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)))

    f += 1
# Insertion the part_ecrou_metal_20d_32_95e_16m

# ok
# Insertion the part_ecrou_metal_20d_32_95e_16m
color = (0.30,0.60,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_20d_32_95e_16m"
filename = folder + file + ".stl"

for i in range(0, 1):
    x = 0
    y = 0
    z = -h_ecrou_20d_16m

    if f == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    if 1 <= f < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)))
    elif 10 <= f < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)))
    elif 100 <= f < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)))

    f += 1
# Insertion the part_ecrou_metal_20d_32_95e_16m

# ok
# Insertion the part_p_m_r_1D40_2D20_10h (bottom)
d = 0
color = (0.50,0.30,0.10)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D40_2D20_10h"
filename = folder + file + ".stl"

degre = 36
for i1 in range(0, number_of_steps):
    for i2 in range(0, int(360/degre)):    
        radius = De/2 - Dp/2 - E
        alpha = (i2*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = h_support + (h_coil + h_magnet_1D40_2D20_10h*2 + h_support)*i1
    
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
# Insertion the part_p_m_r_1D40_2D20_10h (bottom)

# ok
# Insertion the part_p_m_r_1D40_2D20_10h (top)
color = (0.50,0.30,0.10)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D40_2D20_10h"
filename = folder + file + ".stl"

degre = 36
for i1 in range(0, number_of_steps):
    for i2 in range(0, int(360/degre)):    
        radius = De/2 - Dp/2 - E
        alpha = (i2*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = (h_support + h_magnet_1D40_2D20_10h + h_coil) + (h_coil + h_magnet_1D40_2D20_10h*2 + h_support)*i1
    
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
# Insertion the part_p_m_r_1D40_2D20_10h (top)

# ok
# Insertion the part_coil_40de
e = 0
color = (0.10,0.30,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_4/"
file = "part_coil_40de"
filename = folder + file + ".stl"

degre = 36
for i1 in range(0, number_of_steps):
    for i2 in range(0, int(360/degre)):    
        radius = De/2 - Dp/2 - E
        alpha=(i2*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = (h_support + h_magnet_1D40_2D20_10h) + (h_coil + h_magnet_1D40_2D20_10h*2 + h_support)*i1
    
        if e == 0:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
        elif 1 <= e < 10:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(e)).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(e)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(e)))
        elif 10 <= e < 100:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(e)).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(e)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(e)))
        elif 100 <= e < 1000:
            Mesh.insert(filename, DOC_NAME)
            FreeCADGui.getDocument(DOC_NAME).getObject(file + str(e)).ShapeColor = color
            FreeCAD.getDocument(DOC_NAME).getObject(file + str(e)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
            __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(e)))
    
        e += 1
# Insertion the part_coil_40de

# ok
# Insertion the part_ecrou_metal_20d_32_95e_16m
degre = 36
color = (0.30,0.60,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_20d_32_95e_16m"
filename = folder + file + ".stl"

for i in range(0, int(360/degre)):    
    radius = De/2 - Dp/2 - E
    alpha = (i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = h_tige - h_ecrou_20d_16m*3 + h_support/2

    if f == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    elif 1 <= f < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)))
    elif 10 <= f < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)))
    elif 100 <= f < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)))

    f += 1

# ok
# Insertion the part_ecrou_metal_20d_32_95e_16m
color = (0.30,0.60,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_20d_32_95e_16m"
filename = folder + file + ".stl"

for i in range(0, int(360/degre)):
    x = 0
    y = 0
    z = h_tige - h_ecrou_20d_16m*3 + h_support/2

    if f == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    elif 1 <= f < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(f)))
    elif 10 <= f < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(f)))
    elif 100 <= f < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(f)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(f)))

    f += 1

# ok
# Insertion the part_coil_40de (middle)
color = (0.10,0.30,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_4/"
file = "part_coil_40de"
filename = folder + file + ".stl"

for i1 in range(0, number_of_steps):
    x = 0
    y = 0
    z = (h_support + h_magnet_1D40_2D20_10h) + (h_coil + h_magnet_1D40_2D20_10h*2 + h_support)*i1

    if e == 0:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
    elif 1 <= e < 10:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(e)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(e)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(e)))
    elif 10 <= e < 100:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + "0" + str(e)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(e)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "0" + str(e)))
    elif 100 <= e < 1000:
        Mesh.insert(filename, DOC_NAME)
        FreeCADGui.getDocument(DOC_NAME).getObject(file + str(e)).ShapeColor = color
        FreeCAD.getDocument(DOC_NAME).getObject(file + str(e)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
        __objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + str(e)))

    e += 1
# Insertion the part_coil_40de (middle)

# ok
# Insertion the part_p_m_r_1D40_2D20_10h (middle - bottom)
color = (0.50,0.30,0.10)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D40_2D20_10h"
filename = folder + file + ".stl"

for i1 in range(0, number_of_steps):
    x = 0
    y = 0
    z = h_support + (h_coil + h_magnet_1D40_2D20_10h*2 + h_support)*i1

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
# Insertion the part_p_m_r_1D40_2D20_10h (middle - bottom)

# ok
# Insertion the part_p_m_r_1D40_2D20_10h (middle - top)
color = (0.50,0.30,0.10)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D40_2D20_10h"
filename = folder + file + ".stl"

for i1 in range(0, number_of_steps):
    x = 0
    y = 0
    z = (h_support + h_magnet_1D40_2D20_10h + h_coil) + (h_coil + h_magnet_1D40_2D20_10h*2 + h_support)*i1

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
# Insertion the part_p_m_r_1D40_2D20_10h (middle - top)

setview()

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle', 5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/4/' + file + str(i) + '.png',1117,388,'Current')
