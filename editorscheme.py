import sublime, sublime_plugin

class ChangeEditorSchemeCommand(sublime_plugin.WindowCommand):
	_is_checked = False

	def __init__(self, view):
		sl = sublime.load_settings("lsl.sublime-settings")
		ossl = sublime.load_settings("ossl.sublime-settings")
		self._is_checked = sl.has("color_scheme")
		if self._is_checked:
			sl.set("color_scheme", "Packages/LSL/lsl.hidden-tmTheme")
			ossl.set("color_scheme", "Packages/LSL/lsl.hidden-tmTheme")
		else:
			sl.erase("color_scheme")
			ossl.erase("color_scheme")
		sublime.save_settings("lsl.sublime-settings")
		sublime.save_settings("ossl.sublime-settings")

	def run(self):
		sl = sublime.load_settings("lsl.sublime-settings")
		ossl = sublime.load_settings("ossl.sublime-settings")
		if not self._is_checked:
			sl.set("color_scheme", "Packages/LSL/lsl.hidden-tmTheme")
			ossl.set("color_scheme", "Packages/LSL/lsl.hidden-tmTheme")
		else:
			sl.erase("color_scheme")
			ossl.erase("color_scheme")
		sublime.save_settings("lsl.sublime-settings")
		sublime.save_settings("ossl.sublime-settings")
		self._is_checked = not self._is_checked

	def is_checked(self):
		return self._is_checked

