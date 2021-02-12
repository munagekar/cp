class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = format(num, 'b')
        return len(b) + b.count('1') - 1
