import random
import math
from random import randrange

def shuffle(array):
    "Fisher–Yates shuffle"
    for i in range(len(array)-1, 0, -1):
        j = randrange(i+1)
        array[i], array[j] = array[j], array[i]

def removeprefix(input: str, prefix: str):
    if input[0] == prefix:
        return input[1:]
    return input

# helper functions

latex_mode =  False
superscript_list = ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"]

def random_coeff_pos(max_incl: int = 9):
    return random.randint(1, max_incl)

def random_coeff(min_incl: int = -9, max_incl: int = 9):
    number = random.randint(min_incl, max_incl-1) # don't include max: map getting 0 to max
    if number == 0:
        number = max_incl # avoid recursive
    return number

def superscript(num: int = 2):
    global latex_mode
    local_superscript_list = superscript_list
    if num < 10 and not latex_mode:
        return(local_superscript_list[num])
    elif not latex_mode:
        return(local_superscript_list[2])
    else:
        return(f"^{num}")

def parity_shift(unk):
    unk = unk + 1 if unk != -1 else -2
    return unk

def with_sign(coeff: int, trim_one: bool = True):
    sign = "+"
    if coeff < 0:
        sign = ""

    if trim_one:
        if coeff == 1: # don't write out 1 as coeff
            return(sign)
        elif coeff == -1:
            return("-")

    return(f"{sign}{coeff}")

def linear_generator(x_unk: str = "x", y_unk: str = "y", minus_form: bool = False, with_common_factor: bool = False, trim: bool = True, coeff_limit: int = 3, x_coeff: int = None, y_coeff: int = None):
    if x_coeff == None and y_coeff == None:
        x_coeff = random_coeff(-coeff_limit, coeff_limit)
        y_coeff = random_coeff(-coeff_limit, coeff_limit)
    
        if minus_form: # output must be in (ax-by) form
            x_coeff = random_coeff_pos(coeff_limit)
            y_coeff = -random_coeff_pos(coeff_limit)
    
        if with_common_factor:
            common_factor_coeff = random_coeff()
            if trim == False:
                common_factor_coeff = with_sign(common_factor_coeff)
    
        if abs(x_coeff) == abs(y_coeff):
            x_coeff = parity_shift(x_coeff)

    x_term = append_unk_to_coeff(x_unk, x_coeff)
    y_term = append_unk_to_coeff(y_unk, y_coeff)

    if y_unk == "":
        y_term = with_sign(y_coeff, False)

    linear_unk = removeprefix(x_term + y_term, "+")

    linear_term = "(" + linear_unk + ")"
    return(str(common_factor_coeff) + linear_term if with_common_factor else linear_term)

# does not check if input is in (ax-by) form
def flip_linear_term(term: str):
    local_superscript_list = superscript_list
    term = removeprefix(term, "(")
    term_power = term.split(")")[-1]
    term_list = term[0:term.index(")")].split("-")

    new_term = "(" + term_list[-1] + "-" + term_list[0] + ")"
    if term_power in local_superscript_list:
        new_term = new_term + term_power
    return(new_term)

def multiply_term_to_polynomial(term: str, polynomial_list: list, random_flip_sign: bool = False, higher_degree: bool = False):
    local_superscript_list = superscript_list
    
    global latex_mode
    if latex_mode:
        local_superscript_list = ["^0", "^1", "^2", "^3", "^4", "^5", "^6", "^7", "^8", "^9"]
    
    linear_term = term[0:term.index(")")+1]
    added_term = term
    new_list = []

    if higher_degree:
        item_power = local_superscript_list.index(term.split(")")[-1]) + 1
    
    for item in polynomial_list:
        if random_flip_sign:
            is_flip_sign = random.choice([True, False])
            if is_flip_sign:
                added_term = flip_linear_term(term)
                
        if linear_term in item or flip_linear_term(linear_term) in item:
            if higher_degree:
                item = item + superscript(item_power)
            else:
                item = item + superscript(2)
        elif item != "1":
            item = item + added_term
        else:
            item = added_term

        new_list.append(item)
    return(new_list)

def append_unk_to_coeff(unk: str, coeff: int, power: int = 1, sign: bool = True):
    if power != 1:
        if sign:
            return(f"{with_sign(coeff)}{unk}{superscript(power)}")
        else:
            return(f"{coeff}{unk}{superscript(power)}")
    else:
        if sign:
            return(f"{with_sign(coeff)}{unk}")
        else:
            return(f"{coeff}{unk}")

def shuffle_list(input_list: list):
    shuffle(input_list)
    return input_list

