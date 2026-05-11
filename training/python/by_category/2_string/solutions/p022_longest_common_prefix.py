"""P022 Longest Common Prefix (LeetCode 14)
Time: O(n*m), Space: O(1)
"""


def solve(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == '__main__':
    print(solve(["flower", "flow", "flight"]))  # expected: "fl"
    print(solve(["dog", "racecar", "car"]))     # expected: ""


#def solve(strs):
#    """Default: horizontal scanning (shrink prefix)."""
#    return solve_shrink_prefix(strs)
#
#
#def solve_vertical_scan(strs):
#    """Compare characters by column using the first word as reference."""
#    if not strs:
#        return ""
#
#    first = strs[0]
#    i = 0
#    while i < len(first):
#        ch = first[i]
#        j = 1
#        while j < len(strs):
#            if i >= len(strs[j]) or strs[j][i] != ch:
#                return first[:i]
#            j += 1
#        i += 1
#    return first
#
#
#def solve_shrink_prefix(strs):
#    """Start with first word as candidate prefix, shrink until all match."""
#    if not strs:
#        return ""
#
#    prefix = strs[0]
#    i = 1
#    while i < len(strs):
#        word = strs[i]
#        while not word.startswith(prefix):
#            prefix = prefix[:-1]
#            if prefix == "":
#                return ""
#        i += 1
#    return prefix
#
#
#def solve_sorting(strs):
#    """Sort, then LCP is the common prefix of first and last words."""
#    if not strs:
#        return ""
#
#    words = sorted(strs)
#    first = words[0]
#    last = words[-1]
#    i = 0
#    while i < len(first) and i < len(last) and first[i] == last[i]:
#        i += 1
#    return first[:i]
#
#
#def solve_divide_conquer(strs):
#    """Recursively compute LCP on left/right halves, then merge."""
#    if not strs:
#        return ""
#
#    def lcp_two(a, b):
#        i = 0
#        while i < len(a) and i < len(b) and a[i] == b[i]:
#            i += 1
#        return a[:i]
#
#    def helper(left, right):
#        if left == right:
#            return strs[left]
#        mid = (left + right) // 2
#        l = helper(left, mid)
#        r = helper(mid + 1, right)
#        return lcp_two(l, r)
#
#    return helper(0, len(strs) - 1)
#
#if __name__ == '__main__':
#    case1 = ["flower", "flow", "flight"]
#    case2 = ["dog", "racecar", "car"]
#
#    print("default:", solve(case1), solve(case2))
#    print("vertical:", solve_vertical_scan(case1), solve_vertical_scan(case2))
#    print("shrink:", solve_shrink_prefix(case1), solve_shrink_prefix(case2))
#    print("sorting:", solve_sorting(case1), solve_sorting(case2))
#    print("divide:", solve_divide_conquer(case1), solve_divide_conquer(case2))

