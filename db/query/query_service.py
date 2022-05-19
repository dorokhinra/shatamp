from PyQt5.QtSql import QSqlQuery, QSqlDatabase


def sql_prepare():
    insert_print_job_injournal = """
        INSERT INTO mark_journal (
        number_pu,
    	user_name,
    	fio_executor,
    	doc_name,
    	date_print,
    	mac_level
        )
        VALUES (?, ?, ?, ?,?,?)
        """

    select_year = """
    SELECT date_print FROM mark_journal
    """

    return {'insert_print_job': insert_print_job_injournal, 'select_year': select_year }