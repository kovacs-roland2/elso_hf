import sympy as sy

def egyenlet(egyenlet, **kwargs) -> int:
    """
    A függvény elvégzi az egyenletet a beadott értékekkel
    """
    egyenlet = sy.sympify(egyenlet)
    return egyenlet.evalf(subs=kwargs)

print(egyenlet("a+a+b*c", a=2, b=3, c=-4))