import numpy as np

def Func(x):
    return (x**2 + 1)/(x**4 + x**2 + 1)


def simpson(interval, intervalStep):
    integral = 1
    simpsonSum = 0
    for i in range(0, (len(interval) - 1), 1):
        simpsonSum += Func(interval[i]) + 4 * Func(((interval[i] + interval[i + 1]) / 2)) + Func(interval[i + 1])
    integral = integral * (intervalStep / 6) * simpsonSum
    return integral


def rungeIteration(intervalStart, intervalFinish, intervalStep = 0.1):
    runge = 0
    k = 4
    error = 0.0001

    interval = np.arange(intervalStart, intervalFinish + 0.01, intervalStep)
    newInth = simpson(interval, intervalStep)

    while True:
        inth = newInth
        intervalStep = intervalStep / 2
        interval = np.arange(intervalStart, intervalFinish + 0.01, intervalStep)
        newInth = simpson(interval, intervalStep)

        if ((newInth - inth) / ((2 ** k) - 1)) <= error:
            runge = ((newInth - inth) / ((2 ** k) - 1))
            break
        else:
            k = k + 1

    print("%-30.15g %-30.15g %-30.15g %-30.15g %-30.15g" % (intervalStart, intervalFinish, runge, intervalStep, newInth))


if __name__ == '__main__':
    funcField = np.arange(0, 1.01, 0.1)

    print("Study the function from the beginning of the domain of definition")
    print("%-30s %-30s %-30s %-30s %-30s" % ("Left border", "Right border", "Error", "Step", "Integral"))
    for m in range(len(funcField)):
        intervalStart = 0
        intervalFinish = funcField[m]
        rungeIteration(intervalStart, intervalFinish)

    print("\nStudy of a function on an interval of size 0.1")
    print("%-30s %-30s %-30s %-30s %-30s" % ("Left border", "Right border", "Error", "Step", "Integral"))
    for m in range(len(funcField) - 1):
        intervalStart = funcField[m]
        intervalFinish = funcField[m + 1]
        rungeIteration(intervalStart, intervalFinish)