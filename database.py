import sqlite3
import datetime

def init_db():
    """Инициализация базы данных и создание таблицы пользователей"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER UNIQUE,
        username TEXT,
        registration_date TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def add_user(tg_id: int, username: str = None):
    """Добавление пользователя в базу данных"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Получаем текущую дату
    registration_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        cursor.execute(
            'INSERT INTO users (tg_id, username, registration_date) VALUES (?, ?, ?)',
            (tg_id, username, registration_date)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        # Пользователь уже существует в базе
        pass
    finally:
        conn.close()

def get_user_count():
    """Получение количества пользователей в базе"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    
    conn.close()
    return count

def get_all_users():
    """Получение всех пользователей из базы"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT tg_id, username, registration_date FROM users ORDER BY registration_date DESC')
    users = cursor.fetchall()
    
    conn.close()
    return users