def list_to_string(input_list: list, trim: bool = True):
    output_str = ""
    global latex_mode

    for item in input_list:
        output_str = output_str + str(item)

    if trim:
        output_str = removeprefix(output_str, "+")

    if latex_mode:
        output_str = "$" + output_str + "$"
    
    return output_str

def append_all_to_list(list_to_append: list, *args):
    for item in args:
        if type(item) == list:
            for element in item:
                list_to_append.append(element)
        else:
            list_to_append.append(item)



# generator functions

def linear_difference_of_squares(x_unk: str = "x", y_unk: str = "y", **args):
    first_linear_term = linear_generator(x_unk, y_unk)
    second_linear_term = linear_generator(x_unk, y_unk)

    while first_linear_term == second_linear_term:
        second_linear_term = linear_generator(x_unk, y_unk)

    first_square_coeff = random_coeff_pos(4)
    second_square_coeff = random_coeff_pos(4)

    if first_square_coeff%2 == second_square_coeff%2 == 0 or (first_square_coeff == second_square_coeff and first_square_coeff != 1):
        first_square_coeff = parity_shift(first_square_coeff)

    first_square_term = append_unk_to_coeff(first_linear_term, first_square_coeff**2, 2)
    second_square_term = append_unk_to_coeff(second_linear_term, -second_square_coeff**2, 2)

    polynomial = []

    append_all_to_list(polynomial, first_square_term, second_square_term)
    return(polynomial)


def linear_degree_one_common_factor(flip_sign: bool = False, x_unk: str = "x", y_unk: str = "y", **args):
    first_linear_term = linear_generator(x_unk, y_unk, with_common_factor=True, trim=False, coeff_limit=5)
    second_linear_term = linear_generator(x_unk, y_unk, with_common_factor=True, trim=False, coeff_limit=5)
    third_linear_term = linear_generator(x_unk, y_unk, with_common_factor=True, trim=False, coeff_limit=5)

    degree_one_common_factor = linear_generator(x_unk, y_unk, flip_sign)
    
    if random_coeff_pos(3) == 1: # increase probability of squares happening
        first_coeff = random_coeff(-5, 5)
        first_linear_term = append_unk_to_coeff(degree_one_common_factor, first_coeff)
    
    polynomial = []
    append_all_to_list(polynomial, first_linear_term, second_linear_term, third_linear_term)

    polynomial = multiply_term_to_polynomial(degree_one_common_factor, polynomial, flip_sign)
            
    return(polynomial)


def higher_degree_common_factor(flip_sign: bool = False, x_unk: str = "x", y_unk: str = "y", **args):
    first_linear_equal_common_factor = False
    first_linear_term = linear_generator(x_unk, y_unk, with_common_factor=True, trim=False, coeff_limit=5)
    second_linear_term = linear_generator(x_unk, y_unk, with_common_factor=True, trim=False, coeff_limit=5)

    linear_common_factor = linear_generator(x_unk, y_unk, flip_sign)

    while linear_common_factor in first_linear_term:
        first_linear_term = linear_generator(x_unk, y_unk, with_common_factor=True, trim=False, coeff_limit=5)
    while linear_common_factor in second_linear_term:
        second_linear_term = linear_generator(x_unk, y_unk, with_common_factor=True, trim=False, coeff_limit=5)

    power = random_coeff(2, 4)
    
    common_factor_term = linear_common_factor + superscript(power)
    
    if random_coeff_pos(3) == 1: # chance for same linear generator
        first_coeff = random_coeff(-5, 5)
        first_linear_term = append_unk_to_coeff(linear_common_factor, first_coeff)
        first_linear_equal_common_factor = True
    
    polynomial = []
    append_all_to_list(polynomial, first_linear_term, second_linear_term)

    polynomial = multiply_term_to_polynomial(common_factor_term, polynomial, flip_sign, first_linear_equal_common_factor)
            
    return(polynomial)


def linear_perfect_square(x_unk: str = "x", y_unk: str = "", **args):
    x_coeff = random_coeff(2, 9)
    y_coeff = -random_coeff(2, 9)

    while math.gcd(x_coeff, y_coeff) == 1:
        x_coeff = random_coeff(2, 9)
        y_coeff = -random_coeff(2, 9)
        
    split_int = -random_coeff_pos(abs(y_coeff)-1) # (6x-4) = (6x-3 -1) = 3(2x-1) -1 = 3a-1
    new_y_coeff = y_coeff - split_int

    #original_linear_term = linear_generator(x_unk, y_unk, x_coeff=x_coeff, y_coeff=new_y_coeff)
    #print(original_linear_term)
    common_factor_coeff = math.gcd(x_coeff, new_y_coeff)
    simplified_x_coeff = int(x_coeff/common_factor_coeff)
    simplified_y_coeff = int(new_y_coeff/common_factor_coeff)

    new_linear_term = linear_generator(x_unk, y_unk, x_coeff=simplified_x_coeff, y_coeff=simplified_y_coeff)
    
    perfect_square_term = expanded_perfect_square(1, common_factor_coeff, split_int, new_linear_term, "")

    polynomial = []
    append_all_to_list(polynomial, perfect_square_term)
    return(polynomial)


