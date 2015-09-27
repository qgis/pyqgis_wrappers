from qgis.core import QgsApplication
from parfait import QGIS
import pytest

@pytest.fixture(scope="module")
def QGIS(request):
    app = QGIS.init()
    def fin():
        print ("teardown QGIS")
        QgsApplication.exitQgis()

    request.addfinalizer(fin)
    return app  # provide the fixture value
