# Jellyfy

A simple script that tries to format filenames into Jellyfin's expected structure.

example: Title of Movie (2015)

Still WIP

## Compile

```powershell
pyinstaller jellyfy.py -Fw
```

The "w" flag hides the console window when running from the .exe

## Example right-click menu setup for Windows

This script can be added to Windows right-click menu both for files and folders if desired.

Save this to a .reg file and run it after changing the paths.

```reg
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\RenameFiles]
@="Rename Files"
"Icon"="C:\\path\\to\\icon.ico"

[HKEY_CLASSES_ROOT\*\shell\RenameFiles\command]
@="C:\\path\\to\\rename_files.exe \"%1\""

[HKEY_CLASSES_ROOT\Folder\shell\RenameFiles]
@="Rename Files"
"Icon"="C:\\path\\to\\icon.ico"

[HKEY_CLASSES_ROOT\Folder\shell\RenameFiles\command]
@="C:\\path\\to\\rename_files.exe \"%1\""
```
