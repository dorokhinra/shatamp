# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesMjlson.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1170, 785)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"border:none;")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_7 = QFrame(self.page_1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(800, 540))
        self.frame_7.setMaximumSize(QSize(800, 550))
        self.frame_7.setStyleSheet(u"border:none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.dialog_frame = QFrame(self.frame_7)
        self.dialog_frame.setObjectName(u"dialog_frame")
        self.dialog_frame.setGeometry(QRect(10, 10, 780, 540))
        self.dialog_frame.setMinimumSize(QSize(0, 540))
        self.dialog_frame.setMaximumSize(QSize(16777215, 0))
        self.dialog_frame.setStyleSheet(u"#dialog_frame {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"border:3px solid #c3ccdf;\n"
" border-radius: 10px;\n"
"background-color: #282a36\n"
"}\n"
"\n"
"QLineEdit{\n"
"	\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 5px;\n"
"	font-size: 10pt;\n"
"	border:2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.dialog_frame.setFrameShape(QFrame.StyledPanel)
        self.dialog_frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.dialog_frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 761, 521))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(40, 10, 40, 0)
        self.list_receive_frame = QFrame(self.gridLayoutWidget)
        self.list_receive_frame.setObjectName(u"list_receive_frame")
        self.list_receive_frame.setMinimumSize(QSize(0, 250))
        self.list_receive_frame.setMaximumSize(QSize(16777215, 250))
        self.list_receive_frame.setStyleSheet(u"\n"
"QFrame{background-color: rgba(170, 170, 255, 0.2);\n"
"border:none;\n"
"}\n"
"#list_receive_frame{\n"
"  border: 2px solid #A670E3;\n"
"}\n"
"\n"
"#add_btn {\n"
"   background-color: rgba(56, 85, 153, 0.1);\n"
"  color: rgb(255, 255, 255); \n"
"  \n"
"font-size: 10pt;\n"
"border-radius: 22px;\n"
"}\n"
"\n"
"#add_btn:hover {\n"
"background-color: rgba(56, 85, 153, 0.3); \n"
"}\n"
"\n"
"#add_btn:pressed {\n"
"background-color: rgba(56, 85, 153, 0.5); \n"
"border: 2px solid  rgba(0, 118, 0, 0.9);\n"
"}\n"
"\n"
"\n"
"#delete_btn {\n"
"   background-color: rgba(56, 85, 153, 0.1);\n"
"  color: rgb(255, 255, 255); \n"
"  \n"
"font-size: 10pt;\n"
"border-radius: 22px;\n"
"}\n"
"\n"
"#delete_btn:hover {\n"
"background-color: rgba(56, 85, 153, 0.3); \n"
"}\n"
"\n"
"#delete_btn:pressed {\n"
"background-color: rgba(56, 85, 153, 0.5); \n"
"border: 2px solid  rgba(255, 85, 127, 0.7);\n"
"}")
        self.list_receive_frame.setFrameShape(QFrame.StyledPanel)
        self.list_receive_frame.setFrameShadow(QFrame.Raised)
        self.layoutListReceived = QVBoxLayout(self.list_receive_frame)
        self.layoutListReceived.setObjectName(u"layoutListReceived")
        self.frame_11 = QFrame(self.list_receive_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 180))
        self.frame_11.setStyleSheet(u"#frame_11 {background-color: rgba(170, 170, 255, 0.0);\n"
"border:none;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.layout_for_list_received_edit = QVBoxLayout(self.frame_11)
        self.layout_for_list_received_edit.setObjectName(u"layout_for_list_received_edit")
        self.layout_for_list_received_edit.setContentsMargins(-1, 0, -1, 0)
        self.listReceiveEdit_1 = QLineEdit(self.frame_11)
        self.listReceiveEdit_1.setObjectName(u"listReceiveEdit_1")

        self.layout_for_list_received_edit.addWidget(self.listReceiveEdit_1)


        self.layoutListReceived.addWidget(self.frame_11)

        self.frame_for_btn = QFrame(self.list_receive_frame)
        self.frame_for_btn.setObjectName(u"frame_for_btn")
        self.frame_for_btn.setMinimumSize(QSize(0, 50))
        self.frame_for_btn.setStyleSheet(u"#frame_for_btn {background-color: rgba(170, 170, 255, 0.0);\n"
"border:none;\n"
"}")
        self.frame_for_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_for_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_for_btn)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.add_btn = QPushButton(self.frame_for_btn)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(45, 45))
        icon = QIcon()
        icon.addFile(u"../images/icons/icon_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.add_btn)

        self.delete_btn = QPushButton(self.frame_for_btn)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(45, 45))
        icon1 = QIcon()
        icon1.addFile(u"../images/icons/icon_delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.delete_btn)


        self.layoutListReceived.addWidget(self.frame_for_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layoutListReceived.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.list_receive_frame, 1, 0, 1, 2)

        self.nameExecutorEdit = QLineEdit(self.gridLayoutWidget)
        self.nameExecutorEdit.setObjectName(u"nameExecutorEdit")

        self.gridLayout.addWidget(self.nameExecutorEdit, 3, 0, 1, 1)

        self.hardDickNumberEdit = QLineEdit(self.gridLayoutWidget)
        self.hardDickNumberEdit.setObjectName(u"hardDickNumberEdit")

        self.gridLayout.addWidget(self.hardDickNumberEdit, 2, 1, 1, 1)

        self.info_mark_label = QLabel(self.gridLayoutWidget)
        self.info_mark_label.setObjectName(u"info_mark_label")
        self.info_mark_label.setMinimumSize(QSize(0, 20))
        self.info_mark_label.setMaximumSize(QSize(16777215, 20))
        self.info_mark_label.setStyleSheet(u"color: rgba(255, 85, 127, 0.8);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.info_mark_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.info_mark_label, 4, 0, 1, 2)

        self.frame_10 = QFrame(self.gridLayoutWidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 45))
        self.frame_10.setMaximumSize(QSize(16777215, 45))
        self.frame_10.setStyleSheet(u"border:none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.confirm_mark_parabeters_btn = QPushButton(self.frame_10)
        self.confirm_mark_parabeters_btn.setObjectName(u"confirm_mark_parabeters_btn")
        self.confirm_mark_parabeters_btn.setMinimumSize(QSize(200, 40))
        self.confirm_mark_parabeters_btn.setStyleSheet(u"QPushButton{\n"
"   background-color: rgba(56, 85, 153, 0.7); \n"
"  color: rgb(255, 255, 255); \n"
"  border: 2px solid #A670E3;\n"
"font-size: 10pt;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(68, 71, 90);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.confirm_mark_parabeters_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.frame_10, 5, 0, 1, 2)

        self.executorTelephoneNumberEdit = QLineEdit(self.gridLayoutWidget)
        self.executorTelephoneNumberEdit.setObjectName(u"executorTelephoneNumberEdit")

        self.gridLayout.addWidget(self.executorTelephoneNumberEdit, 2, 0, 1, 1)

        self.fioPrintAdminEdit = QLineEdit(self.gridLayoutWidget)
        self.fioPrintAdminEdit.setObjectName(u"fioPrintAdminEdit")

        self.gridLayout.addWidget(self.fioPrintAdminEdit, 3, 1, 1, 1)

        self.countEkzemEdit = QLineEdit(self.gridLayoutWidget)
        self.countEkzemEdit.setObjectName(u"countEkzemEdit")

        self.gridLayout.addWidget(self.countEkzemEdit, 0, 1, 1, 1)

        self.numberPuEdit = QLineEdit(self.gridLayoutWidget)
        self.numberPuEdit.setObjectName(u"numberPuEdit")

        self.gridLayout.addWidget(self.numberPuEdit, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.gridLayoutWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 20))
        self.frame_9.setStyleSheet(u"QFrame {\n"
"border:none;\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.up_dialog_btn = QPushButton(self.frame_9)
        self.up_dialog_btn.setObjectName(u"up_dialog_btn")
        self.up_dialog_btn.setMinimumSize(QSize(100, 20))
        self.up_dialog_btn.setMaximumSize(QSize(16777215, 20))
        self.up_dialog_btn.setStyleSheet(u"QPushButton{\n"
"   \n"
"	\n"
"	background-color: rgba(91, 91, 91, 0.1);\n"
"  color: rgb(255, 255, 255); \n"
"  border: 2px solid #A670E3;\n"
"font-size: 10pt;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(68, 71, 90);\n"
"height:40px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.up_dialog_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.gridLayout.addWidget(self.frame_9, 6, 0, 1, 2)

        self.table_printer = QTableWidget(self.frame_7)
        if (self.table_printer.columnCount() < 3):
            self.table_printer.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_printer.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_printer.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_printer.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table_printer.rowCount() < 1):
            self.table_printer.setRowCount(1)
        font = QFont()
        font.setPointSize(10)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.table_printer.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.table_printer.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_printer.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_printer.setItem(0, 2, __qtablewidgetitem6)
        self.table_printer.setObjectName(u"table_printer")
        self.table_printer.setGeometry(QRect(10, 10, 781, 540))
        self.table_printer.setMinimumSize(QSize(0, 540))
        self.table_printer.setMaximumSize(QSize(16777215, 550))
        self.table_printer.setStyleSheet(u"QTableWidget {\n"
"	border:3px solid #c3ccdf;\n"
"	border-radius: 10px;\n"
"	background-color: rgba(0, 85, 255, 0.0);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   border-bottom: 1px solid rgb(76, 25, 76);\n"
"  background-color: rgba(170, 170, 255, 0.2);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Arial\";\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget::item:selected {\n"
"   \n"
"	background-color: rgba(0, 85, 255, 0.3);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    background-color: #44475a;\n"
"height: 40px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:10pt;\n"
"\n"
"}")
        self.table_printer.setProperty("showDropIndicator", True)
        self.table_printer.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_printer.setShowGrid(False)
        self.table_printer.horizontalHeader().setVisible(False)
        self.table_printer.horizontalHeader().setCascadingSectionResizes(False)
        self.table_printer.horizontalHeader().setMinimumSectionSize(100)
        self.table_printer.horizontalHeader().setDefaultSectionSize(150)
        self.table_printer.horizontalHeader().setHighlightSections(False)
        self.table_printer.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_printer.horizontalHeader().setStretchLastSection(True)
        self.table_printer.verticalHeader().setVisible(False)
        self.table_printer.verticalHeader().setCascadingSectionResizes(True)
        self.table_printer.verticalHeader().setMinimumSectionSize(40)
        self.table_printer.verticalHeader().setDefaultSectionSize(40)
        self.table_printer.verticalHeader().setHighlightSections(False)
        self.table_printer.verticalHeader().setProperty("showSortIndicator", False)
        self.table_printer.verticalHeader().setStretchLastSection(False)
        self.table_printer.raise_()
        self.dialog_frame.raise_()

        self.horizontalLayout_5.addWidget(self.frame_7)


        self.horizontalLayout.addLayout(self.horizontalLayout_5)

        application_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_8 = QFrame(self.page_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(800, 550))
        self.frame_8.setMaximumSize(QSize(800, 550))
        self.frame_8.setStyleSheet(u"border:none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.filter_panel_frame = QFrame(self.frame_8)
        self.filter_panel_frame.setObjectName(u"filter_panel_frame")
        self.filter_panel_frame.setStyleSheet(u"#filter_panel_frame{\n"
"border:none;\n"
"}\n"
"QLineEdit{\n"
"	\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 5px;\n"
"	font-size: 10pt;\n"
"	border:2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"   background-color: rgba(56, 85, 153, 0.7); \n"
"  color: rgb(255, 255, 255); \n"
"  border: 2px solid #A670E3;\n"
"font-size: 10pt;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(68, 71, 90);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"border-radius: 5px; \n"
"background-color:   rgb(87, 96, 134);\n"
"color:                      rgb(255, 255, 255);\n"
"padding:                    5px \n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"   \n"
"    background-color:   rgb(87, 96, 134);\n"
"    color:                      rgb(255, 255, 255);\n"
"    padding:                    7px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    padding-right:          5p"
                        "x;\n"
"}\n"
"\n"
"QListView{\n"
"   \n"
"    color:                      rgb(87, 96, 134);\n"
"    height: 35px;\n"
"	background-color: rgb(0, 170, 255);\n"
"    font-weight:            bold;\n"
"    selection-background-color: rgb(47, 175, 178);\n"
"    show-decoration-selected: 1;\n"
"    margin-left:                -10px;\n"
"    padding-left    :           15px;\n"
"}\n"
"\n"
"\n"
"QListView::item:hover{\n"
"\n"
"    \n"
"	background-color: rgb(221, 119, 255);\n"
"   \n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    border: none;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    \n"
"	background-color: rgb(208, 88, 255);\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.filter_panel_frame.setFrameShape(QFrame.StyledPanel)
        self.filter_panel_frame.setFrameShadow(QFrame.Raised)
        self.filter_panel_layout = QHBoxLayout(self.filter_panel_frame)
        self.filter_panel_layout.setObjectName(u"filter_panel_layout")
        self.filter_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.select_year_drop_down = QComboBox(self.filter_panel_frame)
        self.select_year_drop_down.setObjectName(u"select_year_drop_down")
        self.select_year_drop_down.setMinimumSize(QSize(100, 35))

        self.filter_panel_layout.addWidget(self.select_year_drop_down)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filter_panel_layout.addItem(self.horizontalSpacer_6)

        self.searchEdit = QLineEdit(self.filter_panel_frame)
        self.searchEdit.setObjectName(u"searchEdit")

        self.filter_panel_layout.addWidget(self.searchEdit)


        self.verticalLayout_2.addWidget(self.filter_panel_frame)

        self.journal_mark = QTableView(self.frame_8)
        self.journal_mark.setObjectName(u"journal_mark")
        self.journal_mark.setStyleSheet(u"QTableView{\n"
"	border:3px solid #c3ccdf;\n"
"	border-radius: 10px;\n"
"	background-color: rgba(0, 85, 255, 0.0);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"   border-bottom: 1px solid rgb(76, 25, 76);\n"
"  background-color: rgba(170, 170, 255, 0.2);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Arial\";\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView::item:selected {\n"
"  \n"
"	background-color: rgba(0, 85, 255, 0.3);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    background-color: #44475a;\n"
"height: 40px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:10pt;\n"
"\n"
"}")
        self.journal_mark.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.journal_mark.setProperty("showDropIndicator", False)
        self.journal_mark.setAlternatingRowColors(False)
        self.journal_mark.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.journal_mark.setShowGrid(False)
        self.journal_mark.horizontalHeader().setDefaultSectionSize(38)
        self.journal_mark.horizontalHeader().setStretchLastSection(True)
        self.journal_mark.verticalHeader().setVisible(False)
        self.journal_mark.verticalHeader().setCascadingSectionResizes(True)
        self.journal_mark.verticalHeader().setDefaultSectionSize(21)

        self.verticalLayout_2.addWidget(self.journal_mark)


        self.horizontalLayout_2.addWidget(self.frame_8)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(700, 500))
        self.frame.setStyleSheet(u"#frame {\n"
"	border:3px solid #c3ccdf;\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.edit_subject = QLineEdit(self.frame)
        self.edit_subject.setObjectName(u"edit_subject")
        self.edit_subject.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 9px;\n"
"	font-size: 10pt;\n"
"	border:2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.edit_subject)

        self.fonaric_for_all_pages = QRadioButton(self.frame)
        self.fonaric_for_all_pages.setObjectName(u"fonaric_for_all_pages")
        self.fonaric_for_all_pages.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 10pt;\n"
"}")
        self.fonaric_for_all_pages.setChecked(True)

        self.verticalLayout.addWidget(self.fonaric_for_all_pages)

        self.fonaric_without_last_page = QRadioButton(self.frame)
        self.fonaric_without_last_page.setObjectName(u"fonaric_without_last_page")
        self.fonaric_without_last_page.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 10pt;\n"
"}")

        self.verticalLayout.addWidget(self.fonaric_without_last_page)

        self.fonaric_only_last_page = QRadioButton(self.frame)
        self.fonaric_only_last_page.setObjectName(u"fonaric_only_last_page")
        self.fonaric_only_last_page.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 10pt;\n"
"}")

        self.verticalLayout.addWidget(self.fonaric_only_last_page)

        self.without_fonaric = QRadioButton(self.frame)
        self.without_fonaric.setObjectName(u"without_fonaric")
        self.without_fonaric.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 10pt;\n"
"}")

        self.verticalLayout.addWidget(self.without_fonaric)

        self.label_info = QLabel(self.frame)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setMaximumSize(QSize(16777215, 20))
        self.label_info.setStyleSheet(u"QLabel {color: rgb(255, 255, 255);\n"
"	font-size: 10pt;}")
        self.label_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_info)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setStyleSheet(u"QFrame{border:none;}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 0, 661, 80))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 50))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"   background-color: rgba(56, 85, 153, 0.7); \n"
"  color: rgb(255, 255, 255); \n"
"  border: 2px solid #A670E3;\n"
"font-size: 10pt;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(68, 71, 90);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.frame)

        application_pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"border:none;")
        self.horizontalLayout_4 = QHBoxLayout(self.page_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(800, 550))
        self.frame_3.setStyleSheet(u"border:none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 781, 531))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(800, 550))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border-top: 4px solid #c3ccdf;\n"
"	border-bottom: 4px solid #c3ccdf;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"    height: 40px;\n"
"    width: 170;\n"
"margin-left: 2px;\n"
"	background-color: rgba(56, 85, 153, 0.7); \n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	font-size: 10pt;\n"
"	color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:hover \n"
"{\n"
"background-color: rgba(56, 85, 153, 0.4); \n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"     border: 2px solid #926DD9\n"
"\n"
"}")
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setStyleSheet(u"#main_tab {\n"
"	border: none\n"
"}\n"
"\n"
"")
        self.frame_4 = QFrame(self.main_tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 30, 761, 300))
        self.frame_4.setMaximumSize(QSize(16777215, 300))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, -1, 761, 324))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 80))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame_6 = QFrame(self.verticalLayoutWidget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 240))
        self.frame_6.setMaximumSize(QSize(16777215, 300))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_3 = QWidget(self.frame_6)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(-1, 0, 761, 252))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(250, 250))
        self.label_4.setMaximumSize(QSize(16777215, 250))
        self.label_4.setPixmap(QPixmap(u"../images/printer.svg"))

        self.horizontalLayout_14.addWidget(self.label_4)

        self.textBrowser = QTextBrowser(self.horizontalLayoutWidget_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0.0);\n"
