import os
# import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['url']
            animal = request.form['animal']
            colour = request.form['colour']
            print(request.form)
            print(url)
            # r = requests.get(url)
            # print(r.text)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
        return "<h1>You wanted " + url + " " + animal + " " + colour + "</h1>"
    if request.method == "GET":
        return render_template('index.html', errors=errors, results=results)
if __name__ == '__main__':
    app.run()
