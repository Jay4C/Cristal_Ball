import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_f_r_p_5d_80h" 


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
r = 2.5
h = 80

cylinder = Part.makeCylinder(r, h)

Part.show(cylinder)

DOC.recompute()

__objs__ = []
__objs__.append(FreeCAD.getDocument("part_f_r_p_5d_80h").getObject("Shape")) 
stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/part_f_r_p_5d_80h.stl" 
Mesh.export(__objs__, stl_file)

setview()
