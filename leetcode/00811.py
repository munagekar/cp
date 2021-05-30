class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        m = defaultdict(lambda: 0)

        for cpdomain in cpdomains:
            count, website = cpdomain.split(' ')
            domains = website.split('.')[::-1]
            x = ""
            for d in domains:
                x = d + x
                m[x] += int(count)
                x = "." + x

        return [f"{v} {k}" for k, v in m.items()]