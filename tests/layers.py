import sys
from wrappers import render_template, map_layers, open_project, qgisapp

pfile = r"F:\gis_data\QGIS_Training\Perth\Perth.qgs"

with qgisapp(sys.argv, True, '') as app:
    with open_project(pfile) as project:
        for layer in map_layers(".*Bound.*"):
            print layer.name()

    sys.exit()


