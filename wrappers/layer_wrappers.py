import re
from qgis.core import QgsMapLayerRegistry

_layerreg = QgsMapLayerRegistry.instance()


def map_layers(name=None, type=None):
    """
    Return all the loaded layers.  Filters by name (optional) first and then type (optional)
    :param name: (optional) name of layer to return..
    :param type: (optional) The QgsMapLayer type of layer to return.
    :return: List of loaded layers. If name given will return all layers with matching name.
    """
    layers = _layerreg.mapLayers().values()
    _layers = []
    if name or type:
        if name:
            _layers = [layer for layer in layers if re.match(name, layer.name())]
        if type:
            _layers += [layer for layer in layers if layer.type() == type]
        return _layers
    else:
        return layers

