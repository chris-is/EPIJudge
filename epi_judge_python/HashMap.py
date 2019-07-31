class HashMap:
    def __init__(self):
        self.buckets = [None] * 10

    def hashing_function(self, x):
        ord_sum = 0
        for char in x:
            ord_sum += ord(char)

        return ord_sum % len(self.buckets)

    def add(self, x):
        bucket = self.hashing_function(x)
        if self.buckets[bucket] is not None:
            self.buckets[bucket].linked_list.append(x)
        else:
            self.buckets[bucket] = Bucket(x)

    def remove(self, x):
        bucket = self.hashing_function(x)
        if not self.get(x):
            return
        else:
            if len(self.buckets[bucket].linked_list) == 1:
                del self.buckets[bucket].linked_list[-1]
            else:
                for index, e in enumerate(self.buckets[bucket].linked_list):
                    if e == x:
                        del self.buckets[bucket].linked_list[index]

    def get(self, x):
        bucket = self.hashing_function(x)
        if self.buckets[bucket]:
            if len(self.buckets[bucket].linked_list) > 1:
                for index, e in enumerate(self.buckets[bucket].linked_list):
                    if e == x:
                        return self.buckets[bucket].linked_list[index]

            else:
                return self.buckets[bucket].linked_list[-1]


class Bucket:
    def __init__(self, x):
        self.linked_list = []
        self.linked_list.append(x)

    def linked_list(self):
        return self.linked_list


class Test:

    if __name__ == '__main__':
        hashmap = HashMap()
        hashmap.add("jessica")
        hashmap.add("bob")

        print(hashmap.get("jessica"))