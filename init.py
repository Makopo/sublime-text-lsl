import os
import stat
import sublime

def chmod_lslint():
	# add permissions to lslint executables
	binaryPath = os.path.join(sublime.packages_path(), "LSL/support/build/osx/lslint")
	os.chmod(binaryPath, stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)
	binaryPath = os.path.join(sublime.packages_path(), "LSL/support/build/linux/lslint")
	os.chmod(binaryPath, stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)

# When Sublime Text 2, we can use any sublime API during initialization.
if sublime.version().startswith('2'):
	chmod_lslint()

# When Sublime Text 3, we can't until they are ready to use.
def plugin_loaded():
	chmod_lslint()
