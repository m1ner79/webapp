from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/")  # HTTP request: GET /
def index():
    return render_template("index.html", title = "Welcome!", heading = "Tell us about yourself",)

# @app.get("/showform")
# def display_form():
#     """
#     Retrieve the form.html file from the hard disk and send it to the browser
#     """
#     return render_template("form.html", title = "Welcome form",
#                            heading = "Please, fill in all required details",)

# @app.post("/processform")
# def save_date():
#     """
#     Receive the data from the HTML form, then save it to a desk file,
#     then respond with nice and friendly message to the awaiting browser.

#     Following inputs are expected:first, last and dob.
#     """
#     # python-name = html-name:
#     the_first = request.form["first"]
#     the_last = request.form["last"]
#     the_dob = request.form["dob"]

#     # use the python names
#     with open("suckers.txt", "a") as sf:
#         print(f"{the_first}, {the_last}, {the_dob}", file=sf)
#     return f"Thanks, {the_first}, we promise not to sell your data to the bad guys"

if __name__ == "__main__":
    app.run(debug=True)
