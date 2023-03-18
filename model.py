from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t, k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,f):

    m = y[0]
    s = y[1]
    a = y[2]
    p = y[3]

    dmdt = k1*s*(1-m/p) - k2*m
    dsdt = k3*s*(1-s/a) + k4*f(t) - k5*s*m
    dadt = k6*p + k7*a - k8*a*s/p
    dpdt = k9*p - k10*m
    
    return [dmdt, dsdt, dadt, dpdt]

t_axis = linspace(start = 0, stop = 10)

simulation = odeint(func    = model 
                   ,y0      = [1,1,1,1] 
                   ,t       = t_axis
                   ,args    = (1,1,1,1,1,1,1,1,1,1,lambda t: 1)
                   )

plt.plot(t_axis, simulation)
plt.show()
