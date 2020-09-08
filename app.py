from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home_page():
    """ will use Jinja2 in the future for templating,
        however for learning experience will be writing our own
        templating decorators

        returns HTML page from directory
    """
    return send_from_directory('web', 'home.html')
