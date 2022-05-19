import os
from qt_core import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from db.models.mark_journal import create_tables


class DbSession(object):

    def __init__(self):
        app_path = os.path.abspath(os.getcwd())
        folder = "db/sqlite"
        path = os.path.join(app_path, folder)
        self.db_path = os.path.normpath(os.path.join(path, "mark_journal.sqlite"))
        self.session = self.session_query()


    def session_query(self):
        session = QSqlDatabase.addDatabase("QSQLITE")
        session.setDatabaseName(self.db_path)
        db = QSqlDatabase.database(open=True)
        return db

    def create_table(self, session):
        self.query = QSqlQuery(session)
        query_string = create_tables()
        self.query.prepare(query_string)
        self.query.exec_()






