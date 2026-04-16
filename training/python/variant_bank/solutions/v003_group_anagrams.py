"""V003 Group Anagrams
Time: O(n * k log k), Space: O(n * k)
"""

from collections import defaultdict


def solve(words):
    groups = defaultdict(list)
    for word in words:
        groups[''.join(sorted(word))].append(word)
    return list(groups.values())


if __name__ == '__main__':
    print(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))
