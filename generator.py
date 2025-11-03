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

def list_to_string(input_list: list, trim: bool = False):
    output_str = ""

    for item in input_list:
        output_str = output_str + str(item)

    if trim:
        output_str = output_str.removeprefix("+")
    
    return output_str

def append_all_to_list(list_to_append: list, *args):
    for item in args:
        if type(item) == list:
            for element in item:
                list_to_append.append(element)
        else:
            list_to_append.append(item)


def expanded_perfect_square(common_factor_coeff: int, x_coeff: int, y_coeff: int, x_unk: str = "x", y_unk: str = "y"):
    common_factor_coeff = random_coeff(-2, 2)
    x_coeff = random_coeff(-6, 6)
    y_coeff = random_coeff(-6, 6)

    x2_coeff = (x_coeff**2)*common_factor_coeff
    y2_coeff = (y_coeff**2)*common_factor_coeff

    middle_coeff = 2*x_coeff*y_coeff*common_factor_coeff

    x2_term = f"{with_sign(x2_coeff)}{x_unk}²"
    middle_term = f"{with_sign(middle_coeff)}{x_unk}{y_unk}"
    y2_term = f"{with_sign(y2_coeff)}{y_unk}²"

    expanded_polynomial = []
    append_all_to_list(expanded_polynomial, x2_term, middle_term, y2_term)

    return(expanded_polynomial)

def expanded_three_square_terms(x_unk: str = "x", y_unk: str = "y", num_unk: str = ""):
    perfect_square_common_factor_coeff = random_coeff(-1, 1)

    perfect_square = expanded_perfect_square(perfect_square_common_factor_coeff, 6, -2, x_unk, y_unk)
    number_square = random_coeff()**2

    number_square_str = str(number_square)

    if num_unk != "":
        number_square_str = str(number_square) + num_unk + "²"

    expanded_polynomial = []

    if perfect_square_common_factor_coeff < 0:
        append_all_to_list(expanded_polynomial, f"+{number_square_str}", perfect_square)
    else:
        append_all_to_list(expanded_polynomial, perfect_square, f"-{number_square_str}")

    return(expanded_polynomial)

def process_input(type: str, shuffle: str, *args):
    result = []
    match type:
        case "3_sq":
            result = expanded_three_square_terms(*args)

        case "perf_sq":
            result = expanded_perfect_square(*args)

    if shuffle == "on":
        shuffle_list(result)

    return result

print(list_to_string(expanded_three_square_terms("(6a-1)")))