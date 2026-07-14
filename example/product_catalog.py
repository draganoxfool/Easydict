"""
example: product_catalog.py — Build a dynamic product list from scratch
"""

from easydotdict import dotdict

products = dotdict()
# ^^ Start with an empty dotdict. Unlike a normal dict,
#    dotdict auto-creates intermediate objects when you
#    assign through missing keys (auto-vivification).

products.prod_1.name = "Wireless Mouse"
# ^^ dotdict auto-creates `products.prod_1` as a nested dotdict,
#    then sets `.name` on it. No `products['prod_1'] = {}` needed.

products.prod_1.price = 29.99
products.prod_1.specs.dpi = 1600
# ^^ Auto-vivification again: `products.prod_1.specs` doesn't exist yet,
#    so dotdict creates it before setting `.dpi`.

products.prod_1.specs.color = "Black"

products.prod_2.name = "Mechanical Keyboard"
products.prod_2.price = 89.99
products.prod_2.specs.switches = "Cherry MX"
products.prod_2.specs.layout = "ANSI"
products.prod_2.specs.color = "White"

for key in products:
    # ^^ dotdict inherits from dict, so standard iteration works.
    p = products[key]
    # ^^ Bracket notation works too, returns the nested dotdict.
    print(f"{p.name} — ${p.price}")
    for spec_key in p.specs:
        print(f"   {spec_key}: {p.specs[spec_key]}")
        # ^^ Mix dot and bracket notation freely.

print(products)
# ^^ __str__ renders as indented JSON via json.dumps(indent=2).
