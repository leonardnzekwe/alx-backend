#!/usr/bin/env python3
"""Flask app with Babel integration, language selection, and translations."""

from flask import Flask, render_template, request
from flask_babel import Babel, _

# Instantiate Flask app
app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


# Configuration class
class Config:
    """Configuration class for Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use Config for Flask app configuration
app.config.from_object(Config)


# Define get_locale
def get_locale():
    """Determine the best match for the user's preferred language."""
    # Check if 'locale' argument is present in request and is a supported
    # language
    if (
        "locale" in request.args and
        request.args["locale"] in app.config["LANGUAGES"]
    ):
        return request.args["locale"]
    # If not, resort to the previous default behavior
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Route handler for the homepage."""
    # Parametrize templates using gettext function
    title = _("Welcome to Holberton")
    header = _("Hello world!")
    return render_template("4-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
