import sqlite3

DB_PATH = "./todo.db"
NOT_STARTED = 'Not Started'
IN_PROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        
        c = conn.cursor() # c is cursor object

        c.execute('insert into items(item, status) values(?,?)', (item, NOT_STARTED))

        conn.commit()
        return {"item": item, "status": NOT_STARTED}
    except Exception as e:
        print('Error: ', e)
        return None
