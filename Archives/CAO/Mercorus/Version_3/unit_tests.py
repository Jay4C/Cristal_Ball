import unittest
import os
import pywinauto.mouse
import pywinauto.keyboard
import time


# Transmute mercury into gold
# https://patents.google.com/patent/FR599762A/en?oq=FR_599762_A
class UnitsTestsMercorusVersion3Parts(unittest.TestCase):
    # ok
    # https://www.visseriefixations.fr/ecrous/ecrous-hexagonaux/ecrou-hexagonal-hu/ecrou-hu-acier-brut-din-934/ecrou-hu-acier-brut-classe-8-din-934/ecrou-hu-m6-brut-din-934.html
    def test_part_ecrou_6m(self):
        print("test_part_ecrou_6m")

        if os.path.exists("Scripts\\part_ecrou_6m.py"):
            os.remove("Scripts\\part_ecrou_6m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_ecrou_6m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou_6m"


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

d1 = 6
e = 11.05
h = 5

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(d1/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou_6m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_ecrou_6m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_ecrou_6m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m6x70-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m6_70l(self):
        print("test_part_vis_metal_m6_70l")

        if os.path.exists("Scripts\\part_vis_metal_m6_70l.py"):
            os.remove("Scripts\\part_vis_metal_m6_70l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m6_70l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m6_70l"


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

L = 70
k = 4
d1 = 6
e = 11.05

cylinder_1 = Part.makeCylinder(e/2, L+k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]
__objs__.append(FreeCAD.getDocument("part_vis_metal_m6_70l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_vis_metal_m6_70l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_vis_metal_m6_70l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.visseriefixations.fr/vis-a-tete-hexagonale/vis-a-tete-hexagonale-standard/acier-8-8-noir/th-acier-8-8-noir-filetage-total-din-933/th-m6x30-acier-8-8-noir-ef-din-933.html
    def test_part_vis_metal_m6_30l(self):
        print("test_part_vis_metal_m6_30l")

        if os.path.exists("Scripts\\part_vis_metal_m6_30l.py"):
            os.remove("Scripts\\part_vis_metal_m6_30l.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_vis_metal_m6_30l.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_vis_metal_m6_30l"


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

L = 30
k = 4
d1 = 6
e = 11.05

cylinder_1 = Part.makeCylinder(e/2, L+k)

cylinder_2 = Part.makeCylinder(d1/2, L)

cylinder_3 = Part.makeCylinder(e/2, L)

# cylinder_3 cut by cylinder_2
cylinder_3 = cylinder_3.cut(cylinder_2)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, k)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]
__objs__.append(FreeCAD.getDocument("part_vis_metal_m6_30l").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_vis_metal_m6_30l.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_vis_metal_m6_30l.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.inoxalu.fr/Article/415-Tube-rond-54-x-2
    # I=E-2/E=54/L=100
    def test_part_tube_inox(self):
        print("test_part_tube_inox")

        if os.path.exists("Scripts\\part_tube_inox.py"):
            os.remove("Scripts\\part_tube_inox.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_tube_inox.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tube_inox"


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

e = 54
i = e - 2*2
h = 100

cylinder_1 = Part.makeCylinder(e/2, h)

cylinder_2 = Part.makeCylinder(i/2, h)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_tube_inox").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_tube_inox.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_tube_inox.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/
    def test_part_top_support(self):
        print("test_part_top_support")

        if os.path.exists("Scripts\\part_top_support.py"):
            os.remove("Scripts\\part_top_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_top_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_top_support"


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

d1 = 50
d2 = 6.1
e1 = d1 + 2*2 + 2*2 + 2*2 + 2*11.05 + 2*2
e2 = d1 + 2*2
e3 = e1
e4 = e2 + 2*2
e5 = d1 + 2*2 + 2*2 + 2*2 + 2*(11.05/2)
e6 = d1 - 2*2 - 2*(11.05/2)
e7 = 16.1
h1 = 20
h2 = h1 - 2

# Cylinder_1
cylinder_1 = Part.makeCylinder(e1/2, h1)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(e2/2, h2)
cylinder_1 = cylinder_1.cut(cylinder_2)

# Cylinder_3
cylinder_3 = Part.makeCylinder(e3/2, h2)

# Cut cylinder_3 by cylinder_4
cylinder_4 = Part.makeCylinder(e4/2, h2)
cylinder_3 = cylinder_3.cut(cylinder_4)

# Cut cylinder_1 by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the device
degre = 15
for i in range(int(360/degre)):
    radius = e5/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d2/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the electrodes
degre = 60
for i in range(int(360/degre)):
    radius = e6/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d2/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cut cylinder_1 by cylinder_5
cylinder_5 = Part.makeCylinder(e7/2, h1)
cylinder_1 = cylinder_1.cut(cylinder_5)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_top_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_top_support.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_top_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-mamelons-a-visser-laiton-m-12-x-17-pour-tube-en-cuivre-65814231.html
    def test_part_mamelon_a_visser_12_17_m(self):
        print("test_part_mamelon_a_visser_12_17_m")

        if os.path.exists("Scripts\\part_mamelon_a_visser_12_17_m.py"):
            os.remove("Scripts\\part_mamelon_a_visser_12_17_m.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_mamelon_a_visser_12_17_m.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_mamelon_a_visser_12_17_m"

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

diametre_maximal = 19

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 19)

cylinder_2 = Part.makeCylinder(11/2, 19)

cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 8)

cylinder_4 = Part.makeCylinder(16/2, 8)

cylinder_3 = cylinder_3.cut(cylinder_4)

cylinder_1 = cylinder_1.cut(cylinder_3)

cylinder_3_vector = FreeCAD.Vector(0, 0, 11)

cylinder_3.translate(cylinder_3_vector)

cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_mamelon_a_visser_12_17_m").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_mamelon_a_visser_12_17_m.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_mamelon_a_visser_12_17_m.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.leroymerlin.fr/produits/chauffage-plomberie/circuit-alimentation-en-eau/tube-et-raccord-alimentation/raccord-alimentation/lot-de-2-manchons-a-visser-laiton-f-12-x-17-pour-tube-en-cuivre-65815253.html
    def test_part_manchon_a_visser_12_17_f(self):
        print("part_manchon_a_visser_12_17_f")

        if os.path.exists("Scripts\\part_manchon_a_visser_12_17_f.py"):
            os.remove("Scripts\\part_manchon_a_visser_12_17_f.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_manchon_a_visser_12_17_f.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_manchon_a_visser_12_17_f"

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

diametre_maximal = 22

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 18)

cylinder_2 = Part.makeCylinder(16.4/2, 18)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_manchon_a_visser_12_17_f").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_manchon_a_visser_12_17_f.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_manchon_a_visser_12_17_f.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    # https://www.sculpteo.com/fr/
    def test_part_bottom_support(self):
        print("test_part_bottom_support")

        if os.path.exists("Scripts\\part_bottom_support.py"):
            os.remove("Scripts\\part_bottom_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\part_bottom_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support"


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

d1 = 50
d2 = 6.1
e1 = d1 + 2*2 + 2*2 + 2*2 + 2*11.05 + 2*2
e2 = d1 + 2*2
e3 = e1
e4 = e2 + 2*2
e5 = d1 + 2*2 + 2*2 + 2*2 + 2*(11.05/2)
e6 = d1 - 2*2 - 2*(11.05/2)
e7 = 16.1
e8 = e7 + 2*3
h1 = 20
h2 = h1 - 2
h3 = 11

# Cylinder_1
cylinder_1 = Part.makeCylinder(e1/2, h1)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(e2/2, h2)
cylinder_1 = cylinder_1.cut(cylinder_2)

# Cylinder_3
cylinder_3 = Part.makeCylinder(e3/2, h2)

# Cut cylinder_3 by cylinder_4
cylinder_4 = Part.makeCylinder(e4/2, h2)
cylinder_3 = cylinder_3.cut(cylinder_4)

# Cut cylinder_1 by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 2)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the device
degre = 15
for i in range(int(360/degre)):
    radius = e5/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d2/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the electrodes
degre = 60
for i in range(int(360/degre)):
    radius = e6/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d2/2, h1)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cut cylinder_1 by cylinder_5
cylinder_5 = Part.makeCylinder(e7/2, h1)
cylinder_1 = cylinder_1.cut(cylinder_5)

cylinder_6 = Part.makeCylinder(e8/2, h3)

# Cut cylinder_6 by cylinder_7
cylinder_7 = Part.makeCylinder(e7/2, h3)
cylinder_6 = cylinder_6.cut(cylinder_7)

cylinder_6_vector = FreeCAD.Vector(0, 0, h1)

cylinder_6.translate(cylinder_6_vector)

cylinder_1 = cylinder_1.fuse(cylinder_6)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_bottom_support").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/part_bottom_support.stl"

Mesh.export(__objs__, stl_file)

setview()
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\part_bottom_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


class UnitsTestsMercorusVersion3Assemblies(unittest.TestCase):
    # ok
    def test_assembly_bottom_support(self):
        print("test_assembly_bottom_support")

        if os.path.exists("Scripts\\assembly_bottom_support.py"):
            os.remove("Scripts\\assembly_bottom_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_bottom_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_bottom_support"


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

assembly = "assembly_bottom_support"

# part_bottom_support
title = "part_bottom_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.00,0.90,0.00)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),180))

# part_tube_inox
title = "part_tube_inox"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.60,0.80,0.90)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,-18),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_6m
color = (0.90,0.00,0.90)
i1 = 8
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(0, i1):
    degre = 45
    d1 = 50
    e1 = d1 + 2*2 + 2*2 + 2*2 + 2*(11.05/2)
    radius = e1/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 0

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

# part_vis_metal_m6_70l
color = (0.90,0.50,0.40)
i2 = 8
title = 'part_vis_metal_m6_70l'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(0, i2):
    degre = 45
    d1 = 50
    e1 = d1 + 2*2 + 2*2 + 2*2 + 2*(11.05/2)
    radius = e1/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - 4 - 2

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

# part_ecrou_6m
color = (0.90,0.00,0.90)
i3 = 6
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(i1, i1 + i3):
    degre = 60
    d1 = 50
    e6 = d1 - 2*2 - 2*(11.05/2)
    radius = e6/2
    alpha=((i-i1)*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = - 20 - 5

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

# part_vis_metal_m6_30l
color = (0.90,0.50,0.40)
i4 = 6
title = 'part_vis_metal_m6_30l'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(0, i4):
    degre = 60
    d1 = 50
    e6 = d1 - 2*2 - 2*(11.05/2)
    radius = e6/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    k = 4
    z = - 20 + 2 + k
    rotation = App.Rotation(App.Vector(0,1,0),180)

    if i == 0:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(x,y,z),rotation)
    elif i >= 1 and i < 10:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "00" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),rotation)
    elif i >= 10 and i < 100:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + "0" + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),rotation)
    elif i >= 100 and i < 1000:
        Mesh.insert(stl_file,assembly)
        FreeCADGui.getDocument(assembly).getObject(title + str(i)).ShapeColor = color
        FreeCAD.getDocument(assembly).getObject(title + str(i)).Placement = App.Placement(App.Vector(x,y,z),rotation)

# part_ecrou_6m
color = (0.90,0.00,0.90)
i5 = 8
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(i1 + i3, i1 + i3 + i5):
    degre = 45
    d1 = 50
    e1 = d1 + 2*2 + 2*2 + 2*2 + 2*(11.05/2)
    radius = e1/2
    alpha=((i - (i1 + i3))*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 20

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

# part_mamelon_a_visser_12_17_m
title = "part_mamelon_a_visser_12_17_m"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.188,0.835,0.784)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,- 18 - 11 - 13),App.Rotation(App.Vector(0,1,0),0))

