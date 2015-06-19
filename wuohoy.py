#!/usr/bin/env python

from gi.repository import Gtk
from configLoader import ConfigLoader
from widgetHandlers import WidgetHandlers

class Wuohoy:

	def activate(self, widget, data=None):
		builder = Gtk.Builder()
		builder.add_from_file("gui.glade")
		builder.connect_signals(WidgetHandlers(builder));

		ConfigLoader.configure(builder)
		self.window = builder.get_object("MainWindow")
		self.window.connect('destroy', self.hide)
		self.window.show_all()

	def hide(self, widget, data=None):
		self.window.hide()

	def staticon_right_click(self, icon, button, time):
		self.menu = Gtk.Menu()
		for item in ConfigLoader.preferences['systray-menu']:
			self.menuItem = Gtk.MenuItem()
			self.menuItem.set_label(item['label'])

			for action in item['actions']:
				module = __import__(action['module'])
				klazz = getattr(module, action['className'])

				function = getattr(klazz(), action['command'])
				self.menuItem.connect(action['name'], function)

			self.menu.append(self.menuItem)

		self.menu.show_all()

		def pos(menu, icon):
			return (Gtk.StatusIcon.position_menu(menu, icon))

		self.menu.popup(None, None, pos, self.staticon, button, time)


	def __init__(self):
		self.staticon = Gtk.StatusIcon()
		self.staticon.set_from_stock(Gtk.STOCK_EXECUTE)
		self.staticon.connect('activate', self.activate)
		self.staticon.connect('popup-menu', self.staticon_right_click)
		self.staticon.set_visible(True)
		self.window = None

if __name__ == "__main__":
	hwg = Wuohoy()
	Gtk.main()