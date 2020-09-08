

def fill_template(func):

    def _decorator(*args, **kwargs):
        """ 
        substitutes html_raw with the key_values dictionary conts 

        takes dict with n pairs 
        """

        html_raw, key_values = func(*args, **kwargs)

        for key,values in key_values:

            #count all occurences of key
            num_occurences = html_raw.count(key)

            #replace all occurences
            html_raw = html_raw.replace(
                r"{{" + key + r"}}",
                value,
                num_occurences
            )

        return html_raw

    return _decorator





