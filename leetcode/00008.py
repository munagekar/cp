import re
# https://leetcode.com/problems/string-to-integer-atoi/
    def myAtoi(self, s: str) -> int:
        match_object = re.match(r"([+-]?[0-9]+).*",s.strip())
        
        if match_object is None:
            return 0
        
        num = int(match_object.group(1))
        if num > 2 ** 31 -1:
            return 2 ** 31 -1
        
        if num < -2 ** 31:
            return -2 ** 31
        
        return num

        