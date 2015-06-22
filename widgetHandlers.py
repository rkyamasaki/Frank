#!/usr/bin/env python

from configLoader import ConfigLoader
import subprocess
import psutil

class WidgetHandlers:

	@staticmethod
	def kill_process_tree(pid):
		print "killing process tree... " + str(pid)
		parent = psutil.Process(pid)
		for child in parent.children(recursive=True):
			print "killing child process " + str(child)
			child.kill()
		parent.kill()


	def __init__(self, builder):
		self.builder = builder
		self.sshProcess = None

	def onToggleButtonVPN_01_clicked(self, widget):

		if widget.get_active():
			vpnHost = ConfigLoader.preferences['credentials']['vpnHost']
			vpnUser = ConfigLoader.preferences['credentials']['vpnUser']
			vpnPassword = ConfigLoader.preferences['credentials']['vpnPassword'].replace(';', '\;')
			vpnAuthGroup = ConfigLoader.preferences['credentials']['vpnAuthGroup']

			self.vpnProcess = subprocess.Popen('echo ' + vpnPassword +
				' | sudo openconnect --user=' + vpnUser +
				' --authgroup=' + vpnAuthGroup +
				' --passwd-on-stdin --no-cert-check --no-xmlpost ' + vpnHost, shell=True)
		else:
			if self.vpnProcess is not None:
				WidgetHandlers.kill_process_tree(self.vpnProcess.pid)
				self.sshProcess = None


	def onToggleButtonVPN_02_clicked(self, widget):
		print "ToggleButton2 Clicked"

	def onToggleButtonConnectTunel_clicked(self, widget):
		selectCombo1 = self.builder.get_object("selectCombo1")

		if widget.get_active():
			selectCombo1.set_sensitive(False)

			user   = ConfigLoader.preferences['credentials']['sshUsername']
			sshKey = ConfigLoader.preferences['credentials']['sshPrivateKey']

			command = ''
			for target in ConfigLoader.preferences['tunnelList'][selectCombo1.get_active()]['path']:
				command = command + ' -L ' + target['originPort'] + ':' + target['targetHost'] + ':' + target['destPort']

			self.sshProcess = subprocess.Popen('ssh -i ' + sshKey + ' ' + user + command, shell=True)
		else:

			if self.sshProcess is not None:
				WidgetHandlers.kill_process_tree(self.sshProcess.pid)
				self.sshProcess = None
			selectCombo1.set_sensitive(True)

	def onButtonRepository_clicked(self, widget):
		print "Button1 Clicked"
