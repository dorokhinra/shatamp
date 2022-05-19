

def create_tables():
    return """
    CREATE TABLE IF NOT EXISTS mark_journal (
    	number_pu TEXT,
    	user_name TEXT,
    	fio_executor TEXT,
    	doc_name TEXT,
    	date_print TEXT,
    	mac_level TEXT
    );
    """

