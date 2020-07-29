class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique = set()

        for email in emails:
            name, domain = email.split('@')
            name = name.replace('.', '')
            index = name.find("+")
            if index != -1:
                name = name[:index]
            unique.add((name, domain))

        return len(unique)