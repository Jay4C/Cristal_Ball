import FreeCAD, Part, math, ImportGui, importOBJ

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_bottom_support"


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

box = Part.makeBox(540, 540, 15)

# Fixing the tank
cylinder_1 = Part.makeCylinder(250, 10, FreeCAD.Vector(270, 270, 0))
cylinder_2 = Part.makeCylinder(245, 10, FreeCAD.Vector(270, 270, 0))
cylinder_3 = cylinder_1.cut(cylinder_2)
box = box.cut(cylinder_3)

# Fixing with the ground
cylinder_4 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(20, 20, 0))
cylinder_5 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(520, 20, 0))
cylinder_6 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(20, 520, 0))
cylinder_7 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(520, 520, 0))
box = box.cut(cylinder_4)
box = box.cut(cylinder_5)
box = box.cut(cylinder_6)
box = box.cut(cylinder_7)

# Fixing with the top support
cylinder_8 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(60, 60, 0))
cylinder_9 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(480, 60, 0))
cylinder_10 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(60, 480, 0))
cylinder_11 = Part.makeCylinder(3.5, 15, FreeCAD.Vector(480, 480, 0))
box = box.cut(cylinder_8)
box = box.cut(cylinder_9)
box = box.cut(cylinder_10)
box = box.cut(cylinder_11)

# Fixing the disc anode
for i in range(3):
    radius_anode = 150
    cylinder = Part.makeCylinder(3.5, 15)
    alpha=(i*2*math.pi)/3
    cylinder_vector=(270 + radius_anode*math.cos(alpha), 270 + radius_anode*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    box = box.cut(cylinder)

# Fixing the disc cathode
for i in range(3):
    radius_cathode = 200
    cylinder = Part.makeCylinder(3.5, 15)
    alpha=(i*2*math.pi)/3
    cylinder_vector=(270 + radius_cathode*math.cos(alpha), 270 + radius_cathode*math.sin(alpha), 0)
    cylinder.translate(cylinder_vector)
    box = box.cut(cylinder)

Part.show(box)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_bottom_support").getObject("Shape"))

step_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser/part_bottom_support.step"

ImportGui.export(__objs__, step_file)

obj_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser/part_bottom_support.obj"

importOBJ.export(__objs__, obj_file)

setview()

# Generate PNG files
file = 'part_bottom_support_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Stanley_Meyer/W_E_1/' + file + str(i) + '.png',1117,388,'Current')
