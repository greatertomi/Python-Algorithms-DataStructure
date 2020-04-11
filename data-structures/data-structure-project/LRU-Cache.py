class LRU_Cache:
    def __init__(self, initial_size=5):
        self.values = [None for _ in range(initial_size)]
        self.word_used_count = dict()
        self.cache_size = 0
        self.next_index = 0

    def get(self, key):
        value = None
        for i in range(self.cache_size):
            if self.values[i][0] == key:
                value = self.values[i][1]
                break

        if value is None:
            return -1
        else:
            self.word_used_count[key] += 1
            return value

    def set(self, key, value):
        if len(self.values) == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        if self.cache_size < len(self.values):
            self.values[self.next_index] = (key, value)
            self.word_used_count[key] = 0
            self.next_index += 1
            self.cache_size += 1
        else:
            most_used = self.word_used_count

            least_used = min(most_used, key=most_used.get)
            for i in range(len(self.values)):
                if self.values[i][0] == least_used:
                    self.values[i] = (key, value)
                    break

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

print(our_cache.values)

print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(3))
print(our_cache.get(9))

# print(our_cache.word_used_count)
our_cache.set(6, 6)
print(our_cache.values)
# word_count = {1: 1, 2: 1, 3: 0, 4: 0, 5: 0}
# print(min(word_count, key=word_count.get))
