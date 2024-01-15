import sqlite3


def create_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT
        )
    ''')

    connection.commit()
    connection.close()


def get_all_records():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM persons')
    records = cursor.fetchall()

    connection.close()
    return records


def delete_record(name, phone):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM persons WHERE name = ? AND phone = ?', (name, phone))

    connection.commit()
    connection.close()


def create_new_record(name, phone):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO persons (name, phone) VALUES (?, ?)', (name, phone))

    connection.commit()
    connection.close()
