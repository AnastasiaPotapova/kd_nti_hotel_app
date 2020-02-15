import sqlite3


class DB:
    def __init__(self):
        conn = sqlite3.connect('news.db', check_same_thread=False)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class UserModel:
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                     login VARCHAR(50),
                                     password_hash VARCHAR(128),
                                     familyname VARCHAR(50),
                                     name VARCHAR(50),
                                     fathername VARCHAR(50),
                                     number VARCHAR(50),
                                     is_admin INTEGER
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, login, password_hash, familyname, name, fathername, number, is_admin):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (login, password_hash, familyname, name, fathername, number, is_admin) 
                          VALUES (?,?,?,?,?,?,?)''',
                       (login, password_hash, familyname, name, fathername, number, str(is_admin)))
        cursor.close()
        self.connection.commit()

    def delete(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM users WHERE id = ?''', (str(room_id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE login = ? AND password_hash = ?", (user_name, password_hash))
        except Exception as e:
            print(e)
        row = cursor.fetchone()
        # print(row)
        return (True, row) if row else (False,)

    def get_users(self, admin):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        row = cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(admin)))
        admin = cursor.fetchone()
        del row[row.index(admin)]
        return row


class LodgerModel:
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS lodgers 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     name VARCHAR(50),
                                     familyname VARCHAR(50),
                                     fathername VARCHAR(50),
                                     number VARCHAR(50),
                                     sex VARCHAR(50),
                                     birth VARCHAR(50),
                                     passport VARCHAR(50),
                                     hotel_id INTEGER,
                                     room_id INTEGER
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, name, familyname, fathername, number, sex, birth, passport):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO lodgers 
                          (name, familyname, fathername, number, sex, birth, passport) 
                          VALUES (?,?,?,?,?,?,?)''', (name, familyname, fathername, number, sex, birth, passport))
        cursor.close()
        self.connection.commit()

    def delete(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM lodgers WHERE id = ?''', (str(room_id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM lodgers WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM lodgers")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM lodgers WHERE user_name = ? AND password_hash = ?", (user_name, password_hash))
        except Exception as e:
            print(e)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get_users(self, admin):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM lodgers")
        row = cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM lodgers WHERE id = ?", (str(admin)))
        admin = cursor.fetchone()
        del row[row.index(admin)]
        return row


class HotelModel:
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS hotels 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                     admin_id INTEGER,
                                     country VARCHAR(50),
                                     city VARCHAR(50),
                                     street VARCHAR(50),
                                     house INTEGER(50),
                                     nlevels INTEGER(50),
                                     nrooms INTEGER(50),
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, country, city, street, house, nlevels, nrooms):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO hotels 
                          (country, city, street, house, nlevels, nrooms) 
                          VALUES (?,?,?,?,?,?)''', (country, city, street, house, nlevels, nrooms))
        cursor.close()
        self.connection.commit()

    def delete(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM users WHERE id = ?''', (str(room_id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE user_name = ? AND password_hash = ?", (user_name, password_hash))
        except Exception as e:
            print(e)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get_users(self, admin):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        row = cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(admin)))
        admin = cursor.fetchone()
        del row[row.index(admin)]
        return row


class RoomModel:
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rooms 
                                    (id INTEGER,
                                     hotel_id(50),
                                     size VARCHAR(128),
                                     is_used INTEGER
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash, email):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO rooms 
                          (login, password_hash, email) 
                          VALUES (?,?,?)''', (user_name, password_hash, email))
        cursor.close()
        self.connection.commit()

    def delete(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM rooms WHERE id = ?''', (str(room_id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM rooms WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM rooms")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM rooms WHERE user_name = ? AND password_hash = ?", (user_name, password_hash))
        except Exception as e:
            print(e)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get_rooms(self, admin):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM rooms")
        row = cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM rooms WHERE id = ?", (str(admin)))
        admin = cursor.fetchone()
        del row[row.index(admin)]
        return row
