"""
Example 1: Membership Testing Optimization
Demonstrates the performance difference between list and set for membership checks.
"""

# ❌ BEFORE: Using list for membership testing (O(n) - SLOW)
def validate_user_slow(user_id, valid_users):
    """Check if user_id is in valid_users list - O(n) operation"""
    valid_users_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    if user_id in valid_users_list:  # Gets slower with more items
        return True
    return False


# ✅ AFTER: Using set for membership testing (O(1) - FAST)
def validate_user_fast(user_id, valid_users):
    """Check if user_id is in valid_users set - O(1) operation"""
    valid_users_set = {100, 200, 300, 400, 500, 600, 700, 800, 900, 1000}
    if user_id in valid_users_set:  # Constant time lookup
        return True
    return False


# Real-world example: API rate limiting
# ❌ BEFORE: Inefficient
class RateLimiterSlow:
    def __init__(self):
        self.blocked_ips = []  # Will be checked frequently

    def is_blocked(self, ip_address):
        return ip_address in self.blocked_ips  # O(n) - gets slower over time

    def block_ip(self, ip_address):
        if ip_address not in self.blocked_ips:  # Another O(n) check
            self.blocked_ips.append(ip_address)


# ✅ AFTER: Optimized
class RateLimiterFast:
    def __init__(self):
        self.blocked_ips = set()  # O(1) lookups

    def is_blocked(self, ip_address):
        return ip_address in self.blocked_ips  # O(1) - always fast

    def block_ip(self, ip_address):
        self.blocked_ips.add(ip_address)  # O(1) - automatically handles duplicates


# Performance demonstration
if __name__ == "__main__":
    import time

    # Test with larger dataset
    test_ids = list(range(1, 10001))  # 10,000 IDs

    # Test list performance
    valid_list = test_ids[:]
    start = time.perf_counter()
    for _ in range(1000):
        _ = 9999 in valid_list  # Worst case: item at end
    list_time = time.perf_counter() - start

    # Test set performance
    valid_set = set(test_ids)
    start = time.perf_counter()
    for _ in range(1000):
        _ = 9999 in valid_set  # Constant time regardless of position
    set_time = time.perf_counter() - start

    print(f"List lookup time: {list_time:.6f}s")
    print(f"Set lookup time:  {set_time:.6f}s")
    print(f"Set is {list_time/set_time:.1f}x faster!")
