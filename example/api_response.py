"""
example: api_response.py — Wrap a raw dict / JSON response for ergonomic access
"""

from easydotdict import dotdict

raw = {
    "user": {
        "name": "Alice",
        "address": {"city": "Berlin", "zip": "10115"},
        "scores": [90, 85, 92],
    }
}

d = dotdict(raw)
# ^^ Wrap a plain dict in dotdict. Nested dicts are auto-converted
#    to dotdict, lists with dicts inside them are also converted.

avg = sum(d.user.scores) / len(d.user.scores)
# ^^ Dot notation to reach a list inside a nested dict.
print(f"{d.user.name} — avg score: {avg:.1f}")
print(f"Lives in {d.user.address.city}")

if d.user.address.zip:
    d.user.address.country = "Germany"
    # ^^ Add new keys to nested dotdicts after creation.

del d.user.scores
# ^^ Delete keys using dot notation (__delattr__).

print(d)
# ^^ Print the modified structure as pretty JSON.
#    Lists and nested dicts are handled automatically.
