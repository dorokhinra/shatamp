import datetime

from PyQt5 import QtSql

from qt_core import *


class PyTableView(object):
    def __init__(self, parent, ui, session):
        self.parent = parent
        self.ui = ui
        self.session = session
        self.set_date_in_table()
        self.create_table_view_data()

    def set_date_in_table(self):
        self.model = QtSql.QSqlTableModel(self.parent, self.session)
        self.model.setTable('mark_journal')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ПУ")
        self.model.setHeaderData(1, Qt.Horizontal, "Пользователь")
        self.model.setHeaderData(2, Qt.Horizontal, "Исполнитель")
        self.model.setHeaderData(3, Qt.Horizontal, "Название документа")
        self.model.setHeaderData(4, Qt.Horizontal, "Дата")
        self.model.setHeaderData(5, Qt.Horizontal, "Уровень")
        self.model.setFilter("date_print LIKE '%{}%'".format(datetime.date.today().year))
        self.model.select()

    def set_filter(self, column, filter):
        date_filter = "{} LIKE '%{}%'".format(column, filter)
        self.model.setFilter(date_filter)
        self.model.select()

    def set_filter_edit(self, filter, ui):
        year = ui.select_year_drop_down.currentText()
        date_filter = "date_print LIKE '%{}%' and (number_pu LIKE '%{}%' OR user_name LIKE '%{}%' OR fio_executor LIKE '%{}%' OR doc_name LIKE '%{}%' OR mac_level LIKE '%{}%')".format(year,
                                                                                                                                                                                        filter,
                                                                                                                                                                                        filter,
                                                                                                                                                                                        filter,
                                                                                                                                                                                        filter,
                                                                                                                                                                                        filter)
        self.model.setFilter(date_filter)
        self.model.select()

    def create_table_view_data(self):
        self.ui.journal_mark.setModel(self.model)
        self.ui.journal_mark.verticalHeader().setDefaultSectionSize(35)
        self.ui.journal_mark.horizontalHeader().setStretchLastSection(True)
        self.ui.journal_mark.setColumnWidth(0, 60)
        self.ui.journal_mark.setColumnWidth(1, 110)
        self.ui.journal_mark.setColumnWidth(2, 200)
        self.ui.journal_mark.setColumnWidth(3, 200)
        self.ui.journal_mark.setColumnWidth(4, 100)
        self.ui.journal_mark.setColumnWidth(5, 100)




