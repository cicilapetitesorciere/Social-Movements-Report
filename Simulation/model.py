from numpy import linspace
from numpy import exp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from typing import List, Final

INFECTED_ENUM: Final = 0
EXPOSED_ENUM: Final = 1
SUSCEPTIBLE_ENUM: Final = 2
RECOVERED_ENUM: Final = 3

def model(
    y: List[float],
    t: float,
    k1: float,
    k2: float,
    k3: float,
    k4: float,
    k5: float,
    k6: float,
    k7: float,
    k8: float
) -> List[float]:
    
    infected: float = y[INFECTED_ENUM]
    exposed: float = y[EXPOSED_ENUM]
    susceptible: float = y[SUSCEPTIBLE_ENUM]
    recovered: float = y[RECOVERED_ENUM]

    population: float = infected + exposed + susceptible + recovered
    trending: float = k8*(1-exp(-infected))

    dy: List[float] = [0,0,0,0]

    dy[INFECTED_ENUM] = k6*population + k2*infected + k5*exposed - k3*susceptible*infected - k7*susceptible
    dy[EXPOSED_ENUM] = k3*infected*susceptible + k4*trending - k5*exposed - k1*exposed*(1-infected/susceptible)
    dy[SUSCEPTIBLE_ENUM] = k1*exposed*(1-infected/susceptible) - k2*infected
    dy[RECOVERED_ENUM] = k7*susceptible

    return dy

def simulate(
    t_lim_lower: float = 0,
    t_lim_upper: float = 10,
    initial_infected: float = 1,
    initial_exposed: float = 0,
    initial_susceptible: float = 100,
    initial_recovered: float = 0,
    k1: float = 1,
    k2: float = 1,
    k3: float = 1,
    k4: float = 1,
    k5: float = 1,
    k6: float = 1,
    k7: float = 1,
    k8: float = 1,
):
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
        args=(k1, k2, k3, k4, k5, k6, k7, k8)
    )

    plt.plot(t_axis, simulation[:,INFECTED_ENUM], label="Engaged in the social movement")
    #plt.plot(t_axis, simulation[:,EXPOSED_ENUM], label="Aware of the movement")
    # plt.plot(t_axis, simulation[:,SUSCEPTIBLE_ENUM], label="Active users")
    plt.legend()
    plt.show()