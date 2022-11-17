import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_with_steel_box_tubes_for_generator"


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
L_support_horizontal2_generator = 454

# Export assembly_global_with_steel_box_tubes_for_generator
__objs__ = []

# assembly_socle_with_steel_box_tubes_for_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_socle_with_steel_box_tubes_for_generator.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_socle_with_steel_box_tubes_for_generator").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_socle_with_steel_box_tubes_for_generator").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_socle_with_steel_box_tubes_for_generator"))

# assembly_alternateur
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_alternateur.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_alternateur").ShapeColor = (0.30,0.20,0.10)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_alternateur").Placement = App.Placement(App.Vector(L_support_horizontal2_generator,0,h_tube),App.Rotation(App.Vector(0,0,1),90))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("assembly_alternateur"))

# generator
A1 = 220
AB = 277
B = 58
C = 305
D = 23
E = 50
K = 14
A = 454
x1 = A - B - C - D
y1 = (AB - A1)/2

h_ecrou_14m = 14
k_vis_14m = 8.8
s_rondelle_14m = 2.5

# part_rondelle_14m

# part_rondelle_14m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m"))

# part_rondelle_14m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m001").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m001").Placement = App.Placement(App.Vector(x1 + C + D,y1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m001"))

# part_rondelle_14m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m002").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m002").Placement = App.Placement(App.Vector(x1,y1 + A1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m002"))

# part_rondelle_14m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_rondelle_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m003").ShapeColor = (0.99,0.66,0.33)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m003").Placement = App.Placement(App.Vector(x1 + C + D,y1 + A1,-s_rondelle_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_rondelle_14m003"))

# part_ecrou_14m

# part_ecrou_14m - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m").Placement = App.Placement(App.Vector(x1,y1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m"))

# part_ecrou_14m - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m001").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m001").Placement = App.Placement(App.Vector(x1 + C + D,y1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m001"))

# part_ecrou_14m - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m002").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m002").Placement = App.Placement(App.Vector(x1,y1 + A1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m002"))

# part_ecrou_14m - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_ecrou_14m.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m003").ShapeColor = (0.88,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m003").Placement = App.Placement(App.Vector(x1 + C + D,y1 + A1,-s_rondelle_14m - h_ecrou_14m),App.Rotation(App.Vector(0,0,1),0))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_ecrou_14m003"))

# part_vis_metal_m14_100l

# part_vis_metal_m14_100l - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l").Placement = App.Placement(App.Vector(x1,y1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l"))

# part_vis_metal_m14_100l - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l001").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l001").Placement = App.Placement(App.Vector(x1 + C + D,y1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l001"))

# part_vis_metal_m14_100l - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l002").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l002").Placement = App.Placement(App.Vector(x1,y1 + A1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l002"))

# part_vis_metal_m14_100l - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/part_vis_metal_m14_100l.stl","assembly_global_with_steel_box_tubes_for_generator")
FreeCADGui.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l003").ShapeColor = (0.22,0.44,0.22)
FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l003").Placement = App.Placement(App.Vector(x1 + C + D,y1 + A1,h_tube + 20 + s_rondelle_14m + k_vis_14m),App.Rotation(App.Vector(1,0,0),180))
__objs__.append(FreeCAD.getDocument("assembly_global_with_steel_box_tubes_for_generator").getObject("part_vis_metal_m14_100l003"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_generator.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_with_steel_box_tubes_for_generator_v1_'
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
