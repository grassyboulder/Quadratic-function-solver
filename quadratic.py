import math
def testplot(a=-1,b=0,c=0):
    import matplotlib.pyplot as plt
    xz = [x for x in range(-10,11,1)]
    yz = [a*x**2+b*x+c for x in xz]
    oz = [0]*len(xz)
    plt.plot(xz,oz,'k-')
    plt.plot(xz,yz,'o-')
    plt.show()
def quadratic(a,b,c):
    if b**2-4*a*c < 0:
        return "no real solutions"
    if b**2-4*a*c == 0:
        return (-b/(2*a))
    sroot = math.sqrt(b**2-4*a*c)
    x1 = (-b + sroot)/(2*a)
    x2 = (-b - sroot)/(2*a)
    return x1, x2
def ask():
    y = ''
    while y not in ['yes','Yes','y','Y']:
        print("give give a")
        a = float(input())
        print("give give b")
        b = float(input())
        print("give give c")
        c = float(input())
        print('you inputed',a,',',b,',',c,", type yes if correct.")
        y = input()
        print()
        
    print('the answer is',quadratic(a,b,c))
    testplot(a,b,c)
ask()

