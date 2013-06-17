import os
import stat
import sublime

# add permissions to lslint executables
binaryPath = os.path.join(sublime.packages_path(), "LSL/osx/lslint")
os.chmod(binaryPath, stat.S_IEXEC)
binaryPath = os.path.join(sublime.packages_path(), "LSL/linux/lslint")
os.chmod(binaryPath, stat.S_IEXEC)
