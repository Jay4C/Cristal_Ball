import FreeCAD, Part, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_we_and_etagere"


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

# dimensions exterieures maximales
longueur_exterieure_maximale = 1000
largeur_exterieure_maximale = 300
hauteur_exterieure_maximale = 2000

etagere = Part.makeBox(longueur_exterieure_maximale, largeur_exterieure_maximale, hauteur_exterieure_maximale)

box_1 = Part.makeBox(longueur_exterieure_maximale - 2*20, largeur_exterieure_maximale, (hauteur_exterieure_maximale - 100 - 5*20)/4)

box_2 = Part.makeBox(longueur_exterieure_maximale, largeur_exterieure_maximale - 2*20, (hauteur_exterieure_maximale - 100 - 5*20)/4)

# etagere cut by box_1
box_1_vector = FreeCAD.Vector(20, 0, hauteur_exterieure_maximale)
box_1.translate(box_1_vector)
for i in range(0, 5):
    box_1_vector = FreeCAD.Vector(0, 0, - (hauteur_exterieure_maximale - 100 - 5*20)/4 - 20)
    box_1.translate(box_1_vector)
    etagere = etagere.cut(box_1)

# etagere cut by box_2
box_2_vector = FreeCAD.Vector(0, 20, hauteur_exterieure_maximale)
box_2.translate(box_2_vector)
for i in range(0, 5):
    box_2_vector = FreeCAD.Vector(0, 0, - (hauteur_exterieure_maximale - 100 - 5*20)/4 - 20)
    box_2.translate(box_2_vector)
    etagere = etagere.cut(box_2)

Part.show(etagere)

DOC.recompute()

__objs__=[]

FreeCADGui.getDocument("assembly_we_and_etagere").getObject("Shape").ShapeColor = (1.00, 1.00, 0.00)
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("Shape"))

# etage 1 / insertion assembly_water_electrolyzer
vector = App.Vector(250/2 + 50, 250/2 + 25, 100 + 40 + (450 + 20)*0)
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
__objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer"))

# insertion assembly_water_electrolyzer
for i in range(1, 3):
    vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*i, 250/2 + 25, 100 + 40 + (450 + 20)*0)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
    FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    __objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)))
    
# etage 2 / insertion assembly_water_electrolyzer
for i in range(3, 6):
    vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-3), 250/2 + 25, 100 + 40 + (450 + 20)*1)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
    FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    __objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)))
    
# etage 3 / insertion assembly_water_electrolyzer
for i in range(6, 9):
    vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-6), 250/2 + 25, 100 + 40 + (450 + 20)*2)
    Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
    FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    __objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)))
    
# etage 4 / insertion assembly_water_electrolyzer
for i in range(9, 12):
    if i < 10:
        vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-9), 250/2 + 25, 100 + 40 + (450 + 20)*3)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
        FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        __objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer00" + str(i)))
    else:
        vector = App.Vector((250/2 + 62.5) + (250 + 62.5)*(i-9), 250/2 + 25, 100 + 40 + (450 + 20)*3)
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Brevet_us_4_124_463_water_electrolyzer_3/assembly_water_electrolyzer.stl", "assembly_we_and_etagere")
        FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        __objs__.append(FreeCAD.getDocument("assembly_we_and_etagere").getObject("assembly_water_electrolyzer0" + str(i)))

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Hydrogen_Container/assembly_we_and_etagere.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_we_and_etagere_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Hydrogen_Container/' + file + str(i) + '.png',1117,388,'Current')
        