import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_rondelle_inox_6_4d_12D_1_2s" 


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
d = 6.4
D = 12
s = 1.2


cylinder_1 = Part.makeCylinder(D/2, s)

cylinder_2 = Part.makeCylinder(d/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

Part.show(cylinder_1)

DOC.recompute()

__objs__ = []
__objs__.append(FreeCAD.getDocument("part_rondelle_inox_6_4d_12D_1_2s").getObject("Shape")) 
stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/part_rondelle_inox_6_4d_12D_1_2s.stl" 
Mesh.export(__objs__, stl_file)

setview()
