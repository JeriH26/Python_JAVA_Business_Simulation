"""V010 Minimum Window Substring
Time: O(n), Space: O(m)
"""

from collections import Counter


def solve(s, t):
    need = Counter(t)
    missing = len(t)
    left = 0
    best_start = 0
    best_len = float('inf')

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        while missing == 0:
            if right - left + 1 < best_len:
                best_start = left
                best_len = right - left + 1

            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    if best_len == float('inf'):
        return ''
    return s[best_start:best_start + best_len]


if __name__ == '__main__':
    print(solve("ADOBECODEBANC", "ABC"))
