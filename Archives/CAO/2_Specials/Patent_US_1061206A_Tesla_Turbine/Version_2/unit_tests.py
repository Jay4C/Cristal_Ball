import os
import time
import unittest
import pywinauto.mouse
import pywinauto.keyboard


# https://patents.google.com/patent/US1061206A/en?q=tesla+turbine&before=priority:19900101
class UnitTestsPatentUS1061206ATeslaTurbineVersion1(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/tiges-filetees/acier-classe-4-6/tige-filetee-acier-4-6-brut-din-975/tige-filetee-m30-acier-4-6-brut-din-975.html
    def test_part_tige_filetee_m30_1000l(self):
        print("test_part_tige_filetee_m30_1000l")

        if os.path.exists("part_tige_filetee_m30_1000l.py"):
            os.remove("part_tige_filetee_m30_1000l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_tige_filetee_m30_1000l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tige_filetee_m30_1000l"


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

# tige_filetee_m30_1000l
tige_filetee_m30_1000l = Part.makeCylinder(30/2, 1000)

Part.show(tige_filetee_m30_1000l)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tige_filetee_m30_1000l").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_tige_filetee_m30_1000l.stl"

Mesh.export(__objs__, stl_file)

setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\Python__Flask__Cristal_Ball\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Patent_US_1061206A_Tesla_Turbine\\\\Version_2\\\\part_tige_filetee_m30_1000l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-autofreines/ecrou-hexagonal-autofreine-nylstop/ecrou-nylstop-acier-zingue-blanc-din-985/ecrou-nylstop-m30-z-blanc-din-985.html
    def test_part_ecrou_30m(self):
        print("test_part_ecrou_30m")

        if os.path.exists("part_ecrou_30m.py"):
            os.remove("part_ecrou_30m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_ecrou_30m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_30m"


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

d1 = 30
e = 50.85
h = 30

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_30m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_ecrou_30m.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\Python__Flask__Cristal_Ball\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Patent_US_1061206A_Tesla_Turbine\\\\Version_2\\\\part_ecrou_30m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/rondelles-circlips/rondelles-plates/sans-chanfrein/serie-etroite-z/acier/rondelle-z-acier-zingue-blanc-nfe-25513/rondelle-z-0-30-z-blanc-nfe-25513.html
    def test_part_rondelle_30m(self):
        print("test_part_rondelle_30m")

        if os.path.exists("part_rondelle_30m.py"):
            os.remove("part_rondelle_30m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_rondelle_30m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_30m"


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

d1 = 31 
d2 = 52
s = 4

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_rondelle_30m").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_rondelle_30m.stl"

Mesh.export(__objs__, stl_file)

setview()
        """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\Python__Flask__Cristal_Ball\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials\\\\'
            'Patent_US_1061206A_Tesla_Turbine\\\\Version_2\\\\part_rondelle_30m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    # https://www.maisondufer.com/tube-rond/1923-tube-construction-rond-1397-x-4-lg-6-m-3660004774467.html
    def test_part_tube_construction_rond_140d_6000l(self):
        print("test_part_tube_construction_rond_140d_6000l")

        if os.path.exists("part_nozzle.py"):
            os.remove("part_nozzle.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_nozzle.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_nozzle"


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
EPS_C = EPS * (-0.5)

diametre_maximal_of_nozzle_front = 85

# part_nozzle
part_nozzle = Part.makeCylinder(diametre_maximal_of_nozzle_front/2, 3)

# part_nozzle cut by cylinder_1
cylinder_1 = Part.makeCylinder(diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5 - 2, 3)
part_nozzle = part_nozzle.cut(cylinder_1)

# holes for fixing the nozzle
degre = 60
for i in range(int(360/degre)):
    radius = diametre_maximal_of_nozzle_front/2 - 2.5 - 3.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    part_nozzle = part_nozzle.cut(hole)

# cone_1
cone_1_radius_1 = diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5
cone_1_radius_2 = 20/2
cone_1_height = 50
cone_1 = Part.makeCone(cone_1_radius_1, cone_1_radius_2, cone_1_height)    

# cone_2
cone_2_radius_1 = cone_1_radius_1 - 2
cone_2_radius_2 = cone_1_radius_2 - 2
cone_2_height = 50
cone_2 = Part.makeCone(cone_2_radius_1, cone_2_radius_2, cone_2_height)    

# cone_1 cut by cone_2
cone_1 = cone_1.cut(cone_2)

# part_nozzle fused with cone_1
cone_1_vector = FreeCAD.Vector(0, 0, 3)
cone_1.translate(cone_1_vector)
part_nozzle = part_nozzle.fuse(cone_1)

# cone_3
cone_3_radius_1 = 20/2
cone_3_radius_2 = diametre_maximal_of_nozzle_front/2
cone_3_height = 100
cone_3 = Part.makeCone(cone_3_radius_1, cone_3_radius_2, cone_3_height)    

# cone_4
cone_4_radius_1 = cone_3_radius_1 - 2
cone_4_radius_2 = cone_3_radius_2 - 2
cone_4_height = 100
cone_4 = Part.makeCone(cone_4_radius_1, cone_4_radius_2, cone_4_height)    

# cone_3 cut by cone_4
cone_3 = cone_3.cut(cone_4)

# part_nozzle fused with cone_3
cone_3_vector = FreeCAD.Vector(0, 0, 3 + cone_1_height)
cone_3.translate(cone_3_vector)
part_nozzle = part_nozzle.fuse(cone_3)

Part.show(part_nozzle)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_nozzle").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_nozzle.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\Python__Flask__Cristal_Ball\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials\\\\'
            'Patent_US_1061206A_Tesla_Turbine\\\\Version_2\\\\part_nozzle.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
    def test_part_blade(self):
        print("test_part_blade")

        if os.path.exists("part_blade.py"):
            os.remove("part_blade.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("part_blade.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh, 

    DOC = FreeCAD.activeDocument()

    DOC_NAME = "part_nozzle"


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
    EPS_C = EPS * (-0.5)

    diametre_maximal_of_nozzle_front = 85

    # part_nozzle
    part_nozzle = Part.makeCylinder(diametre_maximal_of_nozzle_front/2, 3)

    # part_nozzle cut by cylinder_1
    cylinder_1 = Part.makeCylinder(diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5 - 2, 3)
    part_nozzle = part_nozzle.cut(cylinder_1)

    # holes for fixing the nozzle
    degre = 60
    for i in range(int(360/degre)):
        radius = diametre_maximal_of_nozzle_front/2 - 2.5 - 3.5
        alpha=(i*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(2.5, 3)
        hole.translate(hole_vector)
        part_nozzle = part_nozzle.cut(hole)

    # cone_1
    cone_1_radius_1 = diametre_maximal_of_nozzle_front/2 - 3.5 - 5 - 4.5
    cone_1_radius_2 = 20/2
    cone_1_height = 50
    cone_1 = Part.makeCone(cone_1_radius_1, cone_1_radius_2, cone_1_height)    

    # cone_2
    cone_2_radius_1 = cone_1_radius_1 - 2
    cone_2_radius_2 = cone_1_radius_2 - 2
    cone_2_height = 50
    cone_2 = Part.makeCone(cone_2_radius_1, cone_2_radius_2, cone_2_height)    

    # cone_1 cut by cone_2
    cone_1 = cone_1.cut(cone_2)

    # part_nozzle fused with cone_1
    cone_1_vector = FreeCAD.Vector(0, 0, 3)
    cone_1.translate(cone_1_vector)
    part_nozzle = part_nozzle.fuse(cone_1)

    # cone_3
    cone_3_radius_1 = 20/2
    cone_3_radius_2 = diametre_maximal_of_nozzle_front/2
    cone_3_height = 100
    cone_3 = Part.makeCone(cone_3_radius_1, cone_3_radius_2, cone_3_height)    

    # cone_4
    cone_4_radius_1 = cone_3_radius_1 - 2
    cone_4_radius_2 = cone_3_radius_2 - 2
    cone_4_height = 100
    cone_4 = Part.makeCone(cone_4_radius_1, cone_4_radius_2, cone_4_height)    

    # cone_3 cut by cone_4
    cone_3 = cone_3.cut(cone_4)

    # part_nozzle fused with cone_3
    cone_3_vector = FreeCAD.Vector(0, 0, 3 + cone_1_height)
    cone_3.translate(cone_3_vector)
    part_nozzle = part_nozzle.fuse(cone_3)

    Part.show(part_nozzle)

    DOC.recompute()

    __objs__ = []

    __objs__.append(FreeCAD.getDocument("part_nozzle").getObject("Shape"))

    stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_nozzle.stl"

    Mesh.export(__objs__, stl_file)

    setview()
    """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\Python__Flask__Cristal_Ball\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials\\\\'
            'Patent_US_1061206A_Tesla_Turbine\\\\Version_2\\\\part_nozzle.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    #
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

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * (-0.5)

# insertion part_gas_entry
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_gas_entry.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_gas_entry").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_gas_entry").ShapeColor = (0.50,0.40,0.30)

# insertion part_nozzle
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_nozzle.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_nozzle").Placement = App.Placement(App.Vector(0, 0, 3), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_nozzle").ShapeColor = (0.10,0.20,0.30)
FreeCADGui.getDocument("assembly").getObject("part_nozzle").Transparency = 70

# insertion part_element_64
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_element_64.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_64").Placement = App.Placement(App.Vector(0, 0, 3), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_64").ShapeColor = (0.90,0.80,0.70)

# insertion part_element_32
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/part_element_32.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_element_32").Placement = App.Placement(App.Vector(0, 0, -11), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_element_32").ShapeColor = (0.70,0.80,0.90)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_gas_entry"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_nozzle"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_64"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_element_32"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_1061206A_Tesla_Turbine/Version_2/assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__
            """)

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(460, 750))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(70, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"A:\\\\1_Professionnel\\\\1_Holomorphe\\\\2_Archives\\\\2_Outils_Numeriques'
            '\\\\Python__Flask__Cristal_Ball\\\\Test\\\\Service\\\\Archives\\\\CAO\\\\2_Specials'
            '\\\\Patent_US_1061206A_Tesla_Turbine\\\\Version_2\\\\assembly.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
