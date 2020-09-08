from flask import Flask, send_from_directory
import os

from html_stuff import fill_template, build_buttons

app = Flask(__name__)

some_dice = ["SKATE DICE", "DRINK DICE", "DICE DICE"]

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

    # build buttons
    btns = build_buttons(some_dice)

    return content, {
    'template_test':'hello world',
    'roll_buttons_entry':btns
    }

@app.route("/<string:file>")
def get_asset(file):
    return send_from_directory('web', file)

@app.route("/roll/<string:dice_name>", methods=['POST'])
def roll_dice(dice_name):
    print(dice_name)
    return {"result":"put your result here"}, 200

@app.after_request
def disable_caching(resp):
    resp.cache_control.max_age  = 300
    resp.cache_control.public   = True
    resp.cache_control.no_cache = True
    return resp
