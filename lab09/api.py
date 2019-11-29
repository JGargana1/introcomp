import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Hello World!"

books = [
    {
        'id': 0,
        'title': 'A Fire Upon the deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'
    },
    {
           'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows \
            soaring, the Festival of Summer came to the city of Omelas, \
            bright-towered by the sea.',
        'piblished': '1973'
    },
    {
           'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the atumnal city.',
        'published': '1975'
    }
]

@app.route('/api/books/all', methods=["GET"])
def get_all books():
    return jsonify(books)

@app.errorhandler(404)
def page_not_found(e):
    return "404 - The resource could not be found.",404

@app.route('/api/books', methods=['GET'])
def get_book():
    # Check if an ID was provided as part of the URL.
    # IF ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    #create an empty list for our results
    results = []

    #Loop through the data and match results that fit the requested ID.
    #IDs are unique, but other fields might return many results
    for book in books: 
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from flask to convert our list of 
    # Python dictionaries to the JSON format.
    return jsonify(results)
    

app.run()
