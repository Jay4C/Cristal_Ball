import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_half_socle_with_steel_box_tubes"


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

L_flywheel = 1000
number_of_weights = 1
h_ecrou_10m = 10
s_rondelle_10m = 2
s_rondelle_12m = 2.5

h_tube = 50
L_ground = 500
L_elevator = math.sqrt(math.pow(L_flywheel/2,2) + math.pow(h_tube/2 + number_of_weights*(h_tube/2) + h_ecrou_10m + s_rondelle_10m + h_tube,2))+ 50*3

# part_palier
L1 = 127
J = 95
e1 = 20
z_palier = 65

# part_steel_box_tube_for_support_palier_flywheel
Lspf = 50*2 + 20*2 + L1
Ltspf = (L_ground - Lspf)/2 + h_tube/2

k_vis_10m = 6.4

L_roulette_pivotante = 99

# Export assembly_half_socle_with_steel_box_tubes
__objs__ = []

# part_steel_box_tube_for_support_ground_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_ground_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_ground_flywheel").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_ground_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_ground_flywheel"))

# part_steel_box_tube_for_support_elevator_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_elevator_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel").Placement = App.Placement(App.Vector(Ltspf + h_tube/2,-2*h_tube,0),App.Rotation(App.Vector(0,1,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel"))

# part_steel_box_tube_for_support_elevator_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_elevator_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel001").Placement = App.Placement(App.Vector(Ltspf + h_tube/2 + Lspf - h_tube,-2*h_tube,0),App.Rotation(App.Vector(0,1,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_elevator_flywheel001"))

# part_steel_box_tube_for_support_palier_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_palier_flywheel.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_palier_flywheel").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_palier_flywheel").Placement = App.Placement(App.Vector(Ltspf - h_tube/2,-h_tube,L_elevator - h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_palier_flywheel"))

# part_rondelle_10m for ground - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m"))

# part_rondelle_10m for ground - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m001"))

# part_rondelle_10m for ground - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m002"))

# part_rondelle_10m for ground - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,-s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m003"))

# part_rondelle_10m for ground - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m004").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m004"))

# part_rondelle_10m for ground - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m005").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m005"))

# part_rondelle_10m for ground - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m006").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector(Ltspf,s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m006"))

# part_rondelle_10m for ground - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m007").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector(Ltspf,s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m007"))

# part_rondelle_10m for ground - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m008").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m008"))

# part_rondelle_10m for ground - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m009").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m009"))

# part_rondelle_10m for elevator_1 - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m010").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m010"))

# part_rondelle_10m for elevator_1 - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m011").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m011"))

# part_rondelle_10m for elevator_2 - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m012").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m012"))

# part_rondelle_10m for elevator_2 - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m013").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m013"))

# part_rondelle_10m for elevator_1 - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m014").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m014").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m014"))

# part_rondelle_10m for elevator_2 - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m015").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m015").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m015"))

# part_rondelle_10m for palier - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m016").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m016").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m016"))

# part_rondelle_10m for palier - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m017").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m017").Placement = App.Placement(App.Vector(Ltspf,s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_10m017"))

# part_rondelle_12m for palier - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m"))

# part_rondelle_12m for palier - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m001").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m001").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m001"))

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector(Ltspf,k_vis_10m + s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector(Ltspf,k_vis_10m + s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,k_vis_10m + s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,k_vis_10m + s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003"))

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector(Ltspf,k_vis_10m + s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,k_vis_10m + s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,- s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,- s_rondelle_10m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m10_120l007"))

# part_vis_metal_m12_140l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m12_140l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l"))

# part_vis_metal_m12_140l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m12_140l.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l001").ShapeColor = (0.50,0.30,0.20)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l001").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator - h_tube - s_rondelle_12m - k_vis_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_vis_metal_m12_140l001"))

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube - s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube - s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube - s_rondelle_10m,(2*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube - s_rondelle_10m,(8*h_tube)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m003"))

# part_ecrou_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m004").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m004").Placement = App.Placement(App.Vector(Ltspf,-2*h_tube - s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m004"))

# part_ecrou_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m005").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m005").Placement = App.Placement(App.Vector(Ltspf + Lspf - h_tube,-2*h_tube - s_rondelle_10m,L_elevator - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m005"))

# part_rondelle_12m for palier - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m002").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m002").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator + z_palier),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m002"))

# part_rondelle_12m for palier - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m003").ShapeColor = (0.20,0.30,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m003").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator + z_palier),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_rondelle_12m003"))

# part_ecrou_12m for palier - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m").ShapeColor = (0.75,0.50,0.25)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m").Placement = App.Placement(App.Vector(L_ground/2 + J/2,-h_tube/2,L_elevator + z_palier + s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m"))

# part_ecrou_12m for palier - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_12m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m001").ShapeColor = (0.75,0.50,0.25)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m001").Placement = App.Placement(App.Vector(L_ground/2 - J/2,-h_tube/2,L_elevator + z_palier + s_rondelle_12m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_12m001"))

# part_ecrou_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m006").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m006").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,h_tube + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m006"))

# part_ecrou_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m007").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m007").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,h_tube + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("part_ecrou_10m007"))

# assembly_roulette_pivotante - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante").ShapeColor = (0.30,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante").Placement = App.Placement(App.Vector(h_tube/2,-h_tube/2,-L_roulette_pivotante - s_rondelle_10m - k_vis_10m - s_rondelle_10m*3 + 0.5),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante"))

# assembly_roulette_pivotante - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_roulette_pivotante.stl","assembly_half_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante001").ShapeColor = (0.30,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante001").Placement = App.Placement(App.Vector(L_ground - h_tube/2,-h_tube/2,-L_roulette_pivotante - s_rondelle_10m - k_vis_10m - s_rondelle_10m*3 + 0.5),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes").getObject("assembly_roulette_pivotante001"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_half_socle_with_steel_box_tubes_v1_'
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
