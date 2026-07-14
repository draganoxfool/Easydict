"""
example: product_catalog.py — Fetch GitHub repos as a catalog and enrich with dotdict
Uses:    GitHub API (https://api.github.com, free, no key needed for public data)
"""

from urllib.request import urlopen
from json import loads
from easydotdict import dotdict

url = "https://api.github.com/orgs/python/repos?per_page=5&sort=stars"

with urlopen(url) as r:
    data = loads(r.read())

repos = [dotdict(r) for r in data]
# ^^ Wrap each repo dict in a dotdict for dot-notation access.
#    Nested objects (like owner, permissions) are auto-converted too.

for r in repos:
    print(f"{r.name:25s}  stars: {r.stargazers_count:<5d}  {r.language or 'N/A':10s}")
# ^^ Read nested fields with dot notation. Formatting delegates to the underlying value.

for r in repos:
    if r.stargazers_count > 1000:
        # ^^ Comparison operators delegate to the underlying value.
        r.popular = True
        r.tags = ["python", "popular"]
        # ^^ Add new fields dynamically with simple assignment.

print(repos[0])
# ^^ Print as indented JSON. Shows all original fields plus any you added.
