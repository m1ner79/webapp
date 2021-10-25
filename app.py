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


@app.get("/technologies")  # HTTP request: GET /
def technologies():
    return render_template("technologies.html", heading="Amazing Technologies",)


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
    return f"Thank you for your feedback {first_name}!"


if __name__ == "__main__":
    app.run(debug=True)
