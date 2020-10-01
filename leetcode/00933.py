from collections import deque


class RecentCounter:

    def __init__(self):
        self.d = deque()

    def ping(self, t: int) -> int:
        self.d.append(t)
        while t - self.d[0] > 3000:
            self.d.popleft()

        return len(self.d)