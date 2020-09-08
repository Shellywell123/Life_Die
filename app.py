from flask import Flask, send_from_directory
import os

from html_stuff import fill_template

app = Flask(__name__)

@app.route("/")
@fill_template
def home_page():
    """ will use Jinja2 in the future for templating,
        however for learning experience will be writing our own
        templating decorators

        returns HTML page from directory
    """
    with open(os.path.join( 'web', 'home.html' ), 'r') as f:
        content = f.read()

    return content, {'template_test':'hello world'}
