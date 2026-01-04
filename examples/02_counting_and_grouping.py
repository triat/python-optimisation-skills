"""
Example 2: Counting and Grouping Optimization
Shows efficient patterns for counting occurrences and grouping data.
"""

from collections import Counter, defaultdict

# ❌ BEFORE: Inefficient counting with nested loops
def count_words_slow(words):
    """Count word occurrences using list - O(n²) complexity"""
    counts = []
    for word in words:
        found = False
        for count_item in counts:
            if count_item[0] == word:
                count_item[1] += 1
                found = True
                break
        if not found:
            counts.append([word, 1])
    return counts


# ✅ AFTER: Efficient counting with dict - O(n) complexity
def count_words_fast(words):
    """Count word occurrences using dict - O(n) complexity"""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


# ✅ BEST: Using Counter from collections
def count_words_best(words):
    """Count word occurrences using Counter - O(n) and most readable"""
    return Counter(words)


# Real-world example: Log analysis
# ❌ BEFORE: Inefficient grouping
def analyze_logs_slow(log_entries):
    """Group log entries by severity level - inefficient"""
    grouped = []
    for entry in log_entries:
        level = entry['level']
        found = False
        for group in grouped:
            if group['level'] == level:
                group['entries'].append(entry)
                found = True
                break
        if not found:
            grouped.append({'level': level, 'entries': [entry]})
    return grouped


# ✅ AFTER: Efficient grouping with defaultdict
def analyze_logs_fast(log_entries):
    """Group log entries by severity level - efficient O(n)"""
    grouped = defaultdict(list)
    for entry in log_entries:
        grouped[entry['level']].append(entry)
    return dict(grouped)  # Convert to regular dict if needed


# ✅ ALTERNATIVE: Using dict.setdefault
def analyze_logs_alternative(log_entries):
    """Group log entries using setdefault - also efficient"""
    grouped = {}
    for entry in log_entries:
        grouped.setdefault(entry['level'], []).append(entry)
    return grouped


# Performance comparison
if __name__ == "__main__":
    import time
    import random

    # Generate test data
    words = [random.choice(['apple', 'banana', 'cherry', 'date', 'elderberry'])
             for _ in range(10000)]

    # Test slow version
    start = time.perf_counter()
    result_slow = count_words_slow(words)
    slow_time = time.perf_counter() - start

    # Test fast version
    start = time.perf_counter()
    result_fast = count_words_fast(words)
    fast_time = time.perf_counter() - start

    # Test Counter version
    start = time.perf_counter()
    result_best = count_words_best(words)
    best_time = time.perf_counter() - start

    print(f"Slow (list) approach: {slow_time:.6f}s")
    print(f"Fast (dict) approach: {fast_time:.6f}s")
    print(f"Best (Counter) approach: {best_time:.6f}s")
    print(f"\nDict is {slow_time/fast_time:.1f}x faster than list")
    print(f"Counter is {slow_time/best_time:.1f}x faster than list")
