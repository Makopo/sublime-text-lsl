LSL Syntax File for Sublime Text 2
==========

# Current compatible version

* LSL : Second Life V3.4.0
* OSSL: Not yet supported

# Syntax Indentation

Based on LSL Style Guide in [Second Life Wiki](http://wiki.secondlife.com/wiki/LSL_Style_Guide) (method two).

# Features

* More quick completion of functions & events.
* More strict syntax detection - if you miss something, the rest will colored oddly.
* Compatible with [TextMate scoping rules](http://manual.macromates.com/en/language_grammars#naming_convertions).
* No too-old lslint support, no Commands, no Macros, no Templates ... 

# In Future ...

* OSSL support
* LSL Style Guide (method one) support
* Inworld LSL editor Look & Feel theme

# Installation

## Package Control

The easiest way to install this is with [Package Control](http://wbond.net/sublime\_packages/package\_control).

 * If you just went and installed Package Control, you probably need to restart Sublime Text 2 before doing this next bit.
 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Add Repository" and then type "https://github.com/Makopo/sublime-text-lsl.git" in the bottom textfield.
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Select "sublime-text-lsl"(not sublime-text2-lsl) when the list appears.

Package Control will automatically keep Git up to date with the latest version.

## More complex methods

First, you need to have `git` installed and in your `$PATH`. Afterwards you may need to restart Sublime Text 2 before the plugin will work.

### OSX

    $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    $ git clone git://github.com/kemayo/sublime-text-2-git.git Git

### Linux (Ubuntu like distros)

    $ cd ~/.config/sublime-text-2/Packages/
    $ git clone git://github.com/kemayo/sublime-text-2-git.git Git

### Windows 7:

    Copy the directory to: "C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages"

### Windows XP:

    Copy the directory to: "C:\Documents and Settings\<username>\Application Data\Sublime Text 2\Packages"