import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# imports from 4_Basics/Fixations
# part_ecrou_metal_20d_32_95e_16m : ok
# part_vis_metal_20d_33_53e_100l_12_5k : ok

# imports from 4_Basics/Permanent_Magnets/Ferrite
# part_p_m_r_1D40_2D20_10h for assembly : ok


class UnitTestsVibratingMagnetElectromagneticGeneratorFlowerVersion2ForParts(unittest.TestCase):
    # ok
    # 3D printing
    def test_part_coil_80de(self):
        print('test_part_coil_80de')

        if os.path.exists("part_coil_80de.py"):
            os.remove("part_coil_80de.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_coil_80de.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_coil_80de"


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

# EPS = tolerance to use to cut the parts
EPS = 0.3

l_vis_100 = 100
h_ecrou_20d_16m = 16
h_support = 5
Di = 40 + EPS
h_coil = l_vis_100 - h_support*2 - h_ecrou_20d_16m + EPS
Dp = 16 + EPS
De = Di*2
E = 1 + EPS

cylinder_1 = Part.makeCylinder(De/2, h_coil)

# cylinder_1 cut by cylinder_2
cylinder_2 = Part.makeCylinder(Di/2, h_coil)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(De/2, h_coil - 2*2)

# cylinder_3 cut by cylinder_4
cylinder_4 = Part.makeCylinder((Di + 2)/2, h_coil)
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

degre = 36
# cylinder_1 cut by hole in several times
for i in range(int(360/degre)):
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(Dp/2, h_coil)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cut the holes for reducing the quantity of material
degre = 36
for a in range(1, 6):
    for i in range(int(360/degre)):
        dp = 10
        axe_y = FreeCAD.Vector(0, 1, 0)
        axe_z = FreeCAD.Vector(0, 0, 1)
        radius = 1
        alpha=(i*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), (dp + 2)*a)
        hole = Part.makeCylinder(dp/2, 40, hole_vector, axe_y)
        hole.rotate(hole_vector, axe_z, alpha*(360/(2*math.pi)) - 90)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_coil_80de").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_5/part_coil_80de.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_coil_80de_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_5\\\\part_coil_80de.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # Laser cutting
    def test_part_support(self):
        print('test_part_support')

        if os.path.exists("part_support.py"):
            os.remove("part_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support"


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

# EPS = tolerance to use to cut the parts
EPS = 0.15

E_between_coils = 3 + EPS
Di = 40 + EPS
D_exterieur_coil = Di*2
h_support = 5
number_of_satellites = 10
k = 6.5
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 20 + EPS
E = 3 + EPS

cylinder_1 = Part.makeCylinder(De/2, h_support)

# cylinder_1 cut by cylinder_2
cylinder_2 = Part.makeCylinder(Dp/2, h_support)
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_1 cut by hole in several times
degre = 36
for i in range(int(360/degre)):
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(Dp/2, h_support)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cylinder_1 cut by hole in several times
degre = 90
for i in range(int(360/degre)):
    radius = (De/2 - Dp/2 - E)/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(Dp*2.1, h_support)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_5/part_support.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_5/part_support.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_5\\\\part_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsVibratingMagnetElectromagneticGeneratorFlowerForAssemblies(unittest.TestCase):
    # ok
    def test_assembly(self):
        print("test_assembly")

        if os.path.exists("assembly.py"):
            os.remove("assembly.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

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
Di = 40 + EPS
D_exterieur_coil = Di*2
h_support = 5
number_of_satellites = 10
k = 6.5
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 20 + EPS
E = 3 + EPS
k_vis_20d_100l = 12.5
h_magnet_1D40_2D20_10h = 10
l_vis_100 = 100
h_ecrou_20d_16m = 16
h_coil = l_vis_100 - h_support*2 - h_ecrou_20d_16m + EPS
number_of_magnets = int(round(h_coil/h_magnet_1D40_2D20_10h))

# ok
# Insertion the part_support
b = 0
for i in range(0, 2):
    folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_5/"
    file = "part_support"
    filename = folder + file + ".stl"

    x = 0
    y = 0
    z = (h_support + h_coil)*i
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
# Insertion the part_vis_metal_20d_33_53e_100l_12_5k
c = 0
color = (0.50,0.50,0.50)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_vis_metal_20d_33_53e_100l_12_5k"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,-k_vis_20d_100l),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))

c += 1

degre = 36
for i in range(0, int(360/degre)):    
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -k_vis_20d_100l

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
# Insertion the part_vis_metal_20d_33_53e_100l_12_5k

# ok
# Insertion the part_p_m_r_1D40_2D20_10h (cote)
d = 0
color = (0.50,0.30,0.10)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D40_2D20_10h"
filename = folder + file + ".stl"

degre = 36
for i1 in range(0, number_of_magnets):
    for i2 in range(0, int(360/degre)):    
        radius = De/2 - Dp/2 - E
        alpha = (i2*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = h_support + h_magnet_1D40_2D20_10h*i1
    
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
# Insertion the part_p_m_r_1D40_2D20_10h (cote)

# ok
# Insertion the part_p_m_r_1D40_2D20_10h (middle)
color = (0.50,0.30,0.10)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D40_2D20_10h"
filename = folder + file + ".stl"

degre = 36
for i1 in range(0, number_of_magnets):
    for i2 in range(0, int(360/degre)):
        x = 0
        y = 0
        z = h_support + h_magnet_1D40_2D20_10h*i1
    
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
# Insertion the part_p_m_r_1D40_2D20_10h (middle)

# ok
# Insertion the part_coil_80de
e = 0
color = (0.10,0.30,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_5/"
file = "part_coil_80de"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,h_support),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))

e += 1

degre = 36
for i in range(0, int(360/degre)):    
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = h_support

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
# Insertion the part_coil_80de

# ok
# Insertion the part_ecrou_metal_20d_32_95e_16m
f = 0
color = (0.30,0.60,0.90)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_20d_32_95e_16m"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,h_support*2 + h_coil),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))

f += 1

degre = 36
for i in range(0, int(360/degre)):    
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = h_support*2 + h_coil

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
# Insertion the part_ecrou_metal_20d_32_95e_16m

setview()

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/Flower/5/' + file + str(i) + '.png',1117,388,'Current')
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_5\\\\assembly.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
