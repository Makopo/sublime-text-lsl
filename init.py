import os
import sublime

# add permissions to lslint executables
binaryPath = os.path.join(sublime.packages_path(), "LSL/osx/lslint")
os.chmod(binaryPath, 0755)
binaryPath = os.path.join(sublime.packages_path(), "LSL/linux/lslint")
os.chmod(binaryPath, 0755)
