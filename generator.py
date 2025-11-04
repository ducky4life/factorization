import random

def random_coeff_pos(max_incl: int = 9):
    return random.randint(1, max_incl)

def random_coeff(min_incl: int = -9, max_incl: int = 9):
    number = random.randint(min_incl, max_incl)
    if number == 0:
        number = random.choice([min_incl, max_incl]) # avoid recursive
    return number

def with_sign(coeff: int):
    sign = "+"
    if coeff < 0:
        sign = ""

    if coeff == 1: # don't write out 1 as coeff
        return(sign)
    elif coeff == -1:
        return("-")

    return(f"{sign}{coeff}")

def append_unk_to_coeff(unk: str, coeff: int, power: int = 1):
    if power == 2:
        return(f"{with_sign(coeff)}{unk}²")
    else:
        return(f"{with_sign(coeff)}{unk}")

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


def expanded_perfect_square(common_factor_coeff: int = None, x_coeff: int = None, y_coeff: int = None, x_unk: str = "x", y_unk: str = "y", **args):

    if common_factor_coeff == None:
        common_factor_coeff = random_coeff(-4, 4)
    if x_coeff == None:
        x_coeff = random_coeff(-6, 6)
    if y_coeff == None:
        y_coeff = random_coeff(-6, 6)

    x2_coeff = (x_coeff**2)*common_factor_coeff
    y2_coeff = (y_coeff**2)*common_factor_coeff

    middle_coeff = 2*x_coeff*y_coeff*common_factor_coeff
    middle_term = f"{with_sign(middle_coeff)}{x_unk}{y_unk}"

    x2_term = append_unk_to_coeff(x_unk, x2_coeff, 2)
    y2_term = append_unk_to_coeff(y_unk, y2_coeff, 2)

    expanded_polynomial = []
    append_all_to_list(expanded_polynomial, x2_term, middle_term, y2_term)

    return(expanded_polynomial)


def expanded_no_square_terms(**args):
    unk_list = ["a", "b", "c", "d", ""]
    unk_list.pop(random_coeff(0, 4))
    random.shuffle(unk_list)

    a = unk_list[0]
    b = unk_list[1]
    c = unk_list[2]
    d = unk_list[3]

    # a(b+c) + d(b+c) = ab + ac + db + dc

    a_coeff = random_coeff(-3, 3)
    b_coeff = random_coeff(-3, 3)
    c_coeff = random_coeff(-3, 3)
    d_coeff = random_coeff(-3, 3)

    ab_coeff = a_coeff*b_coeff
    ac_coeff = a_coeff*c_coeff
    db_coeff = d_coeff*b_coeff
    dc_coeff = d_coeff*c_coeff

    ab_term = append_unk_to_coeff(random.choice([a+b, b+a]), ab_coeff)
    ac_term = append_unk_to_coeff(random.choice([a+c, c+a]), ac_coeff)
    db_term = append_unk_to_coeff(random.choice([d+b, b+d]), db_coeff)
    dc_term = append_unk_to_coeff(random.choice([d+c, c+d]), dc_coeff)

    expanded_polynomial = []

    append_all_to_list(expanded_polynomial, ab_term, ac_term, db_term, dc_term)

    return(expanded_polynomial)


def expanded_two_square_terms_same(x_unk: str = "x", y_unk: str = "y", **args):
    perfect_square_common_factor_coeff = random_coeff(-1, 1)

    x_coeff = random_coeff(-3, 3)
    y_coeff = random_coeff(-3, 3)

    perfect_square = expanded_perfect_square(perfect_square_common_factor_coeff, x_coeff=x_coeff, y_coeff=y_coeff, x_unk=x_unk, y_unk=y_unk)

    degree_one_common_factor_coeff = random_coeff(-3, 3)

    x_term_coeff = x_coeff*degree_one_common_factor_coeff
    y_term_coeff = y_coeff*degree_one_common_factor_coeff

    x_term = append_unk_to_coeff(x_unk, x_term_coeff)
    y_term = append_unk_to_coeff(y_unk, y_term_coeff)

    expanded_polynomial = []

    append_all_to_list(expanded_polynomial, perfect_square, x_term, y_term)

    return(expanded_polynomial)
    

def expanded_two_square_terms_diff(x_unk: str = "x", y_unk: str = "y", **args):
    answer = ""

    x_coeff = random_coeff_pos(7) # positive so i can control diff sign
    y_coeff = random_coeff_pos(7)

    degree_one_common_factor_coeff = random_coeff(-3, 3)

    x2_coeff = x_coeff**2
    y2_coeff = -y_coeff**2

    x2_term = append_unk_to_coeff(x_unk, x2_coeff, 2)
    y2_term = append_unk_to_coeff(y_unk, y2_coeff, 2)

    x_term_coeff = x_coeff*degree_one_common_factor_coeff*random_coeff(-1, 1)
    y_term_coeff = y_coeff*degree_one_common_factor_coeff*random_coeff(-1, 1)

    x_term = append_unk_to_coeff(x_unk, x_term_coeff)
    y_term = append_unk_to_coeff(y_unk, y_term_coeff)

    expanded_polynomial = []

    append_all_to_list(expanded_polynomial, x2_term, x_term, y_term, y2_term)

    answer = f"({append_unk_to_coeff(x_unk, x_coeff)}+{append_unk_to_coeff(y_unk, y_coeff)})({append_unk_to_coeff(x_unk, x_coeff)}-{append_unk_to_coeff(y_unk, y_coeff)}{with_sign(degree_one_common_factor_coeff)})" # for both x y term coeff pos

    return(expanded_polynomial)



def expanded_three_square_terms(x_unk: str = "x", y_unk: str = "y", num_unk: str = ""):
    answer = ""
    perfect_square_common_factor_coeff = random_coeff(-1, 1)

    perfect_square = expanded_perfect_square(perfect_square_common_factor_coeff, x_unk=x_unk, y_unk=y_unk)

    number = random_coeff()
    number_square = number**2

    number_square_str = str(number_square)

    if num_unk != "":
        number_square_str = append_unk_to_coeff(num_unk, number_square_str, 2)

    expanded_polynomial = []

    if perfect_square_common_factor_coeff < 0:
        append_all_to_list(expanded_polynomial, f"+{number_square_str}", perfect_square)

        answer = f"({number}+)"
    else:
        append_all_to_list(expanded_polynomial, perfect_square, f"-{number_square_str}")

    return(expanded_polynomial)

def process_input(polynomial_type: str, shuffle: str, **args):
    result = []

    if polynomial_type == "mixed":
        polynomial_type = random.choice(["0_sq", "2_sq_same", "2_sq_diff", "3_sq", "perf_sq"])

    match polynomial_type:
        case "0_sq":
            result = expanded_no_square_terms(**args)
            
        case "2_sq_same":
            result = expanded_two_square_terms_same(**args)

        case "2_sq_diff":
            result = expanded_two_square_terms_diff(**args)

        case "3_sq":
            result = expanded_three_square_terms(**args)

        case "perf_sq":
            result = expanded_perfect_square(**args)

    if shuffle == "on":
        shuffle_list(result)

    return result

print(list_to_string(expanded_three_square_terms("(6a-1)")))
