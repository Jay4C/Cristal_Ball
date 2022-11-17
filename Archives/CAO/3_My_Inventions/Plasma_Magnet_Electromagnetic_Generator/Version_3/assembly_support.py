import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support"


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

__objs__ = []

# ok
# Insertion the part_support
folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_3/"
file = "part_support"
filename = folder + file + ".stl"

color = (0.9, 0.8, 0.7)

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
# Insertion the part_support

# ok
# Insertion the part_vis_metal_22d_35_72e_60l_14k
color = (0.50,0.50,0.50)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_vis_metal_22d_35_72e_60l_14k"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,2 + 9 + 3*2 + 14),App.Rotation(App.Vector(0,1,0),180))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
# Insertion the part_vis_metal_22d_35_72e_60l_14k

# ok
# Insertion the part_ecrou_metal_22d_36e_18m
color = (0.50,0.20,0.10)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_ecrou_metal_22d_36e_18m"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,- 18),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(1)).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)).Placement = App.Placement(App.Vector(0,0,- 18*2),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)))
# Insertion the part_ecrou_metal_22d_36e_18m

# ok
# Insertion the part_p_m_r_1D45_2D22_9h
color = (0.60,0.40,0.20)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Permanent_Magnets/Ferrite/"
file = "part_p_m_r_1D45_2D22_9h"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0,2 + 9),App.Rotation(App.Vector(0,1,0),180))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))
# Insertion the part_p_m_r_1D45_2D22_9h

# ok
# Insertion the part_rondelle_metal_23d_40D_3s
color = (0.50,0.50,0.00)

folder = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Fixations/"
file = "part_rondelle_metal_23d_40D_3s"
filename = folder + file + ".stl"

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file).Placement = App.Placement(App.Vector(0,0, 2 + 9),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file))

Mesh.insert(filename, DOC_NAME)
FreeCADGui.getDocument(DOC_NAME).getObject(file + "00" + str(1)).ShapeColor = color
FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)).Placement = App.Placement(App.Vector(0,0,2 + 9 + 3),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject(file + "00" + str(1)))
# Insertion the part_rondelle_metal_23d_40D_3s

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Plasma_Magnet_Electromagnetic_Generator/Version_3/assembly_support.stl"

Mesh.export(__objs__, stl_file)

setview()

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/PMEG/3/' + file + str(i) + '.png',1117,388,'Current')
