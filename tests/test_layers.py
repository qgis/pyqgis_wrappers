import os
import sys
import data

from parfait import render_template, map_layers, open_project, QGIS, load_vector, add_layer


app = QGIS.init()

def test_open_project():
    pfile = data.test_file("project.qgs")
    with open_project(pfile) as project:
        layers = map_layers("points")
        assert len(layers) == 1
        assert layers[0].name() == "points"

def test_load_layer():
    filename = data.test_file("points.shp")
    layer = load_vector(filename)
    assert layer.name() == os.path.basename(filename)
    assert layer.source() == filename
    assert layer.isValid()