setview()

# Export
__objs__=[]
title = "part_bottom_support"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_tube_inox"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_ecrou_6m"
for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m6_70l"
for i in range(0, i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_6m"
for i in range(i1, i1 + i3):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m6_30l"
for i in range(0, i4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_6m"
for i in range(i1 + i3, i1 + i3 + i5):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_mamelon_a_visser_12_17_m"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\assembly_bottom_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_top_support(self):
        print("test_assembly_top_support")

        if os.path.exists("Scripts\\assembly_top_support.py"):
            os.remove("Scripts\\assembly_top_support.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_top_support.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_top_support"


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

assembly = "assembly_top_support"

# part_top_support
title = "part_top_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.00,0.90,0.00)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),0))

# part_mamelon_a_visser_12_17_m
title = "part_mamelon_a_visser_12_17_m"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.188,0.835,0.784)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,11),App.Rotation(App.Vector(0,1,0),0))

# part_manchon_a_visser_12_17_f
title = "part_manchon_a_visser_12_17_f"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.20,0.30,0.40)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),0))

# part_ecrou_6m
color = (0.90,0.00,0.90)
i1 = 8
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(0, i1):
    degre = 45
    d1 = 50
    e1 = d1 + 2*2 + 2*2 + 2*2 + 2*(11.05/2)
    radius = e1/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 2

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

