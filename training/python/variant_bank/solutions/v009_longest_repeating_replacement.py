"""V009 Longest Repeating Character Replacement
Time: O(n), Space: O(1)
"""

from collections import defaultdict


def solve(s, k):
    counts = defaultdict(int)
    left = 0
    max_count = 0
    best = 0

    for right, ch in enumerate(s):
        counts[ch] += 1
        max_count = max(max_count, counts[ch])

        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == '__main__':
    print(solve("AABABBA", 1))
