import math


# The first equation (relative to x1)
def fx1(x2, x3):
    x1 = (1 / 3.8) * (0.4 - 1.7 * x2 - 2.0 * x3)
    return x1


# The second equation (relative to x2)
def fx2(x3):
    x2 = (1 / 2.4) * (9.3 - 0.7 * x3)
    return x2


# The third equation (relative to x3)
def fx3(x1, x2):
    x3 = (1 / 1.8) * (0.9 * x1 - 0.4 * x2 - 1.5)
    return x3


# Condition of the first equation
def ffx1(x1, x2, x3):
    f = 7.6 * x1 + 5.8 * x2 + 4.7 * x3 - 10.1
    return f


# Condition of the second equation
def ffx2(x1, x2, x3):
    f = 3.8 * x1 + 4.1 * x2 + 2.7 * x3 - 9.7
    return f


# Condition of the third equation
def ffx3(x1, x2, x3):
    f = 2.9 * x1 + 2.1 * x2 + 3.8 * x3 - 7.8
    return f


if __name__ == "__main__":
  # Jacobi method
  x01 = 0.4/3.8
  x02 = 9.3/2.4
  x03 = -1.5/1.8
  c = 0
  i = 0
  print("Jacobi method")
  print("%-30s %-30s %-30s %-30s %-30s" % ("k", "X1", "X2", "X3", "Xk - Xk-1" ))
  print("%-30.15g %-30.15g %-30.15g %-30.15g" % (i, x01, x02, x03))
  while True:
      x11 = fx1(x02, x03)
      x12 = fx2(x03)
      x13 = fx3(x01, x02)
      x21 = fx1(x12, x13)
      x22 = fx2(x13)
      x23 = fx3(x11, x12)
      a = [math.fabs(x23-x13), math.fabs(x22-x12), math.fabs(x21-x11)]
      a.sort()
      c = a[2]
      x01 = x21
      x02 = x22
      x03 = x23
      print("%-30.15g %-30.15g %-30.15g %-30.15g %-30.15g" % (i+1, x21, x22, x23, c))
      i = i+1
      if c < 0.0001:
          break

  # Residual (numerical analysis)
  f1 = ffx1(x21, x22, x23)
  f2 = ffx2(x21, x22, x23)
  f3 = ffx3(x21, x22, x23)
  print(f"R = ( {f1} ; {f2} ; {f3} )\n")

  # Jacobi method
  x01 = (0.4/3.8)
  x02 = (9.3/2.4)
  x03 = (-1.5/1.8)
  c = 0
  i = 0
  x11 = fx1(x02, x03)
  x12 = fx2(x03)
  x13 = fx3(x11, x12)
  x01 = x11
  x02 = x12
  x03 = x13
  print("Gauss–Seidel method")
  print("%-30s %-30s %-30s %-30s %-30s" % ("k", "X1", "X2", "X3", "Xk - Xk-1" ))
  print("%-30.15g %-30.15g %-30.15g %-30.15g" % (i, x01, x02, x13))
  while True:
      x11 = fx1(x02, x03)
      x12 = fx2(x03)
      x13 = fx3(x11, x12)
      x21 = fx1(x12, x13)
      x22 = fx2(x13)
      x23 = fx3(x21, x22)
      a = [math.fabs(x23-x13), math.fabs(x22-x12), math.fabs(x21-x11)]
      a.sort()
      c = a[2]
      x01 = x21
      x02 = x22
      x03 = x23
      print("%-30.15g %-30.15g %-30.15g %-30.15g %-30.15g" % (i + 1, x21, x22, x23, c))
      i = i + 1
      if c < 0.0001:
          break

  # Residual (numerical analysis)
  f1 = ffx1(x21, x22, x23)
  f2 = ffx2(x21, x22, x23)
  f3 = ffx3(x21, x22, x23)
  print(f"R = ( {f1} ; {f2} ; {f3} )\n")