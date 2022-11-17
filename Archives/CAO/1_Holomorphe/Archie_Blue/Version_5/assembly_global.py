import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_global"


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

__objs__ = []

# For placing the assembly_bottom
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/assembly_bottom.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_bottom").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_bottom").ShapeColor = (0.30,0.60,0.90)
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_bottom").Transparency = 0
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_bottom"))

# For placing the assembly_top
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/assembly_top.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_top").Placement = App.Placement(App.Vector(0, 0, 150 + 8), App.Rotation(App.Vector(0,1,0), 180))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_top").ShapeColor = (0.60,0.90,0.30)
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_top").Transparency = 0
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_top"))

# For placing the assembly_capacitors
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/assembly_capacitors.stl", DOC_NAME)
FreeCAD.getDocument(DOC_NAME).getObject("assembly_capacitors").Placement = App.Placement(App.Vector(0, 0, 55), App.Rotation(App.Vector(1,0,0), 0))
FreeCADGui.getDocument(DOC_NAME).getObject("assembly_capacitors").ShapeColor = (0.90,0.30,0.60)
__objs__.append(FreeCAD.getDocument(DOC_NAME).getObject("assembly_capacitors"))

setview()

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/1_Holomorphe/Archie_Blue/Version_5/" + DOC_NAME + ".stl"

Mesh.export(__objs__, stl_file)

del __objs__

# Generate PNG files
file = DOC_NAME + '_'
# Ombré
Gui.runCommand('Std_DrawStyle',5)
i = 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

# Filaire
Gui.runCommand('Std_DrawStyle',2)
i += 1
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewFront()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewTop()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRight()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewRear()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewBottom()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')

i += 1
Gui.activeDocument().activeView().viewLeft()
Gui.activeDocument().activeView().saveImage('A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/Images_To_Videos/1_Holomorphe/Archie_Blue/5/' + file + str(i) + '.png',1117,388,'Current')
