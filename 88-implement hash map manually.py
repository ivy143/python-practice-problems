#implement hash map manually
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.map[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
                return
    def display(self):
        for i, bucket in enumerate(self.map):
            if bucket:
                print(f"Bucket {i}: {bucket}")
# Example usage
hash_map = HashMap()
hash_map.put("key1", "value1")
hash_map.put("key2", "value2")
hash_map.put("key3", "value3")

print("Initial hash map:")
hash_map.display()

print("\nValue for 'key2':", hash_map.get("key2"))

hash_map.remove("key2")
print("\nHash map after removing 'key2':")
hash_map.display()
print("\nValue for 'key2' after removal:", hash_map.get("key2"))
