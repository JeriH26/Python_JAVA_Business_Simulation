# OA Variant Problems (English Full Statements)

This file contains full English problem statements for the variant task set.
Each problem includes a Python-oriented signature, description, constraints, and example.

## V001 Two Sum II (Sorted Array)
- Signature: solve(numbers, target) -> list[int]
- Description: Given a non-decreasing sorted array numbers, return the 1-based indices of two numbers whose sum equals target. Exactly one valid answer exists.
- Constraints: 2 <= len(numbers) <= 10^5
- Example: numbers=[2,7,11,15], target=9 -> [1,2]

## V002 Count Pairs Equal to Target
- Signature: solve(nums, target) -> int
- Description: Count how many index pairs (i < j) satisfy nums[i] + nums[j] == target.
- Constraints: 1 <= len(nums) <= 2 * 10^5
- Example: nums=[1,1,2,2,3], target=4 -> 2

## V003 Group Anagrams
- Signature: solve(words) -> list[list[str]]
- Description: Group strings that are anagrams of each other. Output order does not matter.
- Constraints: 1 <= len(words) <= 10^4
- Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]

## V004 Find All Anagram Starts
- Signature: solve(s, p) -> list[int]
- Description: Return all starting indices in s where the substring is an anagram of p.
- Constraints: 1 <= len(s), len(p) <= 3 * 10^4
- Example: s="cbaebabacd", p="abc" -> [0,6]

## V005 Remove Element In Place
- Signature: solve(nums, val) -> int
- Description: Remove all occurrences of val in-place and return the new length k. The first k elements must contain the kept values.
- Constraints: 0 <= len(nums) <= 10^5
- Example: nums=[3,2,2,3], val=3 -> 2

## V006 Stable Sort by Parity
- Signature: solve(nums) -> list[int]
- Description: Return a new list where all even values appear before odd values, while preserving relative order within the even group and within the odd group.
- Constraints: 1 <= len(nums) <= 10^5
- Example: [3,1,2,4] -> [2,4,3,1]

## V007 Trapping Rain Water
- Signature: solve(height) -> int
- Description: Given bar heights, compute the total amount of trapped rain water.
- Constraints: 1 <= len(height) <= 2 * 10^5
- Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6

## V008 Max Area After One Swap
- Signature: solve(height) -> int
- Description: You may swap at most one pair of bars before choosing two sides of a container. Return the maximum possible area.
- Constraints: 2 <= len(height) <= 200 for the training version
- Example: [1,2,4,3] -> 4

## V009 Longest Repeating Character Replacement
- Signature: solve(s, k) -> int
- Description: Replace at most k characters so the chosen substring contains only one repeated character. Return the maximum possible length.
- Constraints: 1 <= len(s) <= 10^5
- Example: s="AABABBA", k=1 -> 4

## V010 Minimum Window Substring
- Signature: solve(s, t) -> str
- Description: Return the smallest substring of s that contains all characters of t with multiplicity. Return an empty string if impossible.
- Constraints: 1 <= len(s), len(t) <= 10^5
- Example: s="ADOBECODEBANC", t="ABC" -> "BANC"

## V011 Minimum Remove to Make Valid Parentheses
- Signature: solve(s) -> str
- Description: Remove the minimum number of parentheses so the resulting string is valid. Return any valid answer.
- Constraints: 1 <= len(s) <= 10^5
- Example: "a)b(c)d" -> "ab(c)d"

## V012 Remove Outermost Parentheses
- Signature: solve(s) -> str
- Description: s is a valid parentheses string made of primitive groups. Remove the outermost pair from each primitive group.
- Constraints: 1 <= len(s) <= 10^5
- Example: "(()())(())" -> "()()()"

## V013 First Bad Version
- Signature: solve(n, is_bad) -> int
- Description: Versions 1..n become bad from some point onward. Use is_bad(version) to find the first bad version.
- Constraints: 1 <= n <= 2 * 10^9
- Example: n=5, first bad=4 -> 4

## V014 Find Peak Element
- Signature: solve(nums) -> int
- Description: Return any index i such that nums[i] is strictly greater than its neighbors.
- Constraints: 1 <= len(nums) <= 10^5
- Example: [1,2,3,1] -> 2

## V015 Lower Bound and Upper Bound
- Signature: solve(nums, target) -> tuple[int, int]
- Description: Return the first index >= target and the first index > target. If not found, return len(nums) for that position.
- Constraints: 0 <= len(nums) <= 10^5
- Example: nums=[1,2,2,2,4], target=2 -> (1,4)

