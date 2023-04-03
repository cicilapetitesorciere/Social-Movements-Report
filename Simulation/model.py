from numpy import linspace
from numpy import exp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from typing import List, Final

SUSCEPTIBLE_ENUM: Final = 0
EXPOSED_ENUM: Final = 1
INFECTED_ENUM: Final = 2
RECOVERED_ENUM: Final = 3

def model(y, t, N, k1, k2, k3, k4, k5, k6, k7, k8)
    
    susceptible =y[SUSCEPTIBLE_ENUM]
    exposed = y[EXPOSED_ENUM]
    infected = y[INFECTED_ENUM]
    recovered = y[RECOVERED_ENUM]

    offline = N - susceptible - exposed - infected
    assert(offline >= 0)
    trending = k8*(1-exp(-infected))

    dy: List[float] = [0,0,0,0]

    dy[INFECTED_ENUM] = k6*offline + k2*infected + k5*exposed - k3*susceptible*infected - k7*susceptible - k4*trending*susceptible
    dy[EXPOSED_ENUM] = k3*infected*susceptible + k4*trending*susceptible - k5*exposed - k1*exposed*(1-infected/susceptible)
    dy[SUSCEPTIBLE_ENUM] = k1*exposed*(1-infected/susceptible) - k2*infected
    dy[RECOVERED_ENUM] = k7*susceptible

    return dy

def simulate(t_lim_lower = 0, t_lim_upper = 10, initial_infected = 1, initial_exposed = 0, initial_susceptible = 1, initial_recovered = 0, n = 2, k1 = 1, k2 = 1, k3 = 1, k4 = 1, k5 = 1, k6 = 1, k7 = 1, k8 = 1)   
    t_axis: List[float] = linspace(start=t_lim_lower, stop=t_lim_upper, num=100)

    initial_y = [0,0,0,0]

    initial_y[INFECTED_ENUM] = initial_infected
    initial_y[EXPOSED_ENUM] = initial_exposed
    initial_y[SUSCEPTIBLE_ENUM] = initial_susceptible
    initial_y[RECOVERED_ENUM] = initial_recovered

    simulation: List[List[float]] = odeint(
        func=model,
        y0=initial_y,
        t=t_axis,
        args=(n, k1, k2, k3, k4, k5, k6, k7, k8)
    )

    plt.plot(t_axis, simulation[:,INFECTED_ENUM], label="Engaged in the social movement")
    plt.plot(t_axis, simulation[:,EXPOSED_ENUM], label="Aware of the movement")
    plt.plot(t_axis, simulation[:,SUSCEPTIBLE_ENUM], label="Active users")
    plt.legend()
    plt.show()