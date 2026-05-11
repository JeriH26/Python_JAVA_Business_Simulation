"""Python Basics Practice - Solutions"""


# 题1：根据分数返回等级。
# 规则：>=90 A，>=80 B，>=70 C，否则 D。
def grade(score):
    """Return letter grade based on score thresholds."""
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    return 'D'


# 题2：用 while 计算 1 到 n 的累加和。
# 思路：从 i=1 开始，每轮加到 total，直到 i > n。
def sum_1_to_n(n):
    """Use a while loop to accumulate 1..n."""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


# 题3：统计列表里偶数的个数。
# 思路：下标遍历，遇到能被 2 整除的元素就计数加一。
def count_even(nums):
    """Count even numbers using index-based traversal."""
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            count += 1
        i += 1
    return count


# 题4：统计字符串中每个字符出现次数。
# 思路：用字典记录频次，字符存在就 +1，不存在就初始化为 1。
def char_count(s):
    """Build frequency map manually: char -> count."""
    freq = {}
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
        i += 1
    return freq


# 题5：计算去重后的元素个数。
# 思路：把所有元素放入 set，最后返回 set 的长度。
def unique_count(nums):
    """Insert each number into a set, then return set size."""
    seen = set()
    for num in nums:
        seen.add(num)
    return len(seen)


# 题6：把句子改成首字母大写格式。
# 思路：按空格切分单词，每个单词首字母大写、其余小写，再拼回去。
def title_case(sentence):
    """Capitalize each word's first letter and lowercase the rest."""
    words = sentence.split()
    out = []
    for w in words:
        if len(w) == 0:
            out.append(w)
        else:
            out.append(w[0].upper() + w[1:].lower())
    return ' '.join(out)


# 题7：判断字符串是否回文。
# 思路：字符串与其反转结果相等则为回文。
def is_palindrome_simple(s):
    """Palindrome check by comparing with reversed string."""
    reversed_s = ""
    i = len(s) - 1
    while i >= 0:
        reversed_s += s[i]
        i -= 1

    return s == reversed_s
    #return s == s[::-1]


# 题8：返回两个数中的较大值（不使用 max）。
# 思路：直接比较 a 和 b。
def my_max(a, b):
    """Return the larger of two values without using max()."""
    if a >= b:
        return a
    return b


# 题9：安全除法。
# 思路：正常返回 a/b；除数为 0 时捕获异常并返回 'Error'。
def safe_divide(a, b):
    """Perform division; return 'Error' when dividing by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return 'Error'


# 题10：返回每个元素的平方列表。
# 思路：遍历输入列表，把每个元素平方后追加到新列表。
def squares(nums):
    """Create a new list containing x^2 for each input element."""
    result = []
    for x in nums:
        result.append(x * x)
    return result


if __name__ == '__main__':
    print('1)', grade(85))
    print('2)', sum_1_to_n(5))
    print('3)', count_even([1, 2, 3, 4, 6]))
    print('4)', char_count('aab'))
    print('5)', unique_count([1, 1, 2, 3, 3]))
    print('6)', title_case('hello world'))
    print('7)', is_palindrome_simple('level'))
    print('8)', my_max(3, 7))
    print('9)', safe_divide(10, 0))
    print('10)', squares([1, 2, 3]))
