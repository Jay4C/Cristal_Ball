import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_support_moteur_electrique"


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

# assembly_moteur_electrique
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/assembly_moteur_electrique.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("assembly_moteur_electrique").ShapeColor = (0.10,0.10,0.10)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("assembly_moteur_electrique").Placement = App.Placement(App.Vector(-(1536 - 1200)/2,(1000 - 657)/2,500),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 1
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 2
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette001").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette001").Placement = App.Placement(App.Vector(0,0,100),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 3
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette002").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette002").Placement = App.Placement(App.Vector(0,0,200),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 4
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette003").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette003").Placement = App.Placement(App.Vector(0,0,300),App.Rotation(App.Vector(0,0,1),0))

# part_palette - 5
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/part_palette.stl","assembly_support_moteur_electrique")
FreeCADGui.getDocument("assembly_support_moteur_electrique").getObject("part_palette004").ShapeColor = (0.10,0.20,0.30)
FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette004").Placement = App.Placement(App.Vector(0,0,400),App.Rotation(App.Vector(0,0,1),0))

setview()

# Export assembly_support_moteur_electrique
__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("assembly_moteur_electrique"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette001"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette002"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette003"))
__objs__.append(FreeCAD.getDocument("assembly_support_moteur_electrique").getObject("part_palette004"))

Mesh.export(__objs__,u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/2_Specials/Chas_Campbell_Gravitational_Engine/Version_3/assembly_support_moteur_electrique.stl")

del __objs__

# Generate PNG files
file = 'assembly_support_moteur_electrique_v3_'
# Ombr�
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
