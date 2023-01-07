from flask import Flask, render_template, request

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


@app.route('/inherit')
def show_extend_page_example():
    """Show example of page that uses base template."""

    return render_template("extend_page_example.html")

@app.route('/hello')
def show_intro_form():
    """Show the intro form."""

    return render_template("html_form.html")

@app.route('/greet')
def show_biography_form_info():
    """Greet the user"""

    # variable = request.args.get(‘variable_name’) 
    # ^whatever goes in the parentheses needs to match whatever was in name in 
    # the form that is being passed through. That then passes the value to 
    # that key with the .get method. 

    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    fav_color = request.args.get("fav_color")

    return render_template("greeting_user.html", 
                            color = fav_color,
                            l_name = last_name,
                            f_name = first_name)
                            # ^ the first variable name will be the name that 
                            # of the variable you will see on the extended page 
                            # (see extend_page_example.html to visualize)
                                    # ^the second variable name will be whatever
                                    # you put as the variable the 
                                    # request.args.get is equal to. 


#this needs to go at the bottom of your python page: 
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
