from data.get_data import get_image

from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtWidgets import (QApplication, QSystemTrayIcon, QMenu, QDialog, 
                               QVBoxLayout,QHBoxLayout,QDialogButtonBox, QLabel)
from PySide6.QtCore import Qt

from custom_dialog import CustomDialog

def show_custom_dialog():
    """Function to show the custom dialog"""
    dialog = CustomDialog()
    
    result = dialog.exec()  # Show dialog and wait for user response
    
    if result == QDialog.DialogCode.Accepted:
        print("User clicked OK")
    else:
        print("User clicked Cancel or closed dialog")


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
image_path = 'src/sunset.png' #get_image()
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
                padding: 5px;
            }}
            QMenu::item {{
                color: #FEBA17;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QMenu::item:selected {{
                color: #74512D;
                background: #FEBA17;
            }}
        '''.format(radius=4))

action = QAction("What does this mean?")
action.triggered.connect(show_custom_dialog) 
menu.addAction(action)

menu.addSeparator()

quit = QAction("❌ Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

app.exec()