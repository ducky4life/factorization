import random

def random_coeff_pos(max_incl: int = 9):
    return random.randint(1, max_incl)

def random_coeff(min_incl: int = -9, max_incl: int = 9):
    number = random.randint(min_incl, max_incl)
    if number == 0:
        number = min_incl # avoid recursive
    return number

def with_sign(coeff: int):
    sign = "+"
    if coeff < 0:
        sign = ""

    return(f"{sign}{coeff}")

def expanded_perfect_square(common_factor_coeff: int, x_coeff: int, y_coeff: int):
    x_coeff = 6
    y_coeff = -1

    x2_coeff = (x_coeff**2)*common_factor_coeff
    y2_coeff = (y_coeff**2)*common_factor_coeff

    middle_coeff = 2*x_coeff*y_coeff*common_factor_coeff

    expanded_polynomial = f"{x2_coeff}x^2 {with_sign(middle_coeff)}xy {with_sign(y2_coeff)}y^2"
    return(expanded_polynomial)

def expanded_three_square_terms(num_unk: str = ""):
    perfect_square_common_factor_coeff = random_coeff(-1, 1)

    perfect_square = expanded_perfect_square(perfect_square_common_factor_coeff, 6,-2)
    number_square = random_coeff()**2

    number_square_str = str(number_square)

    if num_unk != "":
        number_square_str = str(number_square) + num_unk + "^2"

    expanded_polynomial = f"{perfect_square} -{number_square_str}"
    if perfect_square_common_factor_coeff < 0:
        expanded_polynomial = f"{number_square_str} {perfect_square}"

    return(expanded_polynomial)

print(expanded_three_square_terms(""))