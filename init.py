import os
import stat
import sublime

# add permissions to lslint executables
binaryPath = os.path.join(sublime.packages_path(), "LSL/osx/lslint")
os.chmod(binaryPath, stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)
binaryPath = os.path.join(sublime.packages_path(), "LSL/linux/lslint")
os.chmod(binaryPath, stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)
