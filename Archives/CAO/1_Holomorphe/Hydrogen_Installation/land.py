import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "land"


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

land = Part.makeBox(100*1000, 100*1000, 500)

Part.show(land)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("land").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Hydrogen_Installation/land.stl"

Mesh.export(__objs__, stl_file)

setview()
        