def expanded_perfect_square(common_factor_coeff: int = None, x_coeff: int = None, y_coeff: int = None, x_unk: str = "x", y_unk: str = "y", **args):

    if common_factor_coeff == None:
        common_factor_coeff = random_coeff(-3, 3)
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

    if y_unk == "":
        y2_term = with_sign(y2_coeff, False)

    expanded_polynomial = []
    append_all_to_list(expanded_polynomial, x2_term, middle_term, y2_term)

    return(expanded_polynomial)


def expanded_no_square_terms(**args):
    unk_list = ["a", "b", "c", "d", ""]
    unk_list.pop(random.randint(0, 4))
    shuffle_list(unk_list)

    a = unk_list[0]
    b = unk_list[1]
    c = unk_list[2]
    d = unk_list[3]

    # a(b+c) + d(b+c) = ab + ac + db + dc

    a_coeff = random_coeff(-3, 3)
    b_coeff = random_coeff(-3, 3)
    c_coeff = random_coeff(-3, 3)
    d_coeff = random_coeff(-3, 3)

    # avoid the entire polynomial having same common factor
    if abs(a_coeff) == abs(d_coeff):
        a_coeff = parity_shift(a_coeff)

    # 2. make sure b != c
    if abs(b_coeff) == abs(c_coeff):
        b_coeff = parity_shift(b_coeff)

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

    if abs(x_coeff) == abs(y_coeff): # entire polynomial c.f.
        x_coeff = parity_shift(x_coeff)

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

    if x_coeff%3 == y_coeff%3 == 0 or abs(x_coeff) == abs(y_coeff) or x_coeff%2 == y_coeff%2 == 0:
         x_coeff = parity_shift(x_coeff)

    degree_one_common_factor_coeff = random_coeff(-3, 3)

    if degree_one_common_factor_coeff%2 == x_coeff%2 == y_coeff%2:
        degree_one_common_factor_coeff = parity_shift(degree_one_common_factor_coeff)

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
    number_square = number**2 if perfect_square_common_factor_coeff < 0 else -number**2
    number_square_term = with_sign(number_square, False) 

    if num_unk != "":
        number_square_term = with_sign(number_square, True)
        number_square_term = append_unk_to_coeff(num_unk, number_square, 2)

    expanded_polynomial = []

    if perfect_square_common_factor_coeff < 0:
        append_all_to_list(expanded_polynomial, number_square_term, perfect_square)

        answer = f"({number}+)"
    else:
        append_all_to_list(expanded_polynomial, perfect_square, number_square_term)

    return(expanded_polynomial)



