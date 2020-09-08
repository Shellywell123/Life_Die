def fill_template(html_raw, key_values):
    """ 
    substitutes html_raw with the key_values dictionary conts 
    """

    for key,values in key_values:

        #count all occurences of key
        num_occurences = html_raw.count(key)

        #replace all occurences
        html_raw = html_raw.replace(key,value,num_occurences)

    return html_raw





