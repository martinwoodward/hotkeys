# MACROPAD Hotkeys example: Mac System

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : '< Sleep >',             # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', ''),
        (0x000000, '', ''),
        (0x000000, '', ''),     # [Keycode.COMMAND, Keycode.SHIFT, '5']
        # 2nd row ----------

        (0x000000, '', ''),  # Select (path)
        (0x000000, '', ''), # Reflect selection
        (0x000000, '', ''),    # Draw rectangle
        # 3rd row ----------
        (0x000000, '', ''),  # Direct (point) selection
        (0x000000, '', ''),  # Rotate selection
        (0x000000, '', ''),    # Draw ellipse
        # 4th row ----------
        (0x000000, '', ''), # Cycle eyedropper/measure modes
        (0x000000, '', ''),   # Scale selection
        (0x000000, '', ''),    # Type tool
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, Keycode.OPTION, 'S']) # Save for web
    ]
}# Write your code here :-)
