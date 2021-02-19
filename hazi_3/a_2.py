def egyenlet(egyenlet, *args, **kwargs) -> int:
    """
    A függvény összeadja a beadott értékeket
    """
    eredmeny = 0
    for arg in args:
        eredmeny += arg
    for key, value in kwargs.items():
        eredmeny += value
  
    return eredmeny

print(egyenlet("a+b+c", a = 2, b = 3, c = -4))