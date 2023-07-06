import numpy

# The known values of the function at 9 nodal points
x = [-1.6, -1.1, -0.6, -0.2, 0.2, 0.7, 0.93, 1.2, 1.51]
y = [1.48921, 0.71496, 0.87946, 1.07213, 1.07213, 0.81541, 0.70223, 0.78554, 1.29161]

ourx = numpy.arange(-1.5, 1.5, 0.12)  # The interval in which you want to test the function (Step = 0.12)

lagr = []  # list for global interpolation values
lagr_kus = []  # array for linear interpolation


"""
functions: f(x), f`(x) and f``(x)
x - Variable that the function takes
"""
def f(x1):
    number = (x1 ** 4) - 2 * (x1 ** 2) + 3
    ln = numpy.log(number)
    return ln

def f1(x2):
    number1 = (4*(x2**3) - 4*x2)/((x2**4)-2*(x2**2)+3)
    return number1

def f2(x3):
    number2 = (-4*(x3**6) + 4*(x3**4) + 28*(x3**2) -12)/(((x3**4) - 2*(x3**2) +3)**2)
    return number2


"""
Lagrange polynomial for global interpolation
"""
def poli(point):
    return ((y[0] * (point - x[1]) * (point - x[2]) * (point - x[3]) * (point - x[4]) * (point - x[5]) * (point - x[6])
             * (point - x[7]) * (point - x[8])) / ((x[0] - x[1]) * (x[0] - x[2]) * (x[0] - x[3]) * (x[0] - x[4])
                                                   * (x[0] - x[5]) * (x[0] - x[6]) * (x[0] - x[7]) * (x[0] - x[8]))) \
           + ((y[1] * (point - x[0]) * (point - x[2]) * (point - x[3]) * (point - x[4]) * (point - x[5])
               * (point - x[6]) * (point - x[7]) * (point - x[8])) / ((x[1] - x[0]) * (x[1] - x[2]) * (x[1] - x[3])
                                                                      * (x[1] - x[4])
                                                                      * (x[1] - x[5]) * (x[1] - x[6]) * (x[1] - x[7])
                                                                      * (x[1] - x[8])))\
           + ((y[2] * (point - x[1]) * (point - x[0]) * (point - x[3]) * (point - x[4]) * (point - x[5]) * (
                point - x[6])
               * (point - x[7]) * (point - x[8])) / ((x[2] - x[1]) * (x[2] - x[0]) * (x[2] - x[3]) * (x[2] - x[4])
                                                     * (x[2] - x[5]) * (x[2] - x[6]) * (x[2] - x[7]) * (x[2] - x[8]))) \
           + ((y[3] * (point - x[1]) * (point - x[2]) * (point - x[0]) * (point - x[4]) * (point - x[5]) * (
                point - x[6])
               * (point - x[7]) * (point - x[8])) / ((x[3] - x[1]) * (x[3] - x[2]) * (x[3] - x[0]) * (x[3] - x[4])
                                                     * (x[3] - x[5]) * (x[3] - x[6]) * (x[3] - x[7]) * (x[3] - x[8]))) \
           + ((y[4] * (point - x[1]) * (point - x[2]) * (point - x[3]) * (point - x[0]) * (point - x[5]) * (
                point - x[6])
               * (point - x[7]) * (point - x[8])) / ((x[4] - x[1]) * (x[4] - x[2]) * (x[4] - x[3]) * (x[4] - x[0])
                                                     * (x[4] - x[5]) * (x[4] - x[6]) * (x[4] - x[7]) * (x[4] - x[8]))) \
           + ((y[5] * (point - x[1]) * (point - x[2]) * (point - x[3]) * (point - x[4]) * (point - x[0]) * (
                point - x[6])
               * (point - x[7]) * (point - x[8])) / ((x[5] - x[1]) * (x[5] - x[2]) * (x[5] - x[3]) * (x[5] - x[4])
                                                     * (x[5] - x[0]) * (x[5] - x[6]) * (x[5] - x[7]) * (x[5] - x[8]))) \
           + ((y[6] * (point - x[1]) * (point - x[2]) * (point - x[3]) * (point - x[4]) * (point - x[5]) * (
                point - x[0])
               * (point - x[7]) * (point - x[8])) / ((x[6] - x[1]) * (x[6] - x[2]) * (x[6] - x[3]) * (x[6] - x[4])
                                                     * (x[6] - x[5]) * (x[6] - x[0]) * (x[6] - x[7]) * (x[6] - x[8]))) \
           + ((y[7] * (point - x[1]) * (point - x[2]) * (point - x[3]) * (point - x[4]) * (point - x[5]) * (
                point - x[6])
               * (point - x[0]) * (point - x[8])) / ((x[7] - x[1]) * (x[7] - x[2]) * (x[7] - x[3]) * (x[7] - x[4])
                                                     * (x[7] - x[5]) * (x[7] - x[6]) * (x[7] - x[0]) * (x[7] - x[8]))) \
           + ((y[8] * (point - x[1]) * (point - x[2]) * (point - x[3]) * (point - x[4]) * (point - x[5]) * (
                point - x[6])
               * (point - x[7]) * (point - x[0])) / ((x[8] - x[1]) * (x[8] - x[2]) * (x[8] - x[3]) * (x[8] - x[4])
                                                     * (x[8] - x[5]) * (x[8] - x[6]) * (x[8] - x[7]) * (x[8] - x[0])))


