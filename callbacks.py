#!/usr/bin/env python

from gi.repository import Gtk

class Callbacks:

	def exit_application(self, widget):
		Gtk.main_quit()

	def about_application(self, widget):
		print "developers: { rochapaulo, oliveirasevandro }"
