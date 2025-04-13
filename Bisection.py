def f(x):
    return x**3 - x - 2

def bisectionMethod(a, b, E=0.000001):

    if f(a) * f(b) > 0:
        print(f"There is no root between {a} and {b} (f(a) and f(b) have the same sign)")
        return None
    

    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    counter = 0
    while (b - a) > E:  
        counter += 1
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0: 
            b = mid
        else: 
            a = mid
    
    return (a + b) / 2 


print(bisectionMethod(1,2))
