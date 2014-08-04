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

Not much yet, just one thing at the moment.

Editing context manager

Within the the editing with block the layer with be in edit mode, so methods like addFeature and updateFeature will work as expected. When the block exits layer.commitChanges will be called and errors will be handled.

```
import parfait

layer = QgsVectorLayer("Point", "mylayer", "memory")
with parfait.editing(layer):
  layer.addFeature(..)
  
```

  
