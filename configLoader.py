#!/usr/bin/env python

from gi.repository import Gtk
import json

class ConfigLoader:

	widgets = [
		"toggleButton1",
		"toggleButton2",
		"button1"
	]

	credentials = {
		'sshUsername': None,
		'sshPublicKey': None
	}

	preferences = None

	@staticmethod
	def configure(builder, filePath):
		print "Loading configuration from file [" + filePath + "]..."

		with open(filePath) as config_file:
			ConfigLoader.preferences = json.loads(config_file.read())

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
