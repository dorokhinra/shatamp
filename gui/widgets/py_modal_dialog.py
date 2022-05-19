import os
from qt_core import *
from PyQt5.QtWidgets import QWidget

class UiDialog(QWidget):

    def __init__(self, title, message):
        super().__init__()
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, "stamp.png"))
        self.style_d = self.style_dialog()
        self.context_dialog = QDialog()
        self.context_dialog.setWindowIcon(QIcon(icon_path))
        self.context_dialog.setWindowTitle(title)
        self.context_dialog.setStyleSheet(self.style_d['style'])
        self.dialog_layout = QVBoxLayout()

        self.infoLabel = QLabel()
        self.infoLabel.setText(message)
        self.infoLabel.setAlignment(Qt.AlignCenter)

        self.button_ok = QPushButton()
        self.button_ok.setText('Принять')

        self.dialog_layout.addWidget(self.infoLabel)
        self.dialog_layout.addWidget(self.button_ok)

        self.button_ok.clicked.connect(self.close_dialog)
        self.context_dialog.setLayout(self.dialog_layout)
        self.context_dialog.resize(200, 100)
        self.context_dialog.exec_()




    def close_dialog(self):
        self.context_dialog.close()

    def style_dialog(self):
        style = """
            QDialog {background-color: #282a36;}
            QLabel {
            font-size: 10pt;
            color: rgb(255, 255, 255);
            }
            QPushButton {
               background-color: rgba(56, 85, 153, 0.7); 
              border: 2px solid #A670E3;
            font-size: 10pt;
            border-radius: 10px;
            color: rgb(255, 255, 255);
            }
            
            QPushButton:hover {
            background-color: rgb(68, 71, 90);
            }
            
            QPushButton:pressed {
            background-color: rgb(85, 170, 255);
            }       
        """
        return {'style': style}