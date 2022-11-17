import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_block_ring_6d" 


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
d = 6 + EPS

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
__objs__.append(FreeCAD.getDocument("part_block_ring_6d").getObject("Shape")) 
stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Ring_Pipes/part_block_ring_6d.stl"
Mesh.export(__objs__, stl_file)

setview()
