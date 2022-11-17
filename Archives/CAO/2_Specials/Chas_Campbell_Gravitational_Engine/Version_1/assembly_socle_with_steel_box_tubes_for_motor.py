import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_socle_with_steel_box_tubes_for_motor"


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

L_support_vertical_motor = 50*2 + 50*3
h_tube = 50
L_support_horizontal_motor = 367
E_support_horizontal_motor = 50
L_support_link_motor = 175
k_vis_10m = 6.4
L_roulette_pivotante = 99
h_ecrou_10m = 10

# Export assembly_socle_with_steel_box_tubes_for_motor
__objs__ = []

# assembly_half_socle_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor"))

# part_steel_box_tube_for_support_link_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor").ShapeColor = (0.70,0.50,0.20)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor").Placement = App.Placement(App.Vector(h_tube,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor"))

# part_steel_box_tube_for_support_link_motor_2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor_2.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor_2").ShapeColor = (0.70,0.30,0.10)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor_2").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2 - h_tube/2,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor_2"))

# part_steel_box_tube_for_support_link_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor001").ShapeColor = (0.70,0.50,0.20)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - 2*h_tube,0,-L_support_vertical_motor),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_steel_box_tube_for_support_link_motor001"))

# assembly_half_socle_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_motor.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor),L_support_link_motor,0),App.Rotation(App.Vector(0,0,1),180))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_half_socle_with_steel_box_tubes_for_motor001"))

# part_rondelle_10m

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m003"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m004"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m005"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m006"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,h_tube/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m007"))

# part_rondelle_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,L_support_link_motor - h_tube/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m008"))

# part_rondelle_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m009"))

# part_rondelle_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m010"))

# part_rondelle_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m011"))

# part_rondelle_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) -(3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m012"))

# part_rondelle_10m - 14
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_rondelle_10m013"))

# part_ecrou_10m

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").ShapeColor = (0.33,0.22,0.11)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").ShapeColor = (0.33,0.22,0.11)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-(L_support_vertical_motor - 2*h_tube) - h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_ecrou_10m001"))

# part_vis_metal_m10_120l

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l003"))

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor - (8*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor - (2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.11,0.22,0.33)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,(2*h_tube)/10,-L_support_vertical_motor - s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("part_vis_metal_m10_120l007"))

# assembly_roulette_pivotante

# assembly_roulette_pivotante - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante").Placement = App.Placement(App.Vector((3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante"))

# assembly_roulette_pivotante - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante001").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor) - (3*h_tube)/2,L_support_link_motor/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante001"))

# assembly_roulette_pivotante_2v - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante_2v.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,h_tube/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v"))

# assembly_roulette_pivotante_2v - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante_2v.stl","assembly_socle_with_steel_box_tubes_for_motor")
FreeCADGui.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v001").ShapeColor = (0.22,0.66,0.99)
FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v001").Placement = App.Placement(App.Vector((L_support_horizontal_motor - E_support_horizontal_motor)/2,L_support_link_motor - h_tube/2,-L_support_vertical_motor - s_rondelle_10m - L_roulette_pivotante - s_rondelle_10m - h_ecrou_10m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_socle_with_steel_box_tubes_for_motor").getObject("assembly_roulette_pivotante_2v001"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle_with_steel_box_tubes_for_motor.stl")

del __objs__

# Generate PNG files
file = 'assembly_socle_with_steel_box_tubes_for_motor_v1_'
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
