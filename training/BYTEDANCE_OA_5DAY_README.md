# Bytedance OA 5-Day Plan (15 Must-Do Problems)

This is a focused 5-day sprint plan for OA preparation.
Goal: complete 15 core problems in training/python and finish 2 timed mocks.

Companion variant drill:
- training/BYTEDANCE_OA_VARIANTS.md

## Problem List (Core 15)

1. p001_two_sum.py
2. p002_valid_anagram.py
3. p003_move_zeroes.py
4. p004_container_with_most_water.py
5. p005_longest_substring_without_repeating.py
6. p006_valid_parentheses.py
7. p007_binary_search.py
8. p008_search_insert_position.py
9. p009_binary_tree_level_order_traversal.py
10. p010_climbing_stairs.py
11. p011_3sum.py
12. p012_merge_intervals.py
13. p013_top_k_frequent_elements.py
14. p014_number_of_islands.py
15. p015_kth_largest_element_in_array.py

Optional bonus:
- p016_lru_cache.py

## Day-by-Day Plan

### Day 1: Hash + Stack + Binary Search Basics
- p001_two_sum.py
- p002_valid_anagram.py
- p006_valid_parentheses.py
- Target time:
  - 20 min per problem first pass
  - 10 min per problem second pass

### Day 2: Two Pointers + Sliding Window
- p003_move_zeroes.py
- p004_container_with_most_water.py
- p005_longest_substring_without_repeating.py
- Target time:
  - 25 min per problem first pass
  - 12 min per problem second pass

### Day 3: Search + Tree Traversal + DP
- p007_binary_search.py
- p008_search_insert_position.py
- p009_binary_tree_level_order_traversal.py
- p010_climbing_stairs.py
- Target time:
  - 20 min for binary search problems
  - 25 min for BFS/DP problems

### Day 4: Sorting + Interval + Top K
- p011_3sum.py
- p012_merge_intervals.py
- p013_top_k_frequent_elements.py
- Timed mock #1:
  - 60 to 90 minutes
  - Pick any 3 from p001 to p013

### Day 5: Graph + Heap + Final Simulation
- p014_number_of_islands.py
- p015_kth_largest_element_in_array.py
- Optional: p016_lru_cache.py
- Timed mock #2:
  - 90 minutes
  - Pick 4 problems across all topics

## Practice Flow (Every Problem)

1. Open matching practice file in training/python/practice.
2. Implement solve(...) without looking at answer.
3. Run the practice file and compare output comments.
4. If blocked for more than 12 minutes, check the answer file once.
5. Re-code from memory after 2 hours and again next day.

Practice templates available for p001 to p016 in:
- training/python/practice/

## Daily Deliverables

Every day, finish these four items:
1. Solved count and average time.
2. One sentence pattern summary.
3. Top 3 mistakes.
4. One re-solve from yesterday without hints.

Use training/progress_template.md to track this.

## Commands

Run all answer files:
- bash training/python/run.sh

Open practice guide:
- bash training/python/run_practice.sh

Run one target problem:
- python3 training/python/p011_3sum.py
- python3 training/python/practice/p011_3sum_practice.py

## OA Exam Strategy (Quick)

1. First 2 minutes: classify pattern before coding.
2. Write edge cases first: empty input, one element, duplicates, boundaries.
3. Keep variable names stable: left right mid freq visited.
4. If stuck, pivot quickly to a guaranteed-pass approach.
5. Reserve last 8 to 10 minutes for dry-run and bug scan.
