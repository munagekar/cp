class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        
        N = 0
        for i,c in enumerate(S):
            if c.isdigit():
                N *= int(c)
            else:
                N +=1
            if N >= K:
                break
               

        
        for j in range(i,-1,-1):
            if S[j].isdigit():
                N/=int(S[j])
                K %= N
            else:
                if K==0 or K==N:
                    return S[j]
                else:
                    N-=1
