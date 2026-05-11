"""P020 Message Border Practice (TikTok OA)
Algorithm: Count total words, create border with that many stars, join each row with spaces.
TODO: implement solve(messages)

Example:
    [["hello", "world"], ["happy", "birthday"], ["happy", "Friday"]]
    → ["******", "hello world", "happy birthday", "happy Friday", "******"]
"""


def solve(messages):
    total = 0
    for row in messages:
        total += len(row)
    star = "*" * total
    expect_out = [star]
    for row in messages:
        expect_out.append("".join(row))
    expect_out.append(star)

if __name__ == '__main__':
    test_input = [["hello", "world"], ["happy", "birthday"], ["happy", "Friday"]]
    expected = ["******", "hello world", "happy birthday", "happy Friday", "******"]
    output = solve(test_input)
    print("Output:", output)
    print("Expected:", expected)
