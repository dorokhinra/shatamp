#IMPORT MUDULES
import os
import glob
import sys
import time
#IMPORT QTQORE
from qt_core import *

#Разные потоки для проверки очереди печати
import threading

#Import Main_mindow
from gui.windows.ui_main_window import UI_MainWindow

#Import py_context_menu
from gui.widgets.py_context_menu import ContextMenuOn

#import SYSTEM FUNCTIONS
from app_system_functions.mark_job import print_job

#PyDialog
from gui.widgets.py_dialog_setting import PyDialogSetting, pars_setting

#SETTINGS_INI
from app_system_functions.ini_settings import ini_settings

#Проверка очереди печати
from app_system_functions.check_print_job import CheckPrintJob

#Диалог
from gui.widgets.py_modal_dialog import UiDialog

#Соединение с БД
from db.session import DbSession

#Создание таблицы в БД
from gui.widgets.py_table_view import PyTableView

#Добавление данных в комбобокс
from gui.widgets.py_dropdown import PyDropDown

#MAIN_WINDOW
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        #SETUP MAIN WINDOW
        self.app = app
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.context_menu = ContextMenuOn(self.show_dialog_mark, self.del_widget)
        self.add_dinamic_edit = PyDialogSetting()
        self.check_print_job = CheckPrintJob(self.ui.ui_pages)

        #Базка
        self.db = DbSession()
        #Создание таблицы
        self.db.create_table(self.db.session)

        self.view = PyTableView(self, self.ui.ui_pages, self.db.session)
        PyDropDown(self, self.ui.ui_pages, self.db.session)

        #Проверка настроек#
        pars_setting(self, self.ui.ui_pages)

        #Стартуем проверку очереди печати
        self.logic = True
        self.thread = threading.Thread(target=self.start_thread)
        self.thread.start()

        #Добваляем название и иконку
        self.setWindowTitle("Менеджер маркировки и печати документов")
        self.setWindowIcon(QIcon('gui/images/stamp.png'))

        #Применить настройки
        self.ui.ui_pages.pushButton.clicked.connect(lambda: ini_settings(self.ui.ui_pages, self))

        #Убрать диалоговое окно
        self.ui.ui_pages.up_dialog_btn.clicked.connect(self.close_dialog)

        # self.ui.ui_pages.fonaric_for_all_pages.isChecked()


        # Показать выпадающее меню при клике мыши
        self.ui.ui_pages.table_printer.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.ui_pages.table_printer.customContextMenuRequested.connect(self.context_menu.on_custom_context_menu)

        #Добавление дополнительного элемента в список рассылки
        self.ui.ui_pages.add_btn.clicked.connect(lambda: self.add_dinamic_edit.add_line_edit(self.ui.ui_pages))

        #Удаление доболнительного элемента
        self.ui.ui_pages.delete_btn.clicked.connect(lambda: self.add_dinamic_edit.del_line_edit(self.ui.ui_pages))
        # self.ui.ui_pages.layout_for_list_received_edit.findChildren("")

        #Печать документа
        self.ui.ui_pages.confirm_mark_parabeters_btn.clicked.connect(self.print_job_document)

        #По умолчанию показывается певая страница
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)

        #Кнопка Для анимации меню
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        #BTN printer
        self.ui.btn_1.clicked.connect(self.show_page_printer)

        #BTN journal
        self.ui.btn_2.clicked.connect(self.show_page_journal)

        #BTN settings
        self.ui.settings_btn.clicked.connect(self.show_page_settings)

        #BTN about
        self.ui.about_btn.clicked.connect(self.show_page_about)

        #COMBOBOX CHAHNGE
        self.ui.ui_pages.select_year_drop_down.currentTextChanged.connect(self.select_year)

        #SEARCH EDIT
        self.ui.ui_pages.searchEdit.textChanged.connect(self.edit_filter)

        #Окно по центру
        desc = QApplication.desktop()
        self.move(desc.availableGeometry().center() - self.rect().center())

        self.show()

    def edit_filter(self, a):
        self.view.set_filter_edit(a, self.ui.ui_pages)


    def select_year(self, s):
        self.view.set_filter('date_print', s)

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_printer(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_page_journal(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_page_settings(self):
        self.reset_selection()
        pars_setting(self, self.ui.ui_pages)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

    def show_page_about(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
        self.ui.about_btn.set_active(True)

    def toggle_button(self):
        #GET MENU WIDTH
        menu_width = self.ui.left_menu.width()

        width = 50
        #CHECK MENU WIDTH
        if menu_width == 50:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()

        #start dialog mark animation
    def show_dialog_mark(self):
            # GET MENU WIDTH
            start_height = self.ui.ui_pages.dialog_frame.height()
            height = 540
            # CHECK MENU WIDTH
            if start_height == 540:
                hHeight = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 540]
                height = 0

                # self.ui.ui_pages.dialog_frame.resize(780, height)
                for i in reversed(hHeight):
                    self.ui.ui_pages.dialog_frame.setMinimumHeight(i)
                    self.ui.ui_pages.dialog_frame.resize(780, i)
                    self.app.processEvents()
                    time.sleep(.02)
            # Start animation
            else:

                self.animation = QPropertyAnimation(self.ui.ui_pages.dialog_frame, b"minimumHeight")
                self.animation.setStartValue(start_height)
                self.animation.setEndValue(height)
                self.animation.setDuration(300)
                self.animation.setEasingCurve(QEasingCurve.InSine)
                self.animation.start()

    def close_dialog(self):
        self.add_dinamic_edit.clear_mark_dialog(self, self.ui.ui_pages)
        self.show_dialog_mark()

    def print_job_document(self):
        print_job(self, self.ui.ui_pages, self.context_menu.row_index, self.db.session)
        self.view.model.select()
        if self.ui.ui_pages.countEkzemEdit.text() != '':
            if len(self.findChildren(QLineEdit, QRegExp("listReceiveEdit_(\d)+"))) == int(self.ui.ui_pages.countEkzemEdit.text()):
                self.add_dinamic_edit.clear_mark_dialog(self, self.ui.ui_pages)
                self.show_dialog_mark()

    def start_thread(self):
        while self.logic:
            self.check_print_job.parse_file()
            time.sleep(1)

    #удалить виджет и элемент из очереди печати
    @staticmethod
    def del_widget(wid, index):
        del_widget = wid.item(index.row(), 0).text()
        os.system('lprm ' + del_widget)
        UiDialog('удаление документа', 'Задание удалено!')


    #Диалог закрытия приложения
    def closeEvent(self, event):
        # Переопределить colseEvent
        reply = QMessageBox.question \
            (self, 'Выход из приложения',
             "Вы уверены, что хотите уйти?",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            rm_temp_files()
            event.accept()
            self.logic = False
        else:
            event.ignore()

#Очистить дирректорию temp
def rm_temp_files():
    app_path = os.path.abspath(os.getcwd())
    temp_path = os.path.join(app_path, 'temp')
    temp_path = os.path.join(temp_path, '*')
    files = glob.glob(temp_path)

    for f in files:
        os.remove(f)

if __name__ == "__main__":
    rm_temp_files()
    app = QApplication(sys.argv)
    window = MainWindow(app)
    app.exec_()