import configparser
config = configparser.ConfigParser()
config.read('preferences.ini')
['preferences.ini']
a=config.get('sessions','startup_mode')
print (a) # -> "show_last_window" show_last_window
b=config.get('python_frontend','theme')
print (b) # -> "linux" linux