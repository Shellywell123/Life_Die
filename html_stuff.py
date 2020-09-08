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

        return Response(iter(html_raw), status=304, mimetype='text/html')

    return _decorator
