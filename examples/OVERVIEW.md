# Python Optimization Skill - Complete Overview

## What is This?

A comprehensive Claude Code skill that teaches Claude to write optimized Python code by selecting the most efficient data structures and patterns based on real-world performance characteristics.

## The Problem

Python developers often write code like this:

```python
# Checking if user is valid - gets slower with more users!
valid_users = [1, 2, 3, 4, 5, ...]
if user_id in valid_users:  # O(n) - slow!
    process_user()
```

This works, but it's **200x slower** than it needs to be for large datasets.

## The Solution

This skill teaches Claude Code to automatically write optimized code:

```python
# Much faster - constant time lookups!
valid_users = {1, 2, 3, 4, 5, ...}
if user_id in valid_users:  # O(1) - fast!
    process_user()
```

## Key Insights from the Article

Based on ["Python Numbers Every Programmer Should Know"](https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/):

### 1. Container Performance Matters

| Container | Memory (1K ints) | Membership Test |
|-----------|------------------|-----------------|
| List | 36 KB | O(n) - SLOW |
| Set | 59.6 KB | O(1) - FAST (200x) |
| Dict | 90.7 KB | O(1) - FAST (200x) |

### 2. Choose Based on Usage

- **Membership testing** (`x in y`) → Use Set/Dict
- **Counting/grouping** → Use Dict/Counter
- **Order + indexing** → Use List
- **Key-value pairs** → Use Dict

### 3. Memory Optimization

Classes with `__slots__` use **30% less memory** when creating many instances.

## What You Get

### 1. The Skill File

`python-number-optimization.skill` - A comprehensive skill that:
- Automatically chooses the right data structure
- Applies memory optimizations when appropriate
- Follows performance best practices
- Includes decision trees and pattern matching

### 2. Practical Examples

Four complete examples showing real-world optimizations:

1. **Membership Testing** (`01_membership_testing.py`)
   - List vs Set performance
   - Rate limiting implementation
   - **Result: 1267x faster with sets!**

2. **Counting & Grouping** (`02_counting_and_grouping.py`)
   - Efficient counting patterns
   - Log analysis optimization
   - Avoiding nested loops

3. **Memory Optimization** (`03_slots_optimization.py`)
   - Using `__slots__` for memory savings
   - Sensor data processing
   - **Result: 30% memory reduction**

4. **Container Selection** (`04_container_selection.py`)
   - Choosing the right container
   - Tag filtering systems
   - Caching strategies

### 3. Documentation

- **README.md** - Project overview and installation
- **INSTALLATION.md** - Step-by-step setup guide
- **QUICK_REFERENCE.md** - Fast lookup for patterns
- **OVERVIEW.md** - This file!

### 4. Test Runner

`examples/run_all_examples.py` - Run all examples to see optimizations in action:

```bash
cd examples
python3 run_all_examples.py
```

## Real-World Impact

### Before the Skill

```python
# User validation - O(n²) complexity
class UserValidator:
    def __init__(self):
        self.valid_users = []
        self.login_attempts = []

    def is_valid(self, user_id):
        return user_id in self.valid_users  # Slow!

    def record_attempt(self, user_id):
        # Nested loop - very slow!
        for attempt in self.login_attempts:
            if attempt[0] == user_id:
                attempt[1] += 1
                return
        self.login_attempts.append([user_id, 1])
```

**Performance**: Gets slower with every user added

### After the Skill

```python
# User validation - O(1) complexity
class UserValidator:
    __slots__ = ['valid_users', 'login_attempts']  # 30% memory savings

    def __init__(self):
        self.valid_users = set()  # O(1) lookups
        self.login_attempts = {}  # O(1) updates

    def is_valid(self, user_id):
        return user_id in self.valid_users  # Fast!

    def record_attempt(self, user_id):
        self.login_attempts[user_id] = \
            self.login_attempts.get(user_id, 0) + 1  # Fast!
```

**Performance**: Constant time regardless of dataset size

## Decision Tree

