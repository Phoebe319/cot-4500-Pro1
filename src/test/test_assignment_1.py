import math

# apprroximation algorithm
def approx_algo(x0, toll):
    iteration = 0
    diff = x0
    x = x0

    print("{}: {}".format(iteration, x))
    while (diff >= toll):
        iteration += 1
        y = x

        x = (x / 2) + (1 / x)
        print("{}: {}".format(iteration, x))

        diff = abs(x - y)
    print("Convergence after {} iterations".format(iteration))

# example function for bisection method
def f(x):
    return x**3 + 4*x**2 -10

# example prime function for bisection method
def f_prime(x):
    return 3*x**2 + 8*x

# bisection method
def bisection_method(a, b, tol):
    i = 0
    max_iterations = 100 

    while(abs(b - a) > tol and i < max_iterations):
        i += 1
        p = (a + b) / 2
        print("{}: {}".format(i, p))
        if((f(a) < 0 and f(p) > 0) or (f(a) > 0 and f(p) < 0)):
            b = p
        else:
            a = p
    return p

def equation(p0):
    return p0 - p0*p0*p0 - 4*p0*p0 + 10

# fixed point iteration
def fixed_pt(p0, tol, n0):
    result = "Failure"
    i = 1
    p = 0
    while (i <= n0):
        p = equation(p0)
        print("{}: {}".format(i, p))
        if math.isinf(p) or math.isnan(p):
            print("Result diverges")
            break
        if (abs(p - p0) < tol):
            result = "Success"
            break
        
        i += 1
        p0 = p
    print("{} after {} iterations".format(result, i))

# example cosine function for Newton-Raphson
def g(x):
    return math.cos(x) - x

# example prime cosine function for Newton-Raphson
def g_prime(x):
    return -math.sin(x) - 1

# Newton-Raphson method
def newton_raphson(a, b):
    x0 = (a + b) / 2
    epsilon = 1e-4
    max_iterations = 100 

    x = x0
    iterations = 0

    while iterations < max_iterations:
        x_new = x - g(x) / g_prime(x)
        if abs(x_new - x) < epsilon:
            break
        x = x_new
        print("{}: {}".format(iterations, x))
        iterations += 1
    return iterations

print("Approximation Algorithm")
approx_algo(1.5, 0.000001)
print("----------------------------------")

print("Bisection Method")
bisection_method(1, 2, 0.001)
print("----------------------------------")

print("Fixed Point Iteration")
fixed_pt(1.5, 0.000001, 50)
print("----------------------------------")

print("Newton-Raphson Method")
newton_raphson(math.pi / 4, math.pi / 2)
print("----------------------------------")