import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_half_socle_with_steel_box_tubes_for_generator"


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

L_support_horizontal_generator = 454
L_support_vertical_generator = 50*2 + 50*3
h_tube = 50

# Export assembly_half_socle_with_steel_box_tubes_for_generator
__objs__ = []

# part_steel_box_tube_for_support_horizontal_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_generator.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator"))

# part_steel_box_tube_for_support_vertical_generator - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_generator.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator").Placement = App.Placement(App.Vector(0,-h_tube,h_tube),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator"))

# part_steel_box_tube_for_support_vertical_generator - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_vertical_generator.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator001").Placement = App.Placement(App.Vector(L_support_horizontal_generator - h_tube,-h_tube,h_tube),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_vertical_generator001"))

# part_steel_box_tube_for_support_horizontal_generator_2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_horizontal_generator_2.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator_2").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator_2").Placement = App.Placement(App.Vector(0,0,-L_support_vertical_generator + h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_steel_box_tube_for_support_horizontal_generator_2"))

# part_rondelle_10m

# for_support_horizontal_generator

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m003"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m004"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m005"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m006"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m007"))

# for_support_horizontal_generator_2

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m008"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m009"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m010"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m011"))

# part_rondelle_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m012"))

# part_rondelle_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m013"))

# part_rondelle_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m014").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m014").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m014"))

# part_rondelle_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m015").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m015").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m015"))

# part_rondelle_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m016").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m016").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m016"))

# part_rondelle_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m017").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m017").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m017"))

# part_rondelle_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m018").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m018").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m018"))

# part_rondelle_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m019").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m019").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m019"))

# part_rondelle_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m020").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m020").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,h_tube/2,-(L_support_vertical_generator - h_tube*2)),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_rondelle_10m020"))

# part_vis_metal_m10_120l

# for_support_horizontal_generator

# part_vis_metal_m10_120l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l"))

# part_vis_metal_m10_120l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l001"))

# part_vis_metal_m10_120l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l002"))

# part_vis_metal_m10_120l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l003"))

# for_support_horizontal_motor_2

# part_vis_metal_m10_120l - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004").Placement = App.Placement(App.Vector((2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l004"))

# part_vis_metal_m10_120l - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005").Placement = App.Placement(App.Vector((8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l005"))

# part_vis_metal_m10_120l - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l006"))

# part_vis_metal_m10_120l - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007").ShapeColor = (0.33,0.66,0.99)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,-h_tube - s_rondelle_10m - k_vis_10m,-(L_support_vertical_generator - h_tube*2) - h_tube/2),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m10_120l007"))

# part_ecrou_10m

# for_support_horizontal_generator

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m002").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m003").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m003"))

# for_support_horizontal_generator_2

# part_ecrou_10m - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m004").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m004").Placement = App.Placement(App.Vector((2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m004"))

# part_ecrou_10m - 6
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m005").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m005").Placement = App.Placement(App.Vector((8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m005"))

# part_ecrou_10m - 7
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m006").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m006").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (2*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m006"))

# part_ecrou_10m - 8
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m007").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m007").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (8*h_tube)/10,h_tube + s_rondelle_10m + h_ecrou_10m,-(L_support_vertical_generator - 2*h_tube) - h_tube/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m007"))

# part_ecrou_10m - 9
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m008").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m008").Placement = App.Placement(App.Vector((3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m008"))

# part_ecrou_10m - 10
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m009").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m009").Placement = App.Placement(App.Vector((3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m009"))

# part_ecrou_10m - 11
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m010").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m010").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(2*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m010"))

# part_ecrou_10m - 12
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m011").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m011").Placement = App.Placement(App.Vector(L_support_horizontal_generator - (3*h_tube)/2,(8*h_tube)/10,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m011"))

# part_ecrou_10m - 13
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_half_socle_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m012").ShapeColor = (0.99,0.88,0.77)
FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m012").Placement = App.Placement(App.Vector(L_support_horizontal_generator/2,h_tube/2,-(L_support_vertical_generator - 2*h_tube) + s_rondelle_10m),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_half_socle_with_steel_box_tubes_for_generator").getObject("part_ecrou_10m012"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes_for_generator.stl")

del __objs__

# Generate PNG files
file = 'assembly_half_socle_with_steel_box_tubes_for_generator_v1_'
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
