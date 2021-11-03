# import "packages" from flask
from flask import Flask, render_template, request
from flask import Blueprint, render_template
from algorithms.image import image_data
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import requests
import json

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/stub/')
def Stub():
    return render_template("stub.html")

@app.route('/zachgreet', methods=['GET', 'POST'])
def zachgreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("zachary_greet.html", name=name)
    # starting and empty input default
    return render_template("zachary_greet.html", name="World")

@app.route('/ethangreet', methods=['GET', 'POST'])
def ethangreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("ethangreet.html", name=name)
    # starting and empty input default
    return render_template("ethangreet.html", name="World")

@app.route('/leogreet', methods=['GET', 'POST'])
def leogreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("leohtml.html", name=name)
    # starting and empty input default
    return render_template("leohtml.html", name="World")


@app.route('/reem', methods=['GET', 'POST'])
def reem():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("reem.html", name=name)
    # starting and empty input default
    return render_template("reem.html", name="World")

@app.route('/Mini-labs/')
def video():
    return render_template("Mini-labs.html")

@app.route('/binary/', methods = ['GET', 'POST'])
def binary():
    BITS = 4
    if request.method == 'POST':
        BITS =  int(request.form['BITS'])
    # starting and empty input default
    return render_template("binary.html", BITS=BITS)

@app.route('/about_us/')
def about_us():
    return render_template("about_us.html")

@app.route('/wireframe/')
def wireframe():
    return render_template("wireframe.html")

@app.route('/rgb/')
def rgb():
    return render_template('rgb.html', images=image_data())

@app.route("/binaryaddition")
def binaryaddition():
    return render_template("binaryaddition.html")

@app.route("/colorCode")
def colorCode():
    return render_template("colorCode.html")

@app.route("/logicGates")
def logicGates():
    return render_template("logicGates.html")

@app.route("/spaceClick")
def spaceClick():
    return render_template("spaceClick.html")

@app.route("/arcade")
def arcade():
    return render_template("arcade.html")

@app.route("/reviewPageHollowKnight")
def reviewPageHollowKnight():
    return render_template("reviewPageHollowKnight.html")

@app.route("/reviewPageMinecraft")
def reviewPageMinecraft():
    return render_template("reviewPageMinecraft.html")

@app.route("/reviewPageRocketLeague")
def reviewPageRocketLeague():
    return render_template("reviewPageRocketLeague.html")

@app.route("/reviewPageValorant")
def reviewPageValorant():
    return render_template("reviewPageValorant.html")

@app.route("/reviewPageAmongUs")
def reviewPageAmongUs():
    return render_template("reviewPageAmongUs.html")

@app.route("/reviewPageFortnite")
def reviewPageFortnite():
    return render_template("reviewPageFortnite.html")

@app.route("/reviewPageSeaOfThieves")
def reviewPageSeaOfThieves():
    return render_template("reviewPageSeaOfThieves.html")

@app.route("/reviewPage2k21")
def reviewPage2k21():
    return render_template("reviewPage2k21.html")

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("jokes.html", jokes=response.json())


@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("covid19.html", stats=response.json())

@app.route("/tictactoe")
def tictactoe():
    return render_template("tictactoe.html")

@app.route('/arcadeAPI', methods=['GET', 'POST'])
def arcadeAPI():
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"

    querystring = {"sort-by":"alphabetical"}

    headers = {
        'x-rapidapi-host': "free-to-play-games-database.p.rapidapi.com",
        'x-rapidapi-key': "810c60410fmshe6c6bf953125c9ep188957jsn0e6dd57091ec"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    output = json.loads(response.text)

    return render_template("arcadeAPI.html", Games=output)

@app.route('/guessTheNumber', methods=['GET', 'POST'])
def guessTheNumber():
    # submit button has been pushed
    if request.form:
        number = request.form.get("number")
        if len(number) != 0:  # input field has content
            return render_template("guessTheNumber.html", number=number)
    # starting and empty input default
    return render_template("guessTheNumber.html", number="World")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