# part_ecrou_6m
color = (0.90,0.00,0.90)
i2 = 6
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(i1, i1 + i2):
    degre = 60
    d1 = 50
    e6 = d1 - 2*2 - 2*(11.05/2)
    radius = e6/2
    alpha=((i-i1)*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 20

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

# part_ecrou_6m
color = (0.90,0.00,0.90)
i3 = 6
title = 'part_ecrou_6m'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(i1 + i2, i1 + i2 + i3):
    degre = 60
    d1 = 50
    e6 = d1 - 2*2 - 2*(11.05/2)
    radius = e6/2
    alpha=((i-i1)*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = 20 - 2 - 5

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

# part_vis_metal_m6_70l
color = (0.90,0.50,0.40)
i4 = 6
title = 'part_vis_metal_m6_70l'
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
for i in range(0, i4):
    degre = 60
    d1 = 50
    e6 = d1 - 2*2 - 2*(11.05/2)
    radius = e6/2
    alpha=(i*degre*math.pi)/180
    x = radius*math.cos(alpha)
    y = radius*math.sin(alpha)
    z = -20

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

setview()

# Export
__objs__ = []

title = "part_top_support"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_mamelon_a_visser_12_17_m"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_manchon_a_visser_12_17_f"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "part_ecrou_6m"
for i in range(0, i1):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_6m"
for i in range(i1, i1 + i2):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_ecrou_6m"
for i in range(i1 + i2, i1 + i2 + i3):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

title = "part_vis_metal_m6_70l"
for i in range(0, i4):
    if i == 0:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + "0" + str(i)))
    elif i >= 100 and i < 1000:
        __objs__.append(FreeCAD.getDocument(assembly).getObject(title + str(i)))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\assembly_top_support.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

    # ok
    def test_assembly_device(self):
        print("test_assembly_device")

        if os.path.exists("Scripts\\assembly_device.py"):
            os.remove("Scripts\\assembly_device.py")
        else:
            print("The file does not exist")

        # Writing to file
        with open("Scripts\\assembly_device.py", "w") as file:
            # Writing data to a file
            file.write("""import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_device"


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

assembly = "assembly_device"

# assembly_bottom_support
title = "assembly_bottom_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.00,0.90,0.00)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),0))

# assembly_top_support
title = "assembly_top_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.188,0.835,0.784)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,64),App.Rotation(App.Vector(0,1,0),0))

setview()

# Export
__objs__ = []

title = "assembly_top_support"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "assembly_bottom_support"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + assembly + ".stl")

del __objs__
""")

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(670 * 1.5), round(695 * 1.5)))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(round(60 * 1.5), round(615 * 1.5)))

        time.sleep(3)

        pywinauto.keyboard.send_keys(
            'exec{(}open{(}"C:\\\\Users\\\\Jason\\\\Documents\\\\Devs\\\\Cristal_Ball\\\\Archives\\\\CAO\\\\Mercorus\\\\Version_3\\\\Scripts\\\\assembly_device.py"{)}.read{(}{)}{)}'
        )

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')


if __name__ == '__main__':
    unittest.main()
