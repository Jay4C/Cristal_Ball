import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_v1"


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
a = 2
h_vis_10m = 6.4
h_ecrou_10m = 8
h_rondelle_10m = 2
h_magnet = 2
h_coil = l_vis - a - h_ecrou_10m - h_rondelle_10m*2 - 2 + EPS
number_of_magnets = round(h_coil/h_magnet)

h_wire = math.sqrt((1.5/math.pi))*2
number_of_torus = round((h_coil - a*2)/h_wire)

# Insertion part_vis_metal_m10_100l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_vis_metal_m10_100l.stl", "assembly_v1")
FreeCAD.getDocument("assembly_v1").getObject("part_vis_metal_m10_100l").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v1").getObject("part_vis_metal_m10_100l").ShapeColor = (0.60,0.60,0.60)

# Insertion part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_rondelle_10m.stl", "assembly_v1")
FreeCAD.getDocument("assembly_v1").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(0, 0, h_vis_10m), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v1").getObject("part_rondelle_10m").ShapeColor = (0.90,0.70,0.50)

# Insertion part_permanent_magnet_15mm_10mm_2mm_40n
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_vis_10m + h_rondelle_10m + h_magnet*i

    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_permanent_magnet_15mm_10mm_2mm_40n.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n").ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))        
    if 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_permanent_magnet_15mm_10mm_2mm_40n.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n00" + str(i)).ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_permanent_magnet_15mm_10mm_2mm_40n.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n0" + str(i)).ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_permanent_magnet_15mm_10mm_2mm_40n.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n" + str(i)).ShapeColor = (0.90,0.00,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_permanent_magnet_15mm_10mm_2mm_40n" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_o_c_di15_dw19_de40
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_o_c_di15_dw19_de40.stl", "assembly_v1")
FreeCAD.getDocument("assembly_v1").getObject("part_o_c_di15_dw19_de40").Placement = App.Placement(App.Vector(0, 0, h_vis_10m + h_rondelle_10m), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v1").getObject("part_o_c_di15_dw19_de40").ShapeColor = (0.20,0.90,0.70)
FreeCADGui.getDocument("assembly_v1").getObject("part_o_c_di15_dw19_de40").Transparency = 80

# Insertion part_torus_1v
for i in range(0, number_of_torus):
    x = 0
    y = 0
    z = h_vis_10m + h_rondelle_10m + a + h_wire/2 + h_wire*i

    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_1v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_1v").ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_1v").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))        
    if 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_1v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_1v00" + str(i)).ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_1v00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_1v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_1v0" + str(i)).ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_1v0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_1v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_1v" + str(i)).ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_1v" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_torus_2v
for i in range(0, number_of_torus):
    x = 0
    y = 0
    z = h_vis_10m + h_rondelle_10m + a + h_wire/2 + h_wire*i

    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_2v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_2v").ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_2v").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))        
    if 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_2v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_2v00" + str(i)).ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_2v00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_2v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_2v0" + str(i)).ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_2v0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_torus_2v.stl","assembly_v1")
        FreeCADGui.getDocument("assembly_v1").getObject("part_torus_2v" + str(i)).ShapeColor = (0.90,0.90,0.00)
        FreeCAD.getDocument("assembly_v1").getObject("part_torus_2v" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_rondelle_10m.stl", "assembly_v1")
FreeCAD.getDocument("assembly_v1").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(0, 0, h_vis_10m + h_rondelle_10m + h_coil), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v1").getObject("part_rondelle_10m001").ShapeColor = (0.90,0.70,0.50)

# Insertion part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Cylindric/Version_1/part_ecrou_10m.stl", "assembly_v1")
FreeCAD.getDocument("assembly_v1").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(0, 0, h_vis_10m + h_rondelle_10m + h_coil + h_rondelle_10m), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly_v1").getObject("part_ecrou_10m").ShapeColor = (0.70,0.30,0.50)

setview()

# Generate PNG files
file = 'assembly_v1_'
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
