import pytest
import parfait

from qgis.core import QgsVectorLayer, QgsMapLayerRegistry

@pytest.fixture
def cleanup(request):
    def _clean():
        QgsMapLayerRegistry.instance().removeAllMapLayers()
    request.addfinalizer(_clean)
    return cleanup

def test_editing_puts_layer_in_edit_mode(QGIS, cleanup):
    layer = QgsVectorLayer("Point", "test", "memory")
    assert not layer.isEditable()
    with parfait.editing(layer) as layer:
        assert layer.isEditable()
    assert not layer.isEditable()

def test_layer_is_in_registry_inside_with(QGIS, cleanup):
    assert QgsMapLayerRegistry.instance().mapLayers() == {}
    with parfait.open("Point", name='test', provider='memory') as layer:
        assert not QgsMapLayerRegistry.instance().mapLayers() == {}
        assert QgsMapLayerRegistry.instance().mapLayersByName('test')[0] == layer.qgislayer
    assert QgsMapLayerRegistry.instance().mapLayers() == {}

def test_layer_is_in_registry_on_open(QGIS, cleanup):
    assert QgsMapLayerRegistry.instance().mapLayers() == {}
    layer = parfait.open("Point", name='test', provider='memory')
    assert not QgsMapLayerRegistry.instance().mapLayers() == {}
    assert QgsMapLayerRegistry.instance().mapLayersByName('test')[0] == layer.qgislayer

