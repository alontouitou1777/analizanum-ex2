def eval_poly(coeffs, x):
    result = 0
    for c in coeffs:
        result = result * x + c
    return result

def eval_poly_derivative(coeffs, x):
    derivative_coeffs = [coeffs[i] * (len(coeffs) - 1 - i) for i in range(len(coeffs) - 1)]
    return eval_poly(derivative_coeffs, x)


def bisection_method(f, start_point, end_point, epsilon=0.0001):
    if f(start_point) * f(end_point) > 0:
        print("The method does not converge")
        return None

    iterations = 0
    mid = (start_point + end_point) / 2
    while (end_point - start_point) / 2 > epsilon:
        f_mid = f(mid)

        if f(start_point) * f_mid < 0:
            end_point = mid
        else:
            start_point = mid

        mid = (start_point + end_point) / 2
        iterations += 1

    print(f"Number of iterations: {iterations}")
    return mid, iterations



def newton_raphson(coeffs, start_point, end_point, epsilon=0.0001):
    x = (start_point + end_point) / 2
    iterations = 0

    while abs(eval_poly(coeffs, x)) > epsilon:
        derivative = eval_poly_derivative(coeffs, x)
        if derivative == 0:
            print("Derivative is zero, method does not converge")
            return None
        x = x - eval_poly(coeffs, x) / derivative
        iterations += 1
        if x < start_point or x > end_point:
            print("Method does not converge")
            return None

    print(f"Number of iterations: {iterations}")
    return x, iterations

def secant_method(coeffs, start_point, end_point, epsilon=0.0001):
    x0 = start_point
    x1 = end_point
    iterations = 0

    while abs(eval_poly(coeffs, x1)) > epsilon:
        f0 = eval_poly(coeffs, x0)
        f1 = eval_poly(coeffs, x1)
        if f1 - f0 == 0:
            print("Method does not converge")
            return None
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if x2 < start_point or x2 > end_point:
            print("Method does not converge")
            return None
        x0 = x1
        x1 = x2
        iterations += 1

    print(f"Number of iterations: {iterations}")
    return x1, iterations


def find_all_roots(coeffs, start, end, n, choice, epsilon=0.0001):
    if n <= 0:
        print("Number of sections must be greater than 0")
        return

    derivative_coeffs = [coeffs[i] * (len(coeffs) - 1 - i) for i in range(len(coeffs) - 1)]
    step = (end - start) / n
    a = start

    while a < end:
        b = a + step
        if eval_poly(coeffs, a) * eval_poly(coeffs, b) < 0:
            if choice == "1":
                f = lambda x: eval_poly(coeffs, x)
                result = bisection_method(f, a, b, epsilon)
            elif choice == "2":
                result = newton_raphson(coeffs, a, b, epsilon)
            elif choice == "3":
                result = secant_method(coeffs, a, b, epsilon)
            if result is not None:
                root, iterations = result
                print(f"Root: {root}, Iterations: {iterations}")

        if eval_poly(derivative_coeffs, a) * eval_poly(derivative_coeffs, b) < 0:
            if choice == "1":
                f = lambda x: eval_poly(derivative_coeffs, x)
                result = bisection_method(f, a, b, epsilon)
            elif choice == "2":
                result = newton_raphson(derivative_coeffs, a, b, epsilon)
            elif choice == "3":
                result = secant_method(derivative_coeffs, a, b, epsilon)
            if result is not None:
                root, iterations = result
                print(f"Root (even multiplicity): {root}, Iterations: {iterations}")

        a = b