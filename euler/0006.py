t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(int((n*(n+1)/2)**2 -(n*(2*n+1)*(n+1)/6)))