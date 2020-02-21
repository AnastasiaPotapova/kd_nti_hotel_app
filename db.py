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
                                     is_admin INTEGER,
                                     hotel_id INTEGER
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, login, password_hash, familyname, name, fathername, number, is_admin, hotel_id=-1):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (login, password_hash, familyname, name, fathername, number, is_admin, hotel_id) 
                          VALUES (?,?,?,?,?,?,?,?)''',
                       (login, password_hash, familyname, name, fathername, number, str(is_admin), hotel_id))
        cursor.close()
        self.connection.commit()

    def block(self, id):
        a = self.get(id)
        if a[7] != -1:
            cursor = self.connection.cursor()
            try:
                cursor.execute("UPDATE users SET is_admin = {} WHERE id = {}".format(100, id))
            except Exception as e:
                print(e)
            cursor.close()
            self.connection.commit()
        else:
            cursor = self.connection.cursor()
            try:
                cursor.execute("UPDATE users SET is_admin = {} WHERE id = {}".format(1, id))
            except Exception as e:
                print(e)
            cursor.close()
            self.connection.commit()

    def delete(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM users WHERE id = ?''', (str(room_id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = {}".format(str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE is_admin = 1")
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

    def check_in(self, hotel_id, admin_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE users SET hotel_id = {} WHERE id = {}".format(hotel_id, admin_id))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()

    def check_out(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE users SET hotel_id = {} WHERE id = {}".format(-1, id))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()


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
                                     room_id INTEGER,
                                     cnt INTEGER
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, name, familyname, fathername, number, sex, birth, passport, hotel_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO lodgers 
                          (name, familyname, fathername, number, sex, birth, passport, hotel_id, cnt) 
                          VALUES (?,?,?,?,?,?,?,?,?)''',
                       (name, familyname, fathername, number, sex, birth, passport, hotel_id, 0))
        cursor.close()
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM lodgers WHERE id = {}'''.format(str(id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM lodgers WHERE id = {}".format(str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self, hotel_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM lodgers WHERE hotel_id = {}".format(hotel_id))
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM lodgers WHERE user_name = ? AND password_hash = ?",
                           (user_name, password_hash))
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

    def check_in(self, id, room_id, hotel_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "UPDATE lodgers SET room_id = {} AND hotel_id = {} WHERE id = {}".format(room_id, hotel_id, id))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()

    def check_out(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE lodgers SET room_id = {} AND hotel_id = {} WHERE id = {}".format(0, -1, id))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()

    def change(self, id, name, familyname, fathername, number, sex, birth, passport, hotel_id, cnt):
        lod = self.get(id)
        if lod[1] != name:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE lodgers SET name = {} WHERE id = {}'''.format(name, id))
            cursor.close()
            self.connection.commit()

        if lod[2] != familyname:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE lodgers SET familyname = {} WHERE id = {}'''.format(familyname, id))
            cursor.close()
            self.connection.commit()

        if lod[3] != fathername:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE lodgers SET fathername = {} WHERE id = {}'''.format(fathername, id))
            cursor.close()
            self.connection.commit()

        if lod[4] != number:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE lodgers SET number = {} WHERE id = {}'''.format(number, id))
            cursor.close()
            self.connection.commit()

        if lod[5] != sex:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE lodgers SET sex = {} WHERE id = {}'''.format(sex, id))
            cursor.close()
            self.connection.commit()

        if lod[6] != birth:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE lodgers SET birth = {} WHERE id = {}'''.format(birth, id))
            cursor.close()
            self.connection.commit()

        if lod[7] != passport:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE lodgers SET passport = {} WHERE id = {}'''.format(passport, id))
            cursor.close()
            self.connection.commit()


class HotelModel:
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS hotels 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                     country VARCHAR(50),
                                     city VARCHAR(50),
                                     street VARCHAR(50),
                                     house INTEGER(50),
                                     nlevels INTEGER(50),
                                     nrooms INTEGER(50),
                                     is_used INTEGER
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, country, city, street, house, nlevels, nrooms):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO hotels 
                          (country, city, street, house, nlevels, nrooms, is_used) 
                          VALUES (?,?,?,?,?,?,?)''', (country, city, street, house, nlevels, nrooms, -1))
        cursor.close()
        self.connection.commit()

    def delete(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM hotels WHERE id = ?''', (str(room_id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM hotels WHERE id = {}".format(str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM hotels")
        rows = cursor.fetchall()
        return rows

    def in_lodger(self, hotel_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE hotels SET is_used = {} WHERE id = {}".format(1, str(hotel_id)))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()

    def out_lodger(self, hotel_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE hotels SET is_used = {} WHERE id = {}".format(-1, str(hotel_id)))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()

    def change(self, id, country, city, street, house, nlevels, nrooms):
        lod = self.get(id)
        if lod[1] != country:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE hotels SET name = {} WHERE id = {}'''.format(country, id))
            cursor.close()
            self.connection.commit()

        if lod[2] != city:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE hotels SET city = {} WHERE id = {}'''.format(city, id))
            cursor.close()
            self.connection.commit()

        if lod[3] != street:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE hotels SET street = {} WHERE id = {}'''.format(street, id))
            cursor.close()
            self.connection.commit()

        if lod[4] != house:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE hotels SET house = {} WHERE id = {}'''.format(house, id))
            cursor.close()
            self.connection.commit()

        if lod[5] != nlevels:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE hotels SET nlevels = {} WHERE id = {}'''.format(nlevels, id))
            cursor.close()
            self.connection.commit()

        if lod[6] != nrooms:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE hotels SET nrooms = {} WHERE id = {}'''.format(nrooms, id))
            cursor.close()
            self.connection.commit()


class RoomModel:
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rooms 
                                    (id INTEGER,
                                     hotel_id VARCHAR(50),
                                     size VARCHAR(128),
                                     nroom INTEGER,
                                     is_used INTEGER)
                                     ''')
        cursor.close()
        self.connection.commit()

    def insert(self, id, nroom, size, hotel_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO rooms 
                          (id, nroom, size, hotel_id, is_used) 
                          VALUES (?,?,?,?,?)''', (id, nroom, size, hotel_id, 0))
        cursor.close()
        self.connection.commit()

    def delete(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM rooms WHERE id = {}'''.format(str(room_id)))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM rooms WHERE id = {}".format(str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM rooms WHERE hotel_id = {} AND is_used = {}".format(str(id), 0))
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

    def get_ids(self, hotel_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM rooms WHERE hotel_id = {}".format(hotel_id))
        row = cursor.fetchall()
        return row

    def check_in(self, id, room_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE rooms SET is_used = {} WHERE id = {}".format(str(room_id), str(id)))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()

    def check_out(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE rooms SET is_used = {} WHERE is_used = {}".format(0, str(id)))
        except Exception as e:
            print(e)
        cursor.close()
        self.connection.commit()

    def change(self, id, nroom, square):
        lod = self.get(id)
        if lod[3] != nroom:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE rooms SET nroom = {} WHERE id = {}'''.format(nroom, id))
            cursor.close()
            self.connection.commit()

        if lod[2] != square:
            cursor = self.connection.cursor()
            cursor.execute(
                '''UPDATE rooms SET size = {} WHERE id = {}'''.format(square, id))
            cursor.close()
            self.connection.commit()


class ErrModel:
    def __init__(self, connection):
        self.connection = connection
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS errors
                                    (time INTEGER,
                                     reason VARCHAR(50)
                                     )''')
        cursor.close()
        self.connection.commit()

    def insert(self, time, reason):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO errors
                          (time, reason) 
                          VALUES (?,?)''', (time, reason))
        cursor.close()
        self.connection.commit()

    def get_all(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM errors ")
        rows = cursor.fetchall()
        return rows

    def last(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT MAX(time) FROM errors")
        rows = cursor.fetchone()
        return rows[0]
