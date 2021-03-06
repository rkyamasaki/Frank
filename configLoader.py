#!/usr/bin/env python

from gi.repository import Gtk
import json

class ConfigLoader:

	CONFIGURATION_FILE = "config.json"

	widgets = [
		"toggleButtonVPN_01",
		"toggleButtonVPN_02",
		"toggleButtonConnectTunel",
		"buttonRepository"
	]

	@staticmethod
	def configure(builder):
		for widget_id in ConfigLoader.widgets:
			widget = builder.get_object(widget_id)
			widget.set_label(ConfigLoader.preferences[widget_id])

		#config Tunnel selectCombo
		tunnelSelectCombo = builder.get_object("selectCombo1")
		model = Gtk.ListStore(str)
		for entry in ConfigLoader.preferences["tunnelList"]:
			model.append([entry["label"]])
		tunnelSelectCombo.set_model(model)
		renderer_text = Gtk.CellRendererText()
		tunnelSelectCombo.pack_start(renderer_text, True)
		tunnelSelectCombo.add_attribute(renderer_text, "text", 0)


	def loadPreferences(filePath):
		print "Loading preferences"
		with open(filePath) as config_file:
			return json.loads(config_file.read())

	preferences = loadPreferences(CONFIGURATION_FILE)