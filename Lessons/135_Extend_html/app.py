from flask import Flask, render_template

# We need here to render a page "HTML CSS JS" not print message

# Name of application
first_app = Flask(__name__)


# distribute routes like amir.com/
@first_app.route("/")
def home_page():
    return render_template("home.html", pagetitle="Home Page")


# distribute routes like amir.com/about
@first_app.route("/about")
def about_page():
    return render_template("about.html", pagetitle="About Page")


if __name__ == "__main__":
    first_app.run(debug=True)
