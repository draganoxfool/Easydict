# easydict Documentation

## Overview

`easydict` is a lightweight Python library that wraps dictionaries with dot-notation access, safe missing-key handling, automatic nested conversion, and pretty-printing. No external dependencies.

---

## Installation

```bash
pip install easydict
```

Or copy `easydict/easydict.py` into your project.

---

## Getting Started

```python
from easydict import EasyDict

d = EasyDict({'user': {'profile': {'name': 'Alice'}}})
print(d.user.profile.name)  # Alice
```

---

## Core Features

### Dot & Bracket Notation

Access and set values with either style interchangeably:

```python
d = EasyDict()
d.user.name = 'Alice'
d.user['age'] = 30

print(d.user.name)   # Alice
print(d['user'].age) # 30
```

### Safe Missing-Key Access

Dot notation returns `None` for missing keys — no `KeyError` or `AttributeError`:

```python
d = EasyDict({'a': 1})
print(d.user.email)  # None (safe, like JS optional chaining)
print(d['b'])        # None
print(d.get('b'))    # None
```

### Auto-Vivification (Chained Assignment)

Create deep nested structures in one statement:

```python
d = EasyDict()
d.config.database.host = 'localhost'
d.config.database.port = 5432
# d == {'config': {'database': {'host': 'localhost', 'port': 5432}}}
```

### Auto-Conversion

Nested plain `dict`s and `list`s containing `dict`s are automatically wrapped:

```python
data = {'users': [{'name': 'Alice'}, {'name': 'Bob'}]}
d = EasyDict(data)
print(d.users[0].name)  # Alice
print(type(d.users[0])) # <class 'easydict.EasyDict'>
```

### Pretty-Printing

`repr()` and `str()` produce indented JSON output:

```python
d = EasyDict({'name': 'Alice', 'scores': [90, 95]})
print(d)
# {
#   "name": "Alice",
#   "scores": [
#     90,
#     95
#   ]
# }
```

### Deep Path Operations

Use dot-separated path strings for nested access:

```python
d = EasyDict({'user': {'name': 'Alice'}})
print(d.dig('user.name'))       # Alice
print(d.dig('user.missing'))    # None

d.put('server.host', 'localhost')
print(d.server.host)  # localhost

print(d.has('user.name'))   # True
print(d.has('user.email'))  # False
```

### Flatten & Unflatten

Convert nested structures to/from flat dot-separated keys:

```python
d = EasyDict({'user': {'name': 'Alice', 'scores': [90, 95]}})
flat = d.flatten()
# flat == {'user.name': 'Alice', 'user.scores.0': 90, 'user.scores.1': 95}

restored = EasyDict.unflatten({'a.b.c': 1})
print(restored.a.b.c)  # 1
```

### Deep Merge

Merge another dict recursively, preserving existing keys:

```python
d = EasyDict({'user': {'name': 'Alice', 'age': 30}})
d.update({'user': {'email': 'alice@example.com'}})
print(d.user.email)  # alice@example.com
print(d.user.name)   # Alice (preserved)

d.merge({'settings': {'debug': True}})
print(d.settings.debug)  # True
```

### Convert Back to Plain Dict

```python
d = EasyDict({'user': {'name': 'Alice'}})
plain = d.to_dict()
# plain == {'user': {'name': 'Alice'}}
# type(plain['user']) == dict
```

---

## API Reference

### `EasyDict(*args, **kwargs)`

Creates a new `EasyDict`. Accepts the same arguments as `dict()`:

```python
EasyDict()                    # empty
EasyDict({'a': 1})            # from dict
EasyDict(a=1, b=2)            # from keyword args
EasyDict([('a', 1), ('b', 2)])  # from iterable
```

---

### Attribute Access

#### `__getattr__(key)`

Dot-notation read. If the key exists, returns the value. If not, returns `None` (via a `_Missing` sentinel proxy). The proxy auto-creates the path if a value is later assigned through it, enabling `d.a.b.c = x` chained assignment.

#### `__setattr__(key, value)`

Dot-notation write. Wraps nested `dict`s and `list`s automatically.

#### `__delattr__(key)`

Dot-notation delete. Raises `AttributeError` if the key does not exist.

---

### Item Access

#### `__getitem__(key)`

Bracket-notation read. Returns `None` for missing keys (safe access).

#### `__setitem__(key, value)`

Bracket-notation write. Wraps nested `dict`s and `list`s automatically.

---

### Conversion

#### `to_dict()`

Recursively converts all nested `EasyDict`s back to plain `dict`s and `list`s.

#### `flatten(prefix='')`

Recursively flattens the structure into a flat dict with dot-separated keys. List items use numeric indices (e.g., `items.0.id`).

#### `unflatten(data)` *(class method)*

Reverses `flatten()`. Converts a flat dict with dot-separated keys back into a nested `EasyDict`. Numeric keys are converted to lists.

---

### Deep Path Methods

#### `dig(path)`

Traverse a dot-separated path string. Returns the value or `None` if any segment is missing.

#### `put(path, value)`

Traverse a dot-separated path string, creating intermediate `EasyDict`s as needed, then set the value.

#### `has(path)`

Returns `True` if the dot-separated path exists, `False` otherwise.

---

### Mutation

#### `update(other=None, **kwargs)`

Deep merge update. Recursively merges nested dicts, preserving existing keys. Wraps nested `dict`s automatically.

#### `merge(other)`

Deep merge, same as `update()` but returns `self` for chaining.

---

### Copying & Inspection

#### `copy()`

Returns a deep copy as a new `EasyDict`.

#### `clone()`

Explicit deep copy. Returns a new `EasyDict` with all nested structures recursively copied.

#### `is_empty()`

Returns `True` if the `EasyDict` has no keys.

#### `get(key, default=None)`

Returns the value for `key` if it exists, otherwise `default`. Correctly distinguishes between a key whose value is `None` and a missing key.

---

## Inheritance & Compatibility

`EasyDict` inherits from `dict`, so all standard dict methods work:

- `keys()`, `values()`, `items()`
- `pop(key, *args)`
- `clear()`
- `len()`, `in`, `iter()`
- `bool()` (empty = `False`)

---

## Edge Cases & Behavior

| Scenario | Behavior |
|----------|----------|
| Access missing key via bracket `d['x']` | Returns `None` |
| Access missing key via dot `d.x` | Returns `None` (via `_Missing` proxy) |
| Set `d.a.b.c = value` with missing intermediates | Auto-creates intermediate `EasyDict`s |
| Dict in a list `[{'a': 1}]` | Dict becomes `EasyDict` |
| `d.to_dict()` | Recursively unwraps to plain `dict`/`list` |
| `repr(d)` / `print(d)` | Indented JSON via `json.dumps(indent=2)` |
| `bool(d)` | `False` when empty (inherited from `dict`) |
| `d.keys()` / `d.values()` / `d.items()` | Standard dict behavior |
| Dict key shadows method name (e.g., `items`) | Dict value takes priority |
| `d == None` when `d` is missing-key proxy | `True` (proxy compares equal to `None`) |

---

## Limitations

- Keys that clash with `EasyDict` method names (e.g., `keys`, `values`, `items`, `update`, `copy`, `get`, `to_dict`) shadow the method when accessed via dot notation. Use bracket notation to access the method, or key the data under a different name.
- Keys starting with `_` cannot be accessed via dot notation — use bracket notation instead.
- `hasattr(d, 'missing')` returns `True` because `__getattr__` returns a `_Missing` proxy instead of raising `AttributeError`.
