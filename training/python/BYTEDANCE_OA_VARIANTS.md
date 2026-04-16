# Bytedance OA Variant Drill (15 Core Problems)

Use this with the 5-day plan.
For each core problem, train 2 common OA variants and one migration key.

Concrete variant problem bank:
- training/python/variant_bank/README.md

## p001 Two Sum
- Variant A: Two Sum II (sorted array, return 1-based indices)
- Variant B: Two Sum - count pairs or all pairs
- Migration key: hash table to two pointers when input is sorted

## p002 Valid Anagram
- Variant A: Group Anagrams
- Variant B: Find All Anagrams in a String
- Migration key: fixed-size frequency array and sliding window

## p003 Move Zeroes
- Variant A: Remove Element (in-place compaction)
- Variant B: Sort Array by Parity (stable two-pointer style)
- Migration key: write pointer for kept elements

## p004 Container With Most Water
- Variant A: Trapping Rain Water
- Variant B: Max Area after one swap/operation constraint
- Migration key: proof-driven pointer movement by lower boundary

## p005 Longest Substring Without Repeating Characters
- Variant A: Longest Repeating Character Replacement
- Variant B: Minimum Window Substring
- Migration key: sliding window with frequency map and shrink condition

## p006 Valid Parentheses
- Variant A: Minimum Remove to Make Valid Parentheses
- Variant B: Remove Outermost Parentheses
- Migration key: stack index tracking and balance counter

## p007 Binary Search
- Variant A: First Bad Version
- Variant B: Find Peak Element
- Migration key: define monotonic condition before coding

## p008 Search Insert Position
- Variant A: Lower Bound and Upper Bound template
- Variant B: Search Range of target (first and last position)
- Migration key: left-closed right-closed boundary discipline

## p009 Binary Tree Level Order Traversal
- Variant A: Zigzag Level Order Traversal
- Variant B: Right Side View
- Migration key: level-size loop and per-level post-processing

## p010 Climbing Stairs
- Variant A: Min Cost Climbing Stairs
- Variant B: House Robber (linear DP)
- Migration key: state transition and rolling variables

## p011 3Sum
- Variant A: 3Sum Closest
- Variant B: 4Sum
- Migration key: sort + fixed index + two pointers + dedup

## p012 Merge Intervals
- Variant A: Insert Interval
- Variant B: Non-overlapping Intervals (minimum removals)
- Migration key: sort by start, carry current interval

## p013 Top K Frequent Elements
- Variant A: K Closest Points to Origin
- Variant B: Top K Frequent Words
- Migration key: min-heap of size k and custom key

## p014 Number of Islands
- Variant A: Max Area of Island
- Variant B: Number of Closed Islands
- Migration key: BFS/DFS flood fill + visited marking

## p015 Kth Largest Element in Array
- Variant A: Kth Smallest in Sorted Matrix
- Variant B: Find Median from Data Stream
- Migration key: heap selection and stream maintenance

## Bonus p016 LRU Cache
- Variant A: LFU Cache (advanced)
- Variant B: Design Browser History / Recent Calls
- Migration key: hashmap + linked structure for O(1) updates

## 2-Hour Variant Routine

1. Pick 3 core problems.
2. For each, solve core in 12 to 15 minutes.
3. Solve one variant in 20 minutes.
4. Write one sentence: what changed from core to variant.
5. Re-solve failed variant within 24 hours.

## OA Readiness Check

You are ready if you can do all below:
- Identify pattern in less than 90 seconds.
- Write correct boundary handling on first try.
- Finish medium variants in 20 to 25 minutes.
- Explain time and space complexity clearly.
