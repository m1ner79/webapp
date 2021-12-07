from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

import DBcm
from appconfig import config


@app.route("/")  # HTTP request: GET /
def index():
    return render_template(
        "index.html", title="Welcome!", heading="Welcome to my home page!",
    )


@app.route("/cv")  # HTTP request: GET /
def cv():
    return render_template("cv.html", heading="My CV",)


@app.route("/interest")  # HTTP request: GET /
def interest():
    return render_template(
        "interest.html", heading="What I like to do away from the computer.",
    )


@app.route("/technologies")  # HTTP request: GET /
def technologies():
    return render_template("technologies.html", heading="Amazing Technologies",)


@app.route("/technologies/machinelearning")  # HTTP request: GET /
def ml():
    return render_template("machinelearning.html", heading="Machine Learning",)


@app.route("/technologies/cloudcomputing")  # HTTP request: GET /
def cc():
    return render_template("cloudcomputing.html", heading="Cloud Computing",)


@app.route("/technologies/3dprinting")  # HTTP request: GET /
def printing():
    return render_template("3dprinting.html", heading="3D Printing",)


@app.route("/message")  # HTTP request: GET /
def message():
    return render_template("message.html",)


@app.route("/form")
def display_form():
    return render_template(
        "form.html",
        title="Feedback Form",
        heading="Please, let me know what do you think of my website.",
    )


@app.route("/processform", methods=["POST"])
def save_date():
    # python-name = html-name:
    first_name = request.form["fname"]
    email = request.form["email"]
    message = request.form["message"]

    # saving data into database
    with DBcm.UseDatabase(config) as db:
        SQL = """
            insert into visitors
            (fname, email,message)
            values
            (%s, %s, %s)
        """
        db.execute(SQL,())


if __name__ == "__main__":
    app.run(debug=True)
