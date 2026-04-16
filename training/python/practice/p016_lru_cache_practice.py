"""P016 LRU Cache Practice
Algorithm: Hash map + doubly linked list
TODO: implement class LRUCache
"""


class LRUCache:
    def __init__(self, capacity):
        raise NotImplementedError("TODO: implement p016 LRU cache __init__")

    def get(self, key):
        raise NotImplementedError("TODO: implement p016 LRU cache get")

    def put(self, key, value):
        raise NotImplementedError("TODO: implement p016 LRU cache put")


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # expected: 1
    cache.put(3, 3)
    print(cache.get(2))  # expected: -1
