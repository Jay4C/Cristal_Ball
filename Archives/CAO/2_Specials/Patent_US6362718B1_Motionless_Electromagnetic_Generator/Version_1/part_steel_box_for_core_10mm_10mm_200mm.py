import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_steel_box_for_core_10mm_10mm_200mm"


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

# part_steel_box_for_core_10mm_10mm_200mm
h = 10
l = 10
L = 200
part_steel_box_for_core_10mm_10mm_200mm = Part.makeBox(L, h, l)

Part.show(part_steel_box_for_core_10mm_10mm_200mm)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_steel_box_for_core_10mm_10mm_200mm").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US6362718B1_Motionless_Electromagnetic_Generator/Version_1/part_steel_box_for_core_10mm_10mm_200mm.stl"

Mesh.export(__objs__, stl_file)

setview()
        