from database import create_connection

def add_user(username, email):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('''
            INSERT INTO users (username, email) VALUES (?, ?)
        ''', (username, email))
        conn.commit()
        conn.close()
        print("User added successfully")
    except Exception as e:
        print(f"Error occurred: {e}")

