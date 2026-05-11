"""P028 Valid Palindrome Practice
Algorithm: two pointers + skip non-alphanumeric chars
TODO: implement solve(s)
"""


def solve(s):
    n = len(s)
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    print(solve("A man, a plan, a canal: Panama"))  # expected: True
    print(solve("race a car"))                      # expected: False
