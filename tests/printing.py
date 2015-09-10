import sys
from qgis.core import QgsApplication
from qgis.gui import QgsMapCanvas
from wrappers.printing import render_template
from wrappers.layer_wrappers import layers
from wrappers.projects import open_project
from qgis.core.contextmanagers import qgisapp


pfile = r"F:\gis_data\QGIS_Training\Perth\Perth.qgs"
template = r"F:\dev\qgis.wrappers\data\template.qpt"

with qgisapp(sys.argv, guienabled=True) as app:
    canvas = QgsMapCanvas()
    with open_project(pfile, canvas=canvas) as project:
        settings = project.map_settings
        render_template(template, settings, canvas, r"out.pdf")

    sys.exit()

