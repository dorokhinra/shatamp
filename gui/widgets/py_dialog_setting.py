import os

from qt_core import *
import configparser

class PyDialogSetting(object):
    def __init__(self):
        self.count_edit = 1
        self.all_dynamic_edit = []
        self.line_edit = QLineEdit()


    def setup_dialog(self, parent):
    #     style = self.set_style()
    #     #Создаем фрейм диалога
        parent.dialog_frame.setMinimumHeight(0)
        parent.dialog_frame.setMinimumWidth(780)
        parent.dialog_frame.resize(780, 0)
    #
        #Показать заголовок таблицы

        reg_ex = QRegExp("[0-9]+")
        input_validator = QRegExpValidator(reg_ex, parent.countEkzemEdit)
        parent.countEkzemEdit.setValidator(input_validator)
        parent.table_printer.horizontalHeader().show()
        parent.journal_mark.horizontalHeader().show()


        # SET ICCONS FOR BTN ADD and DELETE
        #SET PASS FOR ICON
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_add_path = os.path.normpath(os.path.join(path, "icon_add.svg"))
        icon_delete_path = os.path.normpath(os.path.join(path, "icon_delete.svg"))
        icon_up_path = os.path.normpath(os.path.join(path, "icon_up.svg"))

        #ICON ADD BTN
        icon_add_btn = QIcon()
        icon_add_btn.addFile(icon_add_path, QSize(), QIcon.Normal, QIcon.Off)
        parent.add_btn.setIcon(icon_add_btn)

        # ICON DELETE BTN
        icon_delete_btn = QIcon()
        icon_delete_btn.addFile(icon_delete_path, QSize(), QIcon.Normal, QIcon.Off)
        parent.delete_btn.setIcon(icon_delete_btn)

        #SET IMAGE FOR INSTRUCTION
        folder_images = "gui/images/"
        path_images = os.path.join(app_path, folder_images)
        image = os.path.normpath(os.path.join(path_images, "printer.svg"))
        parent.label_4.setPixmap(QPixmap(image))

        #SET ICON UP
        icon_up_btn = QIcon()
        icon_up_btn.addFile(icon_up_path, QSize(), QIcon.Normal, QIcon.Off)
        parent.up_dialog_btn.setIcon(icon_up_btn)

    def add_line_edit(self, parent):
        if len(self.all_dynamic_edit) <= 2:
            add_line_edit = QLineEdit()
            add_line_edit.setObjectName("listReceiveEdit_{0}".format(self.count_edit + 1))
            add_line_edit.setPlaceholderText('Список рассылки')
            parent.layout_for_list_received_edit.addWidget(add_line_edit)
            self.all_dynamic_edit.append(add_line_edit)
            self.count_edit += 1

    def del_line_edit(self, parent):
        if self.count_edit > 1:
            parent.layout_for_list_received_edit.removeWidget(self.all_dynamic_edit[len(self.all_dynamic_edit)-1])
            self.all_dynamic_edit[len(self.all_dynamic_edit) - 1].deleteLater()
            self.all_dynamic_edit[len(self.all_dynamic_edit) - 1] = None
            self.all_dynamic_edit.pop(len(self.all_dynamic_edit)-1)
            self.count_edit -= 1

        # Очищение формы
    def clear_mark_dialog(self, parent, ui):
            for child in parent.findChildren(QLineEdit, QRegExp("listReceiveEdit_(\d)+")):
                if child.objectName() != "listReceiveEdit_1":
                    ui.layout_for_list_received_edit.removeWidget(child)
                    child.deleteLater()
                    child = None
                    self.count_edit = 1
                    self.all_dynamic_edit = []
            for child in parent.findChildren(QLineEdit):
                child.setText('')
            ui.info_mark_label.setText('')


def pars_setting(main_win, ui):
    app_path = os.path.abspath(os.getcwd())
    path_config = os.path.normpath(os.path.join(app_path, "settings.ini"))
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read(path_config, encoding="utf-8")
    marker_param = config['marker_settings']['marker_param']
    subject = config['marker_settings']['subject_name']
    ui.edit_subject.setText(str(subject))
    child = main_win.findChildren(QRadioButton, str(marker_param))
    child[0].setChecked(True)