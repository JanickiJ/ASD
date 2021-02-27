class employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.g = -1
        self.f = -1
        self.taken = False

def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    for emp in v.emp:
        x += g(emp)
    y = g(v)
    if x > y:
        v.taken = True
        v.f = x
    else:
        v.f = y

    return v.f

def g(v):
    if v.g > 0:
        return v.g
    fun = 0
    for emp in v.emp:
        fun += f(emp)
    v.g = fun
    return v.g


a = employee(1)
b = employee(7)
c = employee(5)
d = employee(2)
e = employee(5)
x = employee(6)
y = employee(1)
h = employee(10)
i = employee(1)
a.emp = [b,c]
b.emp = [d,e]
c.emp = [x]
d.emp = [y,h]
e.emp = [i]

print(f(a))
print(a.taken,b.taken,c.taken,d.taken,e.taken,x.taken,y.taken,h.taken,i.taken)
