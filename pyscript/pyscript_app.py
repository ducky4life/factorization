import time
from pyscript.generator_mpy import process_input, list_to_string
from pyscript import web, when

# def request_url_to_list(url):
#     url_content = requests.get(url, params={"downloadformat": "txt"}).text
#     return url_content.split("\n")

def get_output():
    message = []
    error = ""
    shuffle = ""
    latex_mode = ""

    polynomial_type = web.page["polynomial_type"].value
    amount_str = web.page["amount"].value if web.page["amount"].value else 1
    shuffle = web.page["shuffle"].checked
    latex_mode = web.page["latex_mode"].checked

    latex_bool = True if latex_mode else False

    amount = 1

    try:
        amount = int(amount_str)
    except ValueError:
        error = "please enter an integer as amount"
        
    if amount > 999: # why do you need this many
        amount = 1000
    
    x_unk = web.page["x_unk"].value if web.page["x_unk"].value else None
    y_unk = web.page["y_unk"].value if web.page["y_unk"].value else None
    if y_unk == " ":
        y_unk = ""
    square_unk = web.page["square_unk"].value if web.page["square_unk"].value else ""

    try:
        for i in range(amount):
            message.append(list_to_string(process_input(polynomial_type, shuffle, x_unk=x_unk, y_unk=y_unk, num_unk=square_unk, latex=latex_bool), True))
    except Exception as e:
        error = f"Error: {e}"
        return error

    return " ".join(message)

def display_output(output: str):
    output_box = web.page["#output"]
    output_box.innerHTML = output

@when("click", "#submit")
def output(event):
    display_output(get_output())
