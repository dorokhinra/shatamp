from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
import  datetime
from db.query.query_service import sql_prepare
from qt_core import *


class PyDropDown(object):
    def __init__(self, parent, ui, session):
        self.parent = parent
        self.ui = ui
        self.session = session
        self.list_year = []
        self.find_year()

    def find_year(self):
        query = sql_prepare()['select_year']
        insertDataQuery = QSqlQuery(query)
        while insertDataQuery.next():
            date_obj = datetime.datetime.strptime(insertDataQuery.value(0), '%d.%m.%Y')
            year = date_obj.year
            self.list_year.append(int(year))
        self.list_year = list(set(self.list_year))
        for i in sorted(self.list_year):
            self.ui.select_year_drop_down.addItem(str(i))








