from flask import Flask, render_template

# Name of application
first_app = Flask(__name__)

myTeam = [(1, 'Amir'), (2, 'Ahmed'), (3, 'Shrouk'), (4, 'Omnia'), (5, 'Mayar')]


# distribute routes like amir.com/
@first_app.route("/")
def home_page():
    return render_template("home.html",
                           pagetitle="Home Page",
                           filename_css='home',
                           page_head="Welcome in Home Page",
                           description="This is my Home page",
                           dataset=myTeam)


# distribute routes like amir.com/about
@first_app.route("/about")
def about_page():
    return render_template("about.html",
                           pagetitle="About Page",
                           filename_css="about",
                           page_head="Welcome in About Page",
                           description="This is my About page")


@first_app.route("/add")
def at_page():
    return render_template("add.html",
                           pagetitle="Add Page",
                           filename_css='add',
                           page_head="Welcome in Add Page",
                           description="This is my Add page")


if __name__ == "__main__":
    first_app.run(debug=True, port=9000)
