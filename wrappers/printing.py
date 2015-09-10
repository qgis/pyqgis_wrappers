from PyQt4.QtXml import QDomDocument
from qgis.core import QgsComposition


class ComposerTemplate():
    def __init__(self, composition):
        self.composition = composition

    @classmethod
    def from_file(cls, template_path, mapsettings, data=None):
        if not data:
            data = {}

        with open(template_path) as f:
            template_content = f.read()

        document = QDomDocument()
        document.setContent(template_content)
        composition = QgsComposition(mapsettings)
        composition.loadFromTemplate(document, data)
        return cls(composition)

    def __getitem__(self, item):
        return self.composition.getComposerItemById(item)


def render_template(template_path, settings, canvas, outpath, data=None):
    # You must set the id in the template
    template = ComposerTemplate.from_file(template_path, canvas.mapSettings(), data)
    map_item = template['map']
    map_item.setMapCanvas(canvas)
    map_item.zoomToExtent(settings.extent())
    # # You must set the id in the template
    legend_item = template['legend']
    legend_item.updateLegend()
    template.composition.refreshItems()
    template.composition.exportAsPDF(outpath)
