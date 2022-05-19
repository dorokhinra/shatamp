import os
import re
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
import uuid
import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from PyPDF2 import PdfFileReader


class CreateMarker(object):
    """
    Создает маркер, если копий больше 1
         subject - Название подразделения
         data - Список параметров заполняемых в форме
         job_id - ID работы (в очереди)
         data_for_pdf_parser  - список рассылки в виде списка
         height=56.88 - Отступ в дюймах
         width=84.96 - Отсуп в дюмах
    """
    def __init__(self,
                 subject,
                 data,
                 job_id,
                 data_for_pdf_parser,
                 marker_param,
                 height=56.88,
                 width=84.96
                 ):
        self.data_for_pdf_parser = data_for_pdf_parser
        self.app_path = os.path.abspath(os.getcwd())
        self.temp_path = os.path.join(self.app_path, 'temp')
        self.set_fonts()
        self.name_copies = []
        self.current_height = height
        self.width = width
        self.data = data
        self.job_id = job_id
        self.subject = subject
        self.result_find_file = self.find_job_file(job_id)
        self.page_count_pdf = self.result_find_file['count_pages']
        self.page_count = self.result_find_file['count_pages']
        self.pdf_job = self.result_find_file['doc']

        self.create_marker(marker_param)

    def set_fonts(self):
        folder = "fonts"
        path = os.path.join(self.app_path, folder)
        astra_bold = os.path.normpath(os.path.join(path, "PT-Astra-Serif_Bold.ttf"))
        astra_normal = os.path.normpath(os.path.join(path, "PT-Astra-Serif_Regular.ttf"))
        pdfmetrics.registerFont(TTFont('PtAstraBold', astra_bold))
        pdfmetrics.registerFont(TTFont('PtAstraNormal', astra_normal))

    def create_marker(self, marker_param):
        if marker_param == 'fonaric_for_all_pages':
            self.marker_for_all_pages()

        if marker_param == 'fonaric_without_last_page':
            self.marker_for_any_pages()

        if marker_param == 'fonaric_only_last_page':
            self.marker_only_last_pages()

        if marker_param == 'without_fonaric':
            for val in range(int(self.data['count_ekzem']) - 1):
                pdf_obj = PdfReader(self.pdf_job)
                pages = pdf_obj.pages
                pages = [pagexobj(page) for page in pages]
                self.mark_name = os.path.normpath(os.path.join(self.temp_path, str(uuid.uuid4())))
                self.marker = Canvas(self.mark_name)
                self.name_copies.append(self.mark_name)
                for i in range(1, int(self.page_count + 1)):
                    count = self.current_height
                    self.marker.doForm(makerl(self.marker, pages[i - 1]))
                    self.marker.showPage()
                self.marker.save()
                self.page_count_pdf += self.page_count_pdf

    #Маркер для всех страниц
    def marker_for_all_pages(self):
        date = datetime.date.today()
        current_date = date.strftime('%d.%m.%Y')
        for val in range(int(self.data['count_ekzem'])-1):
            pdf_obj = PdfReader(self.pdf_job)
            pages = pdf_obj.pages
            pages = [pagexobj(page) for page in pages]
            self.mark_name = os.path.normpath(os.path.join(self.temp_path, str(uuid.uuid4())))
            self.marker = Canvas(self.mark_name)
            self.name_copies.append(self.mark_name)
            for i in range(1, int(self.page_count+1)):
                count = self.current_height
                self.marker.doForm(makerl(self.marker, pages[i-1]))
                self.marker.showPage()
                if self.page_count_pdf != i:
                    self.marker.setFont('PtAstraNormal', 12)
                    self.marker.drawString(self.width, count, current_date)
                    self.marker.setFont('PtAstraNormal', 12)
                    self.marker.drawString(self.width, count + 14, 'лист №'+str(self.page_count_pdf+i))
                    count += 14
                    self.marker.setFont('PtAstraNormal', 12)
                    self.marker.drawString(self.width, count + 14, 'уч №' + str(self.data['number_pu']))
                    count += 14
                    self.marker.setFont('PtAstraBold', 12)
                    self.marker.drawString(self.width, count + 14, str(self.subject))
                    count += 14
                    ####
                else:
                    self.marker.setFont('PtAstraNormal', 12)
                    self.marker.drawString(self.width, count, current_date)
                    self.marker.drawString(self.width, count + 14, 'расп. ' + str(self.data['fio_print_admin_edit']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'тел. ' + str(self.data['executor_telephone_number']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'исп. ' + str(self.data['name_executor']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'НЖМД ' + str(self.data['hard_dick_number']))
                    count += 14
                    for item in reversed(self.data_for_pdf_parser):
                        self.marker.drawString(self.width, count + 14, str(item))
                        count += 14
                    self.marker.drawString(self.width, count + 14, 'отп. ' + str(self.data['count_ekzem']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'лист №' + str(self.page_count_pdf+i))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'уч №' + str(self.data['number_pu']))
                self.marker.showPage()
            self.marker.save()
            self.page_count_pdf += self.page_count_pdf


    #Маркер тллько для последней страницы
    def marker_only_last_pages(self):
        date = datetime.date.today()
        current_date = date.strftime('%d.%m.%Y')
        for val in range(int(self.data['count_ekzem'])-1):
            pdf_obj = PdfReader(self.pdf_job)
            pages = pdf_obj.pages
            pages = [pagexobj(page) for page in pages]
            self.mark_name = os.path.normpath(os.path.join(self.temp_path, str(uuid.uuid4())))
            self.marker = Canvas(self.mark_name)
            self.name_copies.append(self.mark_name)
            for i in range(1, int(self.page_count+1)):
                count = self.current_height
                self.marker.doForm(makerl(self.marker, pages[i-1]))
                self.marker.showPage()
                if self.page_count_pdf != i:
                    pass
                else:
                    self.marker.setFont('PtAstraNormal', 12)
                    self.marker.drawString(self.width, count, current_date)
                    self.marker.drawString(self.width, count + 14, 'расп. ' + str(self.data['fio_print_admin_edit']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'тел. ' + str(self.data['executor_telephone_number']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'исп. ' + str(self.data['name_executor']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'НЖМД ' + str(self.data['hard_dick_number']))
                    count += 14
                    for item in reversed(self.data_for_pdf_parser):
                        self.marker.drawString(self.width, count + 14, str(item))
                        count += 14
                    self.marker.drawString(self.width, count + 14, 'отп. ' + str(self.data['count_ekzem']))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'лист №' + str(self.page_count_pdf+i))
                    count += 14
                    self.marker.drawString(self.width, count + 14, 'уч №' + str(self.data['number_pu']))
                self.marker.showPage()
            self.marker.save()
            self.page_count_pdf += self.page_count_pdf

    #маркер только для любых страниц, кроме последней
    def marker_for_any_pages(self):
        date = datetime.date.today()
        current_date = date.strftime('%d.%m.%Y')
        for val in range(int(self.data['count_ekzem'])-1):
            pdf_obj = PdfReader(self.pdf_job)
            pages = pdf_obj.pages
            pages = [pagexobj(page) for page in pages]
            self.mark_name = os.path.normpath(os.path.join(self.temp_path, str(uuid.uuid4())))
            self.marker = Canvas(self.mark_name)
            self.name_copies.append(self.mark_name)
            for i in range(1, int(self.page_count+1)):
                count = self.current_height
                self.marker.doForm(makerl(self.marker, pages[i-1]))
                self.marker.showPage()
                self.marker.setFont('PtAstraNormal', 12)
                self.marker.drawString(self.width, count, current_date)
                self.marker.setFont('PtAstraNormal', 12)
                self.marker.drawString(self.width, count + 14, 'лист №'+str(self.page_count_pdf+i))
                count += 14
                self.marker.setFont('PtAstraNormal', 12)
                self.marker.drawString(self.width, count + 14, 'уч №' + str(self.data['number_pu']))
                count += 14
                self.marker.setFont('PtAstraBold', 12)
                self.marker.drawString(self.width, count + 14, str(self.subject))
                count += 14
                self.marker.showPage()
            self.marker.save()
            self.page_count_pdf += self.page_count_pdf

    @staticmethod
    def find_job_file(job_id):
        path = '/var/spool/cups'
        file = re.compile(r'[a-z]\d+' + str(job_id) + '-001')
        for root, dirs, files in os.walk(path):
            res = [os.path.join(root, x) for x in files if file.match(x)]
            if res:
                pdf = PdfFileReader(str(res[0]))
                return {'count_pages': pdf.getNumPages(), 'doc': res[0]}

    # canvas = Canvas('hello.pdf')
    # canvas.drawString(84.96, 56.88, "Hello world")
    # canvas.drawString(84.96, 70.88, "Privet")
    # canvas.save()

