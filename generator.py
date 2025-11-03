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

def shuffle_list(input_list: list):
    random.shuffle(input_list)
    return input_list

def list_to_string(input_list: list):
    output_str = ""

    for item in input_list:
        output_str = output_str + str(item)
    
    return output_str

def append_all(list_to_append: list, *args):
    for item in args:
        if type(item) == list:
            for element in item:
                list_to_append.append(element)
        else:
            list_to_append.append(item)


def expanded_perfect_square(common_factor_coeff: int, x_coeff: int, y_coeff: int):
    x_coeff = 6
    y_coeff = -1

    x2_coeff = (x_coeff**2)*common_factor_coeff
    y2_coeff = (y_coeff**2)*common_factor_coeff

    middle_coeff = 2*x_coeff*y_coeff*common_factor_coeff

    x2_term = f"{with_sign(x2_coeff)}x^2"
    middle_term = f"{with_sign(middle_coeff)}xy"
    y2_term = f"{with_sign(y2_coeff)}y^2"

    expanded_polynomial = []
    append_all(expanded_polynomial, x2_term, middle_term, y2_term)

    return(expanded_polynomial)

def expanded_three_square_terms(num_unk: str = ""):
    perfect_square_common_factor_coeff = -1

    perfect_square = expanded_perfect_square(perfect_square_common_factor_coeff, 6,-2)
    number_square = random_coeff()**2

    number_square_str = str(number_square)

    if num_unk != "":
        number_square_str = str(number_square) + num_unk + "^2"

    expanded_polynomial = []

    if perfect_square_common_factor_coeff < 0:
        append_all(expanded_polynomial, number_square_str, perfect_square)
    else:
        expanded_polynomial.append(perfect_square, f"-{number_square_str}")

    return(expanded_polynomial)

print(list_to_string(expanded_three_square_terms("")))
