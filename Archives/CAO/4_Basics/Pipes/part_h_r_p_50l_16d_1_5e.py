import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_h_r_p_50l_16d_1_5e" 


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
r = 8.0
e = 1.5

cylinder_1 = Part.makeCylinder(r, l)

# Cut cylinder_1 by cylinder_2
cylinder_2 = Part.makeCylinder(r - e, l)
cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
__objs__.append(FreeCAD.getDocument("part_h_r_p_50l_16d_1_5e").getObject("Shape")) 
stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/part_h_r_p_50l_16d_1_5e.stl" 
Mesh.export(__objs__, stl_file)

setview()
