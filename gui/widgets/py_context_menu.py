from qt_core import *
from PyQt5 import QtCore, QtWidgets

class ContextMenuOn(QtWidgets.QMenu):

    def __init__(self, show_dialog_func, del_widget):
        super().__init__()
        self.show_dialog_mark = show_dialog_func
        self.del_widget = del_widget
        self.row_index = ''



    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_custom_context_menu(self, pos):

        if self.sender().currentIndex().row() == -1:
            return
        widget = self.sender()
        if isinstance(widget, QtWidgets.QAbstractItemView):
            widget = widget.viewport()
        menu = QtWidgets.QMenu()
        # menu.setSeparatorsCollapsible(True)

        #Определяем заголовки
        # menu.addSeparator()
        # menu.addSection('Меню печати')
        mark_item = QAction("Маркировать документ", menu)
        delete_item = QAction("Удалить улемент из очереди", menu)


        #Добавляем заголовки в меню
        menu.addAction(mark_item)
        menu.addAction(delete_item)

        #STYLE
        style = self.menu_style()

        menu.setStyleSheet(style)

        index = self.sender().currentIndex()

        #Отлов Наша таблица
        wid = self.sender()
        # menu_del.triggered.connect(self.DelWidget)
        self.row_index = index.row()

        #передача

        #ДОБАВЛЕНИЕ ДЕЙСТВИЙ ФУНКЦИЙ НА КАЖДЫЙ ЭЛЕМЕНТ
        mark_item.triggered.connect(lambda: self.show_dialog_mark())

        #УЛАЛЕНИЕ ЭЛЕМЕНТА ИЗ ТАБЛИЦЫ
        delete_item.triggered.connect(lambda: self.del_widget(wid, index))


        menu.exec_(widget.mapToGlobal(pos))

    # def show_dialog_mark(self):
    #     # GET MENU WIDTH
    #     start_height = self.ui.ui_pages.dialog_frame.height()
    #     height = 540
    #     # Start animation
    #     self.animation = QPropertyAnimation(self.ui.ui_pages.dialog_frame, b"minimumHeight")
    #     self.animation.setStartValue(start_height)
    #     self.animation.setEndValue(height)
    #     self.animation.setDuration(300)
    #     self.animation.setEasingCurve(QEasingCurve.InSine)
    #     self.animation.start()





    def menu_style(self):
        style = """
            QMenu {
            background-color: #21232d;
            font-size: 10pt;
            padding: 10px;
            border: 1px solid rgba(198,0,124, 0.7);
            border-radius: 6px;
            }
            QMenu::item {
         
           color: rgb(255, 255, 255);
           }
            QMenu::item:selected {
           background-color: rgba(198,0,124, 0.2);
           color: rgb(255, 255, 255);
           }
        """
        return style