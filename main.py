from flask import Flask, request, make_response, jsonify
from selector import get_top_genre


app = Flask(__name__)

'''
Web server for request hadling
'''
@app.route('/')
def get_movies():
    year = request.args.get('year')
    if year == None:
        return make_response("year: parameter required (should be a number)", 400)
    row_count = request.args.get('row_count', default=5)
    top = get_top_genre(int(year), int(row_count))
    return jsonify(top)

app.run(host='0.0.0.0', port=8989)
