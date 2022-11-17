import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly"


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
EPS_C = EPS * (-0.5)

# insertion part_top_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_US4324640A_Pyrolysis_Process/Version_1/part_top_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_top_support").Placement = App.Placement(App.Vector(0, 0, 1000), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_top_support").ShapeColor = (0.10,0.10,0.10)

# insertion part_chamber
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_US4324640A_Pyrolysis_Process/Version_1/part_chamber.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_chamber").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_chamber").ShapeColor = (0.30,0.20,0.10)
FreeCADGui.getDocument("assembly").getObject("part_chamber").Transparency = 70

# insertion part_bottom_support
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_US4324640A_Pyrolysis_Process/Version_1/part_bottom_support.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_bottom_support").Placement = App.Placement(App.Vector(0, 0, -5), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_bottom_support").ShapeColor = (0.90,0.80,0.70)

setview()

__objs__ = []
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_chamber"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_bottom_support"))
__objs__.append(FreeCAD.getDocument("assembly").getObject("part_top_support"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/2_Specials/Patent_US_US4324640A_Pyrolysis_Process/Version_1/assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = 'assembly_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/Images_To_Videos/2_Specials/US4324640A/' + file + str(i) + '.png',1117,388,'Current')
