def ciagi(S, t):
    f = [float('-inf') for _ in range(len(t))]
    for s in S:
        for i in range(len(t)):  # dynamic programming, fill array bottom-up
            substr = t[max(0, i - len(s)+1): i + 1]  # substring ending at current index i, +1, since it’s [start, end)
            if s == substr:  # check if we can use our word
                x = len(s)
                if f[i - len(s)] != float('-inf') and i - len(s) != -1:
                    x = min(len(s), f[i - len(s)])

                f[i] = max(f[i], x)
                print(f)# the longest (max) width, check shortest (min) s_i

    return f[-1]


t = 'ababab'
S = ['ab', 'abab']
print(ciagi(S, t))
