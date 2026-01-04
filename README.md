# Python Optimization Skill for Claude Code

A Claude Code skill that optimizes Python code generation by selecting the most efficient data structures and number handling strategies based on real-world performance and memory characteristics.

## Overview

This skill teaches Claude Code to write more efficient Python code by understanding:
- Memory characteristics of Python numbers and collections
- Performance implications of different data structures
- When to use sets vs lists vs dicts
- Memory optimization techniques like `__slots__`

## Based On

This skill implements best practices from the article ["Python Numbers Every Programmer Should Know"](https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/) by Michael Kennedy.

## Key Optimizations

### 1. Smart Container Selection
- **Sets/Dicts for membership testing**: 200x faster than lists for `x in container` checks
- **Lists for ordered sequences**: Most memory-efficient for iteration
- **Proper usage based on access patterns**

### 2. Memory Optimization
- Use `__slots__` for classes with many instances (30% memory reduction)
- Understanding memory footprint: Lists (36KB) < Sets (59.6KB) < Dicts (90.7KB) per 1000 integers

### 3. Performance Patterns
- O(1) lookups with sets/dicts instead of O(n) with lists
- Efficient counting with `Counter` or dict
- Fast unique value extraction with sets

## Installation

To use this skill with Claude Code:

1. Copy `python-number-optimization.skill` to your Claude Code skills directory:
   - **Linux/macOS**: `~/.claude/skills/`
   - **Windows**: `%USERPROFILE%\.claude\skills\`

2. Or reference it in your project-specific `.claude/skills/` directory

## Usage

Once installed, Claude Code will automatically apply these optimizations when:
- You ask for "optimized" or "efficient" Python code
- Working with collections and data structures
- The code involves membership testing or lookups
- Creating classes with many instances

You can also explicitly invoke it:
```
Use the python-optimization skill to write a function that checks if user IDs are valid
```

## Examples

See `examples/` directory for before/after code samples demonstrating:
- Membership testing optimization
- Counting and grouping patterns
- Class memory optimization with `__slots__`
- Container selection for different use cases

## Performance Quick Reference

| Operation | Best Container | Complexity |
|-----------|---------------|------------|
| Membership test (`x in y`) | Set/Dict | O(1) |
| Ordered iteration | List | O(n) |
| Key-value lookup | Dict | O(1) |
| Memory-efficient storage | List | 36KB/1000 ints |
| Unique values | Set | O(n) dedup |

## Contributing

To improve this skill:
1. Test it with various Python coding scenarios
2. Submit improvements based on real-world usage
3. Add more patterns and anti-patterns

## License

MIT
