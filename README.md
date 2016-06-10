LSL/OSSL Bundle for Sublime Text
==========

* [Current supported language](#current-supported-language)
* [Features](#features)
* [Syntax Indentation](#syntax-indentation)
* [Installation](#installation)
* [Using Sublime Package Control](#using-sublime-package-control)
* [Using Git](#using-git)
* [Download Manually](#download-manually)
* [Additional Features](#additional-features)
* [Second Life Viewer Theme](#second-life-viewer-theme)
* [Changing Snippet Insertion Style](#changing-snippet-insertion-style)
* [lslint Build System](#lslint-build-system)
* [non-ascii system issue](#non-ascii-system-issue)
* [About Keyword Database](#about-keyword-database)

# Current supported language

* LSL [\*.lsl]: Second Life 16.05.24.315768
* OSSL [\*.ossl]: OpenSimulator v0.7.5-rc1
  - Including mod\*, os\*, wl\*(LightShare) functions

[kwdb](https://bitbucket.org/Sei_Lisa/kwdb) version 0.0.20160606000

**I try to update the keyword list as soon as it is updated by kwdb, however, I sometimes may not be able to do that. Please refrain from requesting maintenance for at least one month after the kwdb have higher version than the version above. If you want to make an urgent request, please poke me via [@makopo](https://www.twitter.com/makopo) on Twitter or send an inworld IM to [Mako Nozaki](https://my.secondlife.com/mako.nozaki).**

# Features

* More quick completion of functions & events.
* Stricter syntax detection - if you miss something, the rest will be colored oddly.
* You can even use Second Life Viewer styled theme.
* Compatible with [TextMate scoping rules](http://manual.macromates.com/en/language_grammars#naming_convertions).
* [lslint](https://github.com/Makopo/lslint) as build system(<kbd>F7</kbd>, <kbd>Ctrl</kbd><kbd>B</kbd> or <kbd>Command</kbd><kbd>B</kbd>).
* No Commands, no Macros, no Templates ...

# Syntax Indentation

* [Allman Style](http://en.wikipedia.org/wiki/Indent_style#Allman_style) (default)
* [K&R Style](http://en.wikipedia.org/wiki/Indent_style#K.26R_style)

See [LSL Style Guide](http://wiki.secondlife.com/wiki/LSL_Style_Guide) for coding samples.
(method one = K&R Style, method two = Allman style)

# Installation

This bundle is designed to work with the latest version of [Sublime Text 2](http://www.sublimetext.com/2).

[v1.3.2](https://github.com/makopo/sublime-text-lsl/releases/tag/1.3.2) or later will work with [Sublime Text 3](http://www.sublimetext.com/3) as well.

### Using Sublime Package Control

The easiest way to install this is via [Package Control](https://sublime.wbond.net).

 * If you just went and installed Package Control, you probably need to restart Sublime Text before doing this next bit.
 * Bring up the Command Palette (<kbd>Command</kbd><kbd>Shift</kbd><kbd>P</kbd> on OS X, <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Type and select "LSL" when the list appears.

Package Control will automatically keep LSL/OSSL Bundle up to date with the latest version.

### Using Git

Alternatively, if you are a git user, you can install the plugin and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text application settings area.

You can locate your Sublime Text `Packages` directory by using the menu item `Preferences -> Browse Packages...`.

While inside the `Packages` directory, clone the plugin repository using the command below:

    git clone https://github.com/Makopo/sublime-text-lsl LSL

### Download Manually

* Download the files using the GitHub [*.zip](https://github.com/makopo/sublime-text-lsl/archive/master.zip) and [*.tar.gz](https://github.com/makopo/sublime-text-lsl/archive/master.tar.gz) download options.
* Unzip the files and rename the folder to `LSL`.
* Copy the folder to your Sublime Text `Packages` directory.

## Additional Features

### Second Life Viewer Theme

You can use the bundled theme for only .lsl or .ossl files to the same look-and-feel with inworld editor.

To activate it, use the menu item `Preferences -> Package Settings -> LSL/OSSL -> Use Viewer Theme`.

The same steps to deactivate it.

Note that you need to have this bundle in "LSL" package directory to use it.

### Changing Snippet Insertion Style

You can change insertion style of snippets from default Allman style to K&R style.

To activate it, use the menu item `Preferences -> Package Settings -> LSL/OSSL -> K&R Style`.

The same steps to deactivate it.

### lslint Build System

You can run lslint as LSL/OSSL build system.

lslint is originated by http://w-hat.com.

I added some features on it for use as build command in Sublime Text.
https://github.com/Makopo/lslint

Simply hit <kbd>F7</kbd> or <kbd>Ctrl</kbd><kbd>B</kbd> or <kbd>Command</kbd><kbd>B</kbd> to check the syntax of currently opened lsl/ossl script.

Currently it is not supported for os/mod/wl functions.

If you want to change the key bindings, use "build" command for it in your Default.sublime-keymap. Following example assigns <kbd>Command</kbd><kbd>L</kbd> to lslint.

```json
[
	{
		"keys": ["super+l"],
		"command": "build",
		"context":[
			{ "key": "selector", "operator": "equal", "operand": "source.lsl" }
		]
	},
	{
		"keys": ["super+l"],
		"command": "build",
		"context":[
			{ "key": "selector", "operator": "equal", "operand": "source.ossl" }
		]
	}
]
```


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

This bundle uses [kwdb](https://bitbucket.org/Sei_Lisa/kwdb) as source of its LSL/OSSL funcion/event/constant names. The LSL/OSSL keywords in .tmLanguage and .sublime-completions are automatically generated from the file kwdb.xml within. I have the automation tool in [another project(kwdb_to_sublime)](https://github.com/Makopo/kwdb_to_sublime). Thus, if you find any flaw in the keywords, please first search for the keyword you want to use in `kwdb.xml`. Then compare kwdb version at the top of this readme to that in `kwdb.xml`. If you find mine is way behind of `kwdb.xml`, please be patient or poke me [@makopo](https://www.twitter.com/makopo) on Twitter or send an inworld IM to [Mako Nozaki](https://my.secondlife.com/mako.nozaki).
