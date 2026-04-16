"""V031 LFU Cache Practice
TODO: implement class LFUCache
"""


class LFUCache:
    def __init__(self, capacity):
        raise NotImplementedError("TODO: implement v031 lfu cache __init__")

    def get(self, key):
        raise NotImplementedError("TODO: implement v031 lfu cache get")

    def put(self, key, value):
        raise NotImplementedError("TODO: implement v031 lfu cache put")


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # expected: 1
    cache.put(3, 3)
    print(cache.get(2))  # expected: -1
    print(cache.get(3))  # expected: 3
