"""
example: app_config.py — Load, edit, and persist app config using dotdict
Usage:   python app_config.py          # show current config
         python app_config.py --reset  # reset to defaults
"""

from easydotdict import dotdict
from json import dump, load
from pathlib import Path
from sys import argv

CONFIG_FILE = Path("config.json")

DEFAULTS = dotdict({
    "app": {
        "theme": "dark",
        "locale": "en-US",
    },
    "editor": {
        "font_size": 14,
        "tab_spaces": 4,
        "word_wrap": True,
    },
    "shortcuts": {
        "save": "Ctrl+S",
        "find": "Ctrl+F",
    },
})
# ^^ Define default config as a dotdict.
#    Nested dicts are auto-converted, so DEFAULTS.editor.font_size works.

if "--reset" in argv:
    with open(CONFIG_FILE, "w") as f:
        dump(DEFAULTS.to_dict(), f, indent=2)
    # ^^ to_dict() converts nested dotdicts back to plain dicts for JSON serialization.
    print("Config reset to defaults.")
    config = DEFAULTS

elif CONFIG_FILE.exists():
    with open(CONFIG_FILE) as f:
        config = dotdict(load(f))
    # ^^ Wrap the loaded JSON dict in dotdict for ergonomic access.
    print("Loaded existing config.")

else:
    config = DEFAULTS
    with open(CONFIG_FILE, "w") as f:
        dump(config.to_dict(), f, indent=2)
    print("Created default config.")

theme = config.app.theme
font = config.editor.font_size
wrap = config.editor.word_wrap
# ^^ Read nested config values with dot notation.
#    Missing keys return None instead of raising errors.

print(f"Theme: {theme}  |  Font size: {font}  |  Word wrap: {wrap}")
print(f"Shortcuts: save={config.shortcuts.save}  find={config.shortcuts.find}")
