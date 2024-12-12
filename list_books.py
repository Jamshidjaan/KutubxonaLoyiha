from database import create_connection

def list_books():
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM books')
        results = c.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

