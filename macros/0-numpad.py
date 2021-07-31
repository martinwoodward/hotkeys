# MACROPAD Hotkeys example: Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Numpad',          # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x101010, '  7', [Keycode.KEYPAD_SEVEN]),
        (0x101010, '8', [Keycode.KEYPAD_EIGHT]),
        (0x101010, '9  ', [Keycode.KEYPAD_NINE]),
        # 2nd row ----------
        (0x101010, '  4', [Keycode.KEYPAD_FOUR]),
        (0x101010, '5', [Keycode.KEYPAD_FIVE]),
        (0x101010, '6  ', [Keycode.KEYPAD_SIX]),
        # 3rd row ----------
        (0x101010, '  1', [Keycode.KEYPAD_ONE]),
        (0x101010, '2', [Keycode.KEYPAD_TWO]),
        (0x101010, '3  ', [Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x400000, '  <', [Keycode.BACKSPACE]),
        (0x101010, '0', [Keycode.KEYPAD_ZERO]),
        (0x004000, '.  ', [Keycode.KEYPAD_PERIOD]),
        # Encoder button ---
        (0x000000, '', [Keycode.KEYPAD_ENTER])
    ]
}# Write your code here :-)  [Keycode.OPTION, Keycode.THREE]
