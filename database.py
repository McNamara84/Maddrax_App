import mysql.connector
from mysql.connector import Error
import hashlib
import os
from dotenv import load_dotenv

# Laden der Umgebungsvariablen
load_dotenv()


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        return connection
    except Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None


def init_db():
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Create users table
            print("Versuche, users-Tabelle zu erstellen...")
            cursor.execute('''CREATE TABLE IF NOT EXISTS users
                             (id INT AUTO_INCREMENT PRIMARY KEY,
                              username VARCHAR(255) UNIQUE NOT NULL,
                              password VARCHAR(255) NOT NULL,
                              role VARCHAR(50) NOT NULL,
                              baxx INT NOT NULL)''')
            print("users-Tabelle erstellt oder bereits vorhanden.")

            # Create chat_messages table
            cursor.execute('''CREATE TABLE IF NOT EXISTS chat_messages
                             (id INT AUTO_INCREMENT PRIMARY KEY,
                              user_id INT,
                              channel VARCHAR(255) NOT NULL,
                              message TEXT NOT NULL,
                              timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                              FOREIGN KEY (user_id) REFERENCES users (id))''')

            # Create tasks table
            cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                             (id INT AUTO_INCREMENT PRIMARY KEY,
                              title VARCHAR(255) NOT NULL,
                              description TEXT,
                              status VARCHAR(50) NOT NULL,
                              assigned_to INT,
                              baxx_reward INT NOT NULL,
                              FOREIGN KEY (assigned_to) REFERENCES users (id))''')

            conn.commit()
            print(
                "Alle Tabellen wurden erfolgreich erstellt oder waren bereits vorhanden.")
        except Error as e:
            print(f"Fehler beim Erstellen der Tabellen: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Keine Verbindung zur Datenbank möglich. Tabellen konnten nicht erstellt werden.")


def add_user(username, password, role='guest'):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password, role, baxx) VALUES (%s, %s, %s, 0)",
                           (username, hashed_password, role))
            conn.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def get_user(username, password):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute(
                "SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
            user = cursor.fetchone()
            return user
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    return None


def test_connection():
    conn = get_db_connection()
    if conn is not None:
        print("Verbindung zur Datenbank erfolgreich hergestellt!")
        conn.close()
    else:
        print("Verbindung zur Datenbank fehlgeschlagen!")


# Fügen Sie diese Zeile am Ende der Datei hinzu
test_connection()

# Initialize the database
init_db()
