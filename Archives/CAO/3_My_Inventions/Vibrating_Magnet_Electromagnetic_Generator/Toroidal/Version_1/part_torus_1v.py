import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_torus_1v"


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
EPS = 0.3
EPS_C = EPS * -0.5

Dc = math.sqrt((1.5/math.pi))*2
Di = 10 + 2*Dc

torus = Part.makeTorus(Di/2, Dc/2)

Part.show(torus)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_torus_1v").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_torus_1v.stl"

Mesh.export(__objs__, stl_file)

setview()
