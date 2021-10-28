from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")  # HTTP request: GET /
def index():
    return render_template(
        "index.html", title="Welcome!", heading="Welcome to my home page!",
    )


@app.get("/cv")  # HTTP request: GET /
def cv():
    return render_template("cv.html", heading="My CV",)


@app.get("/interest")  # HTTP request: GET /
def interest():
    return render_template(
        "interest.html", heading="What I like to do away from the computer.",
    )


@app.get("/technologies")  # HTTP request: GET /
def technologies():
    return render_template("technologies.html", heading="Amazing Technologies",)


@app.get("/machinelearning")  # HTTP request: GET /
def ml():
    return render_template("machinelearning.html", heading="Machine Learning",)


@app.get("/cloudcomputing")  # HTTP request: GET /
def cc():
    return render_template("cloudcomputing.html", heading="Cloud Computing",)


@app.get("/3dprinting")  # HTTP request: GET /
def printing():
    return render_template("3dprinting.html", heading="3D Printing",)


@app.get("/message")  # HTTP request: GET /
def message():
    return render_template("message.html",)


@app.get("/form")
def display_form():
    return render_template(
        "form.html",
        title="Feedback Form",
        heading="Please, let me know what do you think of my website.",
    )


@app.post("/processform")
def save_date():
    # python-name = html-name:
    first_name = request.form["firstName"]
    email = request.form["email"]
    message = request.form["message"]

    # use the python names
    with open("comments.txt", "a") as sf:
        print(f"{first_name}, {email}, {message}", file=sf)
    return render_template(
        "message.html", name=first_name, heading="So Long, and Thanks for All the Fish",
    )


if __name__ == "__main__":
    app.run(debug=True)
