def f(x):
    return (x**3)-x-2


def bisection(a,b,E):

    counter=0
    if f(a)*f(b)>0:
        print(f"There are no root between {a} and {b}")
        return None

    if f(a)==0:
        return a

    if f(b)==0:
        return b


    while (b-a)>E:
        mid=(a+b)/2

        if f(mid)==0:
            return mid

        elif f(a)*f(mid)>0:
            a=mid

        else:
            b=mid
        counter+=1
        if counter>5:
            break

    return mid


while True:
    a=int(input("Enter a value : "))
    b=int(input("Enter b value : "))
    E=float(input("Enter E value : "))

    if f(a)*f(b)<0:
        break

print(bisection(a,b,E))
