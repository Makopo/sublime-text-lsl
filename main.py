import os
import plistlib
import shutil
import stat
import sublime
import sublime_plugin
from time import time
import webbrowser
import xml.etree.ElementTree as etree

Pref = None
KWDB = None

if sublime.version().startswith('2'):
    chmod_lslint()

if 3070 <= int(sublime.version()):
    import mdpopups

def plugin_loaded():
    global Pref
    global KWDB

    class Pref:
        def load(self):
            Pref.next_run = time() + 0.0009*400

    Pref = Pref()
    Pref.load()

    binaryPath = os.path.join(sublime.packages_path(), 'LSL', 'osx', 'lslint')
    os.chmod(binaryPath, stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)
    binaryPath = os.path.join(sublime.packages_path(), 'LSL', 'linux', 'lslint')
    os.chmod(binaryPath, stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)

    kwdbElementTree = etree.parse(os.path.join(sublime.packages_path(), 'LSL', 'kwdb', 'kwdb.xml'))
    KWDB = kwdbElementTree.getroot()

class ChangeStyleCommand(sublime_plugin.WindowCommand):
    _is_checked = False

    def __init__(self, view):
        srcdir = os.path.join(sublime.packages_path(), 'LSL')
        destdir = os.path.join(sublime.packages_path(), 'User')
        destfile = os.path.join(destdir, 'lsl_settings_style.tmPreferences')

        if os.path.exists(destfile):
            pl = plistlib.readPlist(destfile)
            self._is_checked = (pl['uuid'] == 'a775771f-1a8d-4741-a1a3-6f6dc0b01ab4')
        else:
            shutil.copyfile(os.path.join(srcdir, 'settings_style.tmPreferences.allman'), destfile)

    def run(self):
        srcdir = os.path.join(sublime.packages_path(), 'LSL')
        destdir = os.path.join(sublime.packages_path(), 'User')
        destfile = os.path.join(destdir, 'lsl_settings_style.tmPreferences')

        if not self._is_checked:
            shutil.copyfile(os.path.join(srcdir, 'settings_style.tmPreferences.kandr'), destfile)
        else:
            shutil.copyfile(os.path.join(srcdir, 'settings_style.tmPreferences.allman'), destfile)

        self._is_checked = not self._is_checked

    def is_checked(self):
        return self._is_checked

class ChangeEditorSchemeCommand(sublime_plugin.WindowCommand):
    _is_checked = False

    def __init__(self, view):
        sl = sublime.load_settings('lsl.sublime-settings')
        ossl = sublime.load_settings('ossl.sublime-settings')
        self._is_checked = sl.has('color_scheme')

        if self._is_checked:
            sl.set('color_scheme', 'Packages/LSL/lsl.hidden-tmTheme')
            ossl.set('color_scheme', 'Packages/LSL/lsl.hidden-tmTheme')
        else:
            sl.erase('color_scheme')
            ossl.erase('color_scheme')

        sublime.save_settings('lsl.sublime-settings')
        sublime.save_settings('ossl.sublime-settings')

    def run(self):
        sl = sublime.load_settings('lsl.sublime-settings')
        ossl = sublime.load_settings('ossl.sublime-settings')

        if not self._is_checked:
            sl.set('color_scheme', 'Packages/LSL/lsl.hidden-tmTheme')
            ossl.set('color_scheme', 'Packages/LSL/lsl.hidden-tmTheme')
        else:
            sl.erase('color_scheme')
            ossl.erase('color_scheme')

        sublime.save_settings('lsl.sublime-settings')
        sublime.save_settings('ossl.sublime-settings')
        self._is_checked = not self._is_checked

    def is_checked(self):
        return self._is_checked

class LslCommand(sublime_plugin.EventListener):

    def on_activated(self, view):
        if 3070 <= int(sublime.version()):
            self.run(view)

    def on_modified(self, view):
        if 3070 <= int(sublime.version()):
            self.run(view)

    def on_selection_modified(self, view):
        if 3070 <= int(sublime.version()):
            self.run(view)

    def run(self, view):
        Pref.next_run = time() + 0.0009*400
        sublime.set_timeout(lambda:self.run_after_delay(view), 400)

    def run_after_delay(self, view):
        if Pref.next_run <= time():
            self.show_tooltip(view)

    def show_tooltip(self, view):
        region = view.sel()[0]
        scope  = view.scope_name(region.a)

        validScopes = []
        validScopes.append('source.lsl')

        validScope_Found = False

        for validScope in validScopes:
            if sublime.score_selector(scope, validScope) != 0:
                validScope_Found = True

        if validScope_Found == False:
            return

        viewSettings = view.settings()

        if viewSettings.get('is_widget'):
            return

        if not KWDB:
            return

        word = view.substr(view.word(region))
        try:
            tooltipRows = []
            for result in KWDB.findall(".//*[@name='" + word + "']"):
                if result.tag == 'param':
                    continue
                if result.tag == 'function' or result.tag == 'constant':
                    tooltipRows.append('### (%s) <a href="https://wiki.secondlife.com/w/index.php?title=Special:Search&go=Go&search=%s">%s</a>' % (result.get('type', 'void'), result.get('name'), result.get('name')))
                else:
                    tooltipRows.append('### <a href="https://wiki.secondlife.com/w/index.php?title=Special:Search&go=Go&search=%s">%s</a>' % (result.get('name'), result.get('name')))
                if result.tag == 'constant':
                    tooltipRows.append(' ')
                    tooltipRows.append('**Value**: %s' % str(result.get('value')))
                if result.get('status', None) is not None and result.get('status', 'normal') != 'normal':
                    tooltipRows.append(' ')
                    tooltipRows.append('<body style="color:#fff;background-color:#820124;">**Status**: %s</body>' % result.get('status', 'normal'))
                if result.get('delay', None) is not None:
                    tooltipRows.append(' ')
                    tooltipRows.append('**Delay**: %s' % str(result.get('delay')))
                if result.get('energy', None) is not None:
                    tooltipRows.append(' ')
                    tooltipRows.append('**Energy**: %s' % str(result.get('energy')))
                if result.tag == 'function' or result.tag == 'event':
                    if result.findall('./param') != []:
                        tooltipRows.append(' ')
                        tooltipRows.append('#### Parameters')
                        for param in result.iter('param'):
                            tooltipRows.append('* (%s) **%s**' % (param.get('type'), param.get('name')))
                if result.find('description').text is not None:
                    tooltipRows.append(' ')
                    tooltipRows.append('#### Description')
                    tooltipRows.append(' ')
                    tooltipRows.append('%s' % result.find('description').text.strip())

#               add version info
#               add grid info by splitting spaces and re-joining as markdown list
#          seperate entries by horizontal line

            if len(tooltipRows) == 0:
                return

            mdpopups.show_popup(view, '\n'.join(tooltipRows),
                flags=sublime.COOPERATE_WITH_AUTO_COMPLETE,
                location=-1, max_width=600, max_height=350,
                on_navigate=self.on_navigate
            )
            return

        except Exception as e:
            print(e)

        mdpopups.hide_popup(view)

    def on_navigate(self, link):
        webbrowser.open_new_tab(link)
