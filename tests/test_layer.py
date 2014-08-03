import pytest
import parfait

from qgis.core import QgsVectorLayer

def test_editing_puts_layer_in_edit_mode(QGIS):
    layer = QgsVectorLayer("Point", "test", "memory")
    assert not layer.isEditable()
    with parfait.editing(layer) as layer:
        assert layer.isEditable()
    assert not layer.isEditable()


