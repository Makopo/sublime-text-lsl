LSL/OSSL Bundle for Sublime Text 2
==========

# Current supported language

* LSL [\*.lsl]: Second Live Server 13.04.12.273874 (Second Life RC Magnum 13.04.19.274352)
* OSSL [\*.ossl]: OpenSimulator v0.7.5 and dev master r/22626(25th April, 2013)
  - Including mod\*, os\*, wl\*(LightShare) functions

# Features

* More quick completion of functions & events.
* More strict syntax detection - if you miss something, the rest will colored oddly.
* You can even use Second Life Viewer styled theme.
* Compatible with [TextMate scoping rules](http://manual.macromates.com/en/language_grammars#naming_convertions).
* lslint as build system(Command + B). **New!**
* No Commands, no Macros, no Templates ... 

# Syntax Indentation

* BSD Style (default)
* K&R Style

See [LSL Style Guide](http://wiki.secondlife.com/wiki/LSL_Style_Guide) for coding samples.
(method one = K&R Style, method two = BSD style)

# Installation

This bundle is designed to work with the latest Sublime Text 2.

### Using Sublime Package Control

The easiest way to install this is with [Package Control](http://wbond.net/sublime\_packages/package\_control).

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

If you have lsl/ossl script in the path conatins non-ascii (eg. UTF-8) characters, the check may fail.

You may workaround this issue by replacing line 130 in "Packages/Default/exec.py".

```python
            def foo(element):
                try:
                    element = element.encode(self.encoding)
                except UnicodeDecodeError:
                    pass
                return element
            print "Running " + " ".join(map(foo, cmd))
```
