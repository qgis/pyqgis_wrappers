from qgis.core import QgsMapLayerRegistry

_layerreg = QgsMapLayerRegistry.instance()


def layers(name=None):
    """
    Return all the loaded layers.
    :param name: (optional) name of layer to return..
    :return: List of loaded layers. If name given will return all layers with matching name.
    """
    if name:
        return _layerreg.mapLayersByName(name)
    return _layerreg.mapLayers().values()
