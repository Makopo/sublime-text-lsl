LSL/OSSL Bundle for Sublime Text
==========

# Current supported language

* LSL [\*.lsl]: Second Life 13.06.21.277682
* OSSL [\*.ossl]: OpenSimulator v0.7.5-rc1
  - Including mod\*, os\*, wl\*(LightShare) functions

kwdb version 0.0.20130627001

**I try to update the keyword list as soon as kwdb update them, however, I sometimes may not be able to do that. Please refrain from requesting maintenance for at least 1 month after the kwdb have higher version than the version above. If you want to make an urgent request, please use Twitter @makopo or SL inworld IM to Mako Nozaki.**

# Features

* More quick completion of functions & events.
* More strict syntax detection - if you miss something, the rest will colored oddly.
* You can even use Second Life Viewer styled theme.
* Compatible with [TextMate scoping rules](http://manual.macromates.com/en/language_grammars#naming_convertions).
* lslint as build system(Command + B).
* No Commands, no Macros, no Templates ... 

# Syntax Indentation

* BSD Style (default)
* K&R Style

See [LSL Style Guide](http://wiki.secondlife.com/wiki/LSL_Style_Guide) for coding samples.
(method one = K&R Style, method two = BSD style)

# Installation

This bundle is designed to work with the latest Sublime Text 2.
v1.3.2 or later works with the latest Sublime Text 3 as well.

### Using Sublime Package Control

The easiest way to install this is with [Package Control](https://sublime.wbond.net).

 * If you just went and installed Package Control, you probably need to restart Sublime Text 2 before doing this next bit.
 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Type and select "LSL" when the list appears.

Package Control will automatically keep LSL/OSSL Bundle up to date with the latest version.

### Using Git

Alternatively, if you are a git user, you can install the plugin and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text 2 application settings area.

You can locate your Sublime Text 2 `Packages` directory by using the menu item `Preferences -> Browse Packages...`.

While inside the `Packages` directory, clone the plugin repository using the command below:

    git clone https://github.com/Makopo/sublime-text-lsl LSL

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `LSL`
* Copy the folder to your Sublime Text 2 `Packages` directory

## Additional Features

### Second Life Viewer Theme

You can use the bundled theme for only .lsl or .ossl files to the same look-and-feel with inworld editor.

To activate it, use the menu item `Preferences -> Package Settings -> LSL/OSSL -> Use Viewer Theme`.

The same steps to deactivate it.

Note that you need to have this bundle in "LSL" package directory to use it.

### Changing Snippet Insertion Style

You can change insertion style of snippets from default BSD style to K&R style.

To activate it, use the menu item `Preferences -> Package Settings -> LSL/OSSL -> K&R Style`.

The same steps to deactivate it.

### lslint Build System

You can run lslint as LSL/OSSL build system.

lslint is originated by http://w-hat.com.

I added some features on it for use as build command in Sublime Text.
https://github.com/Makopo/lslint

Simply hit Command + B to check the syntax of currently opened lsl/ossl script.

Currently it is not supported for os/mod/wl functions.

#### non-ascii system issue

If you have lsl/ossl script in the path conatins non-ascii (eg. UTF-8) characters, the check may fail.

You might want to avoid placing your scripts in such a path, or if you can't,

You may workaround this issue by inserting a line after line 99 in "Packages/Default/exec.py".

```python
        cmd = [c.encode(sys.getfilesystemencoding()) for c in cmd]
```

Additionally if your system encoding isn't UTF-8, you may need to modify "Packages/LSL/LSL.sublime-build".

```python
	"windows":
	{
		"encoding": "cp932",
		"cmd": ["$packages\\LSL\\windows\\lslint.exe", "-p", "$file"]
	},
```

This example above is for Japanese version of Windows. Change the corresponding block(windows/linux/osx) with your environment.

## About Keyword Database

This bundle uses [kwdb](https://code.google.com/p/kwdb/) as the source of LSL/OSSL funcion/event/constant names. The LSL/OSSL keywords in .tmLanguage and .sublime-completions are automatically generated from kwdb.xml in kwdb. I have the automation tool in [another project(kwdb_to_sublime)](https://github.com/Makopo/kwdb_to_sublime). Thus, if you find any flaw in the keyword, please firstly search for the keyword you want to use in [kwdb.xml](https://code.google.com/p/kwdb/source/browse/database/kwdb.xml). Then compare kwdb version at the top of this readme with that in kwdb.xml. If you find mine is way behind of kwdb.xml, please be patient or poke me @makopo in Twitter or send an inworld IM to Mako Nozaki.

