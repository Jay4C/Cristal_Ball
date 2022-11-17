import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_slice_flywheel_with_steel_box_tubes"


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

# Export assembly_slice_flywheel_with_steel_box_tubes
__objs__ = []
h = 50
L_rotor = 1000
s = 2
k = 6.4
h_ecrou = 10

# part_steel_box_tube_for_the_rotor_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_the_rotor_flywheel.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_tube_for_the_rotor_flywheel").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_tube_for_the_rotor_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_tube_for_the_rotor_flywheel"))

# Block 1
# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(h/4,-s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l").Placement = App.Placement(App.Vector(h/4,-s-k,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m001").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(h/4,-s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m001"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001").Placement = App.Placement(App.Vector(h/4,-s-k,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l001"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m002").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(h/4,h,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m002"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m003").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(h/4,h,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m003"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(h/4,h + s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(h/4,h + s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m001"))

# part_steel_box_for_weight
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_for_weight.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight").Placement = App.Placement(App.Vector(0,h + s + h_ecrou,500/2 + 25),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m004").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m004").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m004"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m005").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m005").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m005"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m002").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25 + s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m002"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m003").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(h/4,h + s + h_ecrou + 25 + s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m003"))

# Block 2
# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m006").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m006").Placement = App.Placement(App.Vector(L_rotor-h/4,h,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m006"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002").Placement = App.Placement(App.Vector(L_rotor-h/4,h+s+k,(2*h)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l002"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m007").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m007").Placement = App.Placement(App.Vector(L_rotor-h/4,h,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m007"))

# part_vis_metal_m10_120l
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m10_120l.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003").Placement = App.Placement(App.Vector(L_rotor-h/4,h+s+k,(8*h)/10),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_vis_metal_m10_120l003"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m008").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m008").Placement = App.Placement(App.Vector(L_rotor-h/4,-s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m008"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m009").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m009").Placement = App.Placement(App.Vector(L_rotor-h/4,-s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m009"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m004").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m004").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m004"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m005").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m005").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m005"))

# part_steel_box_for_weight
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_for_weight.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight001").ShapeColor = (0.90,0.80,0.70)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight001").Placement = App.Placement(App.Vector(L_rotor-25,-s-h_ecrou-25,500/2 + 25),App.Rotation(App.Vector(0,1,0),90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_steel_box_for_weight001"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m010").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m010").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m010"))

# part_rondelle_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m011").ShapeColor = (0.20,0.40,0.60)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m011").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_rondelle_10m011"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m006").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m006").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s-h_ecrou,(2*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m006"))

# part_ecrou_10m
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_slice_flywheel_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m007").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m007").Placement = App.Placement(App.Vector(L_rotor-h/4,-s-h_ecrou-25-s-h_ecrou,(8*h)/10),App.Rotation(App.Vector(1,0,0),-90))
__objs__.append(FreeCAD.getDocument("assembly_slice_flywheel_with_steel_box_tubes").getObject("part_ecrou_10m007"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_slice_flywheel_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_slice_flywheel_with_steel_box_tubes_v1_'
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
