from flask import Flask
from flask import render_template

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


# GET Request Notes:
# The GET method is implied by default an HTML form…

# <form action="/greet">
# is the same as specifying:
# <form action="/greet" method="GET">

# ...and the GET method is implied by default in the route
# @app.route('/greet')
# is the same as specifying:
# @app.route('/greet', methods=['GET'])

@app.route('/')
def show_homepage():
    """Home page."""

    return render_template("homepage.html")
    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
