import sys
import matplotlib.pyplot as plt

from numpy import linspace, sqrt
from scipy.integrate import odeint
from typing import Final

SUSCEPTIBLE_ENUM: Final = 0
EXPOSED_ENUM: Final = 1
INFECTED_ENUM: Final = 2

def model(y, t, scale, k1, k2, k3, k4, k5, k6, k7, k8):
    
    susceptible =y[SUSCEPTIBLE_ENUM]
    exposed = y[EXPOSED_ENUM]
    infected = y[INFECTED_ENUM]

    offline = scale - susceptible - exposed - infected
    
    trending = k8*sqrt(infected/scale)

    dy = [0,0,0]

    dy[SUSCEPTIBLE_ENUM] = k6*offline + k2*infected + k5*exposed - k3*susceptible*infected - k7*susceptible - k4*trending*susceptible
    dy[EXPOSED_ENUM] = k3*infected*susceptible + k4*trending*susceptible - k5*exposed - k1*exposed*(1-infected/susceptible)
    dy[INFECTED_ENUM] = k1*exposed*(1-infected/susceptible) - k2*infected

    return dy

def simulate_specific(  k1, k2, k3, k4, k5, k6, k7, k8,
                        t_lim_lower = 0, 
                        t_lim_upper = 52, 
                        initial_infected = 0.5, 
                        initial_exposed = 0, 
                        initial_susceptible = 0.5, 
                        n = 1
                        ):
    
    t_axis = linspace(start=t_lim_lower, stop=t_lim_upper, num=100)

    initial_y = [0,0,0]

    initial_y[INFECTED_ENUM] = initial_infected
    initial_y[EXPOSED_ENUM] = initial_exposed
    initial_y[SUSCEPTIBLE_ENUM] = initial_susceptible

    simulation = odeint(
        func = model,
        y0 = initial_y,
        t = t_axis,
        args = (n, k1, k2, k3, k4, k5, k6, k7, k8)
    )

    plt.plot(t_axis, simulation[:,SUSCEPTIBLE_ENUM], color="tab:green", linewidth=0.5)
    plt.plot(t_axis, simulation[:,EXPOSED_ENUM], color="tab:orange", linewidth=0.5)
    plt.plot(t_axis, simulation[:,INFECTED_ENUM], color="tab:blue", linewidth=0.5)
    

def simulate_broad(k1, k2, k3, k4, k5, k6, k7, k8,nweeks=52):
    for iinf in [0.005, 0.01, 0.015]:
        for isus in linspace(0.1,0.9):
            simulate_specific(k1, k2, k3, k4, k5, k6, k7, k8,initial_infected=iinf, initial_susceptible=isus, t_lim_upper=nweeks)


def legend():
    plt.legend(["Unfamiliar with the movement", "Aware of the movment, but not actively involved", "Actively involved in the movement"])

SAVE_MODE = False
def draw(filename=False):
    if (SAVE_MODE and type(filename).__name__ == 'str'):
        plt.savefig("plots/" + filename)
    else:
        plt.show()