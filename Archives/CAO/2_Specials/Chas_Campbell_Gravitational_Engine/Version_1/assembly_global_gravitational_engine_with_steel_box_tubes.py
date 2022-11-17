import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global_gravitational_engine_with_steel_box_tubes"


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
L_support_vertical_motor = 50*2 + 50*3
L_support_vertical_generator = 50*2 + 50*3
h_tube = 50
L_roulette_pivotante = 99
s_rondelle_10m = 2
h_ecrou_10m = 10
h_ecrou_20m = 20
h_moyeu_amovible_volant_inertie = 22.2

# Export assembly_global_gravitational_engine_with_steel_box_tubes
__objs__ = []

# assembly_global_with_steel_box_tubes_for_generator
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_generator.stl","assembly_global_gravitational_engine_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_generator").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_generator").Placement = App.Placement(App.Vector(-L_flywheel/2 + h_tube*6,-(3*L_flywheel)/2 + h_tube*4,L_support_vertical_generator/2 + h_tube/2 + s_rondelle_10m + L_roulette_pivotante - 1),App.Rotation(App.Vector(0,0,1),90))
__objs__.append(FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_generator"))

# assembly_global_with_steel_box_tubes_for_motor
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_with_steel_box_tubes_for_motor.stl","assembly_global_gravitational_engine_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_motor").ShapeColor = (0.30,0.20,0.10)
FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_motor").Placement = App.Placement(App.Vector(-L_flywheel/2,L_flywheel/2 - h_ecrou_20m - h_moyeu_amovible_volant_inertie - h_tube,L_support_vertical_motor/2 + h_tube/2 + s_rondelle_10m + L_roulette_pivotante - 1),App.Rotation(App.Vector(0,0,1),-90))
__objs__.append(FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_global_with_steel_box_tubes_for_motor"))

# assembly_flywheel_global_with_steel_box_tubes
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_flywheel_global_with_steel_box_tubes.stl","assembly_global_gravitational_engine_with_steel_box_tubes")
FreeCADGui.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_flywheel_global_with_steel_box_tubes").ShapeColor = (0.80,0.60,0.40)
FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_flywheel_global_with_steel_box_tubes").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,1,0),0))
__objs__.append(FreeCAD.getDocument("assembly_global_gravitational_engine_with_steel_box_tubes").getObject("assembly_flywheel_global_with_steel_box_tubes"))

setview()

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_1/assembly_global_gravitational_engine_with_steel_box_tubes.stl")

del __objs__

# Generate PNG files
file = 'assembly_global_gravitational_engine_with_steel_box_tubes_v1_'
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
