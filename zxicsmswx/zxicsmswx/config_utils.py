import json

def get_config(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    conf = json.loads(content)
    return fill_default_config(conf)

def set_config_default_value(config, key, value):
    try:
        config[key]
    except KeyError:
        config[key] = value

def fill_default_config(config):
    set_config_default_value(config, 'wx_key', '')
    set_config_default_value(config, 'modems', [])
    return config
