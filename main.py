# import "packages" from flask
from flask import Flask, render_template, request

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

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
