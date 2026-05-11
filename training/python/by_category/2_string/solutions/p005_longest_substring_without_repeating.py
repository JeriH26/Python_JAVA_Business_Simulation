"""P005 Longest Substring Without Repeating Characters
Time: O(n), Space: O(min(n, alphabet))
"""

def solve(s):
    left = 0
    best = 0
    index = {}
    for right, ch in enumerate(s):
        if ch in index and index[ch] >= left:
            left = index[ch] + 1
        index[ch] = right
        best = max(best, right - left + 1)
    return best

    #n = len(s)
    #best = 0
    #for i in range(n):
    #    seen = set()
    #    for j in range(i,n):
    #        if s[j] in seen:
    #            break
    #        seen.add(s[j])
    #        best = max(best, j-i+1)
    #return best

    #n = len(s)
    #best = 0
    #for i in range(n):
    #    for j in range(i+1, n+1):
    #        sub = s[i:j]
    #        if len(set(sub)) == len(sub):
    #            best = max(best, len(sub))
    #return best


if __name__ == '__main__':
    print(solve('abcabcbb'))
    print(solve('bbbbb'))
