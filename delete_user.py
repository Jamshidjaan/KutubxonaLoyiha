from database import create_connection

def delete_user(user_id):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        print("User deleted successfully")
    except Exception as e:
        print(f"Error occurred: {e}")

