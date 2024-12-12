from database import create_connection

def add_book(title, author, published_date, file_path=None, file_type=None):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('''
            INSERT INTO books (title, author, published_date, file_path, file_type) VALUES (?, ?, ?, ?, ?)
        ''', (title, author, published_date, file_path, file_type))
        conn.commit()
        conn.close()
        print("Book added successfully")
    except Exception as e:
        print(f"Error occurred: {e}")
