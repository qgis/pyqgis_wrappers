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





