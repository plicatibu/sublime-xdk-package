sublime-xdk-package
===================

This repo contains a package for the [Sublime Text editor][1] that allows you to
direct several key Intel XDK activities, including:

[1]: <http://www.sublimetext.com>

-   Starting your app in the Emulate tab.

-   Updating your app for use with the Test tab and App Preview.

-   Starting and stopping your app on an attached device with the Debug tab.

-   Launching and starting memory and CPU profiling on the Profile tab.

All of these actions can be activated directly from within your Sublime Text
edit window using either keyboard shortcuts or a special Intel XDK menu from
within the editor.

Installation
------------

Extract the “XDK” folder into your Sublime Text plugin folder and restart
Sublime Text. [Follow this link to download a ZIP file][2] of the plugin.

[2]: <https://github.com/gomobile/sublime-xdk-package/archive/master.zip>

The Sublime Text plugins folders are usually located in the following places:

-   Windows:  
    `"%AppData%\Sublime Text X\Packages"`  
    where 'X' is ‘2' or ‘3' depending on the version of your Sublime Text
    editor.

-   Mac OS X:  
    `~/Library/Application\ Support/Sublime\ Text\ X/Packages`  
    where ‘X' is ‘2' or ‘3' depending on the version of your Sublime Text
    editor.

-   Linux:  
    usually `~/.Sublime\ Text\ X/Packages`  
    where ‘X' is ‘2' or ‘3', but may vary.

    If you installed Sublime Text via `apt-get`, the Packages folder may be
    located here: `/opt/sublime_text/Packages` on your system.

    If you cannot find the `Packages` folder, try the following command:
    `$ sudo find / -name Packages -type d`

    On a Linux machine you may need to convert the XDK folder into a Sublime
    Text package. Sublime Text packages are simply ZIP archives with the 
    extension `.sublime-package`
    
```
    $ zip -b . XDK.sublime-package ./XDK/*
    $ sudo cp XDK.sublime-package /opt/sublime_text/Packages
```
Most of the features of this plugin require that the Intel XDK is running on the
same system as your Sublime Text editor, and that you are logged into the Intel
XDK.

If you wish to report a bug, please include any log messages from Sublime Text
in your bug report and post your issue on the [Intel XDK forum][3]. To view log
messages you can open the Sublime Text console using Ctrl+\` or View -\> Show
Console. The last 10 lines are generally enough.

[3]: <http://software.intel.com/en-us/forums/intel-xdk>

Detailed Instructions
---------------------

under construction… more to be provided.
