"""V026 Top K Frequent Words
Time: O(n log n), Space: O(n)
"""

from collections import Counter


def solve(words, k):
    freq = Counter(words)
    ordered = sorted(freq.keys(), key=lambda word: (-freq[word], word))
    return ordered[:k]


if __name__ == '__main__':
    print(solve(["i", "love", "leetcode", "i", "love", "coding"], 2))
