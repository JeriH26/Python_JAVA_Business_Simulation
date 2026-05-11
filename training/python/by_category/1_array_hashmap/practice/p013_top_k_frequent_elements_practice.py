"""P013 Top K Frequent Elements Practice
Algorithm: Hash map + min-heap
TODO: implement solve(nums, k)
"""


def solve(nums, k):
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = []
    for num, count in freq.items():
        result.append((num, count))

    result.sort(key=lambda x: x[-1], reverse = True)
    print(result)

    ans = []
    for i in range(k):
        ans.append(result[i][0])
    return ans




if __name__ == '__main__':
    print(solve([1, 1, 1, 2, 2, 3], 2))  # expected: [1, 2] (order can vary)
