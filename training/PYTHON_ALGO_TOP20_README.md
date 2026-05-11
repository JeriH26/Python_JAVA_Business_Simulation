# Python Algorithm Interview Top 20

This note is a compact Python interview cheat sheet focused on high-frequency syntax, data structures, and patterns that show up in algorithm interviews. It is not organized around past practice history. It is organized around what is broadly useful under interview time pressure.

## 1. `list` as dynamic array

Use for indexed access, iteration, and storing results.

```python
nums = [1, 2, 3]
nums[0]
nums[-1]
```

## 2. `list` as stack

Use `append()` to push and `pop()` to remove the top item.

```python
stack = []
stack.append("(")
top = stack[-1]
val = stack.pop()
```

Common interview uses:
- Valid Parentheses
- Daily Temperatures
- DFS iterative traversal

## 3. `dict` as hash map

Use for `value -> index`, counting, grouping, and constant-time membership checks by key.

```python
seen = {}
seen[5] = 2
if 5 in seen:
    print(seen[5])
```

Common interview uses:
- Two Sum
- frequency counting
- lookup tables

## 4. `set` for dedup and membership

Use when you only care whether something has been seen.

```python
seen = set()
seen.add(3)
if 3 in seen:
    ...
```

Common interview uses:
- remove duplicates
- visited states
- fast existence checks

## 5. `collections.deque` as queue

Use for BFS because `popleft()` is efficient.

```python
from collections import deque

q = deque([root])
node = q.popleft()
q.append(child)
```

Common interview uses:
- Binary Tree Level Order Traversal
- Right Side View
- shortest path in unweighted graphs

## 6. `enumerate()`

Use when you need index and value at the same time.

```python
for i, x in enumerate(nums):
    print(i, x)
```

Common interview uses:
- Two Sum
- array scans
- dynamic programming loops

## 7. `range()`

Use for index-based loops.

```python
for i in range(n):
    ...

for i in range(left, right + 1):
    ...
```

## 8. `len()`

Use constantly for arrays, strings, queues, and loop boundaries.

```python
n = len(nums)
```

## 9. `sorted()` and `.sort()`

Use to order arrays, intervals, and strings.

```python
arr2 = sorted(arr)
arr.sort()
intervals.sort(key=lambda x: x[0])
```

Difference:
- `sorted(arr)` returns a new list
- `arr.sort()` sorts in place

Common interview uses:
- Merge Intervals
- 3Sum
- anagram grouping keys

## 10. `dict.get()`

Use for counting without writing extra `if` logic.

```python
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
```

Common interview uses:
- character frequency
- number frequency
- map accumulation

## 11. `in` membership checks

Works on strings, lists, sets, and dicts.

```python
if x in seen_set:
    ...

if key in my_dict:
    ...
```

Important:
- `x in dict` checks keys, not values

## 12. String cleanup helpers

High-frequency methods:
- `lower()`
- `isalnum()`
- `isdigit()`
- `isalpha()`
- `strip()`
- `split()`
- `join()`

```python
s = s.lower()
if ch.isalnum():
    ...
parts = s.split(",")
result = "".join(chars)
```

Common interview uses:
- Valid Palindrome
- string parsing
- token cleanup

## 13. Two-pointer template

Use when scanning from both ends or searching pairs in sorted arrays.

```python
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        ...
    elif total < target:
        left += 1
    else:
        right -= 1
```

Common interview uses:
- Valid Palindrome
- Two Sum II
- Container With Most Water
- 3Sum inner loop

## 14. Binary search template

Use when the input is sorted or the problem asks for a boundary/position.

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

Common interview uses:
- Binary Search
- Search Insert Position

## 15. BFS level-order skeleton

Use when the problem is naturally solved one layer at a time.

```python
from collections import deque

def bfs(root):
    if not root:
        return []

    q = deque([root])
    ans = []

    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)

    return ans
```

## 16. Monotonic stack pattern

Use when the problem asks for next greater/smaller element.

```python
stack = []
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        j = stack.pop()
        ans[j] = i - j
    stack.append(i)
```

Common interview uses:
- Daily Temperatures
- Next Greater Element

## 17. Interval merge pattern

Use for overlapping interval problems.

```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]

for start, end in intervals[1:]:
    if merged[-1][1] >= start:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

## 18. Result preallocation

Use when output size is known in advance.

```python
ans = [0] * n
visited = [False] * n
```

Benefits:
- simpler updates
- avoids repeated appends in some array problems

## 19. Tuple for hashable composite keys

Use when you need to put multiple values into a `set` or use them as a `dict` key.

```python
triplet = tuple(sorted([a, b, c]))
seen.add(triplet)
```

Common interview uses:
- deduplicating 3Sum brute force
- coordinate states
- memo keys

## 20. Complexity habits

Not syntax, but this is one of the highest-frequency interview expectations.

You should be able to say:
- Time complexity
- Space complexity
- Why the chosen data structure fits

Examples:
- Hash map lookup is usually `O(1)` average
- Binary search is `O(log n)`
- One-pass stack scan is often `O(n)`
- Sorting changes complexity to `O(n log n)`

## Minimal must-remember set before an interview

If time is very short, remember these first:
- `list`, `append`, `pop`, `[-1]`
- `dict`, `get`, `in`
- `set`, `add`, `in`
- `deque`, `popleft`
- `enumerate`
- `sorted` and `.sort()`
- `lower`, `isalnum`
- two pointers
- binary search
- BFS by level
- monotonic stack

## Common mistakes to avoid

- Using `and` where the guard should be `or`
- Accessing `stack[-1]` before checking `if not stack`
- Forgetting to sort before interval merge or 3Sum
- Storing values when you really need indices
- Mixing up `sorted(nums)` and `nums.sort()`
- Forgetting that `x in dict` checks keys
- Trying to put a `list` inside a `set`
- Forgetting to dry run a small example after coding
