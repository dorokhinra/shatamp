import os
import re

from PyQt5.QtWidgets import QTableWidgetItem


class CheckPrintJob(object):

    def __init__(self, parrent):
        self.parent_class = parrent
        self.app_path = os.path.abspath(os.getcwd())
        self.check_file = os.path.normpath(os.path.join(self.app_path, 'lpq.txt'))
        self.reg = '(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(.+[.]\S+)(\s+)(\S+\s+\S+)'
        self.job_id = ''

    def parse_file(self):
        os.system("lpq -a > {}".format(self.check_file))
        with open(self.check_file, 'r') as cups:
            string_name = cups.readlines()
            if string_name != ['нет записей\n'] or string_name != ['нет записей\n']:
                ovner_index = re.search('O', string_name[0]).span()[1]
                job_index = re.search('J', string_name[0]).span()[1]
                name_job_index = re.search('F', string_name[0]).span()[1]
                end_string = re.search('T', string_name[0]).span()[1]
                string_name.pop(0)
                self.parent_class.table_printer.setRowCount(len(string_name))
                for res in string_name:
                    a = res[ovner_index - 1:job_index - 1].strip()
                    b = res[job_index - 1:name_job_index - 1].strip()
                    c = res[name_job_index - 1:end_string - 1].strip()
                    self.parent_class.table_printer.setItem(string_name.index(res), 0, QTableWidgetItem(str(b)))
                    self.parent_class.table_printer.setItem(string_name.index(res), 1, QTableWidgetItem(str(a)))
                    self.parent_class.table_printer.setItem(string_name.index(res), 2, QTableWidgetItem(str(c)))
        cups.close()
        #
        #     print(self.math)
        #
        #
        #     string_name.pop(0)
        #     for i in string_name:
        #         self.math.append(re.findall(self.reg, i))
        #     cups.close()
        # self.parent_class.table_printer.setRowCount(len(self.math))  # и одну строку в таблице
        # for i, val in enumerate(self.math):
        #     self.parent_class.table_printer.setItem(i, 0, QTableWidgetItem(str(val[0][4])))
        #     self.parent_class.table_printer.setItem(i, 1, QTableWidgetItem(str(val[0][2])))
        #     self.parent_class.table_printer.setItem(i, 2, QTableWidgetItem(str(val[0][6])))


    def emit_row_table(self, hh):
        sender = self.parent_class.sender()
        self.job_id = sender.item(hh.row(), 0).text()
