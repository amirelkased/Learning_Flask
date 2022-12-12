from flask import Flask

# Name of application
first_app = Flask(__name__)


# distribute routes like amir.com/
@first_app.route("/")
def home_page():
    return "Hello home page From flask framework"


# distribute routes like amir.com/about
@first_app.route("/about")
def about_page():
    return "Hello about page From flask framework"


# this line automatically run by python until you run the basis module of it
# if I imported this module in another module it is not running
# main running if and only if you run in its module "directly"
if __name__ == "__main__":
    first_app.run(debug=True, port=9000)
