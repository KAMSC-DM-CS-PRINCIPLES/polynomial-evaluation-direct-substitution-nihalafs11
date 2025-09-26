def evaluate_polynomial(degree, x, constant_term, *coefficients):
    if len(coefficients) != degree:
        raise ValueError(f"Need {degree} coefficient(s)")

    total = constant_term
    print (f"(value of the constant term)= {total}")

    k=1
    while k <= degree:
        value = coefficients[k-1] * (x**k)
        old_total = total
        total = total + value
        print(f"S{k} (sum of the {k+1} lowest terms) = {old_total} + {coefficients[k-1]}({x}^{k}) = {total}")