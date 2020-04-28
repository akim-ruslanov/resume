
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")
    # return "He"
    # return "He"1


# some lines omitted here

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name") # take the request the user made, access the form,
                                    # and store the field called `name` in a Python variable also called `name`
    print(name)
    return render_template("hello.html", name=name)
    # return name

if __name__ == "__main__":
    app.run(debug = True)