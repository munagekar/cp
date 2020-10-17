class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ptime = -1
        ttime = 0

        for t in timeSeries:
            if ptime < t:
                ttime += duration
            else:
                ttime += duration - (ptime - t + 1)
            ptime = t + duration - 1

        return ttime


