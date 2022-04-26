# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    n = 3
    m = 3
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)
    b = []
    for _ in range(m):
        b.append([0] * n)
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    c = []
    count = 0
    for _ in range(n - 1):
        for row in a:
            for row in b:
                for x in row:
                    for y in row:
                        if row[x] == row[y]:
                            print([x for x in row])
