# MACROPAD Hotkeys example: Visual Studio Code for macOS

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                     # REQUIRED dict, must be named 'app'
    'name' : 'Mac VS Code', # Application name
    'macros' : [            # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Debug', [Keycode.F5]), # Start debug
        (0x000040, 'Cmd', [Keycode.F1]),   # Open command pallette
        (0x004040, 'Open', [Keycode.COMMAND, 'p']), # Open a file
        # 2nd row ----------
        (0x004000, 'Stop', [Keycode.F5]), # Stop debug
        (0x4C0099, 'Settings', [Keycode.COMMAND, ',']), # View settings
        (0x004040, 'Path', [Keycode.COMMAND, 'k', -Keycode.COMMAND, 'p']), # Copy path of current file to clipboard
        # 3rd row ----------
        (0x004000, 'Over', [Keycode.F10]), # Step over (in debug)
        (0x404040, 'Term', [Keycode.CONTROL, '`']), # Open Terminal
        (0xA55F17, 'All', [Keycode.COMMAND, 'L']), # Select all occurences matching selection in file
        # 4th row ----------
        (0x004000, 'In', [Keycode.F11]), # Step in (in debug)
        (0x202000, 'Zoom -', [Keycode.COMMAND, Keycode.SHIFT, '-']), # Zoom out
        (0x202000, 'Zoom +', [Keycode.COMMAND, '=']), # Zoom in
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'k', -Keycode.COMMAND, 'v']) # Preview markdown inline
    ]
}
# 
