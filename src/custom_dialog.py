from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QHBoxLayout, QLabel,QWidget
from PySide6.QtCore import Qt, QMargins
from PySide6.QtGui import QFont


from PySide6.QtGui  import QPixmap


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_explanation()
        self.apply_styles()
    
    def setup_ui(self):
        self.setWindowTitle("What does this mean?")
        self.setFixedSize(500, 350)
        
        QBtn = (QDialogButtonBox.Close)
        main_layout = QHBoxLayout()
        
        explaination_layout = self.setup_explanation()
        sunset_details_layout = self.setup_sunset_details()
        
        main_layout.addLayout(explaination_layout)
        main_layout.addLayout(sunset_details_layout)
        
        self.setLayout(main_layout)
  
        
    def setup_explanation(self):
       setup_main_layout = QVBoxLayout()
       
       group_one_layout = QHBoxLayout()
       image_one = QLabel()
       image_one.setPixmap(QPixmap('src/sunset-grey.png'))
       label_one = QLabel('Poor', alignment=Qt.AlignmentFlag.AlignLeft)
       label_one.setAlignment(Qt.AlignmentFlag.AlignVCenter)
       group_one_layout.addWidget(image_one)
       group_one_layout.addWidget(label_one)
       
       group_two_layout = QHBoxLayout()
       image_two = QLabel()
       image_two.setPixmap(QPixmap('src/sunset-blue.png'))
       label_two = QLabel('Fair', alignment=Qt.AlignmentFlag.AlignLeft)
       label_two.setAlignment(Qt.AlignmentFlag.AlignVCenter)
       group_two_layout.addWidget(image_two)
       group_two_layout.addWidget(label_two)
       
       group_three_layout = QHBoxLayout()
       image_three = QLabel()
       image_three.setPixmap(QPixmap('src/sunset-green.png'))
       label_three = QLabel('Good', alignment=Qt.AlignmentFlag.AlignLeft)
       label_three.setAlignment(Qt.AlignmentFlag.AlignVCenter)
       group_three_layout.addWidget(image_three)
       group_three_layout.addWidget(label_three)
       
       group_four_layout = QHBoxLayout()
       image_four = QLabel()
       image_four.setPixmap(QPixmap('src/sunset-yellow.png'))
       label_four = QLabel('Great', alignment=Qt.AlignmentFlag.AlignLeft)
       label_four.setAlignment(Qt.AlignmentFlag.AlignVCenter)
       group_four_layout.addWidget(image_four)
       group_four_layout.addWidget(label_four)
       
       group_five_layout = QHBoxLayout()
       image_five = QLabel()
       image_five.setPixmap(QPixmap('src/sunset.png'))
       label_five = QLabel('Excellent', alignment=Qt.AlignmentFlag.AlignLeft)
       label_five.setAlignment(Qt.AlignmentFlag.AlignVCenter)
       group_five_layout.addWidget(image_five)
       group_five_layout.addWidget(label_five)
       
       setup_main_layout.addLayout(group_one_layout)
       setup_main_layout.addLayout(group_two_layout)
       setup_main_layout.addLayout(group_three_layout)
       setup_main_layout.addLayout(group_four_layout)
       setup_main_layout.addLayout(group_five_layout)
       
       return setup_main_layout
       
    
    def setup_sunset_details(self):
       sunset_details_main = QVBoxLayout()
       
       widget = QWidget(self)
       
       title = QLabel("Today's Sunset Quality",alignment= Qt.AlignmentFlag.AlignCenter)
       title.setFont(QFont('Arial', 18))
       title.setContentsMargins(QMargins(0,0,0,0))
       
       sunset =  QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
       sunset.setPixmap(QPixmap('src/sunset.png'))
       
       
       sunset_details_main.addWidget(title)
       sunset_details_main.addWidget(sunset)
       sunset_details_main.setSpacing(0)
       
       return sunset_details_main
         
    def apply_styles(self):
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #F8F4E1, stop:1 #E8D4A1);
                border-radius: 15px;
            }
            
            QLabel {
                color: #4E1F00;
                background: transparent;
                border: 1px solid black;
                margin: 0px;
                font: Arial;
                font-size: 20px;
            }
            
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #FEBA17, stop:1 #E8A317);
                border: 2px solid #4E1F00;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 12px;
                font-weight: bold;
                color: #4E1F00;
                min-width: 80px;
            }
            
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #FFCC47, stop:1 #FEBA17);
                border-color: #74512D;
            }
            
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #E8A317, stop:1 #D4930F);
            }
        """)
