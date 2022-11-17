import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_complete_socle_with_steel_box_tubes"


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
s_rondelle_20m = 3
s_rondelle_10m = 2
h_ecrou = 20
L_moyeu_amovible_volant_inertie = 22.2
h1_palier = 38

h_tube = 50
L_ground = 500
L_link = (L_flywheel/2 + 10 - 38 - 10 - h_ecrou - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou)*2 + h1_palier

# Export assembly_complete_socle_with_steel_box_tubes
__objs__ = []

# assembly_half_socle_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes").ShapeColor = (0.25,0.75,1.0)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes"))

# part_steel_box_tube_for_support_link_flywheel
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_steel_box_tube_for_support_link_flywheel.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_link_flywheel").ShapeColor = (0.2,0.5,0.8)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_link_flywheel").Placement = App.Placement(App.Vector(L_ground/2 - h_tube/2,-L_link,h_tube),App.Rotation(90,0,90))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_steel_box_tube_for_support_link_flywheel"))

# assembly_half_socle_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_half_socle_with_steel_box_tubes.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes001").ShapeColor = (0.25,0.75,1.0)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes001").Placement = App.Placement(App.Vector(L_ground,-L_link,0),App.Rotation(App.Vector(0,0,1),180))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("assembly_half_socle_with_steel_box_tubes001"))

# part_rondelle_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m"))

# part_rondelle_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m001").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m001"))

# part_rondelle_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m002").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (2*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m002"))

# part_rondelle_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m003").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (8*h_tube)/10,2*h_tube),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_rondelle_10m003"))

# part_ecrou_10m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m").Placement = App.Placement(App.Vector(L_ground/2,-(2*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m"))

# part_ecrou_10m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m001").Placement = App.Placement(App.Vector(L_ground/2,-(8*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m001"))

# part_ecrou_10m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m002").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (2*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m002"))

# part_ecrou_10m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_10m.stl","assembly_complete_socle_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").ShapeColor = (0.60,0.40,0.20)
FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m003").Placement = App.Placement(App.Vector(L_ground/2,-L_link + (8*h_tube)/10,2*h_tube + s_rondelle_10m),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_complete_socle_with_steel_box_tubes").getObject("part_ecrou_10m003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_complete_socle_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_complete_socle_with_steel_box_tubes_v1_'
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
