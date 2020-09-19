class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        d = collections.defaultdict(lambda: [])

        ans = []

        for i, s in enumerate(groupSizes):
            li = d[s]
            li.append(i)
            if len(li) == s:
                ans.append(li)
                del d[s]

        return ans