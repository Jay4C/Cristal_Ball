import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_f_s_p_100l_8h" 


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
l = 100
h = 8

box_1 = Part.makeBox(l, h, h)

Part.show(box_1)

DOC.recompute()

__objs__ = []
__objs__.append(FreeCAD.getDocument("part_f_s_p_100l_8h").getObject("Shape")) 
stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/part_f_s_p_100l_8h.stl" 
Mesh.export(__objs__, stl_file)

setview()
