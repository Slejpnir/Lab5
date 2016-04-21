import numpy as np
from scipy.integrate import odeintfrom matplotlib.pyplot import plotfrom scipy import integratex = np.linspace(-1,1,1000)
def f(z,x):
    xx,v = z
    return [v, 2*v-xx+np.cos(x)]sol = odeint(f,[0,0],x)
import matplotlib.pyplot as plt
plt.plot(x, sol[:, 0], 'b', label="y(x)")

plt.legend(loc="best")
plt.xlabel("x")
plt.grid()
plt.show()

t=np.linspace(-1,1,10000)
def ff(der,t):
    xx,v,yy,w = der
    #yy,w=y_der[1]
    return [v,w+np.sin(t),w, -v*yy+np.cos(t)]
sol2 = odeint(ff,[0,0,0,0],t)
#import matplotlib.pyplot as plt
#plt.plot(t, sol2[:, 0], 'b', label='x(t)')
plt.plot(sol2[:, 0], sol2[:, 2], 'g', label='y(x)')
plt.legend(loc='best')
plt.xlabel('x')
plt.grid()
plt.show()

x1 = lambda x: x*np.sin(x)
print(integrate.quad(x1, 0, 1))
x2=lambda x,y:x*np.cos(x+y)
gfun=lambda x:0
hfun=lambda x:1
print(integrate.dblquad(x2, 0, 1,gfun,hfun))
x3=lambda x,y,z:1
gfun3=lambda x:0
hfun3=lambda x:1
rfun3=lambda x,y:0
qfun3=lambda x,y:1
print(integrate.tplquad(x3, 0, 1,gfun3,hfun3,rfun3,qfun3))