__author__ = 'nathan'
import contextlib

from qgis.core import QgsVectorLayer, QgsRasterLayer, QgsMapLayerRegistry

class LayerError(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return '\n'.join(self.errors)

@contextlib.contextmanager
def editing(layer):
    layer.startEditing()
    yield layer
    passed = layer.commitChanges()
    if not passed:
        errors = layer.commitErrors()
        errors = '\n'.join(errors)
        raise LayerError()


class Layer(object):
    def __init__(self, qgislayer):
        self.qgislayer = qgislayer
        QgsMapLayerRegistry.instance().addMapLayer(self.qgislayer)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        QgsMapLayerRegistry.instance().removeMapLayer(self.qgislayer.id())



def open(path, name=None, provider=None):
    layer = QgsVectorLayer(path, name, provider)
    return Layer(layer)

