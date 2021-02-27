
def ship(M, t):
    n = len(M)

    stack = []
    stack.append((0, 0))

    while stack:
        (x, y) = stack.pop()
        M[x][y] = -1
        for i in range(-1, 2):
            for j in range(-1, 2):

                if x + i >= 0 and x + i < n and y + j >= 0 and y + j < n:
                    if M[x + i][y + j] != -1 and M[x + i][y + j] >= t:
                        if x+i== n-1 and y+j == n-1:
                            return True
                        stack.append((x + i, y + j))

    return False

M=[     [9,1,1],
        [3,1,9],
        [2,2,1]
]
print(ship(M,2))