from database import create_connection

def search_books(title):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('''
            SELECT * FROM books WHERE title LIKE ?
        ''', ('%' + title + '%',))
        results = c.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
