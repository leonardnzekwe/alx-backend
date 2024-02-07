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


# Define get_locale function with babel.localeselector decorator
def get_locale():
    """Determine the best match for the user's preferred language."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Route handler for the homepage."""
    # Parametrize templates using gettext function
    title = "Welcome to Holberton"
    header = "Hello world!"
    # Get the selected language
    selected_language = get_locale()
    # Pass the selected language to the template
    return render_template(
        "3-index.html", title=title, header=header,
        selected_language=selected_language
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
