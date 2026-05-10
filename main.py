from question1 import bisection_method, newton_raphson, secant_method, eval_poly, eval_poly_derivative, find_all_roots


def main():
    coeffs = list(map(float, input("Enter polynomial coefficients (highest degree first, e.g. 1 0 -1 -2): ").split()))
    start = float(input("Enter start point: "))
    end = float(input("Enter end point: "))
    n = int(input("Enter number of sections: "))
    epsilon = float(input("Enter epsilon (or press Enter for 0.0001): ") or 0.0001)

    print("Choose method:")
    print("1. Bisection")
    print("2. Newton-Raphson")
    print("3. Secant")
    choice = input("Enter choice: ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice")
        return

    find_all_roots(coeffs, start, end, n, choice, epsilon)


main()