# Python OA Variant Problem Bank

This bank turns each core topic into concrete, practice-ready variant questions.
Each question uses a short original description and expected function signature.

Directory layout:
- training/python/variant_bank/solutions/: worked Python examples for V001 to V032
- training/python/variant_bank/practice/: TODO Python templates for V001 to V032
- training/python/variant_bank/VARIANT_PROBLEMS.md: full English statements

5-day execution list:
- training/python/variant_bank/5DAY_VARIANT_TASKS.md

Full problem statements:
- training/python/variant_bank/VARIANT_PROBLEMS.md

## How to Use

1. Pick 1 core topic from p001 to p015.
2. Solve Variant A in 20 minutes.
3. Solve Variant B in 20 minutes.
4. Explain what changed from the core pattern.

Run all worked examples:
- bash training/python/variant_bank/run.sh

Open the practice guide:
- bash training/python/variant_bank/run_practice.sh

## Hash / Counting

### V001 Two Sum II (Sorted)
- Signature: solve(numbers, target) -> list[int]
- Prompt: numbers is sorted ascending. Return 1-based indices of two values whose sum is target. Exactly one answer exists.
- Example: numbers=[2,7,11,15], target=9 -> [1,2]

### V002 Pair Count Equals Target
- Signature: solve(nums, target) -> int
- Prompt: Count how many unique index pairs (i < j) satisfy nums[i] + nums[j] == target.
- Example: nums=[1,1,2,2,3], target=4 -> 2

### V003 Group Anagrams
- Signature: solve(words) -> list[list[str]]
- Prompt: Group words that are anagrams of each other.
- Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]

### V004 Find All Anagram Starts
- Signature: solve(s, p) -> list[int]
- Prompt: Return all start indices of substrings in s that are anagrams of p.
- Example: s="cbaebabacd", p="abc" -> [0,6]

## Two Pointers / Array

### V005 Remove Element In-Place
- Signature: solve(nums, val) -> int
- Prompt: Remove all val in-place and return the new length. The first k items should be valid remaining values.
- Example: nums=[3,2,2,3], val=3 -> 2

### V006 Sort by Parity (Stable)
- Signature: solve(nums) -> list[int]
- Prompt: Return array where all even values come before odd values while preserving relative order inside each group.
- Example: [3,1,2,4] -> [2,4,3,1]

### V007 Trapping Rain Water
- Signature: solve(height) -> int
- Prompt: Given bar heights, compute total trapped water.
- Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6

### V008 Max Area After One Swap
- Signature: solve(height) -> int
- Prompt: You may swap at most one pair of bars before choosing container boundaries. Return maximum area possible.
- Example: [1,2,4,3] -> 4

## Sliding Window

### V009 Longest Repeating Replacement
- Signature: solve(s, k) -> int
- Prompt: Replace at most k chars so the window becomes all same letter. Return max window length.
- Example: s="AABABBA", k=1 -> 4

### V010 Minimum Window Cover
- Signature: solve(s, t) -> str
- Prompt: Return the smallest substring of s containing all chars in t with multiplicity.
- Example: s="ADOBECODEBANC", t="ABC" -> "BANC"

## Stack / Parentheses

### V011 Minimum Remove to Valid
- Signature: solve(s) -> str
- Prompt: Remove the minimum number of parentheses to make the string valid.
- Example: "a)b(c)d" -> "ab(c)d"

### V012 Remove Outermost Parentheses
- Signature: solve(s) -> str
- Prompt: s is a valid parentheses sequence composed of primitive blocks. Remove outermost pair from each block.
- Example: "(()())(())" -> "()()()"

## Binary Search Family

### V013 First Bad Version
- Signature: solve(n, is_bad) -> int
- Prompt: Versions 1..n, once bad then all later are bad. Return first bad version.
- Example: first bad=4 in n=5 -> 4

### V014 Find Peak Element
- Signature: solve(nums) -> int
- Prompt: Return index i where nums[i] is greater than neighbors.
- Example: [1,2,3,1] -> 2

