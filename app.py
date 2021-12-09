from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

import DBcm
from appconfig import config


@app.route("/")
def index():
    return render_template(
        "index.html", title="Welcome!", heading="Welcome to my home page!",
    )


@app.route("/cv")
def cv():
    return render_template("cv.html", heading="My CV",)


@app.route("/interest")
def interest():
    return render_template(
        "interest.html", heading="What I like to do away from the computer.",
    )


@app.route("/technologies")
def technologies():
    return render_template("technologies.html", heading="Amazing Technologies",)


@app.route("/technologies/machinelearning")
def ml():
    return render_template("machinelearning.html", heading="Machine Learning",)


@app.route("/technologies/cloudcomputing")
def cc():
    return render_template("cloudcomputing.html", heading="Cloud Computing",)


@app.route("/technologies/3dprinting")
def printing():
    return render_template("3dprinting.html", heading="3D Printing",)


@app.route("/message")
def message():
    return render_template("message.html",)


@app.route("/form")
def display_form():
    return render_template(
        "form.html",
        title="Feedback Form",
        heading="Please, let me know what do you think of my website.",
    )


@app.route("/processform", methods=["post"])
def save_data():
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
        db.execute(SQL, (first_name, email, message))
    return render_template(
        "message.html", name=first_name, heading="So Long, and Thanks for All the Fish",
    )


@app.get("/visitors")
def get_latest_comments():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select fname,message,time
            from visitors order by time desc
            limit 10
        """
        db.execute(SQL)
        data = db.fetchall()
    return render_template(
        "visitors.html", data=data, heading="Comments from the visitors.",
    )


# this is to display data in json style
@app.get("/getdata")
def get_latest_data():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select fname,email,message,time
            from visitors order by time desc
        """
        db.execute(SQL)
        data = db.fetchall()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
