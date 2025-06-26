from data.get_data import get_image

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
image_path = get_image()
icon = QIcon(image_path)

# Create the tray
tray = QSystemTrayIcon(icon=icon)

tray.setVisible(True)

# Create the menu
menu = QMenu()

menu.setStyleSheet('''QMenu {{
                background: #F8F4E1;
                border: 2px solid #4E1F00;
                border-radius: {radius}px;
            }}
            QMenu::item {{
                color: #FEBA17;
            }}
            QMenu::item:selected {{
                color: #74512D;
            }}
        '''.format(radius=4))


action = QAction("A menu item")
menu.addAction(action)
menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec()