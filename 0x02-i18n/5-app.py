#!/usr/bin/env python3
"""Flask app with user login system and internationalization."""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Instantiate Flask app
app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Define get_user function to get user by ID or login_as parameter
def get_user():
    """Get user dictionary based on ID or login_as parameter."""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


# Define before_request function to set user as global on flask.g
@app.before_request
def before_request():
    """Set user as global on flask.g."""
    g.user = get_user()


@app.route("/")
def index():
    """Route handler for the homepage."""
    # Get user's name from user dictionary if logged in
    username = g.user["name"] if g.user else None
    # Parametrize templates using gettext function
    welcome_message = (
        _("You are logged in as %(username)s.") % {"username": username}
        if g.user
        else _("You are not logged in.")
    )
    return render_template("5-index.html", welcome_message=welcome_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