# for (randomly) choosing one of the generator functions
def process_input(polynomial_type: str, shuffle: str, x_unk: str, y_unk: str, num_unk: str, latex: bool, **args):
    result = []
    default_y_unk_constant = ["perf_sq_2"]
    cannot_have_constant_y_unk = ["2_sq_diff", "2_sq_same"]

    global latex_mode
    latex_mode = latex

    if polynomial_type == "mixed_all":
        polynomial_type = random.choice(["0_sq", "2_sq_same", "2_sq_diff", "3_sq", "perf_sq", "diff_sq", "deg_1_cf", "higher_deg_cf"])
        
        if polynomial_type == "deg_1_cf":
            polynomial_type = random.choice(["deg_1_cf_flip", "deg_1_cf_noflip"])
        elif polynomial_type == "perf_sq":
            polynomial_type = random.choice(["perf_sq_1", "perf_sq_2"])
        elif polynomial_type == "higher_deg_cf":
            polynomial_type = random.choice(["higher_deg_cf_flip", "higher_deg_cf_noflip"])
            
    elif polynomial_type == "mixed_identities_only":
        polynomial_type = random.choice(["2_sq_same", "2_sq_diff", "3_sq", "perf_sq", "diff_sq"])
        if polynomial_type == "perf_sq":
            polynomial_type = random.choice(["perf_sq_1", "perf_sq_2"])

    elif polynomial_type == "mixed_no_identities":
        polynomial_type = random.choice(["0_sq", "deg_1_cf", "higher_deg_cf"])
        if polynomial_type == "deg_1_cf":
            polynomial_type = random.choice(["deg_1_cf_flip", "deg_1_cf_noflip"])
        elif polynomial_type == "higher_deg_cf":
            polynomial_type = random.choice(["higher_deg_cf_flip", "higher_deg_cf_noflip"])

    if x_unk == None:
        x_unk = "x"

    if y_unk == None:
        if polynomial_type in default_y_unk_constant:
            y_unk = ""
        else:
            y_unk = "y"

    if y_unk == "" and polynomial_type in cannot_have_constant_y_unk:
        y_unk = "y"
        
    # match polynomial_type:
    #     case "0_sq":
    #         result = expanded_no_square_terms(x_unk=x_unk, y_unk=y_unk, **args)
            
    #     case "2_sq_same":
    #         result = expanded_two_square_terms_same(x_unk=x_unk, y_unk=y_unk, **args)

    #     case "2_sq_diff":
    #         result = expanded_two_square_terms_diff(x_unk=x_unk, y_unk=y_unk, **args)

    #     case "3_sq":
    #         if num_unk == "" and y_unk == "":
    #             y_unk = "y"
                
    #         result = expanded_three_square_terms(x_unk=x_unk, y_unk=y_unk, num_unk=num_unk, **args)

    #     case "perf_sq_1":
    #         result = expanded_perfect_square(x_unk=x_unk, y_unk=y_unk, **args)

    #     case "perf_sq_2":
    #         result = linear_perfect_square(x_unk=x_unk, y_unk=y_unk, **args)

    #     case "diff_sq":
    #         result = linear_difference_of_squares(x_unk=x_unk, y_unk=y_unk, **args)

    #     case "deg_1_cf_flip":
    #         result = linear_degree_one_common_factor(True, x_unk=x_unk, y_unk=y_unk, **args)

    #     case "deg_1_cf_noflip":
    #         result = linear_degree_one_common_factor(False, x_unk=x_unk, y_unk=y_unk, **args)

    #     case "higher_deg_cf_flip":
    #         result = higher_degree_common_factor(True, x_unk=x_unk, y_unk=y_unk, **args)

    #     case "higher_deg_cf_noflip":
    #         result = higher_degree_common_factor(False, x_unk=x_unk, y_unk=y_unk, **args)

    if polynomial_type == "0_sq":
        result = expanded_no_square_terms(x_unk=x_unk, y_unk=y_unk, **args)
        
    elif polynomial_type == "2_sq_same":
        result = expanded_two_square_terms_same(x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "2_sq_diff":
        result = expanded_two_square_terms_diff(x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "3_sq":
        if num_unk == "" and y_unk == "":
            y_unk = "y"
            
        result = expanded_three_square_terms(x_unk=x_unk, y_unk=y_unk, num_unk=num_unk, **args)

    elif polynomial_type == "perf_sq_1":
        result = expanded_perfect_square(x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "perf_sq_2":
        result = linear_perfect_square(x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "diff_sq":
        result = linear_difference_of_squares(x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "deg_1_cf_flip":
        result = linear_degree_one_common_factor(True, x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "deg_1_cf_noflip":
        result = linear_degree_one_common_factor(False, x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "higher_deg_cf_flip":
        result = higher_degree_common_factor(True, x_unk=x_unk, y_unk=y_unk, **args)

    elif polynomial_type == "higher_deg_cf_noflip":
        result = higher_degree_common_factor(False, x_unk=x_unk, y_unk=y_unk, **args)

    if shuffle == "on":
        shuffle_list(result)

    return result



def print_examples():
    # examples

    # 3 square terms
    print("3 square terms: ", list_to_string(expanded_three_square_terms("(6a-1)")))

    # 2 square terms
    print("2 square terms (diff sign): ", list_to_string(expanded_two_square_terms_diff()))
    print("2 square terms (same sign): ", list_to_string(expanded_two_square_terms_same()))

    # no square terms
    print("no square terms: ", list_to_string(expanded_no_square_terms()))

    # difference of squares
    print("difference of squares: ", list_to_string(linear_difference_of_squares()))

    # perfect squares
    print("perfect squares: ", list_to_string(expanded_perfect_square()))
    print("linear term perfect squares: ", list_to_string(linear_perfect_square()))

    # common factors for an entire polynomial
    print("degree one common factor (flip signs): ", list_to_string(linear_degree_one_common_factor(True)))
    print("degree one common factor (without flipping signs): ", list_to_string(linear_degree_one_common_factor(False)))
    print("higher degrees common factor (flip signs): ", list_to_string(higher_degree_common_factor(True)))
    print("higher degrees common factor (without flipping signs): ", list_to_string(higher_degree_common_factor(False)))

# print_examples()
