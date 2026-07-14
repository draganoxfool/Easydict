"""
example: dig_demo.py — Compare dot notation vs .dig() for nested access
"""

from easydotdict import dotdict

data = dotdict({
    "user": {
        "name": "Alice",
        "address": {"city": "Berlin", "zip": "10115"},
    }
})

# Dot notation — path is hardcoded at write time
print(data.user.name)             # Alice
print(data.user.address.city)     # Berlin

# .dig() — path is a string, can come from a variable
path = "user.name"
print(data.dig(path))             # Alice

paths = ["user.address.city", "user.address.zip"]
for p in paths:
    print(f"{p}: {data.dig(p)}")
# ^^ Same result as dot notation, but the paths are built at runtime

# Missing paths return None safely
print(data.dig("user.age"))       # None
print(data.dig("nope.key"))       # None
