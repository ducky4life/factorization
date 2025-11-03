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
    message = ""
    error = ""

    

    if request.method == 'POST':

        try:
            message = list_to_string(expanded_three_square_terms("x", "y", ""))
        except Exception as e:
            error = f"Error: {e}"
            
    return render_template("index.html", message=message, error=error, filepath=output_file_name)

def run():
    serve(app, host="0.0.0.0", port=port)

def keep_alive():
    server = Thread(target=run)
    server.start()
    print(f"server is running on port {port}, api route: http://127.0.0.1:{port}/api")

keep_alive()
