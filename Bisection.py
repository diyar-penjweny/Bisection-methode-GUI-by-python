def f(x):
    return  (x**3 - x - 2)

def bisectionMethod(a,b,E=0.000001):
    if f(a)*f(b)>0:   #ئەگەر f(a) و f(b)ئەنجامەکانیان نیشانەکانی جیاواز نەبێ ئەوا لێگدانیان هەمیشە ئەکاتە موجەب
        print(f"There is no number between {a} and {b} that makes the function zero")

    else:
        counter = 0

        while abs(f(b)-f(a))>E:
            counter += 1
            mid = (a+b)/2
            if f(mid)==0:   #ئەگەر ژمارەکە نەخشەکەی کرد بە سفر ئەوا لووپەکە ئەوەستێ و ئەنجامەکەمان بۆ ئەهێنێتەوە
                return mid
            elif f(a)*f(mid)>0:     #ب ئەگەر f(a) و f(mid)ئەنجامەکانیان نیشانەکانی جیاواز نەبێ ئەوا لێگدانیان هەمیشە ئەکاتە موجەب بۆیە ئەبێ نرخی a بکەین بە نرخی mid
                a = mid
            else:
                b = mid
        return mid

print(bisectionMethod(1,2))



