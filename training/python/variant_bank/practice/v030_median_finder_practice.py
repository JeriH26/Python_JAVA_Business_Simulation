"""V030 Median from Data Stream Practice
TODO: implement class MedianFinder
"""


class MedianFinder:
    def __init__(self):
        raise NotImplementedError("TODO: implement v030 median finder __init__")

    def add_num(self, num):
        raise NotImplementedError("TODO: implement v030 median finder add_num")

    def find_median(self):
        raise NotImplementedError("TODO: implement v030 median finder find_median")


if __name__ == '__main__':
    finder = MedianFinder()
    finder.add_num(1)
    finder.add_num(2)
    print(finder.find_median())  # expected: 1.5
    finder.add_num(3)
    print(finder.find_median())  # expected: 2.0
