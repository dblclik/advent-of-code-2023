import math


def quadratic_solver(a, b, c):
    # calculate the discriminant
    d = (b**2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    return min(sol1, sol2), max(sol1, sol2)
