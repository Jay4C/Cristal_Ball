import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "container"


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

# container
container = Part.makeBox(2.4*1000, 2.6*1000, 6*1000)

# inner_container
inner_container = Part.makeBox(2.3*1000, 2.4*1000, 5.9*1000)

# container cut by inner_container
inner_container_vector = FreeCAD.Vector((2.4*1000 - 2.3*1000)/2, (2.6*1000 - 2.4*1000)/2, 0)
inner_container.translate(inner_container_vector)
container = container.cut(inner_container)

Part.show(container)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("container").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Hydrogen_Installation/container.stl"

Mesh.export(__objs__, stl_file)

setview()
        