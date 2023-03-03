from flask import Flask, render_template, redirect, url_for

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to the different paths
@app.route("/")
def index():
    return render_template("index.html", name_browser_tab="Index")


@app.route("/home")
def home():
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html", name_browser_tab="About")


@app.route("/cow")
def cow():
    return render_template("cow.html", name_browser_tab="Cow")


@app.route("/dog")
def dog():
    return render_template("dog.html", name_browser_tab="Dog")
