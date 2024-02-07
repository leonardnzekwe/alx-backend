#!/usr/bin/env python3
"""Flask app with Babel integration and language selection."""

from flask import Flask, render_template, request

# Instantiate Flask app
app = Flask(__name__)


# Configuration class
class Config:
    """Configuration class for Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Use Config for Flask app configuration
app.config.from_object(Config)


def get_locale():
    """Determine the best match for the user's preferred language."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Route handler for the homepage."""
    # Get the selected language
    selected_language = get_locale()
    # Pass the selected language to the template
    return render_template("2-index.html", selected_language=selected_language)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
