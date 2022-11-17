import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel_with_steel_box_tubes"


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

h_flywheel = 50
L_flywheel = 1000
s_rondelle_20m = 3
h_ecrou = 20
L_moyeu_amovible_volant_inertie = 22.2

# Export assembly_flywheel_with_steel_box_tubes
__objs__ = []

# assembly_slice_flywheel_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_slice_flywheel_with_steel_box_tubes.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("assembly_slice_flywheel_with_steel_box_tubes").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("assembly_slice_flywheel_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("assembly_slice_flywheel_with_steel_box_tubes"))

# part_tige_filetee_m20_1000l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_tige_filetee_m20_1000l.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.40,0.20,0.10)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-(L_flywheel-h_flywheel)/2),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_tige_filetee_m20_1000l"))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,h_flywheel),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m"))

# part_rondelle_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-s_rondelle_20m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m001"))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,h_flywheel + s_rondelle_20m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m"))

# part_ecrou_20m for slice_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,- s_rondelle_20m - h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m001"))

# For moteur electrique

# part_poulie_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - L_moyeu_amovible_volant_inertie - 10 - h_ecrou - s_rondelle_20m + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie"))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - L_moyeu_amovible_volant_inertie - 10 - h_ecrou - s_rondelle_20m + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m002").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - s_rondelle_20m - 10 - h_ecrou + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m002"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m002").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - h_ecrou - 10 + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m002"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m003").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - s_rondelle_20m - 10 - h_ecrou - L_moyeu_amovible_volant_inertie - s_rondelle_20m + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m003"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m003").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 - 10 - s_rondelle_20m - 10 - h_ecrou - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou + h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m003"))

# For alternateur

# part_poulie_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_poulie_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 -12.2 + L_moyeu_amovible_volant_inertie + 10 + h_ecrou + s_rondelle_20m + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_poulie_volant_inertie001"))

# part_moyeu_amovible_volant_inertie
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_moyeu_amovible_volant_inertie.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie001").ShapeColor = (0.50,0.50,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie001").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_moyeu_amovible_volant_inertie001"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m004").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m004"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m004").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m004"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m005").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m005"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m005").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m005"))

# For moteur electrique

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m006").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 + 10 - s_rondelle_20m - 10 - h_ecrou - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m006"))

# part_palier
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palier.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier").Placement = App.Placement(App.Vector(L_flywheel/2 - 127/2,h_flywheel/2 + 65/2,L_flywheel/2 + 10 - 38 - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m007").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 + 10 - s_rondelle_20m - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou - 38),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m007"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m006").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,L_flywheel/2 + 10 - h_ecrou - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou - 38 - s_rondelle_20m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m006"))

# For alternateur

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m008").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m008"))

# part_palier
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_palier.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier001").ShapeColor = (0.30,0.30,0.30)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier001").Placement = App.Placement(App.Vector(L_flywheel/2 - 127/2,h_flywheel/2 + 65/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 + s_rondelle_20m - s_rondelle_20m - 0.5),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_palier001"))

# part_rondelle_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m009").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 + s_rondelle_20m + 38 - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_rondelle_20m009"))

# part_ecrou_20m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_20m.stl","assembly_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m007").Placement = App.Placement(App.Vector(L_flywheel/2,h_flywheel/2,-L_flywheel/2 + 10 + 10 + h_ecrou + s_rondelle_20m + L_moyeu_amovible_volant_inertie + s_rondelle_20m + h_ecrou + 30 + s_rondelle_20m + 38 + s_rondelle_20m - s_rondelle_20m - 0.5),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_with_steel_box_tubes").getObject("part_ecrou_20m007"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_flywheel_with_steel_box_tubes_v1_'
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