## V016 Search Range
- Signature: solve(nums, target) -> list[int]
- Description: Return the first and last index of target in sorted nums, or [-1,-1] if absent.
- Constraints: 0 <= len(nums) <= 10^5
- Example: [5,7,7,8,8,10], target=8 -> [3,4]

## V017 Binary Tree Zigzag Level Order
- Signature: solve(root) -> list[list[int]]
- Description: Return level order traversal where the direction alternates on each level.
- Constraints: Number of nodes <= 2 * 10^5
- Example: [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]

## V018 Binary Tree Right Side View
- Signature: solve(root) -> list[int]
- Description: Return the values visible from the right side of the tree.
- Constraints: Number of nodes <= 2 * 10^5
- Example: [1,2,3,null,5,null,4] -> [1,3,4]

## V019 Min Cost Climbing Stairs
- Signature: solve(cost) -> int
- Description: You may start at step 0 or 1 and climb 1 or 2 steps each move. Pay cost when stepping on an index. Return minimum total cost to reach the top.
- Constraints: 2 <= len(cost) <= 10^5
- Example: [10,15,20] -> 15

## V020 House Robber
- Signature: solve(nums) -> int
- Description: Return the maximum amount that can be robbed without robbing adjacent houses.
- Constraints: 1 <= len(nums) <= 10^5
- Example: [2,7,9,3,1] -> 12

## V021 3Sum Closest
- Signature: solve(nums, target) -> int
- Description: Choose three numbers whose sum is closest to target and return that sum.
- Constraints: 3 <= len(nums) <= 3000
- Example: nums=[-1,2,1,-4], target=1 -> 2

## V022 4Sum
- Signature: solve(nums, target) -> list[list[int]]
- Description: Return all unique quadruplets that sum to target.
- Constraints: 1 <= len(nums) <= 200
- Example: nums=[1,0,-1,0,-2,2], target=0 -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

## V023 Insert Interval
- Signature: solve(intervals, new_interval) -> list[list[int]]
- Description: Insert new_interval into sorted non-overlapping intervals and merge where needed.
- Constraints: 0 <= len(intervals) <= 10^4
- Example: [[1,3],[6,9]], [2,5] -> [[1,5],[6,9]]

## V024 Non-overlapping Intervals
- Signature: solve(intervals) -> int
- Description: Return the minimum number of intervals to remove so the rest do not overlap.
- Constraints: 1 <= len(intervals) <= 10^5
- Example: [[1,2],[2,3],[3,4],[1,3]] -> 1

## V025 K Closest Points to Origin
- Signature: solve(points, k) -> list[list[int]]
- Description: Return any k points closest to the origin.
- Constraints: 1 <= len(points) <= 10^5
- Example: points=[[1,3],[-2,2]], k=1 -> [[-2,2]]

## V026 Top K Frequent Words
- Signature: solve(words, k) -> list[str]
- Description: Return the k most frequent words. If frequencies tie, smaller lexicographic order comes first.
- Constraints: 1 <= len(words) <= 10^5
- Example: ["i","love","leetcode","i","love","coding"], k=2 -> ["i","love"]

## V027 Max Area of Island
- Signature: solve(grid) -> int
- Description: In a 0/1 grid, return the largest 4-directionally connected area of 1s.
- Constraints: 1 <= rows, cols <= 500
- Example: [[0,0,1],[1,1,1],[0,1,0]] -> 5

## V028 Number of Closed Islands
- Signature: solve(grid) -> int
- Description: In a 0/1 grid where 0 is land, count connected land components that do not touch the border.
- Constraints: 1 <= rows, cols <= 500

## V029 Kth Smallest in Sorted Matrix
- Signature: solve(matrix, k) -> int
- Description: Each row and column is sorted ascending. Return the kth smallest value.
- Constraints: 1 <= n <= 300
- Example: [[1,5,9],[10,11,13],[12,13,15]], k=8 -> 13

## V030 Median from Data Stream
- Signature: class MedianFinder with add_num(x), find_median() -> float
- Description: Support streaming inserts and median queries at any time.
- Constraints: Number of operations <= 2 * 10^5
- Example: add 1,2 -> 1.5; add 3 -> 2

## V031 LFU Cache
- Signature: class LFUCache(capacity), get(key), put(key, value)
- Description: Implement LFU eviction. Break ties by least recently used.
- Constraint target: get and put should be O(1) average.

## V032 Browser History Design
- Signature: class BrowserHistory(homepage), visit(url), back(steps), forward(steps)
- Description: Simulate browser history with back and forward navigation.
- Constraints: Number of operations <= 2 * 10^5
