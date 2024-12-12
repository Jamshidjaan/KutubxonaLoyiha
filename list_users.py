from database import create_connection

def list_users():
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        results = c.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

