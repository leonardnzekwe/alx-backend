#!/usr/bin/env python3
"""
Flask app with user login system, internationalization, and locale priority.
"""

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


# Configuration class
class Config:
    """Configuration class for Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use Config for Flask app configuration
app.config.from_object(Config)


# Define get_user function to get user by ID or login_as parameter
def get_user():
    """Get user dictionary based on ID or login_as parameter."""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


# Define get_locale function
def get_locale():
    """Determine the best match for the user's preferred language."""
    # Check if 'locale' argument is present in request and is a supported
    # language
    if (
        "locale" in request.args and
        request.args["locale"] in app.config["LANGUAGES"]
    ):
        return request.args["locale"]

    # Check if user is logged in and has a preferred locale
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]

    # Check if request header contains a preferred language
    header_locale = request.headers.get("Accept-Language")
    if header_locale:
        # Extract the first language from the Accept-Language header
        languages = [lang.strip() for lang in header_locale.split(",")]
        for lang in languages:
            if lang in app.config["LANGUAGES"]:
                return lang

    # Return default locale
    return app.config["BABEL_DEFAULT_LOCALE"]


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
    return render_template("6-index.html", welcome_message=welcome_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
