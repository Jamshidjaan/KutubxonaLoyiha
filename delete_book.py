from database import create_connection

def delete_book(book_id):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()
        print("Book deleted successfully")
    except Exception as e:
        print(f"Error occurred: {e}")

