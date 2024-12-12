from database import create_connection

def search_users(username):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('''
            SELECT * FROM users WHERE username LIKE ?
        ''', ('%' + username + '%',))
        results = c.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

