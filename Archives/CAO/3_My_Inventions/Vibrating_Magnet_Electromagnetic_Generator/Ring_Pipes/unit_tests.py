import time
import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard


# Function for creating each block ring
def draw_block_ring(d):
    filename = "part_block_ring_" + d.replace(".", "_") + "d"

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

        file.write("d = " + d + " + EPS\n")

        file.write("""
De = d*6
D = d + 2.5
Dp = 10 + EPS
E = 1 + EPS
degre = 60

cylinder_1 = Part.makeCylinder(De/2, 3)

cylinder_2 = Part.makeCylinder(d/2, 3)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# cylinder_1 cut by cylinder_4 in several times
for i in range(int(360/degre)):
    radius = De/2 - Dp/2 - E
    alpha=(i*degre*math.pi)/180
    cylinder_4_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    cylinder_4 = Part.makeCylinder(Dp/2, 8)
    cylinder_4.translate(cylinder_4_vector)
    cylinder_1 = cylinder_1.cut(cylinder_4)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
""")

        file.write('__objs__.append(FreeCAD.getDocument("' + filename + '").getObject("Shape")) \n')

        file.write('stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Ring_Pipes/' + filename + '.stl"\n')

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
        'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Ring_Pipes\\\\' + filename + '.py"{)}.read{(}{)}{)}'
    )

    time.sleep(3)

    pywinauto.keyboard.send_keys('{ENTER}')


class UnitTestsVMEGRingPipesForParts(unittest.TestCase):
    # ok
    # 3D printing
    def test_part_block_ring_6d(self):
        draw_block_ring("6")


class UnitTestsVMEGRingPipesForAssemblies(unittest.TestCase):
    # ok
    def test_assembly_without_spheres_d6(self):
        print("test_assembly_without_spheres_d6")

        if os.path.exists("assembly_without_spheres_d6.py"):
            os.remove("assembly_without_spheres_d6.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("assembly_without_spheres_d6.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_without_spheres_d6"


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

l_vis = 100
h_block_ring = 8
h_magnet = 5
h_coil = l_vis - h_block_ring*2
number_of_magnets = round(h_coil/h_magnet)

# Insertion part_block_ring_6d
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Ring_Pipes/part_block_ring_6d.stl","assembly_without_spheres_d6")
FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d").ShapeColor = (0.90,0.60,0.60)
FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d").Placement = App.Placement(App.Vector(0,0,h_block_ring - 3),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_f_r_p_6d_100h
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/part_f_r_p_6d_100h.stl","assembly_without_spheres_d6")
FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_f_r_p_6d_100h").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_f_r_p_6d_100h").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_p_m_r_1D20_2D6_5h
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_block_ring + h_magnet*i
    
    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h").ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    if 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h00" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h0" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_block_ring_6d
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Ring_Pipes/part_block_ring_6d.stl","assembly_without_spheres_d6")
FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d001").ShapeColor = (0.90,0.60,0.60)
FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d001").Placement = App.Placement(App.Vector(0,0,h_block_ring + h_magnet*number_of_magnets),App.Rotation(App.Vector(0,0,1),0))

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques\\\\My_Tools\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\3_My_Inventions\\\\Vibrating_Magnet_Electromagnetic_Generator\\\\Ring_Pipes\\\\assembly_without_spheres_d6.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
