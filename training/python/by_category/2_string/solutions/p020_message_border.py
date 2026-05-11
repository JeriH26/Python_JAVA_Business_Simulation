"""P020 Message Border (TikTok OA)
Time: O(n*m), Space: O(n*m)

Given a list of message rows (each row is a list of words), format output as:
    [top border] + [row1 words joined by space] + [row2 words joined by space] + ... + [bottom border]

Border is made of '*' characters, where count = total number of words across all rows.

Example:
    Input:  [["hello", "world"], ["happy", "birthday"], ["happy", "Friday"]]
    Output: ["******", "hello world", "happy birthday", "happy Friday", "******"]
    
    Explanation:
        Total words = 2 + 2 + 2 = 6 → border has 6 stars
"""


def solve(messages):
    total_words = sum(len(row) for row in messages)
    border = "*" * total_words
    
    result = [border]
    for row in messages:
        result.append(" ".join(row))
    result.append(border)
    
    return result


if __name__ == '__main__':
    test_input = [["hello", "world"], ["happy", "birthday"], ["happy", "Friday"]]
    expected = ["******", "hello world", "happy birthday", "happy Friday", "******"]
    output = solve(test_input)
    print(output)
    print("Correct:", output == expected)
