from flask import Flask, send_from_directory
import os

from html_stuff import fill_template, build_buttons

from Die_class import *
d = die()

app = Flask(__name__)

some_dice = ["SKATE DICE", "DRINK DICE", "DICE DICE","COIN FLIP"]

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
    'template_test':'<a href="https://github.com/Shellywell123/Life_Die">Github Project</a>',
    'roll_buttons_entry':btns
    }

@app.route("/<string:file>")
def get_asset(file):
    return send_from_directory('web', file)

@app.route("/roll/<string:dice_name>", methods=['POST'])
def roll_dice(dice_name):
    """
    execute roll
    """
    # needs to be a unique statment for each dice in some_dice
    if dice_name == "SKATE DICE":
        return {"result":d.roll_skate_preset()}, 200

    if dice_name == "DRINK DICE":
        return {"result":d.roll_cocktail_preset()}, 200

    if dice_name == "DICE DICE":
        return {"result":d.roll_roll_a_dice()}, 200

    if dice_name == "COIN FLIP":
        return {"result":d.flip_coin_preset()}, 200

@app.after_request
def disable_caching(resp):
    resp.cache_control.max_age  = 300
    resp.cache_control.public   = True
    resp.cache_control.no_cache = True
    return resp
