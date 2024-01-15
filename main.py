from app.gui import window, fetch_data_to_list_box
from app.db import create_database


if __name__ == '__main__':
    create_database()
    window.resizable(False, False)
    fetch_data_to_list_box()
    window.mainloop()
