class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)

        zeros = c['z']
        c['z'] -= zeros
        c['e'] -= zeros
        c['r'] -= zeros
        c['o'] -= zeros

        twos = c['w']
        c['t'] -= twos
        c['w'] -= twos
        c['o'] -= twos

        fours = c['u']
        c['u'] -= fours
        c['f'] -= fours
        c['o'] -= fours
        c['r'] -= fours

        fives = c['f']
        c['f'] -= fives
        c['i'] -= fives
        c['v'] -= fives
        c['e'] -= fives

        six = c['x']
        c['s'] -= six
        c['i'] -= six
        c['x'] -= six

        one = c['o']
        c['o'] -= one
        c['n'] -= one
        c['e'] -= one

        seven = c['v']
        c['s'] -= seven
        c['e'] -= seven * 2
        c['v'] -= seven
        c['n'] -= seven

        three = c['r']
        eight = c['g']
        nine = c['n'] // 2

        return '0' * zeros + '1' * one + '2' * twos + '3' * three + '4' * fours + '5' * fives + '6' * six + '7' * seven + '8' * eight + '9' * nine