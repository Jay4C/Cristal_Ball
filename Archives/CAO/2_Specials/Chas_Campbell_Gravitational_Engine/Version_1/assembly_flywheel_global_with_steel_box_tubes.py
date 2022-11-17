import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel_global_with_steel_box_tubes"


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
number_of_weights = 1
h_ecrou_10m = 10
s_rondelle_10m = 2

L_flywheel = 1000
s_rondelle_20m = 3
h_ecrou_20m = 20
L_moyeu_amovible_volant_inertie = 22.2
h1_palier = 38

L_ground = 500
L_link = (L_flywheel/2 + 10 - h1_palier - 10 - h_ecrou_20m - s_rondelle_20m - L_moyeu_amovible_volant_inertie - s_rondelle_20m - h_ecrou_20m)*2 + h1_palier
L_elevator = math.sqrt(math.pow(L_flywheel/2,2) + math.pow(h_tube/2 + number_of_weights*(h_tube/2) + h_ecrou_10m + s_rondelle_10m + h_tube,2))+ 50*3
h_palier = 65
d_vis = 13

# Export assembly_flywheel_global_with_steel_box_tubes
__objs__ = []

# assembly_complete_socle_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_complete_socle_with_steel_box_tubes.stl","assembly_flywheel_global_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_complete_socle_with_steel_box_tubes").ShapeColor = (0.25,0.75,1.0)
FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_complete_socle_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(1,0,0),0))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_complete_socle_with_steel_box_tubes"))

# assembly_flywheel_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_with_steel_box_tubes.stl","assembly_flywheel_global_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_flywheel_with_steel_box_tubes").ShapeColor = (0.2,0.5,0.8)
FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_flywheel_with_steel_box_tubes").Placement = App.Placement(App.Vector(-L_ground/2,-L_link/2 + h1_palier - d_vis,L_elevator + (h_palier - h_tube)/2),App.Rotation(App.Vector(1,0,0),90))
__objs__.append(FreeCAD.getDocument("assembly_flywheel_global_with_steel_box_tubes").getObject("assembly_flywheel_with_steel_box_tubes"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_global_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_flywheel_global_with_steel_box_tubes_v1_'
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
