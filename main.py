# import "packages" from flask
from flask import Flask, render_template, request
from flask import Blueprint, render_template
from algorithms.image import image_data
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


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

@app.route('/logic_gates/')
def logic():
    return render_template('logic_gates.html')

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

@app.route("/colorCode")
def colorCode():
    return render_template("colorCode.html")

@app.route("/logicGates")
def logicGates():
    return render_template("logicGates.html")

@app.route("/arcade")
def arcade():
    return render_template("arcade.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
