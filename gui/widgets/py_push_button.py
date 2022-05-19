import os

from qt_core import *

class PyPushButton(QPushButton):
    def __init__(self,
                 text="",
                 height = 40,
                 minimum_width = 50,
                 text_padding = 55,
                 text_color = "#c3ccdf",
                 icon_path = "",
                 icon_color = "#44475a",
                 btn_color = "#44475a",
                 btn_hover = "#4f5368",
                 btn_pressed = "#282a36",
                 is_active = False
                 ):
        super().__init__()

        # Set defaults parametr
        self.setText(text)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        #COSTOM PARAMETRS
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self. text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        #Set style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu)

    def set_style(self,
                  text_padding= 55,
                  text_color = "#c3ccdf",
                  btn_color = "#44475a",
                  btn_hover = "#4f5368",
                  btn_pressed = "#282a36",
                  is_active = False
                  ):
        style = """
        QPushButton {{ 
        color: {};
        background-color: {};
        padding-left: {}px;
        text-align: left;
        border: none;
        font-size: 10pt;
        }}
        QPushButton:hover {{
        background-color: {};
        }}
        QPushButton:pressed {{
        background-color: {};
        }}
        """.format(text_color, btn_color, text_padding, btn_hover, btn_pressed)

        active_style = """
        QPushButton {{ 
        background-color: {};
        border-right: 6px solid #282a36;
        }}
        """.format(btn_hover)
        self.setStyleSheet(style) if not is_active else self.setStyleSheet(style + active_style)

    def paintEvent(self, event):
        #Return Default style
        QPushButton.paintEvent(self, event)
        # Pinter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        rect = QRect(0,0, self.minimum_width, self.height())
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)
        qp.end()

    def draw_icon(self, qp, image, rect, color):
        #format_path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))
        #Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        # painter.fillRect(icon.rect(), color)
        qp.drawPixmap((rect.width() - icon.width()) / 2,
                      (rect.height() - icon.height()) / 2,
                        icon)
        painter.end()
