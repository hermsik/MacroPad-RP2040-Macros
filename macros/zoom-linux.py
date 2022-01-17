
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Zoom', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 2nd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x101010, 'Audio', [Keycode.ALT, Keycode.A]),
        (0x000000, '', []),
        (0x101010, 'Video', [Keycode.ALT, Keycode.V]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
