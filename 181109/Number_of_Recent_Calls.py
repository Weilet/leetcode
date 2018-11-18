from collections import deque
class RecentCounter:

    def __init__(self):
        self.times = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.times and self.times[0] < t - 3000:
            self.times.popleft()
        self.times.append(t)
        return len(self.times)

        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)