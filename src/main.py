import pystray
from PIL import Image

def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()

image_path = 'src/sunset-green.png'

image = Image.open(image_path)

icon = pystray.Icon("Sunset", image, "Sun Tray", menu=pystray.Menu(pystray.MenuItem("Exit", after_click)))

print('Starting!')
icon.run()