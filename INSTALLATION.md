# Installation Guide

## Installing the Python Optimization Skill for Claude Code

This guide will help you install and use the `python-number-optimization.skill` with Claude Code.

## Prerequisites

- Claude Code CLI installed and configured
- Basic familiarity with Claude Code skills

## Installation Steps

### Option 1: Global Installation (Recommended)

Install the skill globally to use it across all projects:

```bash
# Create the skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill file
cp python-number-optimization.skill ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/python-number-optimization.skill
```

**Linux/macOS**: `~/.claude/skills/`
**Windows**: `%USERPROFILE%\.claude\skills\`

### Option 2: Project-Specific Installation

Install the skill only for the current project:

```bash
# In your project directory
mkdir -p .claude/skills
cp python-number-optimization.skill .claude/skills/
```

### Option 3: Symlink (For Development)

Create a symlink to easily update the skill:

```bash
# Clone or navigate to this repository
cd /path/to/python-optimisation-skills

# Create global symlink
ln -s "$(pwd)/python-number-optimization.skill" ~/.claude/skills/python-number-optimization.skill

# Or project-specific
mkdir -p .claude/skills
ln -s "$(pwd)/python-number-optimization.skill" .claude/skills/python-number-optimization.skill
```

## Verifying Installation

1. Start Claude Code in any Python project
2. Type `/help` to see available skills
3. Look for `python-optimization` in the list

Or test directly:

```bash
# In your project directory
claude-code

# Ask Claude to use the skill
> Use the python-optimization skill to write a function that validates user IDs efficiently
```

## Using the Skill

### Automatic Usage

Once installed, Claude Code will automatically apply optimizations when:

- You request "optimized" or "efficient" code
- Working with collections or data structures
- The context involves membership testing or lookups
- Creating classes with many instances

### Explicit Invocation

You can explicitly invoke the skill:

```
Use the python-optimization skill to refactor this code for better performance
```

Or reference it in your requests:

```
Write an efficient function to filter unique user IDs from a large dataset
```

Claude will automatically select appropriate data structures (sets instead of lists, etc.).

## Examples of Skill Usage

### Example 1: User Validation

**Your prompt:**
```
Write a function to check if a user ID is in a list of approved users
```

**Without skill:**
```python
def is_approved(user_id, approved_users):
    if user_id in approved_users:  # List - O(n)
        return True
    return False
```

**With skill:**
```python
def is_approved(user_id, approved_users_set):
    """Check if user is approved - O(1) lookup with set"""
    if user_id in approved_users_set:  # Set - O(1)
        return True
    return False

# Usage:
approved = {100, 200, 300, 400}  # Automatically suggests set
```

### Example 2: Data Processing

**Your prompt:**
```
Create a class to store sensor readings with timestamp and temperature
```

**Without skill:**
```python
class SensorReading:
    def __init__(self, timestamp, temperature):
        self.timestamp = timestamp
        self.temperature = temperature
```

**With skill:**
```python
class SensorReading:
    __slots__ = ['timestamp', 'temperature']  # 30% memory savings

    def __init__(self, timestamp, temperature):
        self.timestamp = timestamp
        self.temperature = temperature
```

### Example 3: Counting Operations

**Your prompt:**
```
Count how many times each word appears in a list
```

**Without skill:**
```python
def count_words(words):
    counts = []
    for word in words:
        found = False
        for item in counts:
            if item[0] == word:
                item[1] += 1
                found = True
                break
        if not found:
            counts.append([word, 1])
    return counts
```

**With skill:**
```python
from collections import Counter

def count_words(words):
    """Count word occurrences - O(n) with Counter"""
    return Counter(words)

# Or using dict:
def count_words_dict(words):
    """Count word occurrences - O(n) with dict"""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
```

## Testing the Examples

Run the included examples to see the optimizations in action:

```bash
cd examples
python run_all_examples.py
```

This will demonstrate:
- Performance differences between list and set membership testing
- Efficient counting and grouping patterns
- Memory savings with `__slots__`
- Container selection strategies

## Quick Reference

Keep `QUICK_REFERENCE.md` handy for:
- Container selection decision tree
- Performance comparison tables
- Common optimization patterns
- Anti-patterns to avoid

## Troubleshooting

### Skill Not Found

If Claude Code doesn't recognize the skill:

1. Check installation path:
   ```bash
   ls -la ~/.claude/skills/python-number-optimization.skill
   ```

2. Verify file permissions:
   ```bash
   chmod 644 ~/.claude/skills/python-number-optimization.skill
   ```

3. Restart Claude Code

### Skill Not Being Applied

If optimizations aren't being applied:

1. Be explicit in your request:
   ```
   Write an EFFICIENT function to...
   ```

2. Mention performance:
   ```
   I need this to be fast for large datasets
   ```

3. Explicitly invoke:
   ```
   Use python-optimization skill to...
   ```

## Updating the Skill

To update the skill:

```bash
# If you used symlink (recommended for development)
cd /path/to/python-optimisation-skills
git pull

# If you copied the file
cp python-number-optimization.skill ~/.claude/skills/
```

## Uninstallation

To remove the skill:

```bash
# Global installation
rm ~/.claude/skills/python-number-optimization.skill

# Project-specific
rm .claude/skills/python-number-optimization.skill
```

## Learn More

- Read `README.md` for overview and key concepts
- Check `QUICK_REFERENCE.md` for quick lookup
- Run examples in `examples/` directory
- Review the article: https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/

## Support

For issues or improvements:
1. Check the examples work correctly
2. Review the skill file for patterns
3. Test with explicit skill invocation
4. Submit feedback or improvements to the repository

---

**Happy optimizing!** Remember: choose the right data structure from the start, and you won't need to optimize later.
