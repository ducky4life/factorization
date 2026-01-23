from flask import Flask, jsonify, current_app, Response
from threading import Thread
from waitress import serve
from flask_restful import Resource, Api, reqparse
import requests
from generator import *

parser = reqparse.RequestParser()
parser.add_argument('polynomial_type', type=str, location='form')
parser.add_argument('amount', type=int, location='form')
parser.add_argument('x_unk', type=str, location='form')
parser.add_argument('y_unk', type=str, location='form')
parser.add_argument('sq_unk', type=str, location='form')
parser.add_argument('shuffle_terms', type=str, location='form')
parser.add_argument('prettify', type=str, location='form')
parser.add_argument('help', type=str, location='form')

help_message = """Usage: curl -d '[options]=[value]' https://factorization-generator.vercel.app/api
Options:
    'polynomial_type' (required) - type of polynomial to be generated.

        available options: 0_sq, 2_sq_same, 2_sq_diff, 3_sq,
            perf_sq_1 (expanded), perf_sq_2, diff_sq,
            deg_1_cf_flip, deg_1_cf_noflip, higher_deg_cf_flip, higher_deg_cf_noflip

        randomized options: mixed_all, mixed_identities_only, mixed_no_identities

    'amount' - the amount of polynomials to be generated. defaults to 1.

    'x_unk' - the name for the 'x' unknown.

    'y_unk' - the name for the 'y' unknown. you can enter a space character for constants (no unknown).

    'sq_unk' - the name for the extra square term unknown. only used for 3 square terms.

    'shuffle_terms' - whether to shuffle the different terms in the polynomial. defaults to false.

    'help' - shows this message.

Examples can be found at https://github.com/ducky4life/factorization?tab=readme-ov-file#api-examples
"""

def request_url_to_list(url):
    url_content = requests.get(url, params={"downloadformat": "txt"}).text
    return url_content.split("\n")

class FactorizationApi(Resource):
    def post(self):
        args = parser.parse_args()
        polynomial_type = args['polynomial_type'] if args['polynomial_type'] else 'none'
        amount = args['amount'] if args['amount'] else 1
        x_unk = args['x_unk'] if args['x_unk'] else "x"
        y_unk = args['y_unk'] if args['y_unk'] else "y"
        sq_unk = args['sq_unk'] if args['sq_unk'] else ""
        shuffle_terms = args['shuffle_terms'] if args['shuffle_terms'] else "False"
        prettify = args['prettify'] if args['prettify'] else "False"
        help_needed = args['help']

        if y_unk == " ":
            y_unk = ""

        if help_needed == "":
            response = Response(help_message)
            return(response)

        if prettify.lower() == "true":
            current_app.json.compact = False
        else:
            current_app.json.compact = True

        if shuffle_terms.lower() == "true":
            shuffle_terms = "on"

        generated_dict = dict()
        for i in range(amount):
            generated_dict[f'polynomial_{i+1}'] = list_to_string(process_input(polynomial_type, shuffle_terms, x_unk, y_unk, sq_unk, True), True)

        print(generated_dict)
        return jsonify(generated_dict)
    
    def get(self):
        response = Response(help_message)
        return(response)