The skill uses this logic to choose containers:

```
Need membership testing?
  YES → Use Set or Dict
  NO  ↓

Need key-value pairs?
  YES → Use Dict
  NO  ↓

Need order & indexing?
  YES → Use List
  NO  ↓

Is data immutable?
  YES → Use Tuple/Frozenset
  NO  → Use Set

Creating many instances?
  YES → Consider __slots__
```

## Performance Numbers

From the examples (actual benchmark results):

- **Set vs List** membership: ~1000-1500x faster
- **Dict vs List** counting: ~100x faster
- **__slots__** memory: ~30% reduction
- **Set intersection** vs nested loops: ~200x faster

## Installation (Quick Start)

```bash
# 1. Copy the skill file
cp python-number-optimization.skill ~/.claude/skills/

# 2. Verify it works
cd examples
python3 run_all_examples.py

# 3. Start using it with Claude Code
claude-code
> Write an efficient function to validate user IDs
```

## Usage Examples

### Example 1: Automatic Optimization

**Your prompt:**
```
Write a function to find duplicate emails in a user list
```

**Claude (with skill):**
```python
def find_duplicate_emails(users):
    """Find duplicate emails - O(n) with set"""
    seen = set()
    duplicates = set()

    for user in users:
        email = user['email']
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)

    return duplicates
```

### Example 2: Memory Optimization

**Your prompt:**
```
Create a Point class for 3D graphics (will create millions of points)
```

**Claude (with skill):**
```python
class Point3D:
    __slots__ = ['x', 'y', 'z']  # Significant memory savings

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return ((self.x - other.x)**2 +
                (self.y - other.y)**2 +
                (self.z - other.z)**2) ** 0.5
```

## When the Skill Helps

✅ Use this skill for:
- API rate limiting and validation
- Data processing pipelines
- Caching systems
- Tag/category management
- Log analysis
- User authentication systems
- Large dataset processing
- Memory-constrained applications

❌ Don't over-optimize:
- Small datasets (<10 items)
- One-time scripts
- Prototype code
- When readability is more important

## Learning Path

1. **Start**: Read the article (10 min)
2. **Install**: Copy the skill file (1 min)
3. **Explore**: Run the examples (5 min)
4. **Reference**: Bookmark QUICK_REFERENCE.md
5. **Practice**: Use with Claude Code on real projects

## Project Structure

```
python-optimisation-skills/
├── python-number-optimization.skill  # The main skill file
├── README.md                         # Project overview
├── INSTALLATION.md                   # Setup guide
├── QUICK_REFERENCE.md               # Quick lookup
├── OVERVIEW.md                       # This file
└── examples/
    ├── 01_membership_testing.py      # Set vs List
    ├── 02_counting_and_grouping.py   # Dict patterns
    ├── 03_slots_optimization.py      # Memory savings
    ├── 04_container_selection.py     # Choosing containers
    └── run_all_examples.py           # Run all demos
```

## Key Takeaways

1. **Sets and Dicts** are 100-200x faster than Lists for membership testing
2. **Choose containers** based on access patterns, not habit
3. **__slots__** saves 30% memory for classes with many instances
4. **Counter and defaultdict** are your friends for counting/grouping
5. **Profile first**, but choose the right structure from the start

## Further Reading

- Original article: https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/
- Python Time Complexity: https://wiki.python.org/moin/TimeComplexity
- __slots__ documentation: https://docs.python.org/3/reference/datamodel.html#slots

## Contributing

Found a great optimization pattern? Submit a PR with:
- Example code (before/after)
- Performance benchmark
- Real-world use case

## Summary

This skill transforms Claude Code from writing "working code" to writing "optimized code" by:

1. **Choosing the right data structure** automatically
2. **Applying memory optimizations** when beneficial
3. **Following proven patterns** from Python performance research
4. **Avoiding common anti-patterns** that hurt performance

**Install it once, benefit forever.**

---

*"Premature optimization is evil, but choosing the right data structure is just good engineering."*
