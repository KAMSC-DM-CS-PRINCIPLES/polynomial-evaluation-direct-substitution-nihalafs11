def evaluate_polynomial(degree, x, constant_term, *coefficients):
    result = constant_term
    i = len(coefficients) - 1
    while i >= 0:
        result *= x**i + coefficients[i]
        i -= 1
    return result