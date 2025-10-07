def evaluate_polynomial(degree, x, constant_term, *coefficients):
    s=constant_term
    k=1
    pwr=x
    if (degree!=len(coefficients)):
        return "Should have raised ValueError"
    while (k<degree+1):
        s+=coefficients[k-1]*pwr**k
        k+=1
    return s
    # TODO: Implement polynomial evaluation using direct substitution method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result

    if len(coefficients) < degree: raise ValueError(f"need {degree} coefficient(s)")
    p = constant_term
    k = 1
    print(f"S0 (value of the constant term) = {p}")
    while k <= degree:
        print(f"S{k} (sum of the {k + 1} lowest terms) = {p} + {coefficients[k-1]}({x}{'' if k == 1 else f'^{k}'}) = {p+x**k*coefficients[k-1]}")
        p += x**k*coefficients[k-1]
        k += 1
    return p


if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial function
    # TODO: Ask user if they want to run again
    while True:
        print("Degree of the polynomial: ", end="")
        degree = int(input())
        print("Value of x: ", end="")
        x = int(input())
        print("Value of constant term: ", end="")
        constant = int(input())

        coeffs = [print(f"Coefficient of the x^{i+1} term: ", end="") or
                  int(input()) for i in range(degree)]
        print(f"P(x) = {evaluate_polynomial(degree, x, constant, *coeffs)}")

        print("Do you want to evaluate another polynomial? (y/n): ")
        if input() == "n":
            break
