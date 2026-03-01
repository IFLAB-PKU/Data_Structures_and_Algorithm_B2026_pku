x = float(input())
y = 0.0
if x < 5 :
    y = 2.5-x
elif x < 10 :
    y = 2-1.5*(x-3)*(x-3)
else :
    y = (x/2)-1.5

print("{:.3f}".format(y))