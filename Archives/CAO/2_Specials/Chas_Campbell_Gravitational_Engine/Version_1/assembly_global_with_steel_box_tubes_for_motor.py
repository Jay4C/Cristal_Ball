import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_with_steel_box_tubes_for_motor"


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

h_tube = 50
L_support_horizontal_motor = 367
E_support_horizontal_motor = 50
s_rondelle_10m = 2

# Export assembly_global_with_steel_box_tubes_for_motor
__objs__ = []

# assembly_socle_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle_with_steel_box_tubes_for_motor.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_socle_with_steel_box_tubes_for_motor").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_socle_with_steel_box_tubes_for_motor").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_socle_with_steel_box_tubes_for_motor"))

# assembly_moteur_electrique
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_moteur_electrique.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_moteur_electrique").ShapeColor = (0.30,0.20,0.10)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_moteur_electrique").Placement = App.Placement(App.Vector(L_support_horizontal_motor - E_support_horizontal_motor,0,h_tube),App.Rotation(App.Vector(0,0,1),90))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("assembly_moteur_electrique"))

# motor
A = 140
AB = 175
B = 125
C = 56
E = 50
L = 367
K = 10
y1 = (AB - A)/2
x1 = L - B - C - E

h_ecrou_10m = 10
k_vis_10m = 6.4

# part_rondelle_10m

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(x1 + B,y1,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(x1,y1 + A,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(x1 + B,y1 + A,-s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003"))

# part_ecrou_10m

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(x1 + B,y1,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(x1,y1 + A,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(x1 + B,y1 + A,-s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m003"))

# part_vis_metal_m10_120l

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector(x1,y1,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector(x1 + B,y1,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(x1,y1 + A,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_global_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(x1 + B,y1 + A,h_tube + 20 + s_rondelle_10m + k_vis_10m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_motor.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_with_steel_box_tubes_for_motor_v1_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/2_Specials/Chas_Campbell/' + file + str(i) + '.png',1117,388,'Current')
