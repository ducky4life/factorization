from flask import Flask, request, render_template, jsonify, Response
from threading import Thread
from waitress import serve
import requests
import time
from generator import *

app = Flask('')
port = 8080
app.json.compact = False

def request_url_to_list(url):
    url_content = requests.get(url, params={"downloadformat": "txt"}).text
    return url_content.split("\n")

@app.route('/', methods=['GET', 'POST'])
def main_route():
    message = []
    error = ""
    output_as_file = ""
    shuffle = ""

    polynomial_type = request.form.get("polynomial_type")
    amount = int(request.form.get("amount")) if type(request.form.get("amount")) == int else 1
    shuffle = request.form.get("shuffle")
    output_as_file = request.form.get("output_as_file")

    if amount > 999: # why do you need this many
        amount = 1000

    x_unk = request.form.get("x_unk") if request.form.get("x_unk") else "x"
    y_unk = request.form.get("y_unk") if request.form.get("y_unk") else "y"
    square_unk = request.form.get("square_unk")

    if request.method == 'POST':

        try:
            for i in range(amount):
                message.append(list_to_string(process_input(polynomial_type, shuffle, x_unk=x_unk, y_unk=y_unk, num_unk=square_unk), True))
        except Exception as e:
            error = f"Error: {e}"


        if output_as_file == "on":

            output_file_name = f"factorization_output_{int(time.time())}"
            response = Response("\n".join(message), mimetype="text/plain")
            response.headers["Content-Disposition"] = f"attachment; filename={output_file_name}"
            return response
            
    return render_template("index.html", message=message, error=error, form=request.form)

def run():
    serve(app, host="0.0.0.0", port=port)

def keep_alive():
    server = Thread(target=run)
    server.start()
    print(f"server is running on port {port}, api route: http://127.0.0.1:{port}/api")

keep_alive()
