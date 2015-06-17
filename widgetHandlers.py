#!/usr/bin/env python

class WidgetHandlers:

	def __init__(self, builder):
		self.builder = builder

	def onToggleButton1_clicked(self, widget):
		print "ToggleButton1 Clicked"

	def onToggleButton2_clicked(self, widget):
		print "ToggleButton2 Clicked"

	def onToggleButton3_clicked(self, widget):
		selectCombo1 = self.builder.get_object("selectCombo1")
		if widget.get_active():
			selectCombo1.set_sensitive(False)
		else:
			selectCombo1.set_sensitive(True)

	def onButton1_clicked(self, widget):
		print "Button1 Clicked"
