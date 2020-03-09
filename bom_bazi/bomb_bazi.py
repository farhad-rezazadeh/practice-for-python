row, cols = map(int, input().split())
mine = int(input())
arr = [[0 for i in range(cols)] for j in range(row)]
for i in range(mine):
    _row, _cols = map(int, input().split())
    arr[_row-1][_cols-1] = "*"
for R in range(row):
    for C in range(cols):
        if arr[R][C] == "*":
            for _R in range(R-1, R+2):
                for _C in range(C-1, C+2):
                    if _R>=0 and _C>=0:
                        try:
                            arr[_R][_C]+=1
                        except:
                            pass
for i in range(row):
    for j in range(cols):
        print(arr[i][j], end=" ")
    print()