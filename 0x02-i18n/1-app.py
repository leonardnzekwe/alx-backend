#!/usr/bin/env python3
"""Flask app with Babel integration."""

from flask import Flask, render_template
from flask_babel import Babel

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


@app.route("/")
def index():
    """Route handler for the homepage."""
    return render_template("1-index.html", languages=app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
