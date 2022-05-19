#IMPORT QT_CORE
from qt_core import *
from gui.pages.ui_pages import Ui_application_pages
from gui.widgets.py_push_button import PyPushButton
from gui.widgets.py_dialog_setting import PyDialogSetting
# from gui.widgets.py_context_menu import ContextMenuOn

class UI_MainWindow(object):

    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        #УСТАНОВИТЬ МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ
        parent.resize(1100, 700)
        parent.setMinimumSize(1060, 640)

        #Создаем центральный widget
        self.central_frame = QFrame()

        #УСТАНОВИТЬ ЦЕНТРАЛЬНУЮ СЕТКУ
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        #LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        #LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # TOP_FRAME_MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red }")

        #TOP_FRAME_LAYOUT
        self.left_menu_top_frame_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_frame_layout.setSpacing(0)


        #TOP BTNS
        self.toggle_button = PyPushButton(text="Меню", icon_path="icon_menu.svg")
        self.btn_1 = PyPushButton(text="Очередь печати", icon_path="main_icon.svg", is_active=True)
        self.btn_2 = PyPushButton(text="Журнал маркировки", icon_path="icon_jurnal.svg" )

        #ADD BTN TOP FRAME
        self.left_menu_top_frame_layout.addWidget(self.toggle_button)
        self.left_menu_top_frame_layout.addWidget(self.btn_1)
        self.left_menu_top_frame_layout.addWidget(self.btn_2)

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #BOTTOM_FRAME_MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red }")

        # BOTTOM_FRAME_LAYOUT
        self.left_menu_bottom_frame_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_frame_layout.setSpacing(0)

        #BOTTOM BTN

        self.settings_btn = PyPushButton(text="Настройки", icon_path="icon_settings.svg")
        self.about_btn = PyPushButton(text="О программе", icon_path="icon_info.svg")

        #ADD BOTTON LAYOUT BTN
        self.left_menu_bottom_frame_layout.addWidget(self.settings_btn)
        self.left_menu_bottom_frame_layout.addWidget(self.about_btn)

        #LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setStyleSheet("font-size: 9pt; color: #DCDCDC")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setMinimumHeight(30)

        #ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        #Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        #CONTENT LAYOUT
        self.content_loyout = QVBoxLayout(self.content)
        self.content_loyout.setContentsMargins(0, 0, 0, 0)
        self.content_loyout.setSpacing(0)


        # TOP BAR
        # self.top_bar = QFrame()
        # self.top_bar.setMinimumHeight(30)
        # self.top_bar.setMaximumHeight(30)
        # self.top_bar.setStyleSheet("background-color: #21232d; color: #627a4")

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #627a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)


        #RIGHT_LABEL
        self.bottom_right_label = QLabel("@ 2022")
        self.bottom_right_label.setStyleSheet("font-size: 10pt; color: #483D8B")

        # BOTTOM_LEFT_LABEL
        self.bottom_left_label = QLabel("dorokhinra")
        self.bottom_left_label.setStyleSheet("font-size: 10pt; color: #483D8B")

        #BOTTOM SPACER
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #Add bottom bar layout
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_right_label)

        #Application Pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.dialog_setting = PyDialogSetting()
        self.dialog_setting.setup_dialog(self.ui_pages)



        #УСтановка страницы для каждой кнопки
        # self.pages.setCurrentWidget(self.ui_pages.page_2)

        #ADD WIDGETS IN APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        #ADD content layout
        # self.content_loyout.addWidget(self.top_bar)
        self.content_loyout.addWidget(self.pages)
        self.content_loyout.addWidget(self.bottom_bar)



        #SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)