import sublime, sublime_plugin, os

class ChangeEditorSchemeCommand(sublime_plugin.WindowCommand):
	_is_checked = False

	def __init__(self, view):
		s = sublime.load_settings("lsl.sublime-settings")
		self._is_checked = s.has("color_scheme")

	def run(self):
		s = sublime.load_settings("lsl.sublime-settings")
		if not self._is_checked:
			s.set("color_scheme", os.path.abspath(os.path.dirname(__file__)) + "/LLViewer.tmTheme")
		else:
			s.erase("color_scheme")
		sublime.save_settings("lsl.sublime-settings")
		self._is_checked = not self._is_checked

	def is_checked(self):
		return self._is_checked

