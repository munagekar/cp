# Used JIT Pypy3
# https://www.hackerrank.com/contests/101hack/challenges/mr-k-marsh/problem

#
# Complete the kMarsh function below.
#
def kMarsh(grid, r, c):
    left = [[0] * c for _ in range(r)]

    up = [[0] * c for _ in range(r)]
    

    # Left Precompute
    for i in range(0, r):
        if grid[i][0] == 'x':
            left[i][0] = -1

    for i in range(0, r):
        for j in range(1, c):
            if grid[i][j] == '.':
                left[i][j] = left[i][j - 1] + 1
            else:
                left[i][j] = -1

    # Top Precompute
    for j in range(0, c):
        if grid[0][j] == 'x':
            up[0][j] = -1

    for i in range(1, r):
        for j in range(0, c):
            if grid[i][j] == '.':
                up[i][j] = up[i - 1][j] + 1
            else:
                up[i][j] = -1

    peri = -1

    # Row Scans 0(n2)
    for r1 in range(0,r):
        for r2 in range(r1+1,r):
            rdiff = r2 - r1
            # Linear Scan O(n)
            target_columns = [c for c in range(0, c) if up[r2][c] >= rdiff]

            # l,r Scan 0(n)
            ltc = len(target_columns)

            lci = 0  # Left Column Index

            for rci in range(1, ltc):  # Right Column Index

                rc = target_columns[rci]
                left_clearance = min(left[r1][rc], left[r2][rc])

                min_left_start = rc - left_clearance

                while target_columns[lci] < min_left_start:
                    lci += 1

                lc = target_columns[lci]

                if lc < rc:
                    peri2 = (rc - lc + rdiff) * 2
                    peri = max(peri, peri2)

    if peri > -1:
        print(peri)
    else:
        print("impossible")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    grid = []

    for r in range(m):
        grid.append(list(input()))

    kMarsh(grid, m, n)

