from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():

    response = requests.get('https://swapi.co/api/planets')
    data = response.json()
    planets = data['results']

    # print(data['results'])

    for planet in planets:
        print(planet['name'])

    index_file = open('index.html', 'r')
    my_html = index_file.read()
    index_file.close()

    return my_html
