class RecentCounter:
    def __init__(self):
        self.times = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        for i in range(len(self.times)):
            if (t-3000) > self.times[i]:
                self.times.pop(i)
        return len(self.times)

        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)