"""
Lagrange polynomial of the first degree for linear interpolation
"""
def lin (point2, k):
    return ((y[k] * (point2 - x[k + 1])) / (x[k] - x[k + 1])) + ((y[k + 1] * (point2 - x[k])) / (x[k + 1] - x[k]))


""" 
"frames" for linear interpolation
"""
def linnorm(point3):
    if point3 <= -1.1:
        return lin(point3, 0)
    elif -1.1 <= point3 <= -0.6:
        return lin(point3, 1)
    elif -0.6 <= point3 <= -0.2:
        return lin(point3, 2)
    elif -0.2 <= point3 <= 0.2:
        return lin(point3, 3)
    elif 0.2 <= point3 <= 0.7:
        return lin(point3, 4)
    elif 0.7 <= point3 <= 0.93:
        return lin(point3, 5)
    elif 0.93 <= point3 <= 1.2:
        return lin(point3, 6)
    elif point3 >= 1.2:
        return lin(point3, 7)


def df(dx):
    a = -1.5
    b = 1.6
    h = 0.12
    dy = 0
    if dx == a:
        dy = (linnorm(dx + h) - linnorm(dx))/h
    elif dx == b:
        dy = (linnorm(dx) - linnorm(dx - h))/h
    else:
        dy = (linnorm(dx + h) - linnorm(dx - h))/(2*h)
    return dy


def ddf(ddx):
    a = -1.5
    b = 1.6
    h = 0.12
    ddy = 0
    if ddx == a:
        ddy = (linnorm(df(ddx + h)) - linnorm(df(ddx)))/h
    elif ddx == b:
        ddy = (linnorm(df(ddx)) - linnorm(df(ddx - h)))/h
    else:
        ddy = (linnorm(ddx + h) + linnorm(ddx - h) - 2*linnorm(ddx))/(h**2)
    return ddy


if __name__ == '__main__':
    """
    Result output
    %-30.15g (left alignment, using 30 characters to write the value, 15 decimal places, data type)
    """
    print("%-30s %-30s %-30s %-30.15s %-30.15s %-30.15s %-30.15s" % (
        "Logarithm", "Global interpolation", "Linear interpolation",
        "First derivative", "Second derivative",
        "DifPLH1", "DifPLH2")
    )

    for m in range(len(ourx)):
        print("%-30.15g %-30.15g %-30.15g %-30.15g %-30.15g %-30.15g %-30.15g" % (
            f(ourx[m]), poli(ourx[m]), linnorm(ourx[m]),
            f1(ourx[m]), f2(ourx[m]),
            df(ourx[m]), ddf(ourx[m]))
        )
        lagr.append(poli(ourx[m]))
        lagr_kus.append(linnorm(ourx[m]))
