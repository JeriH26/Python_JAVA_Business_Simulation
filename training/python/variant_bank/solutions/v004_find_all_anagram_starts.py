"""V004 Find All Anagram Starts
Time: O(n), Space: O(1)
"""

from collections import Counter


def solve(s, p):
    if len(p) > len(s):
        return []

    need = Counter(p)
    window = Counter(s[:len(p)])
    ans = []

    if window == need:
        ans.append(0)

    for right in range(len(p), len(s)):
        left = right - len(p)
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        window[s[right]] += 1
        if window == need:
            ans.append(left + 1)

    return ans


if __name__ == '__main__':
    print(solve("cbaebabacd", "abc"))
