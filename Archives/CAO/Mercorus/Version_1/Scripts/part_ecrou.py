import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_ecrou"


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

# ecrou
ecrou = Part.makeCylinder(4.5, 4)

# cylinder_1
cylinder_1 = Part.makeCylinder(2.5, 5)

# ecrou cut by cylinder_1
ecrou = ecrou.cut(cylinder_1)

Part.show(ecrou)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_ecrou").getObject("Shape"))

stl_file = u"C:/Users/Jason/Dropbox/1_Personnel/1_Recurrentes/3_Outils_Numeriques/GitHub/Cristal_Ball/Archives/CAO/Mercorus/Version_1/Stl/part_ecrou.stl"

Mesh.export(__objs__, stl_file)

setview()

del __objs__
