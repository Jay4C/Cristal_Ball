import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_h_s_p_50l_16h_1_5e" 


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
l = 50
h = 16
e = 1.5

box_1 = Part.makeBox(l, h, h)

# Cut box_1 by box_2
box_2 = Part.makeBox(l, h - e*2, h - e*2)
box_2_vector = FreeCAD.Vector(0, e, e)
box_2.translate(box_2_vector)
box_1 = box_1.cut(box_2)

Part.show(box_1)

DOC.recompute()

__objs__ = []
__objs__.append(FreeCAD.getDocument("part_h_s_p_50l_16h_1_5e").getObject("Shape")) 
stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/part_h_s_p_50l_16h_1_5e.stl" 
Mesh.export(__objs__, stl_file)

setview()
