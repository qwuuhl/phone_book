from app.gui import window
from app.db import db, Person


def setup_db():
    db.create_tables([Person])


if __name__ == '__main__':
    setup_db()
    window.resizable(False, False)
    window.mainloop()
