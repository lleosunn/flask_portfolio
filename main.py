# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def Stub():
    return render_template("stub.html")

@app.route('/zachary_greet', methods=['GET', 'POST'])
def zachary_greet():
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


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
