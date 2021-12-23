#!/usr/bin/env python

UPDATE = 300    # update interval in ms
last = ""

import gi, psutil
gi.require_version('Gtk', '3.0')
from gi.repository import GObject
from gi.repository import Gtk
tray = Gtk.StatusIcon()
tray.set_visible(True)

def update():
    global last

    m = psutil.virtual_memory()
    mt = m.total
    ma = m.available
    perc = int(100 * (1 - ma / mt))
    perc = min(99, max(perc, 1))
    i = f"icons/{perc}.png"
    if i != last:
        tray.set_from_file(i)
        tray.set_visible(True)
        last = i
    GObject.timeout_add(UPDATE, update)

update()
Gtk.main()

