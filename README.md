parfait
=======

parfait is a wrapper around common pyqgis idioms that allows for faster development and hopefully removes
some of the (sometimes) ugly C/C++ based API (read: not Python-ish)

The current plan is to flesh out ideas using parfait and then mirgate them to core QGIS as they become stable or well designed.

What the heck is a Parfait
---------------------------

mmmmmmmmmmmm [parfait](http://en.wikipedia.org/wiki/Parfait)

A Parfait has layers, this is a layer on pyqgis, therefore parfait.
Ok..don't blame me, the wife came up with it. I suck at naming.


What can it do so far?
----------------------

```
import sys
from qgis.gui import QgsMapCanvas
from wrappers import render_template, map_layers, open_project, qgisapp

pfile = r"project.qgs"
template = r"template.qpt"

with qgisapp(sys.argv, guienabled=True) as app:
    canvas = QgsMapCanvas()
    with open_project(pfile, canvas=canvas) as project:
        settings = project.map_settings
        render_template(template, settings, canvas, r"out.pdf")
```

or without the `with` block

```
with qgisapp(sys.argv, guienabled=True) as app:
    canvas = QgsMapCanvas()
    project = open_project(pfile, canvas=canvas)
    settings = project.map_settings
    render_template(template, settings, canvas, r"out.pdf")
    project.close()
```

Listing loaded layers

```
from wrappers import map_layers
layers = map_layers()
mylayer = map_layers(name='mylayer')
```

