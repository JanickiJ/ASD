class Employee:
    def __init__(self, fun, name):
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1
        self.name = name

#f(v) mozliwe najepsze rowiaznie dla v
def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    for i in v.emp:     # v idzie na impreze
        x += i.g
    y = g(v)            # v nie idzie na impreze
    v.f = max(x, y)
    return v.f

#g(v) mozliwe najlepsze rozwiązanie dla v w którym
# v nie idzie na impreze
def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for i in v.emp:
        v.g += f(i)
    return v.g






