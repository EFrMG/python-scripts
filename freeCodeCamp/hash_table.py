class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, input):
        res = 0

        for char in input:
            res += ord(char)
        return res

    def add(self, key_input, val_input):
        key_hash = self.hash(key_input)

        if key_hash in self.collection:
            self.collection[key_hash][key_input] = val_input
        else:
            self.collection[key_hash] = {key_input: val_input}

    def remove(self, key_input):
        key_hash = self.hash(key_input)

        if key_hash in self.collection:
            bucket = self.collection[key_hash]

            if key_input in bucket:
                del bucket[key_input]

                if not bucket:
                    del self.collection[key_hash]

    def lookup(self, key_input):
        key_hash = self.hash(key_input)
        bucket = self.collection.get(key_hash)

        if bucket:
            return bucket.get(key_input)
        else:
            return None
