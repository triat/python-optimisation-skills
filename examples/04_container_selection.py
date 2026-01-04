"""
Example 4: Container Selection Based on Use Case
Shows how to choose the right container for different scenarios.
"""

import time
from typing import List, Set, Dict


# Scenario 1: Filtering duplicates from a stream
# ❌ BEFORE: Using list (O(n²) due to membership checks)
def remove_duplicates_slow(items: List[int]) -> List[int]:
    """Remove duplicates while preserving order - O(n²) with list"""
    unique = []
    for item in items:
        if item not in unique:  # O(n) check for each item
            unique.append(item)
    return unique


# ✅ AFTER: Using set for tracking (O(n) overall)
def remove_duplicates_fast(items: List[int]) -> List[int]:
    """Remove duplicates while preserving order - O(n) with set"""
    seen = set()
    unique = []
    for item in items:
        if item not in seen:  # O(1) check
            seen.add(item)
            unique.append(item)
    return unique


# ✅ ALTERNATIVE: If order doesn't matter, just use set
def remove_duplicates_simple(items: List[int]) -> Set[int]:
    """Remove duplicates, order not preserved - simplest and fastest"""
    return set(items)


# Scenario 2: Tag-based filtering system
# ❌ BEFORE: Using lists for tags
class ArticleSlow:
    """Article with tags stored in list - slow for tag checks"""

    def __init__(self, title: str, tags: List[str]):
        self.title = title
        self.tags = tags  # List makes has_tag() slow

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags  # O(n) lookup

    def has_any_tags(self, search_tags: List[str]) -> bool:
        for tag in search_tags:
            if tag in self.tags:  # O(n*m) - very slow!
                return True
        return False


# ✅ AFTER: Using set for tags
class ArticleFast:
    """Article with tags stored in set - fast tag operations"""

    def __init__(self, title: str, tags: List[str]):
        self.title = title
        self.tags = set(tags)  # Convert to set for O(1) lookups

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags  # O(1) lookup

    def has_any_tags(self, search_tags: List[str]) -> bool:
        # O(m) where m is len(search_tags)
        return bool(self.tags & set(search_tags))  # Set intersection


# Scenario 3: Caching computed values
# ❌ BEFORE: Linear search through list of tuples
class ComputationCacheSlow:
    """Cache using list - O(n) lookups"""

    def __init__(self):
        self.cache = []  # List of (key, value) tuples

    def get(self, key: str):
        for k, v in self.cache:  # O(n) search
            if k == key:
                return v
        return None

    def set(self, key: str, value):
        # Check if exists first
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                self.cache[i] = (key, value)
                return
        self.cache.append((key, value))


# ✅ AFTER: Using dict for O(1) lookups
class ComputationCacheFast:
    """Cache using dict - O(1) lookups"""

    def __init__(self):
        self.cache = {}  # Dict for instant lookups

    def get(self, key: str):
        return self.cache.get(key)  # O(1)

    def set(self, key: str, value):
        self.cache[key] = value  # O(1)


# Scenario 4: Finding common elements between datasets
def find_common_elements_slow(list1: List[int], list2: List[int]) -> List[int]:
    """Find common elements - O(n*m) with lists"""
    common = []
    for item in list1:
        if item in list2 and item not in common:  # Two O(n) operations!
            common.append(item)
    return common


def find_common_elements_fast(list1: List[int], list2: List[int]) -> Set[int]:
    """Find common elements - O(n+m) with sets"""
    return set(list1) & set(list2)  # Set intersection is very fast


# Performance comparison
if __name__ == "__main__":
    # Test duplicate removal
    test_data = [i % 1000 for i in range(10000)]  # Many duplicates

    start = time.perf_counter()
    result_slow = remove_duplicates_slow(test_data)
    slow_time = time.perf_counter() - start

    start = time.perf_counter()
    result_fast = remove_duplicates_fast(test_data)
    fast_time = time.perf_counter() - start

    print("Duplicate Removal:")
    print(f"  List approach: {slow_time:.6f}s")
    print(f"  Set approach:  {fast_time:.6f}s")
    print(f"  Speedup: {slow_time/fast_time:.1f}x\n")

    # Test article tag filtering
    articles_slow = [
        ArticleSlow(f"Article {i}", [f"tag{j}" for j in range(i % 20)])
        for i in range(1000)
    ]
    articles_fast = [
        ArticleFast(f"Article {i}", [f"tag{j}" for j in range(i % 20)])
        for i in range(1000)
    ]

    search_tags = ["tag5", "tag10", "tag15"]

    start = time.perf_counter()
    slow_matches = sum(1 for a in articles_slow if a.has_any_tags(search_tags))
    slow_time = time.perf_counter() - start

    start = time.perf_counter()
    fast_matches = sum(1 for a in articles_fast if a.has_any_tags(search_tags))
    fast_time = time.perf_counter() - start

    print("Tag Filtering:")
    print(f"  List approach: {slow_time:.6f}s")
    print(f"  Set approach:  {fast_time:.6f}s")
    print(f"  Speedup: {slow_time/fast_time:.1f}x\n")

    # Test finding common elements
    data1 = list(range(10000))
    data2 = list(range(5000, 15000))

    start = time.perf_counter()
    common_slow = find_common_elements_slow(data1[:100], data2[:100])  # Small subset
    slow_time = time.perf_counter() - start

    start = time.perf_counter()
    common_fast = find_common_elements_fast(data1, data2)  # Full dataset
    fast_time = time.perf_counter() - start

    print("Finding Common Elements:")
    print(f"  List approach (100 items): {slow_time:.6f}s")
    print(f"  Set approach (10000 items): {fast_time:.6f}s")
    print(f"  Set handles 100x more data in similar time!\n")

    print("="*60)
    print("CONTAINER SELECTION GUIDE:")
    print("  List  → Ordered sequences, index access, iteration")
    print("  Set   → Membership testing, unique values, set operations")
    print("  Dict  → Key-value pairs, O(1) lookups by key")
    print("  Tuple → Immutable sequences, dict keys, unpacking")
    print("="*60)
