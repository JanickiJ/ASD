def min_cost(G, v, t, cache):
    if cache[v] == -1:
        min = float('inf')
        for i in range(len(G[v])):
            if G[v][i][1] + min_cost(G, G[v][i][0], t, cache) < min:
                min = G[v][i][1] + min_cost(G, G[v][i][0], t, cache)
            cache[v] = min
    return cache[v]


def f(G, s, t):
    cache = [-1] * len(G)
    cache[t] = 0
    return  min_cost(G, s, t, cache)


G = [[(1, 0), (2, 1)], [(3, 1), (2, 0)], [(3, 0)], []]
print(f(G, 0, 3))
