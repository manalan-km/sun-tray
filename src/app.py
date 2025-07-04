from data.get_data import get_image

from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtWidgets import (QApplication, QSystemTrayIcon, QMenu, QDialog, 
                               QVBoxLayout,QHBoxLayout,QDialogButtonBox, QLabel)
from PySide6.QtCore import Qt

from custom_dialog import CustomDialog


class App():
    def __init__(self):
       self.app = QApplication([])
       self.app.setQuitOnLastWindowClosed(False)
       self.image_path = get_image()
       
    def start_app(self):
        
        icon = QIcon(self.image_path)

        tray = QSystemTrayIcon(icon=icon)
        tray.setVisible(True)

        menu = QMenu()
        
        action = QAction("What does this mean?")
        action.triggered.connect(self.show_custom_dialog) 
        menu.addAction(action)

        menu.addSeparator()

        quit = QAction("Quit")
        quit.triggered.connect(self.app.quit)
        menu.addAction(quit)

        self.set_style_for_menu(menu)
        tray.setContextMenu(menu)

        self.app.exec()
        
    def show_custom_dialog(self):
        """Function to show the custom dialog"""
        dialog = CustomDialog(self.image_path)
        
        dialog.exec() 
    
    def set_style_for_menu(self,q_menu: QMenu):
        q_menu.setStyleSheet('''QMenu {{
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