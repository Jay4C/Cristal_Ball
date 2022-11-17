import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_v2"


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
EPS = 0.30
EPS_C = EPS * (-0.5)

l_vis = 100
h_support = 1.2 + EPS
h_vis_10m = 6.4
h_ecrou_10m = 8
h_rondelle_10m = 2
h_magnet = 10
h_coil = l_vis - h_support*2 - h_ecrou_10m - 3 + EPS

number_of_magnets = round(h_coil/h_magnet)

# Insertion part_vis_metal_m10_100l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_vis_metal_m10_100l.stl", "assembly_v2")
FreeCAD.getDocument("assembly_v2").getObject("part_vis_metal_m10_100l").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v2").getObject("part_vis_metal_m10_100l").ShapeColor = (0.60,0.60,0.60)

# Insertion part_support_2v
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_support_2v.stl", "assembly_v2")
FreeCAD.getDocument("assembly_v2").getObject("part_support_2v").Placement = App.Placement(App.Vector(0, 0, h_vis_10m), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v2").getObject("part_support_2v").ShapeColor = (0.20,0.90,0.70)

# Insertion part_permanent_magnet_40mm_20mm_10mm_35y
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_vis_10m + h_support + h_magnet*i

    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_permanent_magnet_40mm_20mm_10mm_35y.stl","assembly_v2")
        FreeCADGui.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y").ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))        
    if 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_permanent_magnet_40mm_20mm_10mm_35y.stl","assembly_v2")
        FreeCADGui.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y00" + str(i)).ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_permanent_magnet_40mm_20mm_10mm_35y.stl","assembly_v2")
        FreeCADGui.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y0" + str(i)).ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_permanent_magnet_40mm_20mm_10mm_35y.stl","assembly_v2")
        FreeCADGui.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y" + str(i)).ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v2").getObject("part_permanent_magnet_40mm_20mm_10mm_35y" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_support_2v
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_support_2v.stl", "assembly_v2")
FreeCAD.getDocument("assembly_v2").getObject("part_support_2v001").Placement = App.Placement(App.Vector(0, 0, h_vis_10m + h_magnet*number_of_magnets + h_support), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v2").getObject("part_support_2v001").ShapeColor = (0.20,0.90,0.70)

# Insertion part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Toroidal/Version_1/part_ecrou_10m.stl", "assembly_v2")
FreeCAD.getDocument("assembly_v2").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(0, 0, h_vis_10m + h_magnet*number_of_magnets + h_support*2), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v2").getObject("part_ecrou_10m").ShapeColor = (0.70,0.30,0.50)

setview()

# Generate PNG files
file = 'assembly_v2_t_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/3_My_Inventions/VMEG/' + file + str(i) + '.png',1117,388,'Current')
