import pystray
from data.get_data import get_image
from dotenv import load_dotenv

import data.get_data

load_dotenv()

def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()

image = get_image() 

icon = pystray.Icon("Sunset", image, "Sun Tray", menu=pystray.Menu(pystray.MenuItem("Exit", after_click)))

print('Starting!')
icon.run()