"""
example: api_response.py — Fetch live data from an API and work with dotdict
Uses:    JSONPlaceholder (free, no API key needed)
"""

from urllib.request import urlopen
from json import loads
from easydotdict import dotdict

url = "https://jsonplaceholder.typicode.com/users/2"

with urlopen(url) as r:
    data = loads(r.read())

user = dotdict(data)
# ^^ Wrap the raw API response dict in a dotdict.
#    Nested dicts inside (address, company, geo) are auto-converted to dotdict too.

print(f"Name:    {user.name}")
# ^^ Read deeply nested fields with dot notation instead of user['name'].

print(f"Email:   {user.email}")
print(f"City:    {user.address.city}")
# ^^ Three levels deep: address -> city. No chained brackets needed.

print(f"Company: {user.company.name}")
# ^^ Two levels deep: company -> name.

user.phone = "N/A"
user.address.zipcode = "Unknown"
# ^^ Modify existing fields or add new ones with simple assignment.

print(f"\nGeo: {user.address.geo.lat}, {user.address.geo.lng}")

print(user)
# ^^ __str__ renders the entire structure as indented JSON.
