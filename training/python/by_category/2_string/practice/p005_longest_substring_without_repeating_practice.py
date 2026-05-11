"""P005 Longest Substring Without Repeating Practice
Algorithm: Sliding window with hash set/map
TODO: implement solve(s)
"""


def solve(s):
    #left = 0
    #count = {}
    #best = 0
    #for right, ch in enumerate(s):
    #    if ch in count and count[ch] >= left:
    #        left = count[ch] + 1
    #    count[ch] = right
    #    best = max(best, right - left + 1)
    #return best

    #best = 0
    #n = len(s)
    #for i in range(n):
    #    for j in range(i+1, n+1):
    #        sub = s[i:j]
    #        if len(set(sub)) == len(sub):
    #            best = max(best, len(sub))
    #return best

    best = 0
    n = len(s)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j-i+1)
    return best


if __name__ == '__main__':
    print(solve('abcabcbb'))  # expected: 3
    print(solve('bbbbb'))     # expected: 1
