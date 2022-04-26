# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)

    for i in range(n - 1):
        for j in range(m - 1):
            count_row = len([a[i][j] for a[i][j] in i if a[i][j] == 0])
            if count_row == n:
                del a[i]
    for i in range(m - 1):
        for j in range(n - 1):
            count_row = len([a[i][j] for a[i][j] in j if a[i][j] == 0])
            if count_row == n:
                del a[j]
    print(a)
