import os
from qt_core import *
import configparser

def ini_settings(parent, main_win):
    #Определяем дирректорию
    app_path = os.path.abspath(os.getcwd())
    path = os.path.normpath(os.path.join(app_path, "settings.ini"))

    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read(path)  # читаем конфиг
    if parent.edit_subject.text() != '':
        config.set("marker_settings", "subject_name", str(parent.edit_subject.text()))

        for child in main_win.findChildren(QRadioButton):
            if child.isChecked():
                config.set("marker_settings", "marker_param", child.objectName())


        with open(path, "w") as config_file:
            config.write(config_file)
        parent.label_info.setText('Настройки применены успешно!')
    else:
        parent.label_info.setText('Заполните все значения!')