import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_block_square_8h" 


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
h = 8 + EPS

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
__objs__.append(FreeCAD.getDocument("part_block_square_8h").getObject("Shape")) 
stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Square_Pipes/part_block_square_8h.stl"
Mesh.export(__objs__, stl_file)

setview()
