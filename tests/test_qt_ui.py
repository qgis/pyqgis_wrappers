from parfait.qt import load_ui

def test_load_ui():
    widget, base = load_ui("test.ui")
    assert widget
    widget, base = load_ui("test2.ui")
    assert widget
