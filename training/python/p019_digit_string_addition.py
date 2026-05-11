"""P019 Digit String Addition (TikTok OA)
Time: O(n), Space: O(n)

Given two numeric strings a and b, add them digit by digit (no carry between positions).
Each pair of digits is summed independently and concatenated as a string.

Example:
    Input:  a="99", b="99"  → Output: "1818"   (9+9=18, 9+9=18)
    Input:  a="11", b="9"   → Output: "110"    (1+0=1,  1+9=10)
"""


def solve(a: str, b: str) -> str:
    # 短的左补零对齐
    n = max(len(a), len(b))
    while len(a) < n:
        a = "0" + a
    while len(b) < n:
        b = "0" + b

    result = ""
    for i in range(n):
        digit_sum = int(a[i]) + int(b[i])
        result = result + str(digit_sum)

    return result


if __name__ == '__main__':
    print(solve("99", "99"))  # expected: "1818"
    print(solve("11", "9"))   # expected: "110"
    print(solve("1", "999"))  # expected: "1000"  (001+999 → 1, 9+9=18... wait)
    # 001 + 999 → (0+9)=9, (0+9)=9, (1+9)=10 → "9910"
    print(solve("1", "999"))  # expected: "9910"