### V015 Lower and Upper Bound
- Signature: solve(nums, target) -> tuple[int,int]
- Prompt: Return first index >= target and first index > target.
- Example: nums=[1,2,2,2,4], target=2 -> (1,4)

### V016 Search Range
- Signature: solve(nums, target) -> list[int]
- Prompt: Return first and last index of target in sorted nums; if missing return [-1,-1].
- Example: [5,7,7,8,8,10], target=8 -> [3,4]

## Tree / BFS

### V017 Zigzag Level Order
- Signature: solve(root) -> list[list[int]]
- Prompt: Return level order traversal, alternating direction each level.
- Example: [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]

### V018 Right Side View
- Signature: solve(root) -> list[int]
- Prompt: Return values visible when viewing binary tree from right side.
- Example: [1,2,3,null,5,null,4] -> [1,3,4]

## DP Basics

### V019 Min Cost Climbing Stairs
- Signature: solve(cost) -> int
- Prompt: You can start at step 0 or 1. Each move climb 1 or 2. Pay cost at stepped index. Return minimum total cost to reach top.
- Example: [10,15,20] -> 15

### V020 House Robber
- Signature: solve(nums) -> int
- Prompt: Max money without robbing adjacent houses.
- Example: [2,7,9,3,1] -> 12

## Sort + Two Pointers

### V021 3Sum Closest
- Signature: solve(nums, target) -> int
- Prompt: Return sum of 3 numbers closest to target.
- Example: nums=[-1,2,1,-4], target=1 -> 2

### V022 4Sum
- Signature: solve(nums, target) -> list[list[int]]
- Prompt: Return unique quadruplets summing to target.
- Example: nums=[1,0,-1,0,-2,2], target=0 -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

## Intervals

### V023 Insert Interval
- Signature: solve(intervals, new_interval) -> list[list[int]]
- Prompt: Insert and merge new interval into sorted non-overlapping intervals.
- Example: [[1,3],[6,9]], [2,5] -> [[1,5],[6,9]]

### V024 Non-overlapping Intervals
- Signature: solve(intervals) -> int
- Prompt: Return minimum number of intervals to remove so the rest do not overlap.
- Example: [[1,2],[2,3],[3,4],[1,3]] -> 1

## Heap / Top K

### V025 K Closest Points
- Signature: solve(points, k) -> list[list[int]]
- Prompt: Return any k points closest to origin.
- Example: points=[[1,3],[-2,2]], k=1 -> [[-2,2]]

### V026 Top K Frequent Words
- Signature: solve(words, k) -> list[str]
- Prompt: Return k most frequent words; if same frequency, lexicographically smaller first.
- Example: words=["i","love","leetcode","i","love","coding"], k=2 -> ["i","love"]

## Graph / Grid

### V027 Max Area of Island
- Signature: solve(grid) -> int
- Prompt: In a 0/1 grid, return largest connected component area of 1s (4-directional).
- Example: [[0,0,1],[1,1,1],[0,1,0]] -> 5

### V028 Number of Closed Islands
- Signature: solve(grid) -> int
- Prompt: In a 0/1 grid where 0 is land, count land components fully surrounded by water and not touching border.
- Example: standard test should return > 0 depending on map

## Selection / Stream

### V029 Kth Smallest in Sorted Matrix
- Signature: solve(matrix, k) -> int
- Prompt: Rows and columns are sorted ascending. Return kth smallest value.
- Example: [[1,5,9],[10,11,13],[12,13,15]], k=8 -> 13

### V030 Median from Data Stream
- Signature: class MedianFinder with add_num(x), find_median() -> float
- Prompt: Support streaming inserts and median query at any time.
- Example: add 1,2 => 1.5; add 3 => 2

## Bonus Design

### V031 LFU Cache
- Signature: class LFUCache(capacity), get(key), put(key,val)
- Prompt: Evict least frequently used key. Tie-breaker: least recently used.

### V032 Browser History Design
- Signature: class BrowserHistory(homepage), visit(url), back(steps), forward(steps)
- Prompt: Simulate browser navigation with efficient movement.
