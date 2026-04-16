"""V031 LFU Cache
Time: O(1) average get/put, Space: O(capacity)
"""

from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.values = {}
        self.freqs = {}
        self.groups = defaultdict(OrderedDict)

    def _touch(self, key):
        freq = self.freqs[key]
        value = self.values[key]
        del self.groups[freq][key]
        if not self.groups[freq]:
            del self.groups[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.freqs[key] = freq + 1
        self.groups[freq + 1][key] = value

    def get(self, key):
        if key not in self.values:
            return -1
        self._touch(key)
        return self.values[key]

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.values:
            self.values[key] = value
            self.groups[self.freqs[key]][key] = value
            self._touch(key)
            return
        if self.size == self.capacity:
            old_key, _ = self.groups[self.min_freq].popitem(last=False)
            del self.values[old_key]
            del self.freqs[old_key]
            self.size -= 1
            if not self.groups[self.min_freq]:
                del self.groups[self.min_freq]
        self.values[key] = value
        self.freqs[key] = 1
        self.groups[1][key] = value
        self.min_freq = 1
        self.size += 1


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
