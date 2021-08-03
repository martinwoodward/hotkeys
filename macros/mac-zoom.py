# MACROPAD Hotkeys example: Visual Studio Code for macOS

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                     # REQUIRED dict, must be named 'app'
    'name' : 'Mac Zoom', # Application name
    'macros' : [            # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Video', [Keycode.COMMAND, 'V']), 
        (0x000040, 'Share', [Keycode.COMMAND, 'S']),   
        (0x000040, 'Pause', [Keycode.COMMAND, 'T']), 
        # 2nd row ----------
        (0x400000, 'Rec', [Keycode.COMMAND, 'C']), 
        (0x004040, 'View', [Keycode.COMMAND, 'W']), 
        (0x101010, 'Join', [Keycode.COMMAND, 'j']), 
        # 3rd row ----------
        (0x402000, 'Rec ||', [Keycode.COMMAND, 'P']), 
        (0x004040, '<', [Keycode.CONTROL, 'p']), 
        (0x004040, '>', [Keycode.CONTROL, 'n']), 
        # 4th row ----------
        (0x004000, 'Chat', [Keycode.COMMAND, 'H']), 
        (0x202000, 'Ctrls', [Keycode.COMMAND, Keycode.CONTROL, Keycode.OPTION, 'h']), 
        (0x4C0099, 'Mute', [Keycode.COMMAND, 'A']), 
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) 
    ]
}
# 
