def f(x):
    return x**3 - x - 1

def g(x):
    return (3*x**2)-1


def newtonRaphson(x0,N):
    print('\n "CALCULATION WITH NEWTON s  RAPHSON FORMULA"')
    step = 1
    koşul = True
    while koşul:
        if g(x0) == 0:
            print('error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('calculation-%d, x1 = %f ' % (step, x1,))
        x0 = x1
        step = step + 1
        
        if step > N:
        
            break


x0 = input('başla:')    
N = input('bitir:')
x0 = float(x0)
N = int(N)


newtonRaphson(x0,N)
print("calculation finished") 


"-----------------------------------------"



"""created by emreglds"""
