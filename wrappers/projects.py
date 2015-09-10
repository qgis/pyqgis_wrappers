from wrappers.layer_wrappers import map_layers
from qgis.core.contextmanagers import qgisapp
from qgis.core import QgsProject, QgsMapLayerRegistry, QgsMapSettings
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from PyQt4.QtCore import QFileInfo
from PyQt4.QtXml import QDomDocument


class Project(object):
    def __init__(self, bridge=None):
        self.bridge = bridge

    def __enter__(self):
        return self

    @classmethod
    def from_file(cls, filename, canvas):
        QgsProject.instance().clear()
        bridge = None
        if canvas:
            bridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), canvas)
        QgsProject.instance().read(QFileInfo(filename))
        if bridge:
            bridge.setCanvasLayers()
        return cls(bridge)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        QgsProject.instance().clear()
        QgsMapLayerRegistry.instance().removeAllMapLayers()
        if self.bridge:
            self.bridge.clear()

    @property
    def map_settings(self):
        """
        Return the settings that have been set for the map canvas.
        @return: A QgsMapSettings instance with the settings read from the project.
        """
        xml = open(QgsProject.instance().fileName()).read()
        doc = QDomDocument()
        doc.setContent(xml)
        canvasnodes = doc.elementsByTagName("mapcanvas")
        node = canvasnodes.at(0).toElement()
        settings = QgsMapSettings()
        settings.readXML(node)
        return settings


def open_project(projectfile, canvas=None):
    """
    Open a QGIS project file
    :param projectfile: The path to the project file to load.
    :param canvas: (optional) Canvas object.
    :return: A Project object wrapper with handy functions for doing project related stuff.
    """
    return Project.from_file(projectfile, canvas)



