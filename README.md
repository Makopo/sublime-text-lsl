LSL Bundle for Sublime Text 2
==========

# Current compatible version

* LSL : Second Life V3.4.0
* OSSL: Not yet supported

# Syntax Indentation

Based on LSL Style Guide in [Second Life Wiki](http://wiki.secondlife.com/wiki/LSL_Style_Guide) (method two).

# Features

* More quick completion of functions & events.
* More strict syntax detection - if you miss something, the rest will colored oddly.
* You can even use Second Life Viewer styled theme. **New!**
* Compatible with [TextMate scoping rules](http://manual.macromates.com/en/language_grammars#naming_convertions).
* No too-old lslint support, no Commands, no Macros, no Templates ... 

# In Future ...

* OSSL support
* LSL Style Guide (method one) support

# Installation

This bundle is designed to work with the latest Sublime Text 2.

### Using Sublime Package Control

The easiest way to install this is with [Package Control](http://wbond.net/sublime\_packages/package\_control).

 * If you just went and installed Package Control, you probably need to restart Sublime Text 2 before doing this next bit.
 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Add Repository" and then type following in the bottom textfield.

```
https://raw.github.com/Makopo/sublime-text-lsl/master/package.json
```

 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Type and select "LSL" when the list appears.

Package Control will automatically keep LSL Bundle up to date with the latest version.

### Using Git

Alternatively, if you are a git user, you can install the theme and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text 2 application settings area.

You can locate your Sublime Text 2 `Packages` directory by using the menu item `Preferences -> Browse Packages...`.

While inside the `Packages` directory, clone the theme repository using the command below:

    git clone https://github.com/Makopo/sublime-text-lsl LSL

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `LSL`
* Copy the folder to your Sublime Text 2 `Packages` directory

## Additional Features

### Second Life Viewer Theme

You can use the bundled theme for only .lsl files to the same look-and-feel with inworld editor.

To activate it, use the menu item `Preferences -> Package Settings -> LSL -> Use Viewer Theme`.

The same steps to deactivate it.

Note that you need to have this bundle in "LSL" package directory to use it.

