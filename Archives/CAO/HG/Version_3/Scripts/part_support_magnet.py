import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_support_magnet"


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

d_magnet = 140

d_exterieur = d_magnet + 2*2
d_interieur = d_magnet
d_arbre = 30.1
h_support_global = 5
h_support_magnet = 3

# Cylinder_1
cylinder_1 = Part.makeCylinder(d_exterieur/2, h_support_global)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(d_arbre/2, h_support_global)
cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for emptying the part
degre = 72
for i in range(int(360/degre)):
    radius = d_interieur/2 - 3 - (d_arbre + 10)/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder((d_arbre + 10)/2, h_support_global)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# Cylinder_3
cylinder_3 = Part.makeCylinder(d_interieur/2, h_support_magnet)
cylinder_3_vector = FreeCAD.Vector(0, 0, h_support_global - h_support_magnet)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_support_magnet").getObject("Shape"))

stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/HG/Version_3/Stl/part_support_magnet.stl"

Mesh.export(__objs__, stl_file)

setview()
