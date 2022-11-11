import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_device"


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

assembly = "assembly_device"

# assembly_bottom_support
title = "assembly_bottom_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.00,0.90,0.00)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),0))

# assembly_top_support
title = "assembly_top_support"
stl_file = u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + title + ".stl"
Mesh.insert(stl_file,assembly)
FreeCADGui.getDocument(assembly).getObject(title).ShapeColor = (0.188,0.835,0.784)
FreeCAD.getDocument(assembly).getObject(title).Placement = App.Placement(App.Vector(0,0,64),App.Rotation(App.Vector(0,1,0),0))

setview()

# Export
__objs__ = []

title = "assembly_top_support"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

title = "assembly_bottom_support"
__objs__.append(FreeCAD.getDocument(assembly).getObject(title))

Mesh.export(__objs__,u"C:/Users/Jason/Documents/Devs/Cristal_Ball/Archives/CAO/Mercorus/Version_3/Stl/" + assembly + ".stl")

del __objs__
