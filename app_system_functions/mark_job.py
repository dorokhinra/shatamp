import datetime
import os

from PyQt5.QtSql import QSqlQuery

from qt_core import *

import configparser
from gui.widgets.py_modal_dialog import UiDialog
from app_system_functions.pdf_parser_for_mark import CreateMarker
from db.session import DbSession
from db.query.query_service import sql_prepare


def print_job(main_win, parent, row_index, session):
    #Путь до маркера
    path = '/etc/cups/marker.template'

    #Файл настроек
    app_path = os.path.abspath(os.getcwd())
    path_config = os.path.normpath(os.path.join(app_path, "settings.ini"))
    config = configparser.ConfigParser()  # создаём объект парсера
    config.read(path_config, encoding="utf-8")
    subject = config['marker_settings']['subject_name']
    marker_param = config['marker_settings']['marker_param']
    data_for_pdf_parser = list_received(main_win)
    list_received_data = data_for_pdf_parser
    job_id = parent.table_printer.item(row_index, 0).text()
    info_job = {'user_name': parent.table_printer.item(row_index, 1).text(),
                'doc_name': parent.table_printer.item(row_index, 2).text()}
    count_pages = CreateMarker.find_job_file(job_id)['count_pages']


    data = {
            'number_pu': parent.numberPuEdit.text(),
            'count_ekzem': parent.countEkzemEdit.text(),
            'list_received': list_received_data['received'],
            'executor_telephone_number': parent.executorTelephoneNumberEdit.text(),
            'hard_dick_number': parent.hardDickNumberEdit.text(),
            'name_executor': parent.nameExecutorEdit.text(),
            'fio_print_admin_edit': parent.fioPrintAdminEdit.text(),
            }

    if data['count_ekzem'] != '':
        text = """
fonarik_border=5 
charset=utf-8.PTAstraSerif 
        """
        if marker_param == 'fonaric_for_all_pages':
            text += marker_for_all_pages(subject, data)
        if marker_param == 'fonaric_without_last_page':
            text += marker_without_last_pages(subject, data['number_pu'])
        if marker_param == 'fonaric_only_last_page':
            text += marker_only_last_pages(data)
        if marker_param == 'without_fonaric':
            text = ''
        if marker_param != 'without_fonaric' and count_pages == 1:
            text = last_page_marker_for_only_page(data, list_received_data['received_arr_for_only_pages'])
        write_file(path, text)

        if int(list_received_data['count_list_received_item']) == int(data['count_ekzem']):
            print_document(job_id, data, subject, data_for_pdf_parser['rec_for_pdf_parser'], marker_param)
            UiDialog('Печать...', 'Задание отправлено на печать!')
            insert_data_in_journal(data, info_job, job_id, session)
        else:
            parent.info_mark_label.setText('Пожалуйста заполните список рассылки соглассно количеству копий!')
    else:
        parent.info_mark_label.setText('Пожалуйста заполните количество экземпляров')


def write_file(path, text):
    file = open(path, "w")
    file.write(text)
    file.close()


def marker_for_all_pages(subject, data):
    return marker_without_last_pages(subject, data['number_pu']) + marker_only_last_pages(data)


def last_page_marker_for_only_page(data, received_arr_for_only_pages):
    return """
fonarik_border=5 
charset=utf-8.PTAstraSerif 
any:normal:12:PT Astra Serif:bottom-left:уч. {} 
any:normal:12:PT Astra Serif:bottom-left:лист № {{CURRENT_PAGE}} 
any:normal:12:PT Astra Serif:bottom-left:отп. {} экз.
{} 
any:normal:12:PT Astra Serif:bottom-left:НЖМД {}
any:normal:12:PT Astra Serif:bottom-left:исп. {}
any:normal:12:PT Astra Serif:bottom-left:тел. {}
any:normal:12:PT Astra Serif:bottom-left:расп. {}
any:normal:12:PT Astra Serif:bottom-left:{{DATE}}
        """.format(data['number_pu'],
                   data['count_ekzem'],
                   received_arr_for_only_pages,
                   data['hard_dick_number'],
                   data['name_executor'],
                   data['executor_telephone_number'],
                   data['fio_print_admin_edit'])

def marker_only_last_pages(data):
    return """
last:normal:12:PT Astra Serif:bottom-left:уч. {} 
last:normal:12:PT Astra Serif:bottom-left:лист № {{CURRENT_PAGE}} 
last:normal:12:PT Astra Serif:bottom-left:отп. {} экз.
{} 
last:normal:12:PT Astra Serif:bottom-left:НЖМД {}
last:normal:12:PT Astra Serif:bottom-left:исп. {}
last:normal:12:PT Astra Serif:bottom-left:тел. {}
last:normal:12:PT Astra Serif:bottom-left:расп. {}
last:normal:12:PT Astra Serif:bottom-left:{{DATE}}
    """.format(data['number_pu'],
               data['count_ekzem'],
               data['list_received'],
               data['hard_dick_number'],
               data['name_executor'],
               data['executor_telephone_number'],
               data['fio_print_admin_edit'])


def marker_without_last_pages(subject, number_pu):
    return """
any:bold:12:PT Astra Serif:bottom-left:{}
any:normal:12:PT Astra Serif:bottom-left:уч №{}
any:normal:12:PT Astra Serif:bottom-left:лист №{{CURRENT_PAGE}}
any:normal:12:PT Astra Serif:bottom-left:{{DATE}}
    """.format(subject, number_pu)


def list_received(parent):
    received_arr = ''
    received_arr_for_only_pages = ''
    rec_for_pdf_parser = []
    for child in parent.findChildren(QLineEdit, QRegExp("listReceiveEdit_(\d)+")):
        received_arr = received_arr + 'last:normal:12:PT Astra Serif:bottom-left:' + child.text() + '\n'
        received_arr_for_only_pages = received_arr_for_only_pages + 'any:normal:12:PT Astra Serif:bottom-left:' + child.text() + '\n'
        rec_for_pdf_parser.append(child.text())
    count_list_received_item = len(parent.findChildren(QLineEdit, QRegExp("listReceiveEdit_(\d)+")))
    return {'received': received_arr,
            'rec_for_pdf_parser': rec_for_pdf_parser,
            'count_list_received_item': count_list_received_item,
            'received_arr_for_only_pages': received_arr_for_only_pages}


def print_document(job_id, data, subject, data_for_pdf_parser, marker_param):
    job_copies = []
    #Узнать Имя принтера
    comand_out = os.popen("lpattr -j {} -q printer-uri".format(job_id)).read()
    name_printer = comand_out.split('/')[4]
    name_printer = name_printer.split('\n')[0]

    if int(data['count_ekzem']) > 1:
        job_copies = CreateMarker(subject, data, job_id, data_for_pdf_parser, marker_param).name_copies
    os.system("lpattr -j {} -s copies=1".format(job_id))
    os.system("lpattr -j {} -s mac-inv-num={}".format(job_id, data['number_pu']))
    os.system("lpattr -j {} -s mac-workplace-id=1".format(job_id))
    os.system("lpattr -j {} -s mac-owner-phone={}".format(job_id, data['executor_telephone_number']))
    os.system("lpattr -j {} -s mac-distribution=-".format(job_id))
    os.system("lpattr -j {} -m".format(job_id))
    os.system("lp -i {} -H resume".format(job_id))
    #Печать копий
    for i in job_copies:
        os.system("lp -d {} {}".format(name_printer, i))


def insert_data_in_journal(data, info_job, job_id, session):
    comand_out = os.popen("lpattr -j {} -q mac-job-mac".format(job_id)).read()
    mac_level = comand_out.split('=')[1]
    mac_level = mac_level.split('\n')[0]
    date = datetime.date.today()
    current_date = date.strftime('%d.%m.%Y')
    session = session
    query = sql_prepare()['insert_print_job']
    insertDataQuery = QSqlQuery(session)
    insertDataQuery.prepare(query)
    insertDataQuery.addBindValue(data['number_pu'])
    insertDataQuery.addBindValue(info_job['user_name'])
    insertDataQuery.addBindValue(data['name_executor'])
    insertDataQuery.addBindValue(info_job['doc_name'])
    insertDataQuery.addBindValue(current_date)
    insertDataQuery.addBindValue(mac_level)
    insertDataQuery.exec_()
    insertDataQuery.finish()


