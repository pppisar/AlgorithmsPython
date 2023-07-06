import math


# The first equation (relative to y)
def f1y(x):
    y = 0.8 - math.cos(x + 0.5)
    return y


# The second equation (relative to y)
def f2x(y):
    x = (1/2) * (math.sin(y)) - 0.8
    return x


# Condition of the first equation
def ff1(x, y):
    f = math.cos(x + 0.5) + y - 0.8
    return f


# Condition of the second equation
def ff2(x, y):
    f = math.sin(y) - 2 * x - 1.6
    return f


if __name__ == "__main__":
    # Fixed-point iteration
    x0 = -0.75
    y0 = -0.25
    i = 0
    print("%-30s %-30s %-30s %-30s" % ("k", "Xk", "Yk", "Xk - Xk - 1"))
    print("%-30.15g %-30.15g %-30.15g" % (i, x0, y0))
    while i < 13:
        y1 = f1y(x0)
        x1 = f2x(y0)
        y2 = f1y(x1)
        x2 = f2x(y1)
        if math.fabs(x2-x1) < math.fabs(y2-y1):
            c = math.fabs(y2-y1)
        else:
            c = math.fabs(x2-x1)
        x0 = x2
        y0 = y2
        print("%-30.15g %-30.15g %-30.15g %-30.15g" % (i+1, x2, y2, c))
        i = i + 1
        if c < 0.0001:
            break

    # Residual (numerical analysis)
    f1 = ff1(x2, y2)
    f2 = ff2(x2, y2)
    print(f"R = ( {f1} ; {f2} )\n")