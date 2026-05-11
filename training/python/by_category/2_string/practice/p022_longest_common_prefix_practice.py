"""P022 Longest Common Prefix Practice
Algorithm: shrink prefix until each string starts with it
TODO: implement solve(strs)
"""


def solve(strs):
    #if not strs:
    #    return ""
    #
    #first = strs[0]
    #for word in strs[1:]:
    #    while not word.startswith(first):
    #        first = first[:-1]
    #        if first == "":
    #            return ""
    #return first

    if not strs:
        return ""
    
    words = sorted(strs)
    first = words[0]
    last = words[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]



if __name__ == '__main__':
    print(solve(["flower", "flow", "flight"]))  # expected: "fl"
    print(solve(["dog", "racecar", "car"]))     # expected: ""