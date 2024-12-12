from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTabWidget
from database import create_table
from add_book import add_book
from search_books import search_books
from delete_book import delete_book
from add_user import add_user
from search_users import search_users
from delete_user import delete_user

app = QApplication([])

# Jadvalni yaratishni chaqiramiz
create_table()

# Asosiy oynani yaratish
window = QTabWidget()
window.setWindowTitle('Kutubxona Ilovasi')
window.resize(800, 600)

# Kitoblarni Boshqarish Tab
book_tab = QWidget()
book_layout = QVBoxLayout()
book_tab.setLayout(book_layout)

# Foydalanuvchilarni Boshqarish Tab
user_tab = QWidget()
user_layout = QVBoxLayout()
user_tab.setLayout(user_layout)

# Kitoblar Tab Widgetlari
title_label = QLabel('Kitob Nomi:')
title_input = QLineEdit()
author_label = QLabel('Muallif:')
author_input = QLineEdit()
date_label = QLabel('Nashr Yili:')
date_input = QLineEdit()
file_path_label = QLabel('Fayl Yo\'li:')
file_path_input = QLineEdit()
file_type_label = QLabel('Fayl Turi:')
file_type_input = QLineEdit()
add_button = QPushButton('Kitob Qo\'shish')

def on_add_button_clicked():
    title = title_input.text()
    author = author_input.text()
    date = date_input.text()
    file_path = file_path_input.text()
    file_type = file_type_input.text()
    add_book(title, author, date, file_path, file_type)

add_button.clicked.connect(on_add_button_clicked)

search_label = QLabel('Kitobni Qidirish:')
search_input = QLineEdit()
search_button = QPushButton('Qidirish')

result_label = QLabel('Qidiruv Natijalari:')
result_list = QVBoxLayout()

def on_search_button_clicked():
    title = search_input.text()
    results = search_books(title)
    display_search_results(results)

def display_search_results(results):
    for i in reversed(range(result_list.count())): 
        widget = result_list.itemAt(i).widget()
        if widget is not None: 
            widget.deleteLater()
    for result in results:
        result_text = f"ID: {result[0]}, Nomi: {result[1]}, Muallif: {result[2]}, Nashr yili: {result[3]}, Fayl Yo'li: {result[4]}, Fayl Turi: {result[5]}"
        result_label = QLabel(result_text)
        result_list.addWidget(result_label)

search_button.clicked.connect(on_search_button_clicked)

delete_label = QLabel('Kitobni O\'chirish ID:')
delete_input = QLineEdit()
delete_button = QPushButton('O\'chirish')

def on_delete_button_clicked():
    book_id = int(delete_input.text())
    delete_book(book_id)

delete_button.clicked.connect(on_delete_button_clicked)

book_layout.addWidget(title_label)
book_layout.addWidget(title_input)
book_layout.addWidget(author_label)
book_layout.addWidget(author_input)
book_layout.addWidget(date_label)
book_layout.addWidget(date_input)
book_layout.addWidget(file_path_label)
book_layout.addWidget(file_path_input)
book_layout.addWidget(file_type_label)
book_layout.addWidget(file_type_input)
book_layout.addWidget(add_button)
book_layout.addWidget(search_label)
book_layout.addWidget(search_input)
book_layout.addWidget(search_button)
book_layout.addWidget(result_label)
book_layout.addLayout(result_list)
book_layout.addWidget(delete_label)
book_layout.addWidget(delete_input)
book_layout.addWidget(delete_button)

# Foydalanuvchilar Tab Widgetlari
username_label = QLabel('Foydalanuvchi Nomi:')
username_input = QLineEdit()
email_label = QLabel('Email:')
email_input = QLineEdit()
add_user_button = QPushButton('Foydalanuvchi Qo\'shish')

def on_add_user_button_clicked():
    username = username_input.text()
    email = email_input.text()
    add_user(username, email)

add_user_button.clicked.connect(on_add_user_button_clicked)

search_user_label = QLabel('Foydalanuvchini Qidirish:')
search_user_input = QLineEdit()
search_user_button = QPushButton('Qidirish')

user_result_label = QLabel('Qidiruv Natijalari:')
user_result_list = QVBoxLayout()

def on_search_user_button_clicked():
    username = search_user_input.text()
    results = search_users(username)
    display_user_search_results(results)

def display_user_search_results(results):
    for i in reversed(range(user_result_list.count())): 
        widget = user_result_list.itemAt(i).widget()
        if widget is not None: 
            widget.deleteLater()
    for result in results:
        result_text = f"ID: {result[0]}, Foydalanuvchi Nomi: {result[1]}, Email: {result[2]}"
        result_label = QLabel(result_text)
        user_result_list.addWidget(result_label)

search_user_button.clicked.connect(on_search_user_button_clicked)

delete_user_label = QLabel('Foydalanuvchini O\'chirish ID:')
delete_user_input = QLineEdit()
delete_user_button = QPushButton('O\'chirish')

def on_delete_user_button_clicked():
    user_id = int(delete_user_input.text())
    delete_user(user_id)

delete_user_button.clicked.connect(on_delete_user_button_clicked)

user_layout.addWidget(username_label)
user_layout.addWidget(username_input)
user_layout.addWidget(email_label)
user_layout.addWidget(email_input)
user_layout.addWidget(add_user_button)
user_layout.addWidget(search_user_label)
user_layout.addWidget(search_user_input)
user_layout.addWidget(search_user_button)
user_layout.addWidget(user_result_label)
user_layout.addLayout(user_result_list)
user_layout.addWidget(delete_user_label)
user_layout.addWidget(delete_user_input)
user_layout.addWidget(delete_user_button)

# Asosiy oynaga tablarni qo'shish
window.addTab(book_tab, "Kitoblar")
window.addTab(user_tab, "Foydalanuvchilar")

window.show()
app.exec_()
