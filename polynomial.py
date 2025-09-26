def evaluate_polynomial(degree, x, constant_term, *coefficients):
    if len(coefficients) != degree:
        raise ValueError(f"Need {degree} coefficient(s)")

    result = 0
    highest_degree=degree-1

    while highest_degree >= 0:
        result += coefficients[highest_degree]
        highest_degree -= 1

    result= result * x + coefficients[highest_degree]
    return result