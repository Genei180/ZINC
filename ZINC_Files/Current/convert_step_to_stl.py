import sys
sys.path.insert(0, "C:\\Program Files\\FreeCAD 0.21\\bin")
import FreeCAD
import Part
import Mesh

from os import listdir
from os.path import isfile, join

path_to_step = "STEP"
path_to_stl = "STL"
files = [f for f in listdir(path_to_step) if isfile(join(path_to_step,f)) ]

for file in files:
    shape = Part.Shape()
    shape.read(join(path_to_step,file))
    doc = App.newDocument('Doc')
    pf = doc.addObject("Part::Feature","MyShape")
    pf.Shape = shape
    new_file_name = file.split(".step")[0] + ".stl"
    Mesh.export([pf], join(path_to_stl,new_file_name))
    print("Finished Exporting:", new_file_name)

sys.exit()

