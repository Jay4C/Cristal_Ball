import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# imports from 4_Basics/Fixations
# ok
# ecrou metal m10 (part_ecrou_metal_10d_18_9e_8m)

# ok
# vis metal m10 (part_vis_metal_10d_18_9e_100l_6_4k)


# imports from 4_Basics/Permanent_Magnets/Ferrite
# part_p_m_r_1D20_2D10_6h for assembly : ok
# part_p_m_r_1D30_2D10_10h for assembly_5 : ok


# imports from 4_Basics/Permanent_Magnets/Neodyme
# part_p_m_r_1D20_2D10_6h_n for assembly_2 : ok
# part_p_m_r_1D15_2D10_2h_n for assembly_3 : ok
# part_p_m_r_1D18_2D10_4h_n for assembly_4 : ok


class UnitTestsVibratingMagnetElectromagneticGeneratorFlowerForParts(unittest.TestCase):
    # ok
    # 3D printing
    def test_part_support_coil_40de(self):
        print('test_part_support_coil_40de')

        if os.path.exists("part_support_coil_40de.py"):
            os.remove("part_support_coil_40de.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_support_coil_40de.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math, importDXF

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_coil_40de"


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
EPS = 0.30
EPS_C = EPS * -0.5

Di = 10 + EPS
hc = 1.2 + EPS
De = 40 + EPS
Dp = 10 + EPS
E = 1 + EPS
degre = 50

cylinder_1 = Part.makeCylinder(De/2, hc)

# cylinder_1 cut by cylinder_2
cylinder_2 = Part.makeCylinder(Di/2, hc)
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_1 cut by cylinder_4 in several times
for i in range(int(360/degre)):
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    cylinder_4_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_4 = Part.makeCylinder(Dp/2, hc)
    cylinder_4.translate(cylinder_4_vector)
    cylinder_1 = cylinder_1.cut(cylinder_4)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_support_coil_40de").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support_coil_40de.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_support_coil_40de_'
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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_1\\\\part_support_coil_40de.py"{)}.read{(}{)}{)}'
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
EPS = 5/100

E_between_coils = 5 * (1 + EPS)
D_exterieur_coil = 40 * (1 + EPS)
h_support = 1
number_of_satellites = 8
k = 5.25
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 10 * (1 + EPS)
E = 3 * (1 + EPS)

cylinder_1 = Part.makeCylinder(De/2, h_support)

# cylinder_1 cut by cylinder_2
cylinder_2 = Part.makeCylinder(Dp/2, h_support)
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_1 cut by hole in several times
degre = 15
for i in range(int(360/degre)):
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(Dp/2, h_support)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cylinder_1 cut by hole in several times
degre = 120
for i in range(int(360/degre)):
    radius = (De/2 - Dp/2 - E)/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(Dp*2, h_support)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support.dxf"

importDXF.export(__objs__, dxf_file)

setview()

# Generate PNG files
file = 'part_support_'
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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_1\\\\part_support.py"{)}.read{(}{)}{)}'
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
EPS = 5/100

E_between_coils = 5 * (1 + EPS)
D_exterieur_coil = 40 * (1 + EPS)
h_support = 1
number_of_satellites = 8
k = 5.25
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 10 * (1 + EPS)
E = 3 * (1 + EPS)
degre = 45

h_magnet = 6
EPS_1 = 0.3
h_support_coil = 1.2 + EPS_1
h_ecrou_10m = 8
l_vis = 100
number_of_magnets = int(round((l_vis - h_support*2 - h_support_coil*2 - h_ecrou_10m*2)/h_magnet))

# Insertion part_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_support").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_support").ShapeColor = (0.50,0.40,0.30)

# Insertion part_support_coil_40de
b = 0
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support_coil_40de.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_support_coil_40de").Placement = App.Placement(App.Vector(0, 0, h_support), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_support_coil_40de").ShapeColor = (0.50,0.50,0.50)
b += 1

# Insertion part_support_coil_40de
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Flower/Version_1/part_support_coil_40de.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_support_coil_40de00" + str(b)).Placement = App.Placement(App.Vector(0, 0, h_support + h_support_coil + h_magnet*number_of_magnets), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_support_coil_40de00" + str(b)).ShapeColor = (0.50,0.50,0.50)
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

# Insertion the part_p_m_r_1D20_2D10_6h
a = 0
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_support + h_support_coil + h_magnet*i
    color = (0.90,0.00,0.00)
    
    filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D10_6h.stl"
    file = "part_p_m_r_1D20_2D10_6h"
     
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

