# Python Optimization Quick Reference

## Container Selection Decision Tree

```
┌─────────────────────────────────────────────┐
│ What do you need to do with the data?      │
└─────────────────────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ Membership testing?   │
        │   (x in container)    │
        └───────────────────────┘
         │YES              │NO
         ▼                 ▼
    ┌────────┐      ┌──────────────┐
    │  SET   │      │ Key-value    │
    │  or    │      │ pairs?       │
    │  DICT  │      └──────────────┘
    └────────┘       │YES      │NO
                     ▼         ▼
                 ┌──────┐  ┌─────────┐
                 │ DICT │  │ Ordered │
                 └──────┘  │ & index?│
                           └─────────┘
                            │YES  │NO
                            ▼     ▼
                         ┌─────┐ ┌─────┐
                         │LIST │ │ SET │
                         └─────┘ └─────┘
```

## Performance Cheat Sheet

### Time Complexity

| Operation | List | Set | Dict |
|-----------|------|-----|------|
| `x in container` | O(n) ❌ | O(1) ✅ | O(1) ✅ |
| `container[i]` | O(1) ✅ | N/A | O(1) ✅ |
| `append/add` | O(1) ✅ | O(1) ✅ | O(1) ✅ |
| `remove` | O(n) ⚠️ | O(1) ✅ | O(1) ✅ |
| `iteration` | O(n) ✅ | O(n) ✅ | O(n) ✅ |

### Memory Usage (for 1,000 integers)

| Container | Memory | Use When |
|-----------|--------|----------|
| List | ~36 KB | Need order/indexing, memory-constrained |
| Set | ~59.6 KB | Need fast membership testing |
| Dict | ~90.7 KB | Need key-value lookups |

### Speed Comparison

For 1,000 items, `x in set` is **~200x faster** than `x in list`

## Common Patterns

### ❌ ANTI-PATTERN: List for membership

```python
# SLOW - O(n) for each check
valid_users = [1, 2, 3, 4, 5]
if user_id in valid_users:  # Gets slower as list grows
    process()
```

### ✅ PATTERN: Set for membership

```python
# FAST - O(1) for each check
valid_users = {1, 2, 3, 4, 5}
if user_id in valid_users:  # Always fast
    process()
```

### ❌ ANTI-PATTERN: Nested loop counting

```python
# SLOW - O(n²)
counts = []
for item in data:
    for count in counts:
        if count[0] == item:
            count[1] += 1
            break
```

### ✅ PATTERN: Dict or Counter

```python
# FAST - O(n)
from collections import Counter
counts = Counter(data)

# or
counts = {}
for item in data:
    counts[item] = counts.get(item, 0) + 1
```

### ❌ ANTI-PATTERN: List for unique values

```python
# SLOW - O(n²)
unique = []
for item in data:
    if item not in unique:  # O(n) each time
        unique.append(item)
```

### ✅ PATTERN: Set for unique values

```python
# FAST - O(n)
unique = set(data)

# If order matters:
unique = list(dict.fromkeys(data))  # Python 3.7+
```

## Memory Optimization with `__slots__`

### When to Use

✅ **DO use** `__slots__` when:
- Creating hundreds/thousands of instances
- Attributes are fixed and known upfront
- Memory efficiency is critical
- You don't need dynamic attributes

❌ **DON'T use** `__slots__` when:
- Only creating a few instances (<100)
- Need to add attributes dynamically
- Need `__dict__` for serialization
- Inheriting from classes without `__slots__`

### Pattern

```python
class OptimizedPoint:
    __slots__ = ['x', 'y', 'z']  # 30% memory reduction

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

## Number Types Memory

```python
import sys

sys.getsizeof(42)      # 28 bytes (small int, cached)
sys.getsizeof(10**100) # 72 bytes (large int)
sys.getsizeof(3.14)    # 24 bytes (float)
```

## Real-World Guidelines

### 1. API Rate Limiting
```python
# ✅ GOOD: Fast lookups
blocked_ips = set()
if ip in blocked_ips: ...

# ❌ BAD: Slow as it grows
blocked_ips = []
if ip in blocked_ips: ...
```

### 2. Configuration Validation
```python
# ✅ GOOD: O(1) validation
VALID_CONFIGS = {'debug', 'production', 'staging'}
if config in VALID_CONFIGS: ...

# ❌ BAD: O(n) validation
VALID_CONFIGS = ['debug', 'production', 'staging']
if config in VALID_CONFIGS: ...
```

### 3. Tag/Category Systems
```python
# ✅ GOOD: Set operations
user_tags = {'python', 'django', 'react'}
required_tags = {'python', 'django'}
if required_tags <= user_tags:  # Subset check, O(m)
    grant_access()

# ❌ BAD: Nested loops
user_tags = ['python', 'django', 'react']
required_tags = ['python', 'django']
if all(tag in user_tags for tag in required_tags):  # O(n*m)
    grant_access()
```

### 4. Caching
```python
# ✅ GOOD: Dict for cache
cache = {}
result = cache.get(key)  # O(1)

# ❌ BAD: List for cache
cache = []
result = next((v for k, v in cache if k == key), None)  # O(n)
```

## Collection Conversions

```python
# List → Set (remove duplicates)
unique_items = set(my_list)

# Set → List (for indexing/ordering)
ordered_items = sorted(my_set)

# List → Dict (for fast lookup with values)
lookup = {item: True for item in my_list}

# Dict keys → Set (for set operations)
key_set = set(my_dict.keys())
```

## When Size Doesn't Matter

For **small collections** (<10 items), the performance difference is negligible:
- Use the most **readable** option
- Lists are fine for small lookup sets
- Don't over-optimize

For **large collections** (>100 items), optimization matters:
- Choose based on access patterns
- Profile if unsure
- Prefer sets/dicts for frequent lookups

## Summary Rules

1. **Membership testing** → Set or Dict (200x faster than list)
2. **Counting/grouping** → Dict or Counter (avoid nested loops)
3. **Unique values** → Set (one-liner, efficient)
4. **Order + indexing** → List (most memory-efficient)
5. **Key-value pairs** → Dict (O(1) lookups)
6. **Many instances** → Consider `__slots__` (30% memory savings)
7. **Small data** (<10 items) → Readability over optimization
8. **Large data** (>100 items) → Choose wisely, profile if needed
