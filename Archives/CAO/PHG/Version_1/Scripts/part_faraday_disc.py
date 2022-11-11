import FreeCAD, Part, Mesh, importDXF, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_faraday_disc"


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

d1 = 60
d2 = 140 + 2*1.5 + 2*11.05 + 2*1.5
d3 = 11.05
d4 = 6.05
s = 1

cylinder_1 = Part.makeCylinder(d2/2, s)

cylinder_2 = Part.makeCylinder(d1/2, s)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the device
degre = 120
for i in range(int(360/degre)):
    radius = (140 + 2*1.5 + 2*(d3/2))/2
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(d4/2, s)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_faraday_disc").getObject("Shape"))

stl_file = u"C:/Users/Jason/Dropbox/1_Personnel/1_Recurrentes/3_Outils_Numeriques/GitHub/Cristal_Ball/Archives/CAO/PHG/Version_1/Stl/part_faraday_disc.stl"

Mesh.export(__objs__, stl_file)

dxf_file = u"C:/Users/Jason/Dropbox/1_Personnel/1_Recurrentes/3_Outils_Numeriques/GitHub/Cristal_Ball/Archives/CAO/PHG/Version_1/Stl/part_faraday_disc.dxf"

importDXF.export(__objs__, dxf_file)

setview()

del __objs__
