#!/usr/bin/env python
from configLoader import ConfigLoader
import subprocess

from configLoader import ConfigLoader
import subprocess

class WidgetHandlers:

	def __init__(self, builder):
		self.builder = builder
		self.sshProcess = None

	def onToggleButton1_clicked(self, widget):
		print "ToggleButton1 Clicked"

		vpnHost = ConfigLoader.preferences['credentials']['vpnHost']
		vpnUser = ConfigLoader.preferences['credentials']['vpnUser']
		vpnPassword = ConfigLoader.preferences['credentials']['vpnPassword'].replace(';', '\;')
		vpnAuthGroup = ConfigLoader.preferences['credentials']['vpnAuthGroup']

		subprocess.call('echo ' + vpnPassword +
			' | sudo openconnect --user=' + vpnUser +
			' --authgroup=' + vpnAuthGroup +
			' --passwd-on-stdin --no-cert-check --no-xmlpost ' + vpnHost, shell=True)

	def onToggleButton2_clicked(self, widget):
		print "ToggleButton2 Clicked"

	def onToggleButton3_clicked(self, widget):
		selectCombo1 = self.builder.get_object("selectCombo1")

		if widget.get_active():
			selectCombo1.set_sensitive(False)

			user   = ConfigLoader.preferences['credentials']['sshUsername']
			sshKey = ConfigLoader.preferences['credentials']['sshPrivateKey']

			command = ''
			for target in ConfigLoader.preferences['tunnelList'][0]['path']:
				command = command + ' -L ' + target['originPort'] + ':' + target['targetHost'] + ':' + target['destPort']

			self.sshProcess = subprocess.Popen('ssh -i ' + sshKey + ' ' + user + command, shell=True)
		else:

			if self.sshProcess is not None:
				print "Killing process..."
				self.sshProcess.terminate()
				self.sshProcess = None
			selectCombo1.set_sensitive(True)

	def onButton1_clicked(self, widget):
		print "Button1 Clicked"
