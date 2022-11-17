import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# Function for creating each block square
def draw_block_square(h):
    filename = "part_block_square_" + h.replace(".", "_") + "h"

    print("test_" + filename)

    if os.path.exists(filename + ".py"):
        os.remove(filename + ".py")
    else:
        print("The file does not exist")

    # Writing to file
    with open(filename + ".py", "w") as file:
        # Writing data to a file
        file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

""")

        file.write('DOC_NAME = "' + filename + '" \n\n')

        file.write("""
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
EPS = 0.20
EPS_C = EPS * (-0.5)
""")

        file.write("h = " + h + " + EPS\n")

        file.write("""
h1 = h*6
Dp = 12 + EPS
E = 1.2 + EPS
degre = 60

box_1 = Part.makeBox(h1, h1, 3)

# box_1 cut by box_2
box_2 = Part.makeBox(h, h, 3)
box_2_vector = FreeCAD.Vector((h1-h)/2, (h1-h)/2, 0)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

# box_1 cut by cylinder_1 in several times
for i in range(int(360/degre)):
    cylinder_1 = Part.makeCylinder(Dp/2, 3)
    radius = h1/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    cylinder_1_vector = FreeCAD.Vector(h1/2, h1/2, 0)
    cylinder_1.translate(cylinder_1_vector)
    cylinder_1_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_1.translate(cylinder_1_vector)
    box_1 = box_1.cut(cylinder_1)

Part.show(box_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Square_Pipes/' + filename + '.stl"\n')

        file.write("""Mesh.export(__objs__, stl_file)

setview()
""")

        file.close()

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(460, 750))

    time.sleep(3)

    pywinauto.mouse.click(button="left", coords=(70, 670))

    time.sleep(3)

    pywinauto.keyboard.send_keys(
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Square_Pipes\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsVMEGSquarePipesForParts(unittest.TestCase):
    # ok
    # 3D printing
    def test_part_block_square_8h(self):
        draw_block_square("8")


class UnitTestsVMEGSquarePipesForAssemblies(unittest.TestCase):
    #
    def test_assembly_without_spheres_h8(self):
        print("test_assembly_without_spheres_h8")

        if os.path.exists("assembly_without_spheres_h8.py"):
            os.remove("assembly_without_spheres_h8.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_without_spheres_h8.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_without_spheres_h8"


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

EPS = 0.20
l_pipe = 100
h_block_square = 8
h_square_pipe = 8 + EPS
h1 = h_square_pipe*6
h_magnet = 8
h_coil = l_pipe - h_block_square*2
number_of_magnets = round(h_coil/h_magnet)

# Insertion part_block_square_8h
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Square_Pipes/part_block_square_8h.stl","assembly_without_spheres_h8")
FreeCADGui.getDocument("assembly_without_spheres_h8").getObject("part_block_square_8h").ShapeColor = (0.90,0.60,0.60)
FreeCAD.getDocument("assembly_without_spheres_h8").getObject("part_block_square_8h").Placement = App.Placement(App.Vector(0,0,h_block_ring - 3),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_f_s_p_100l_8h
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/part_f_s_p_100l_8h.stl","assembly_without_spheres_h8")
FreeCADGui.getDocument("assembly_without_spheres_h8").getObject("part_f_s_p_100l_8h").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_without_spheres_h8").getObject("part_f_s_p_100l_8h").Placement = App.Placement(App.Vector(h1/2 + h_square_pipe/2,h1/2 - h_square_pipe/2,0),App.Rotation(App.Vector(0,1,0),-90))

# Insertion part_p_m_c_8l
category = 'Neodyme'
file_magnet = 'part_p_m_c_8l'

for i in range(0, number_of_magnets):
    x = h1/2 - h_magnet/2
    y = h1/2 + h_magnet/2
    z = h_block_square + h_magnet*i
    
    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/" + category + "/" + file_magnet + ".stl","assembly_without_spheres_h8")
        FreeCADGui.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    if 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/" + category + "/" + file_magnet + ".stl","assembly_without_spheres_h8")
        FreeCADGui.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet) + "00" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet) + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/" + category + "/" + file_magnet + ".stl","assembly_without_spheres_h8")
        FreeCADGui.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet) + "0" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet) + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/" + category + "/" + file_magnet + ".stl","assembly_without_spheres_h8")
        FreeCADGui.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet) + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_h8").getObject(str(file_magnet) + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_block_square_8h
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Square_Pipes/part_block_square_8h.stl","assembly_without_spheres_h8")
FreeCADGui.getDocument("assembly_without_spheres_h8").getObject("part_block_square_8h001").ShapeColor = (0.90,0.60,0.60)
FreeCAD.getDocument("assembly_without_spheres_h8").getObject("part_block_square_8h001").Placement = App.Placement(App.Vector(0,0,h_block_ring + h_magnet*number_of_magnets),App.Rotation(App.Vector(0,0,1),0))

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Square_Pipes\\\\assembly_without_spheres_h8.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
