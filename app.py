from flask import Flask, request, render_template, jsonify
from threading import Thread
from waitress import serve
import requests
import time
from generator import *

app = Flask('')
port = 8085
app.json.compact = False

def request_url_to_list(url):
    url_content = requests.get(url, params={"downloadformat": "txt"}).text
    return url_content.split("\n")

@app.route('/', methods=['GET', 'POST'])
def main_route():
    message = []
    error = ""
    shuffle = ""

    polynomial_type = request.form.get("polynomial_type")
    amount = int(request.form.get("amount")) if request.form.get("amount") else 1
    shuffle = request.form.get("shuffle")

    x_unk = request.form.get("x_unk") if request.form.get("x_unk") else "x"
    y_unk = request.form.get("y_unk") if request.form.get("y_unk") else "y"
    square_unk = request.form.get("square_unk")

    if request.method == 'POST':

        try:
            for i in range(amount):
                message.append(list_to_string(process_input(polynomial_type, shuffle, x_unk, y_unk, square_unk), True))
        except Exception as e:
            error = f"Error: {e}"
            
    return render_template("index.html", message=message, error=error)

def run():
    serve(app, host="0.0.0.0", port=port)

def keep_alive():
    server = Thread(target=run)
    server.start()
    print(f"server is running on port {port}, api route: http://127.0.0.1:{port}/api")

keep_alive()
