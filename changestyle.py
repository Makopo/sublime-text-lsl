import sublime, sublime_plugin
import os
import shutil
import plistlib

class ChangeStyleCommand(sublime_plugin.WindowCommand):
	_is_checked = False

	def __init__(self, view):
		srcdir = os.path.join(sublime.packages_path(), "LSL/preferences")
		destdir = os.path.join(sublime.packages_path(), "User")
		destfile = os.path.join(destdir, "lsl_settings_style.tmPreferences")
		if os.path.exists(destfile):
			pl = plistlib.readPlist(destfile)
			self._is_checked = (pl['uuid'] == "a775771f-1a8d-4741-a1a3-6f6dc0b01ab4")
		else:
			shutil.copyfile(os.path.join(srcdir, "settings_style.tmPreferences.allman"), destfile)

	def run(self):
		srcdir = os.path.join(sublime.packages_path(), "LSL/preferences")
		destdir = os.path.join(sublime.packages_path(), "User")
		destfile = os.path.join(destdir, "lsl_settings_style.tmPreferences")
		if not self._is_checked:
			shutil.copyfile(os.path.join(srcdir, "settings_style.tmPreferences.kandr"), destfile)
		else:
			shutil.copyfile(os.path.join(srcdir, "settings_style.tmPreferences.allman"), destfile)
		self._is_checked = not self._is_checked

	def is_checked(self):
		return self._is_checked
