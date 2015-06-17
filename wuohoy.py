#!/usr/bin/env python

from gi.repository import Gtk
from configLoader import ConfigLoader
from widgetHandlers import WidgetHandlers

class Wuohoy:

	def __init__(self):

		builder = Gtk.Builder()
		builder.add_from_file("gui.glade")
		builder.connect_signals(WidgetHandlers(builder));

		ConfigLoader.configure(builder, "config.json")

		self.window = builder.get_object("MainWindow")
		self.window.connect("destroy", Gtk.main_quit);
		
		self.window.show_all()

if __name__ == "__main__":
	hwg = Wuohoy()
	Gtk.main()