"border: none;")

        self.horizontalLayout_14.addWidget(self.textBrowser)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.tabWidget.addTab(self.main_tab, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"#tab_1 {\n"
"	border: none\n"
"}")
        self.verticalLayoutWidget_4 = QWidget(self.tab_1)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 10, 741, 441))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.verticalLayoutWidget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_5 = QWidget(self.frame_5)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(-1, -1, 741, 441))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.label_5 = QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 80))
        self.label_5.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.textBrowser_2 = QTextBrowser(self.verticalLayoutWidget_5)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setStyleSheet(u"background-color: rgba(85, 85, 255, 0.0);\n"
"border: none;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.textBrowser_2)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab_1, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout_11.addWidget(self.frame_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_11)

        application_pages.addWidget(self.page_4)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.listReceiveEdit_1.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438", None))
        self.add_btn.setText("")
        self.delete_btn.setText("")
        self.nameExecutorEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u0424\u0418\u041e \u0438\u0441\u043f\u043e\u043b\u043d\u0442\u0435\u043b\u044f", None))
        self.hardDickNumberEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u041d\u043e\u043c\u0435\u0440 \u0436\u0435\u0441\u0442\u043a\u043e\u0433\u043e \u0434\u0438\u0441\u043a\u0430", None))
        self.info_mark_label.setText("")
        self.confirm_mark_parabeters_btn.setText(QCoreApplication.translate("application_pages", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.executorTelephoneNumberEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f", None))
        self.fioPrintAdminEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u0424\u0418\u041e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430 \u043f\u0435\u0447\u0430\u0442\u0438", None))
        self.countEkzemEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043a\u0437\u0435\u043c\u043f\u043b\u044f\u0440\u043e\u0432", None))
        self.numberPuEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u041d\u043e\u043c\u0435\u0440 \u041f\u0423", None))
        self.up_dialog_btn.setText("")
        ___qtablewidgetitem = self.table_printer.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("application_pages", u"ID", None));
        ___qtablewidgetitem1 = self.table_printer.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("application_pages", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem2 = self.table_printer.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("application_pages", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u043c\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem3 = self.table_printer.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("application_pages", u"1", None));

        __sortingEnabled = self.table_printer.isSortingEnabled()
        self.table_printer.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.table_printer.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("application_pages", u"\u043e\u0447\u0435\u0440\u0435\u0434\u044c \u043f\u0443\u0441\u0442\u0430", None));
        self.table_printer.setSortingEnabled(__sortingEnabled)

        self.searchEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0436\u0443\u0440\u043d\u0430\u043b\u0443", None))
        self.edit_subject.setPlaceholderText(QCoreApplication.translate("application_pages", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438", None))
        self.fonaric_for_all_pages.setText(QCoreApplication.translate("application_pages", u"\u041c\u0430\u0440\u043a\u0435\u0440 \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446", None))
        self.fonaric_without_last_page.setText(QCoreApplication.translate("application_pages", u"\u041c\u0430\u0440\u043a\u0435\u0440 \u0431\u0435\u0437 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043b\u0438\u0441\u0442\u0430", None))
        self.fonaric_only_last_page.setText(QCoreApplication.translate("application_pages", u"\u041c\u0430\u0440\u043a\u0435\u0440 \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043b\u0438\u0441\u0442\u0430", None))
        self.without_fonaric.setText(QCoreApplication.translate("application_pages", u"\u0411\u0435\u0437 \u043c\u0430\u0440\u043a\u0435\u0440\u0430", None))
        self.label_info.setText("")
        self.pushButton.setText(QCoreApplication.translate("application_pages", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0435\u0447\u0430\u0442\u0438 \u0438 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label_4.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("application_pages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:14pt;\">	\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f \u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0443\u0447\u0435\u0442\u0430 \u0438 \u043f\u0435\u0447\u0430\u0442\u0438 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430"
                        "\u043c\u0438 \u0440\u0435\u0436\u0438\u043c\u043d\u043e \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u043e\u0433\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:14pt;\">	\u0412 \u0441\u043e\u0441\u0442\u0430\u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0432\u0445\u043e\u0434\u044f\u0442 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u043c \u043f\u0435\u0447\u0430\u0442\u0438, \u0436\u0443\u0440\u043d\u0430\u043b \u0443\u0447\u0435\u0442\u0430 \u043f\u0435\u0447\u0430\u0442\u0438 \u0438 \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438 \u043e\u0442\u043f\u0435\u0447\u0430\u0442\u0430\u043d\u043d\u044b\u0445 \u0434\u043e\u043a\u0443\u043c\u0435"
                        "\u043d\u0442\u043e\u0432.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("application_pages", u"\u041e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("application_pages", u"\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u043f\u0435\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("application_pages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt;\">	1. \u041f\u0435\u0440\u0435\u0439\u0434\u0438\u0442\u0435 \u043d\u0430 \u0432\u043a\u043b\u0430\u0434\u043a\u0443 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt;\">	2. \u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u0432\u043e\u0451 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt;\">	3. \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u043a\u0438 (\u043e\u0434\u0438\u043d \u0438\u0437 \u043f\u0443\u043d\u043a\u0442\u043e\u0432)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt;\">	4. \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("application_pages", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u0440\u0433\u0440\u0430\u043c\u043c\u044b", None))
    # retranslateUi

