# API Reference

The following section outlines the API of easydotdict.

---

## Version Related Info

easydotdict.\_\_version\_\_[​](#easydotdict.__version__ "Permalink to this headline")

A string representation of the version. e.g. `'1.1.2'`.

---

## Core Classes

### dotdict

Attributes

- [is_frozen](#easydotdict.dotdict.is_frozen)
- [is_empty](#easydotdict.dotdict.is_empty)

Methods

- [\_\_getattribute\_\_](#easydotdict.dotdict.__getattribute__)
- [\_\_getattr\_\_](#easydotdict.dotdict.__getattr__)
- [\_\_setattr\_\_](#easydotdict.dotdict.__setattr__)
- [\_\_delattr\_\_](#easydotdict.dotdict.__delattr__)
- [\_\_getitem\_\_](#easydotdict.dotdict.__getitem__)
- [\_\_setitem\_\_](#easydotdict.dotdict.__setitem__)
- [\_\_delitem\_\_](#easydotdict.dotdict.__delitem__)
- [\_\_repr\_\_](#easydotdict.dotdict.__repr__)
- [to_dict](#easydotdict.dotdict.to_dict)
- [copy](#easydotdict.dotdict.copy)
- [clone](#easydotdict.dotdict.clone)
- [update](#easydotdict.dotdict.update)
- [merge](#easydotdict.dotdict.merge)
- [get](#easydotdict.dotdict.get)
- [dig](#easydotdict.dotdict.dig)
- [put](#easydotdict.dotdict.put)
- [has](#easydotdict.dotdict.has)
- [set_many](#easydotdict.dotdict.set_many)
- [delete](#easydotdict.dotdict.delete)
- [flatten](#easydotdict.dotdict.flatten)
- [unflatten](#easydotdict.dotdict.unflatten)
- [find](#easydotdict.dotdict.find)
- [diff](#easydotdict.dotdict.diff)
- [patch](#easydotdict.dotdict.patch)
- [expect](#easydotdict.dotdict.expect)
- [on_change](#easydotdict.dotdict.on_change)
- [freeze](#easydotdict.dotdict.freeze)
- [unfreeze](#easydotdict.dotdict.unfreeze)
- [cursor](#easydotdict.dotdict.cursor)

*class* easydotdict.dotdict(*\*args*, *\*\*kwargs*)[​](#easydotdict.dotdict "Permalink to this headline")

A subclass of `dict` that provides dot-notation access, safe missing-key handling, auto-vivification, and deep-path utility methods.

All nested `dict` objects encountered during construction are automatically converted to `dotdict`. Lists containing dictionaries receive the same treatment.

Examples

Basic usage:

```python
from easydotdict import dotdict

d = dotdict({"user": {"name": "Alice"}})
print(d.user.name)  # Alice
print(d.user.email) # None (safe missing-key access)
```

Auto-vivification:

```python
d = dotdict()
d.config.database.host = "localhost"
# Result: {'config': {'database': {'host': 'localhost'}}}
```

Parameters

- **\*args** – Positional arguments forwarded to `dict.__init__`.
- **\*\*kwargs** – Keyword arguments forwarded to `dict.__init__`.

---

*property* is_frozen[​](#easydotdict.dotdict.is_frozen "Permalink to this headline")

Whether the `dotdict` is currently frozen and immutable.

Type

[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

---

*property* is_empty[​](#easydotdict.dotdict.is_empty "Permalink to this headline")

Whether the `dotdict` has zero items.

Type

[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

Equivalent to `len(d) == 0`.

---

\_\_getattribute\_\_(key)[​](#easydotdict.dotdict.__getattribute__ "Permalink to this headline")

Intercepts attribute access. If the key does not start with `_` and exists as a data key, returns the value (wrapping scalars in a `_ValueProxy`). Otherwise delegates to `dict.__getattribute__`.

Parameters

- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The attribute name.

Returns

The stored value, a `_ValueProxy` for scalars, or the standard attribute.

---

\_\_getattr\_\_(key)[​](#easydotdict.dotdict.__getattr__ "Permalink to this headline")

Fallback attribute access for keys that are not data entries. Returns a `_Missing` proxy that behaves like `None`.

Parameters

- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The attribute name.

Returns

A `_Missing` instance that compares equal to `None`.

---

\_\_setattr\_\_(key, value)[​](#easydotdict.dotdict.__setattr__ "Permalink to this headline")

Sets a data key via attribute assignment. If the root is frozen, raises `AttributeError`.

Parameters

- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The attribute name.
- **value** – The value to store. Nested `dict` values are converted to `dotdict`.

Raises

- **AttributeError** – If the root `dotdict` is frozen.

---

\_\_delattr\_\_(key)[​](#easydotdict.dotdict.__delattr__ "Permalink to this headline")

Deletes a data key via attribute syntax. If the root is frozen, raises `AttributeError`.

Parameters

- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The attribute name.

Raises

- **AttributeError** – If the key does not exist or the root is frozen.

---

\_\_getitem\_\_(key)[​](#easydotdict.dotdict.__getitem__ "Permalink to this headline")

Accesses a value by bracket notation. Returns `None` instead of raising `KeyError`.

Parameters

- **key** – The key to look up.

Returns

The stored value or `None`.

---

\_\_setitem\_\_(key, value)[​](#easydotdict.dotdict.__setitem__ "Permalink to this headline")

Sets a value by bracket notation. If the root is frozen, raises `KeyError`.

Parameters

- **key** – The key to set.
- **value** – The value to store. Nested `dict` values are converted to `dotdict`.

Raises

- **KeyError** – If the root `dotdict` is frozen.

---

\_\_delitem\_\_(key)[​](#easydotdict.dotdict.__delitem__ "Permalink to this headline")

Deletes a key by bracket notation.

Parameters

- **key** – The key to delete.

Raises

- **KeyError** – If the root is frozen.

---

\_\_repr\_\_()[​](#easydotdict.dotdict.__repr__ "Permalink to this headline")

Returns an indented JSON representation of the `dotdict`.

Return type

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

---

to_dict()[​](#easydotdict.dotdict.to_dict "Permalink to this headline")

Recursively converts all nested `dotdict` objects back into plain `dict` and `list` instances.

Returns

A plain Python dictionary with no `dotdict` nesting.

Return type

[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

---

copy()[​](#easydotdict.dotdict.copy "Permalink to this headline")

Returns a deep copy of the `dotdict` as a new `dotdict`. Identical to `clone()`.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

---

clone()[​](#easydotdict.dotdict.clone "Permalink to this headline")

Returns a deep copy of the `dotdict` as a new `dotdict`.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

---

update(other=None, **kwargs)[​](#easydotdict.dotdict.update "Permalink to this headline")

Performs a recursive deep merge of `other` (and keyword arguments) into the current `dotdict`. Existing keys are preserved unless overridden by the merge.

Parameters

- **other** (Optional\[Union\[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")\]\]) – A mapping to deep-merge. Accepts any `Mapping` type (e.g. `dict`, `OrderedDict`, `defaultdict`). If not a `Mapping`, treated as an iterable of key-value pairs.
- **\*\*kwargs** – Additional key-value pairs to deep-merge.

Examples

```python
d = dotdict({"user": {"name": "Alice", "age": 30}})
d.update({"user": {"email": "alice@example.com"}})
# Result: {'user': {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}}
```

---

merge(other)[​](#easydotdict.dotdict.merge "Permalink to this headline")

Performs a recursive deep merge of `other` into the current `dotdict` and returns `self` for chaining.

Parameters

- **other** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – The dictionary to merge.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

Examples

```python
d = dotdict()
d.merge({"a": 1}).merge({"b": 2})
# Result: {'a': 1, 'b': 2}
```

---

get(path, default=None)[​](#easydotdict.dotdict.get "Permalink to this headline")

Retrieves a value by dot-separated path or single key. Returns `default` if the path does not exist.

Unlike standard `dict.get`, this correctly distinguishes between a key whose value is `None` and a key that is genuinely missing.

Parameters

- **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A dot-separated path or a single key.
- **default** – The value to return if the path is not found. Defaults to `None`.

Returns

The stored value or `default`.

Examples

```python
d = dotdict({"user": {"name": "Alice"}})
d.get("user.name")       # Alice
d.get("user.email")      # None
d.get("user.email", "n/a")  # n/a
```

---

dig(path)[​](#easydotdict.dotdict.dig "Permalink to this headline")

Traverses a dot-separated path and returns the value at the end. Returns `None` if any segment is missing. Numeric segments are treated as list indices.

Parameters

- **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A dot-separated path.

Returns

The value at the end of the path, or `None`.

Examples

```python
d = dotdict({"user": {"addresses": [{"city": "Berlin"}]}})
d.dig("user.addresses.0.city")  # Berlin
d.dig("user.addresses.1.city")  # None
```

---

put(path, value)[​](#easydotdict.dotdict.put "Permalink to this headline")

Traverses a dot-separated path, creating intermediate `dotdict` objects (or extending lists) as needed, then assigns the value.

Parameters

- **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A dot-separated path.
- **value** – The value to assign.

Raises

- **AttributeError** – If the root `dotdict` is frozen.

Examples

```python
d = dotdict()
d.put("server.host", "localhost")
d.put("server.ports.0", 8080)
# Result: {'server': {'host': 'localhost', 'ports': [8080]}}
```

---

has(path)[​](#easydotdict.dotdict.has "Permalink to this headline")

Returns `True` if the dot-separated path resolves to an existing value, `False` otherwise.

Parameters

- **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A dot-separated path.

Return type

[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

Examples

```python
d = dotdict({"user": {"name": "Alice"}})
d.has("user.name")   # True
d.has("user.email")  # False
d.has("user.name.first")  # False (name is a string)
```

---

set_many(items)[​](#easydotdict.dotdict.set_many "Permalink to this headline")

Accepts a dictionary of `{path: value}` pairs and applies each via `put()`. Returns `self` for chaining.

New in version 1.0.

Parameters

- **items** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A mapping of dot-separated paths to values.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

Raises

- **AttributeError** – If the root `dotdict` is frozen.

Examples

```python
d = dotdict()
d.set_many({
    "database.host": "localhost",
    "database.port": 5432,
})
```

---

delete(*paths)[​](#easydotdict.dotdict.delete "Permalink to this headline")

Removes one or more paths from the structure. Silently ignores paths that do not exist. Returns `self` for chaining.

New in version 1.0.

Parameters

- **\*paths** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – One or more dot-separated paths to delete.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

Raises

- **AttributeError** – If the root `dotdict` is frozen.

Examples

```python
d = dotdict({"a": {"b": 1, "c": 2}, "x": 3})
d.delete("a.b", "x")
# Result: {'a': {'c': 2}}
```

---

flatten(prefix='')[​](#easydotdict.dotdict.flatten "Permalink to this headline")

Reduces a nested `dotdict` to a single-level dictionary where each key is a dot-separated path. List items are indexed numerically.

Parameters

- **prefix** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – An optional prefix prepended to every key.

Returns

A flat dictionary of `{path: value}` pairs.

Return type

[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

Examples

```python
d = dotdict({"user": {"name": "Alice", "scores": [90, 95]}})
d.flatten()
# {"user.name": "Alice", "user.scores.0": 90, "user.scores.1": 95}
```

---

*classmethod* unflatten(data)[​](#easydotdict.dotdict.unflatten "Permalink to this headline")

Reverses `flatten()`, converting flat dot-separated keys back into a nested `dotdict`. Numeric keys become list indices.

Parameters

- **data** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A flat dictionary with dot-separated keys.

Returns

A nested `dotdict`.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

Examples

```python
restored = dotdict.unflatten({"a.b.c": 1, "x.0": "first"})
restored.a.b.c  # 1
restored.x[0]   # first
```

---

find(name)[​](#easydotdict.dotdict.find "Permalink to this headline")

Recursively searches the entire structure for keys whose name matches the given string and returns a sorted list of dot-separated paths to each match.

Parameters

- **name** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The key name to search for.

Returns

A sorted list of dot-separated paths.

Return type

[`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\]

Examples

```python
d = dotdict({"a": {"b": 1, "c": {"b": 2}}, "x": {"b": 3}})
d.find("b")
# ["a.b", "a.c.b", "x.b"]
```

---

diff(other)[​](#easydotdict.dotdict.diff "Permalink to this headline")

Compares the current `dotdict` with another and returns a dictionary describing every difference. Each entry maps a dot-separated path to a `{"from": old_value, "to": new_value}` record. Paths present in only one side use `None` for the missing value.

New in version 1.0.

Parameters

- **other** ([`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")) – The other `dotdict` to compare against.

Returns

A dictionary of `{path: {"from": ..., "to": ...}}`.

Return type

[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

Examples

```python
v1 = dotdict({"app": {"name": "MyApp", "debug": True}})
v2 = dotdict({"app": {"name": "MyApp", "debug": False, "version": "2.0"}})
v1.diff(v2)
# {"app.debug": {"from": True, "to": False}, "app.version": {"from": None, "to": "2.0"}}
```

---

patch(changes)[​](#easydotdict.dotdict.patch "Permalink to this headline")

Applies the output of `diff()` (or any compatible dictionary) back to the current object. Paths with `"to"` set to `None` are deleted.

New in version 1.0.

Parameters

- **changes** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary in the format produced by `diff()`: `{path: {"from": ..., "to": ...}}`.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

Raises

- **AttributeError** – If the root `dotdict` is frozen.

---

expect(schema)[​](#easydotdict.dotdict.expect "Permalink to this headline")

Validates the types of values at runtime. The schema is a dictionary mapping dot-separated paths to expected types (or tuples of acceptable types).

New in version 1.0.

Parameters

- **schema** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A mapping of paths to types or tuples of types.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

Raises

- **KeyError** – If a required path is missing.
- **TypeError** – If the value's type does not match.

Examples

```python
user = dotdict({"name": "Alice", "age": 30})
user.expect({"name": str, "age": int})  # passes
user.expect({"email": str})             # KeyError
```

---

on_change(path, callback)[​](#easydotdict.dotdict.on_change "Permalink to this headline")

Registers a callback that is invoked whenever the value at the specified path is modified via `__setitem__` or `put()`. The callback receives the path string and the new value.

New in version 1.0.

Parameters

- **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The dot-separated path to watch.
- **callback** (Callable\[\[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), Any\]\]) – A callable accepting `(path, value)`.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

Examples

```python
config = dotdict()
config.on_change("app.debug", lambda p, v: print(f"{p} changed to {v}"))
config.app.debug = False  # prints: app.debug changed to False
```

---

freeze()[​](#easydotdict.dotdict.freeze "Permalink to this headline")

Renders the `dotdict` immutable. Any attempt to set, delete, or modify an attribute or item raises `AttributeError` (or `KeyError` for bracket mutations).

Returns `self` for chaining.

New in version 1.0.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

---

unfreeze()[​](#easydotdict.dotdict.unfreeze "Permalink to this headline")

Restores mutability to a previously frozen `dotdict`.

Returns `self` for chaining.

New in version 1.0.

Return type

[`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")

---

cursor(path, create=False)[​](#easydotdict.dotdict.cursor "Permalink to this headline")

Creates a lightweight cursor that exposes a nested portion of the `dotdict` as if it were the root. All reads and writes through the cursor affect the original object directly.

New in version 1.0.

Parameters

- **path** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The dot-separated path to the target nested dict.
- **create** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – If `True`, auto-creates intermediate paths if they do not exist. Defaults to `False`.

Returns

A cursor object for focused access.

Return type

[`_Cursor`](#easydotdict._Cursor "easydotdict._Cursor")

Raises

- **KeyError** – If the path is not found and `create` is `False`.
- **TypeError** – If the target is not a dict-like object.

Examples

```python
d = dotdict({"database": {"host": "localhost", "port": 5432}})
db = d.cursor("database")
print(db.host)     # localhost
db.port = 8080     # modifies d.database.port
```

---

## Decorators

easydotdict.dotdictify[​](#easydotdict.dotdictify "Permalink to this headline")

A decorator that converts the first positional argument from a plain `dict` into a `dotdict` before the function body executes.

Examples

```python
from easydotdict import dotdictify

@dotdictify
def process_user(data):
    print(data.user.name)  # data is a dotdict

process_user({"user": {"name": "Alice"}})
```

---

easydotdict.defaults(*_defaults=None*, **kwargs)[​](#easydotdict.defaults "Permalink to this headline")

A decorator that merges default values into the first positional argument (which should be a `dotdict`) before the function runs. Only missing keys are populated — existing values are never overwritten.

Parameters

- **\_defaults** (Optional\[[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")\]) – A dictionary of default values.
- **\*\*kwargs** – Additional default values as keyword arguments.

Examples

```python
from easydotdict import defaults, dotdict

@defaults(page=1, limit=20)
def list_items(params):
    print(params.page)   # uses caller's value or falls back to 1

list_items(dotdict({"page": 5}))  # page=5, limit=20
list_items(dotdict())             # page=1, limit=20
```

---

easydotdict.expect_schema(schema)[​](#easydotdict.expect_schema "Permalink to this headline")

A decorator that validates the first positional argument against a schema at call time, raising `TypeError` or `KeyError` if validation fails.

Parameters

- **schema** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A mapping of paths to expected types, identical to the format used by `dotdict.expect()`.

Raises

- **KeyError** – If a required path is missing.
- **TypeError** – If a value's type does not match.

Examples

```python
from easydotdict import expect_schema, dotdict

@expect_schema({"name": str, "age": int})
def save_user(user):
    print(f"Saving {user.name}")

save_user(dotdict({"name": "Alice", "age": 30}))  # OK
save_user(dotdict({"name": 123}))                  # TypeError
```

---

easydotdict.freeze[​](#easydotdict.freeze "Permalink to this headline")

A decorator that freezes the return value of the decorated function if it is a `dotdict`. This prevents callers from accidentally mutating a returned configuration or state object.

Examples

```python
from easydotdict import freeze, dotdict

@freeze
def load_config():
    return dotdict({"debug": True, "port": 8080})

cfg = load_config()
# cfg is frozen — cfg.debug = False raises AttributeError
```

---

## Internal Classes

### \_Missing

*class* easydotdict.\_Missing(parent, key)[​](#easydotdict._Missing "Permalink to this headline")

A lightweight proxy returned when accessing a missing key via dot notation. Behaves identically to `None` in boolean contexts, comparisons, and truth checks. When a value is assigned through it, intermediate `dotdict` objects are automatically materialized.

Note

This class is primarily internal. Users interact with it indirectly whenever they access a non-existent attribute and then assign through it (auto-vivification).

Parameters

- **parent** – The parent `dotdict` that contains this missing key.
- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The missing key name.

---

\_\_bool\_\_()[​](#easydotdict._Missing.__bool__ "Permalink to this headline")

Always returns `False`.

Return type

[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

---

\_\_eq\_\_(other)[​](#easydotdict._Missing.__eq__ "Permalink to this headline")

Returns `True` if `other` is `None`, otherwise returns `NotImplemented`.

---

\_\_ne\_\_(other)[​](#easydotdict._Missing.__ne__ "Permalink to this headline")

Returns `False` if `other` is `None`, otherwise returns `NotImplemented`.

---

\_\_repr\_\_()[​](#easydotdict._Missing.__repr__ "Permalink to this headline")

Returns `'None'`.

Return type

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

---

### \_ValueProxy

*class* easydotdict.\_ValueProxy(value, parent, key)[​](#easydotdict._ValueProxy "Permalink to this headline")

A transparent wrapper around scalar values stored in a `dotdict`. Delegates comparison operators, formatting, iteration, hashing, and length to the underlying value. When an attribute is accessed on the proxy, the scalar is promoted to a nested `dotdict` keyed by its own string representation.

Note

This class is primarily internal. Users interact with it indirectly when they read a scalar value (string, int, float, bool, or `None`) from a `dotdict` via attribute access.

Parameters

- **value** – The underlying scalar value.
- **parent** – The parent `dotdict` that contains this value.
- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The key under which the value is stored.

Examples

```python
d = dotdict()
d.name = "Alice"
d.name.character = 5  # promotes "Alice" to a nested dict
# Result: {'name': {'Alice': {'character': 5}}}
```

---

\_\_lt\_\_(other)[​](#easydotdict._ValueProxy.__lt__ "Permalink to this headline")

Delegate to the underlying value's `__lt__`.

---

\_\_le\_\_(other)[​](#easydotdict._ValueProxy.__le__ "Permalink to this headline")

Delegate to the underlying value's `__le__`.

---

\_\_gt\_\_(other)[​](#easydotdict._ValueProxy.__gt__ "Permalink to this headline")

Delegate to the underlying value's `__gt__`.

---

\_\_ge\_\_(other)[​](#easydotdict._ValueProxy.__ge__ "Permalink to this headline")

Delegate to the underlying value's `__ge__`.

---

\_\_format\_\_(spec)[​](#easydotdict._ValueProxy.__format__ "Permalink to this headline")

Delegate to the underlying value's `__format__`, enabling f-string formatting like `f"{d.count:05d}"`.

---

\_\_hash\_\_()[​](#easydotdict._ValueProxy.__hash__ "Permalink to this headline")

Delegate to the underlying value's `__hash__`.

---

\_\_len\_\_()[​](#easydotdict._ValueProxy.__len__ "Permalink to this headline")

Delegate to the underlying value's `__len__`.

---

\_\_iter\_\_()[​](#easydotdict._ValueProxy.__iter__ "Permalink to this headline")

Delegate to the underlying value's `__iter__`.

---

\_\_contains\_\_(item)[​](#easydotdict._ValueProxy.__contains__ "Permalink to this headline")

Delegate to the underlying value's `__contains__`.

---

### \_Cursor

*class* easydotdict.\_Cursor(target)[​](#easydotdict._Cursor "Permalink to this headline")

A lightweight view that exposes a nested portion of a `dotdict` as if it were the root. All reads and writes through the cursor affect the original object directly — no copy is made.

Note

This class is primarily internal. Instances are created via `dotdict.cursor()`.

Parameters

- **target** ([`dotdict`](#easydotdict.dotdict "easydotdict.dotdict")) – The nested `dotdict` to wrap.

Examples

```python
d = dotdict({"database": {"host": "localhost", "port": 5432}})
c = d.cursor("database")
c.host      # localhost
c.port = 8080  # modifies d.database.port
```

---

\_\_getattr\_\_(key)[​](#easydotdict._Cursor.__getattr__ "Permalink to this headline")

Delegates attribute access to the target `dotdict`.

Parameters

- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The attribute name.

---

\_\_setattr\_\_(key, value)[​](#easydotdict._Cursor.__setattr__ "Permalink to this headline")

Delegates attribute assignment to the target `dotdict`.

Parameters

- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The attribute name.
- **value** – The value to set.

---

\_\_delattr\_\_(key)[​](#easydotdict._Cursor.__delattr__ "Permalink to this headline")

Delegates attribute deletion to the target `dotdict`.

Parameters

- **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The attribute name.

---

\_\_getitem\_\_(key)[​](#easydotdict._Cursor.__getitem__ "Permalink to this headline")

Delegates bracket access to the target `dotdict`.

---

\_\_setitem\_\_(key, value)[​](#easydotdict._Cursor.__setitem__ "Permalink to this headline")

Delegates bracket assignment to the target `dotdict`.

---

\_\_delitem\_\_(key)[​](#easydotdict._Cursor.__delitem__ "Permalink to this headline")

Delegates bracket deletion to the target `dotdict`.

---

\_\_repr\_\_()[​](#easydotdict._Cursor.__repr__ "Permalink to this headline")

Delegates to the target's `__repr__`.

Return type

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

---

## Standard dict Compatibility

Because `dotdict` inherits from `dict`, all standard dictionary methods work as expected:

- `keys()`, `values()`, `items()`
- `pop(key, *args)`
- `clear()`
- `len()`, `in`, `iter()`
- `bool()` — returns `False` when empty

Note

Keys that coincide with `dotdict` method names (such as `keys`, `values`, `items`, `update`, `copy`, `get`, `to_dict`) shadow the method when accessed via dot notation. Use bracket notation (`d["keys"]`) to access the data value.
