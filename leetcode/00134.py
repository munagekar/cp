class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [g - c for g, c in zip(gas, cost)]

        potential = list(itertools.accumulate(diffs, operator.add))

        if potential[-1] < 0:
            return -1

        mini = min(potential)
        return (potential.index(mini) + 1) % len(potential)