# Insertion the part_p_m_r_1D20_2D10_6h
degre = 45
for i in range(number_of_magnets, number_of_magnets*2):
    for i1 in range(1, int(360/degre) + 1):
        radius = De/2 - Dp/2 - E
        alpha=(i1*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = h_support + h_support_coil + h_magnet*(i - number_of_magnets)
        color = (0.90,0.00,0.00)
        
        filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D10_6h.stl"
        file = "part_p_m_r_1D20_2D10_6h"
        
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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_1\\\\assembly.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_2(self):
        print("test_assembly_2")

        if os.path.exists("assembly_2.py"):
            os.remove("assembly_2.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_2.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_2"


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
h_support = 1
number_of_satellites = 8
k = 5.25
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 10 * (1 + EPS)
E = 3 * (1 + EPS)
degre = 45

h_magnet = 6
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

# Insertion the part_p_m_r_1D20_2D10_6h_n
a = 0
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_support + h_support_coil + h_magnet*i
    color = (0.90,0.00,0.00)

    filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/part_p_m_r_1D20_2D10_6h_n.stl"
    file = "part_p_m_r_1D20_2D10_6h_n"

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

# Insertion the part_p_m_r_1D20_2D10_6h_n
degre = 45
for i in range(number_of_magnets, number_of_magnets*2):
    for i1 in range(1, int(360/degre) + 1):
        radius = De/2 - Dp/2 - E
        alpha=(i1*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = h_support + h_support_coil + h_magnet*(i - number_of_magnets)
        color = (0.90,0.00,0.00)

        filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/part_p_m_r_1D20_2D10_6h_n.stl"
        file = "part_p_m_r_1D20_2D10_6h_n"

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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_1\\\\assembly_2.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_3(self):
        print("test_assembly_3")

        if os.path.exists("assembly_3.py"):
            os.remove("assembly_3.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_3.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

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
h_support = 1
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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_1\\\\assembly_3.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_4(self):
        print("test_assembly_4")

        if os.path.exists("assembly_4.py"):
            os.remove("assembly_4.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_4.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_4"


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
h_support = 1
number_of_satellites = 8
k = 5.25
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 10 * (1 + EPS)
E = 3 * (1 + EPS)
degre = 45

h_magnet = 4
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

# Insertion the part_p_m_r_1D18_2D10_4h_n
a = 0
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_support + h_support_coil + h_magnet*i
    color = (0.90,0.00,0.00)

    filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/part_p_m_r_1D18_2D10_4h_n.stl"
    file = "part_p_m_r_1D18_2D10_4h_n"

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

# Insertion the part_p_m_r_1D18_2D10_4h_n
degre = 45
for i in range(number_of_magnets, number_of_magnets*2):
    for i1 in range(1, int(360/degre) + 1):
        radius = De/2 - Dp/2 - E
        alpha=(i1*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = h_support + h_support_coil + h_magnet*(i - number_of_magnets)
        color = (0.90,0.00,0.00)

        filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Neodyme/part_p_m_r_1D18_2D10_4h_n.stl"
        file = "part_p_m_r_1D18_2D10_4h_n"

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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_1\\\\assembly_4.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_5(self):
        print("test_assembly_5")

        if os.path.exists("assembly_5.py"):
            os.remove("assembly_5.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_5.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_5"


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
h_support = 1
number_of_satellites = 8
k = 5.25
De = (D_exterieur_coil + E_between_coils)*(number_of_satellites - k)
Dp = 10 * (1 + EPS)
E = 3 * (1 + EPS)
degre = 45

h_magnet = 10
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

# Insertion the part_p_m_r_1D30_2D10_10h
a = 0
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_support + h_support_coil + h_magnet*i
    color = (0.90,0.00,0.00)

    filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/part_p_m_r_1D30_2D10_10h.stl"
    file = "part_p_m_r_1D30_2D10_10h"

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

# Insertion the part_p_m_r_1D30_2D10_10h
degre = 45
for i in range(number_of_magnets, number_of_magnets*2):
    for i1 in range(1, int(360/degre) + 1):
        radius = De/2 - Dp/2 - E
        alpha=(i1*degre*math.pi)/180
        x = radius*math.cos(alpha)
        y = radius*math.sin(alpha)
        z = h_support + h_support_coil + h_magnet*(i - number_of_magnets)
        color = (0.90,0.00,0.00)

        filename = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/part_p_m_r_1D30_2D10_10h.stl"
        file = "part_p_m_r_1D30_2D10_10h"

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
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Flower\\\\Version_1\\\\assembly_5.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()