LSL/OSSL Bundle for Sublime Text
==========

# Current supported language

* LSL [\*.lsl]: Second Life 18.11.02.521379
* OSSL [\*.ossl]: OpenSimulator v0.9.0.0-rc2
  - Including mod\*, os\*, wl\*(LightShare) functions

[kwdb](https://bitbucket.org/Sei_Lisa/kwdb) version 0.0.20181208000

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

* Download the files using the GitHub [\*.zip](https://github.com/makopo/sublime-text-lsl/archive/master.zip) or [\*.tar.gz](https://github.com/makopo/sublime-text-lsl/archive/master.tar.gz) download options.
* Unzip the files and rename the folder to `LSL`.
* Copy the folder to your Sublime Text `Packages` directory.

# Upgrade

**I try to update the keyword list as soon as it is updated by kwdb, however, I sometimes may not be able to do that. Please refrain from requesting maintenance for at least one month after the kwdb have higher version than the version above. If you want to make an urgent request, please poke me via [@makopo](https://www.twitter.com/makopo) on Twitter or send an inworld IM to [Mako Nozaki](https://my.secondlife.com/mako.nozaki).**

### Using Sublime Package Control

Having `auto_upgrade` option in your setting file, or due to some other cause, Packate Control may not upgrade this package. If you feel your version is behind, try to upgrade it:

 * Bring up the Command Palette (<kbd>Command</kbd><kbd>Shift</kbd><kbd>P</kbd> on OS X, <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> on Linux/Windows).
 * Select "Package Control: Upgrade Package" (it'll take a few seconds)
 * Type and select "LSL" when the list appears.

### Download Manually

Since nothing will take care of your version, you will need to maintain it by yourself. Simply re-download the [\*.zip](https://github.com/makopo/sublime-text-lsl/archive/master.zip) or [\*.tar.gz](https://github.com/makopo/sublime-text-lsl/archive/master.tar.gz) and overwrite it in the `Packages` directory.


# Additional Features

## Second Life Viewer Theme

You can use the bundled theme for only .lsl or .ossl files to the same look-and-feel with inworld editor.

To activate it, use the menu item `Preferences -> Package Settings -> LSL/OSSL -> Use Viewer Theme`.

The same steps to deactivate it.

Note that you need to have this bundle in "LSL" package directory to use it.

## Changing Snippet Insertion Style

You can change insertion style of snippets from default Allman style to K&R style.

To activate it, use the menu item `Preferences -> Package Settings -> LSL/OSSL -> K&R Style`.

The same steps to deactivate it.

## lslint Build System

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

## Using other build systems for dialects

You can use other build systems than lslint for some dialects.

### LSL-PyOptimizer

You can use [LSL-PyOptimizer](http://lsl.blacktulip-virtual.com/lsl-pyoptimizer/) for optimizing your lsl code.

Navigate `Tools` -> `Build System` -> `New Build System...` and edit the newly created file like that:

For windows:
```
{
    "file_regex": "^::[A-Z]++::\"((?:\\\\.|[^\"\\\\])*+)\":(\\d++):(\\d++): (.*+)",
    "selector": "source.lsl",
    "cmd": ["C:\\Python27\\python.exe", "PYOPTIMIZER_PATH\\main.py", "--emap", "--bom", "$file", "-o", "$file_path/${file_base_name}_optimized.$file_extension"],
    "env": 
    {
        "PYTHONIOENCODING": "utf-8"
    }
}
```

For osx:
```
{
    "file_regex": "^::[A-Z]++::\"((?:\\\\.|[^\"\\\\])*+)\":(\\d++):(\\d++): (.*+)",
    "selector": "source.lsl",
    "cmd": ["python2.7", "PYOPTIMIZER_PATH/main.py", "--emap", "--bom", "$file", "-o", "$file_path/${file_base_name}_optimized.$file_extension"],
    "env": 
    {
        "PYTHONIOENCODING": "utf-8"
    }
}
```

* These samples assume that LSL-PyOptimizer revision is 7282e53 (Feb 5, 2019) or later.
* In this example, output will be created as `SOURCE_FILE_NAME_optimized.SOURCE_EXTENSION`.
* [Official document](http://lsl.blacktulip-virtual.com/lsl-pyoptimizer/) says you need to use Python 2.7.
* Outputs are streamed as utf-8 so you need `PYTHONIOENCODING` environment variable to successfully decode them.

Save this file as `LSL-PyOptimizer.sublime-build`.

Now you'll find `LSL-PyOptimizer` in `Tools` -> `Build System`.

Select `Tools` -> `Build With...`(<kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>B</kbd> or <kbd>Command</kbd><kbd>Shift</kbd><kbd>B</kbd>) and choose `LSL-PyOptimizer`.

From now on, your source will be compiled with LSL-PyOptimizer. `Tools` -> `Build With...` again to switch back to lslint.

## LSL/OSSL sidebar icons

Starting from Sublime Text 3062, you can assign file icons on the sidebar. However, since this plugin is not a theme, I can't provide this feature, instead you can assign your favorite icon to LSL/OSSL entries by yourself.

In short: scope "source.lsl" for LSL and "source.ossl" for OSSL.

1. Create or fetch a 16x16 image. FYI, you can find SecondLife icons in [BitBucket repository](https://bitbucket.org/lindenlab/viewer-release/src/5b51b28e057c/indra/newview/icons/release/?at=default).
2. Rename the image to "file_type_lsl.png".
3. You can even add secondary 32x32 image as "file_type_lsl@2x.png". I don't know how it will be used though.
4. Create a file "icon_lsl.tmPreferences" with the following contents.
5. Put the file above and PNG image(s) into your active theme folder.

icon_lsl.tmPreferences:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
      <key>scope</key>
      <string>source.lsl</string>
      <key>settings</key>
      <dict>
          <key>icon</key>
          <string>file_type_lsl</string>
      </dict>
  </dict>
</plist>
```

For ossl, put 16x16 "file_type_ossl.png" and "icon_ossl.tmPreferences" with scope "source.ossl" into the theme folder.

## API Reference Tooltip

Starting from Sublime Text 3070, you can look in the API reference by context meny on the keywords.
Due to performance overhead, I created anothe plugin "TooltipLSL". The project is [here](https://github.com/Makopo/sublime-text-tooltip-lsl).

In short, install "TooltipLSL" with Package Control, then place the caret on functions/constants/events before choosing "Show LSL Reference" from the right-click context menu.

# About Keyword Database

This bundle uses [kwdb](https://bitbucket.org/Sei_Lisa/kwdb) as source of its LSL/OSSL funcion/event/constant names. The LSL/OSSL keywords in .tmLanguage and .sublime-completions are automatically generated from the file kwdb.xml within. I have the automation tool in [another project(kwdb_to_sublime)](https://github.com/Makopo/kwdb_to_sublime). Thus, if you find any flaw in the keywords, please first search for the keyword you want to use in `kwdb.xml`. Then compare kwdb version at the top of this readme to that in `kwdb.xml`. If you find mine is way behind of `kwdb.xml`, please be patient or poke me [@makopo](https://www.twitter.com/makopo) on Twitter or send an inworld IM to [Mako Nozaki](https://my.secondlife.com/mako.nozaki).
