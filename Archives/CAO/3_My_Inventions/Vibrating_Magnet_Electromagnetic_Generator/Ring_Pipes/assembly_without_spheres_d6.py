import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_without_spheres_d6"


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

l_vis = 100
h_block_ring = 8
h_magnet = 5
h_coil = l_vis - h_block_ring*2
number_of_magnets = round(h_coil/h_magnet)

# Insertion part_block_ring_6d
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Ring_Pipes/part_block_ring_6d.stl","assembly_without_spheres_d6")
FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d").ShapeColor = (0.90,0.60,0.60)
FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d").Placement = App.Placement(App.Vector(0,0,h_block_ring - 3),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_f_r_p_6d_100h
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/4_Basics/Pipes/part_f_r_p_6d_100h.stl","assembly_without_spheres_d6")
FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_f_r_p_6d_100h").ShapeColor = (0.90,0.60,0.30)
FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_f_r_p_6d_100h").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_p_m_r_1D20_2D6_5h
for i in range(0, number_of_magnets):
    x = 0
    y = 0
    z = h_block_ring + h_magnet*i
    
    if i == 0:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h").ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h").Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    if 1 <= i < 10:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h00" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h00" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 10 <= i < 100:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h0" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h0" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))
    elif 100 <= i < 1000:
        Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Permanent_Magnets/Ferrite/part_p_m_r_1D20_2D6_5h.stl","assembly_without_spheres_d6")
        FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h" + str(i)).ShapeColor = (0.30,0.60,0.90)
        FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_p_m_r_1D20_2D6_5h" + str(i)).Placement = App.Placement(App.Vector(x,y,z),App.Rotation(App.Vector(0,0,1),0))

# Insertion part_block_ring_6d
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/My_Tools/Test/Service/Archives/CAO/3_My_Inventions/Vibrating_Magnet_Electromagnetic_Generator/Ring_Pipes/part_block_ring_6d.stl","assembly_without_spheres_d6")
FreeCADGui.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d001").ShapeColor = (0.90,0.60,0.60)
FreeCAD.getDocument("assembly_without_spheres_d6").getObject("part_block_ring_6d001").Placement = App.Placement(App.Vector(0,0,h_block_ring + h_magnet*number_of_magnets),App.Rotation(App.Vector(0,0,1),0))

setview()
