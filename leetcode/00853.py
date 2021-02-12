class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars, reverse=True)

        t = -1
        ans = 0
        for p, s in cars:
            nt = (target - p) / s
            if nt > t:
                ans += 1
                t = nt
        return ans