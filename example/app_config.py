"""
example: app_config.py — Manage nested app settings with dot notation
"""

from easydotdict import dotdict

config = dotdict()

config.app.name = "MyApp"
# ^^ Auto-vivification: `config.app` is created on the fly.

config.app.version = "2.1.0"
config.app.debug = False
config.app.features.dark_mode = True
config.app.features.export_pdf = True
config.app.features.export_csv = False
# ^^ Deep nesting in one flat sequence of assignments.
#    No pre-declaration of `features` as an empty dotdict.

config.database.host = "localhost"
config.database.port = 5432
config.database.credentials.user = "admin"
config.database.credentials.password = "secret"
# ^^ Credentials deeply nested for logical grouping.

config.logging.level = "INFO"
config.logging.format = "{time} {level} {message}"

if config.app.debug:
    config.logging.level = "DEBUG"
# ^^ Reading via dot notation — returns None for missing keys
#    instead of raising KeyError/AttributeError.

print("Config:", config)
# ^^ Pretty-prints the whole nested structure as JSON.

print(f"DB host: {config.database.host}")
# ^^ Dot access on deeply nested path: three levels deep.
print(f"Dark mode: {config.app.features.dark_mode}")
