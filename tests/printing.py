import sys
from qgis.gui import QgsMapCanvas
from wrappers import render_template, layers, open_project, qgisapp

pfile = r"F:\gis_data\QGIS_Training\Perth\Perth.qgs"
template = r"F:\dev\qgis.wrappers\data\template.qpt"

with qgisapp(sys.argv, guienabled=True) as app:
    canvas = QgsMapCanvas()
    with open_project(pfile, canvas=canvas) as project:
        settings = project.map_settings
        render_template(template, settings, canvas, r"out.pdf")

    sys.exit()

