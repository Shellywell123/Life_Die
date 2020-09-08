from flask import Response


def fill_template(func):

    def _decorator(*args, **kwargs):
        """ 
        substitutes html_raw with the key_values dictionary conts 

        takes dict with n pairs 
        """

        html_raw, key_values = func(*args, **kwargs)

        for key, value in key_values.items():

            #count all occurences of key
            num_occurences = html_raw.count(key)

            #replace all occurences
            html_raw = html_raw.replace(
                r"{{" + key + r"}}",
                value,
                num_occurences
            )

        return Response(
            iter(html_raw),
            status=200,
            mimetype='text/html'
        )

    return _decorator


def build_buttons(dice_list):
    """
    adds buttons to a string variable, and returns it
    """
    var = ""
    for dice in dice_list:
        var = var + """<!-- Roll Button -->
            <div class="w3-container w3-pink w3-margin w3-padding-large">
                <div class="w3-center">
                  <h3>{}</h3>
                  <h5>{}</h5>
                  <button id="{}" class="w3-button w3-white" onclick="rollDice(this)"><b>Roll</b></button>
                </div>
            </div>
          <!-- End Button -->""".format(dice,"{{todo}}",dice)

    return var
