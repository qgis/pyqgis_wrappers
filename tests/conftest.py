from qgis.core import QgsApplication
import pytest

@pytest.fixture(scope="module")
def QGIS(request):
    app = QgsApplication([], False)
    QgsApplication.initQgis()
    print app
    def fin():
        print ("teardown QGIS")
        QgsApplication.exitQgis()

    request.addfinalizer(fin)
    return app  # provide the fixture value
