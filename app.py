from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():

    index_file = open('index.html', 'r')
    my_html = index_file.read()
    index_file.close()

    return my_html
