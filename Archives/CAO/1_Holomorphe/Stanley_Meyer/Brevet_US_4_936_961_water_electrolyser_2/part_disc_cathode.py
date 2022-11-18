import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_cathode"

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

disc_cathode = Part.makeBox(162, 162, 5)

# cylinder_screw
cylinder_screw = Part.makeCylinder(2.5, 5)

# Cut the holes for fixing the disc on the bottom support
# hole n�1
cylinder_screw_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# hole n�2
cylinder_screw_vector = FreeCAD.Vector(151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# hole n�3
cylinder_screw_vector = FreeCAD.Vector(0, 151, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# hole n�4
cylinder_screw_vector = FreeCAD.Vector(-151, 0, 0)
cylinder_screw.translate(cylinder_screw_vector)
disc_cathode = disc_cathode.cut(cylinder_screw)

# Cut the holes for fixing the cathodes
cylinder_cathode = Part.makeCylinder(4, 3)

cylinder_cathode_vector = FreeCAD.Vector(13.5, 22, 0)
cylinder_cathode.translate(cylinder_cathode_vector)
disc_cathode = disc_cathode.cut(cylinder_cathode)

for w in range(11):
    for l in range(11):
        cylinder_cathode_vector = FreeCAD.Vector(math.pow(-1, w)*12, 0, 0)
        cylinder_cathode.translate(cylinder_cathode_vector)
        disc_cathode = disc_cathode.cut(cylinder_cathode)

    if w < 10:
        cylinder_cathode_vector = FreeCAD.Vector(0, 12, 0)
        cylinder_cathode.translate(cylinder_cathode_vector)
        disc_cathode = disc_cathode.cut(cylinder_cathode)

# Cut the holes for passing the anodes and the spacers
cylinder_anode = Part.makeCylinder(3, 5)

cylinder_anode_vector = FreeCAD.Vector(13.5, 22, 0)
cylinder_anode.translate(cylinder_anode_vector)
disc_cathode = disc_cathode.cut(cylinder_anode)

for w in range(11):
    for l in range(11):
        cylinder_anode_vector = FreeCAD.Vector(math.pow(-1, w)*12, 0, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_cathode = disc_cathode.cut(cylinder_anode)

    if w < 10:
        cylinder_anode_vector = FreeCAD.Vector(0, 12, 0)
        cylinder_anode.translate(cylinder_anode_vector)
        disc_cathode = disc_cathode.cut(cylinder_anode)

# box_evidemment_1
box_evidemment_1 = Part.makeBox(140, 15, 5)

box_evidemment_1_vector = FreeCAD.Vector(11, 0, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_cathode = disc_cathode.cut(box_evidemment_1)

box_evidemment_1_vector = FreeCAD.Vector(0, 152, 0)
box_evidemment_1.translate(box_evidemment_1_vector)
disc_cathode = disc_cathode.cut(box_evidemment_1)

# box_evidemment_2
box_evidemment_2 = Part.makeBox(5, 120, 5)

box_evidemment_2_vector = FreeCAD.Vector(0, 21, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_cathode = disc_cathode.cut(box_evidemment_2)

box_evidemment_2_vector = FreeCAD.Vector(157, 0, 0)
box_evidemment_2.translate(box_evidemment_2_vector)
disc_cathode = disc_cathode.cut(box_evidemment_2)

Part.show(disc_cathode)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_disc_cathode").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_disc_cathode.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = 'part_disc_cathode_'
# Ombr�
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_2/' + file + str(i) + '.png',1117,388,'Current')