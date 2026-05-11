"""Python Basics Practice - TODO
目标：练最常用基础语法（不追求花哨写法）。
"""


# 1) if/else
# 输入成绩 score，返回等级：>=90 "A", >=80 "B", >=70 "C", 否则 "D"
def grade(score):
    if score > 90:
        return "A"
    if score > 80:
        return "B"
    if score > 70:
        return "C"
    return 0


# 2) while + 累加
# 返回 1..n 的和
# 例如 n=5 -> 15
def sum_1_to_n(n):
    i = 0
    result = 0
    while i <= n:
        result += i
        i += 1
    return result


# 3) list 遍历
# 返回列表中偶数个数
# 例如 [1,2,3,4,6] -> 3
def count_even(nums):
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            count += 1
        i += 1
    return count


# 4) dict 计数
# 统计字符串中每个字符出现次数，返回 dict
# 例如 "aab" -> {'a':2, 'b':1}
def char_count(s):
    seen = {}
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in seen:
            seen[ch] += 1
        else:
            seen[ch] = 1
        i += 1
    return seen


# 5) set 去重
# 返回去重后元素个数
# 例如 [1,1,2,3,3] -> 3
def unique_count(nums):
    seen = set()
    for ch in nums:
        seen.add(ch)
    return len(seen)


# 6) 字符串处理
# 把句子里每个单词首字母大写
# 例如 "hello world" -> "Hello World"
# ["Hello", "World"]
def title_case(sentence):
    words = sentence.split()
    out = []
    for w in words:
        if len(w) == 0:
            out.append(w)
        else:
            out.append(w[0].upper() + w[1:].lower())
    result = ""
    i =0
    while i < len(out):
        result += out[i]
        if i != len(out) -1:
            result += " "
        i += 1
    return result


# 7) 切片与反转
# 判断字符串是否回文（区分大小写，直接比较）
# 例如 "level" -> True, "abc" -> False
def is_palindrome_simple(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# 8) 函数参数
# 返回 a 和 b 中较大值（不用 max）
def my_max(a, b):
    if a > b:
        return a
    return b


# 9) try/except
# 安全除法：b 为 0 时返回 "Error"
def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Error'


# 10) 列表推导式（可不用，for 循环也行）
# 返回 nums 里每个数的平方列表
# 例如 [1,2,3] -> [1,4,9]
def squares(nums):
    squrel = []
    for i in nums:
        squrel.append(i*i)

    return squrel


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
