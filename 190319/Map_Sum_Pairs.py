class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ms = {}

    def insert(self, key: str, val: int) -> None:
        self.ms[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        prefix_len = len(prefix)
        for x in self.ms:
            if len(x) < prefix_len:
                continue
            elif prefix == x[:prefix_len]:
                res += self.ms[x]
        return res
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)