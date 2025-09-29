def evaluate_polynomial(degree, x, constant_term, *coefficients):
    # set P and k
    k = 0
    P = constant_term
    print(f"S0 (value of the constant term) = {P}")
    while k < degree-1:
        P = str(int(P) + coefficients[k] * (x ** (k)))
        print(f"S{k+1} (Sum of the {k} lowest terms) = {P}")
        k = k + 1
    print(f"P(x)= {P}")

    # TODO: Implement polynomial evaluation using direct substitution method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result ok


if __name__ == "__main__":
    coefficients = []
    degree = int(input("Degree of the polynomial: "))
    x = int(input("Value of x: "))
    constant_term = int(input("Value of constant term: "))
    for i in range(degree-1):
        coefficients.append(int(input(f"Value of coefficient x^{str(i+1)}: ")))
    evaluate_polynomial(degree, x, constant_term, *coefficients)



    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial function
    # TODO: Ask user if they want to run again


