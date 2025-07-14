# notes for review

## input

the following converts the user input to usable form

```python
map(int, input().split())
```

tuple(), set(), or list() are common/primary wrappers depending on problem type

- list
  - ordered, mutable, used in arrays, sorting, sliding window, etc.
  - use it when need indexing (`arr[2]`) or you'll be modifying it e.g. `arr.append()` or `arr.pop()`
- set
  - unordered, only stores unique elments, fast membership tests e.g. `if x in s`, important built in methods include `.add()`, `.remove()`, `.union()`, `issubset()`
  - use it when need to remove duplicates, or need to test for existence fast, or need solving math/logic problems (e.g. union, intersection, subsets)
- tuple
  - ordered, immutable, llows duplicates, can be usde as a key in dictionary
  - use it when the data is fixed and read-only, or returning multiple values, or storing coordinate-like or config data

one liners to go from raw stdin to structured data

```python
a = list(map(int, input().split())) # standard list
b = set(map(int, input().split())) # remove dups
c = tuple(map(int, input().split())) # locked-in
```

## dictionaries

`dict = {key : value}`

dict.get(key, default) = no KeyError, always safe

direct lookup with [] crashes if key is missing

```python
d = {}                   # create
d['John'] = 95           # insert
print(d['John'])         # access
d.get('Jake', 0)         # safe access
del d['John']            # delete

# count frequency
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

use for:

- memoization (DP/cache),
- graphs, e.g. `adj = { node: [neighbors] }`
- hash map tricks like leetcode two sum, subarrays, and longest streaks

## sets

automatically kill duplicates, no indexing but fast for membership checks

Some important functions in Set in Python:

- add(): Adds an element to the set.
- clear(): Removes all elements from the set
- discard(): Removes an element from the set if present.
- remove(): Removes an element from the set. If the element is not present, it raises error.
- pop(): Removes and returns an arbitary set element. Raise error if the set is empty.
- union(): Returns the union of sets in a new set
- update(): Updates the set with the union of itself and others
- len(): Return the length of set.
- sorted(): Return a new sorted list from elements in the set.
- sum(): Return the sum of all elements in the set.

```python
s = set()            # create
s.add(3)             # add
s.discard(3)         # remove safely
x in s               # check existence
set1.union(set2)     # merge
len(s)               # count
```

use for:

- deduping a list
- checking if something was “seen”
- tracking visited states
- subset/superset logic
- solving "find first non-repeating" type problems

## tuples

immutable buyt not unique, can contian duplicates

`.index` returns first match

great for static data, configs, or as dict keyts

```python
t = (1, 2)
print(t[0])        # access

# as dict key
visited = {}
visited[(1, 2)] = True

# as return
def stats():
    return (min_val, max_val)
```

use for

- grid problems (coordinates)
- pair tracking in hash maps
- return multiple values cleanly

## dicts, tuples, sets

tuples use parenthesis, while dict and set use curly brace

syntax:

- dictionary: `{key: value}`
- tuples: `(al1, val2)`
- sets: `{val1, val2}`

## distinct check

unique elements

```python
len(set(arr)) == len(arr)
```

subset

```python
a <= b
```

```python
a.issubset(b)
```

## swappnig values

```python
temp = a
a = b
b = temp
```

```python
# pythonic version
a, b = b, a
```

```python
# interview trick relying on arithmetic
a = a + b
b = a - b
a = a - b

# trick that relies on XOR
a = a ^ b
b = a ^ b
a = a ^ b
```

## manual

- .union()
  - rebuilt via loops and `set.add`
- .issubset()
  - rebuilt with `for item in a: if item not in b`
- .get()
  - replciated with `if key in d`
- .index()
  - basically just: for i, val in enumerate(...)
