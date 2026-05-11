"""P020 Message Border Practice (TikTok OA)
Algorithm: Count total words, create border with that many stars, join each row with spaces.
TODO: implement solve(messages)

Example:
    [["hello", "world"], ["happy", "birthday"], ["happy", "Friday"]]
    → ["******", "hello world", "happy birthday", "happy Friday", "******"]
"""


def solve(messages):
    raise NotImplementedError("TODO: implement p020 message border")


if __name__ == '__main__':
    test_input = [["hello", "world"], ["happy", "birthday"], ["happy", "Friday"]]
    expected = ["******", "hello world", "happy birthday", "happy Friday", "******"]
    output = solve(test_input)
    print("Output:", output)
    print("Expected:", expected)
