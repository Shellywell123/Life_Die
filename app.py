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

@app.route("/<string:file>")
def get_asset(file):
    return send_from_directory('web', file)

@app.route("/roll/<string:dice_name>")
def roll_dice(dice_name):
    print(dice_name)
    return {}, 200

@app.after_request
def disable_caching(resp):
    resp.cache_control.max_age  = 300
    resp.cache_control.public   = True
    resp.cache_control.no_cache = True
    return resp
