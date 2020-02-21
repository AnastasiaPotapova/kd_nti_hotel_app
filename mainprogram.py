import sys
from openpyxl import load_workbook
import csv
import time

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt

from db import UserModel, DB, LodgerModel, HotelModel, RoomModel, ErrModel

from add_hostelvisual import Ui_Qadd_hostel
from add_lodgervisual import Ui_Qadd_lodger
from add_adminvisual import Ui_Qadd_admin
from add_roomvisual import Ui_Qadd_room
from adminvisual import Ui_Qadmin
from loginvisual import Ui_Qlogin
from managervisual import Ui_Qmanager
from to_csvvisual import Ui_ToCSV

db = DB()
user_model = UserModel(db.get_connection())
if not (user_model.exists('Admin', 'Admin')[0]):
    d = {'login': 'Admin', 'password': 'Admin', 'is_admin': '1'}
    a = {'login': 'Manager', 'password': 'Manager', 'is_admin': '0'}
    user_model.insert(d['login'], d['password'], '0', '0', '0', '0', d['is_admin'])
    user_model.insert(a["login"], a["password"], '0', '0', '0', '0', a["is_admin"])
    data = load_workbook('admins.xlsx')
    admins = data.get_sheet_by_name('Лист1')
    n = 1
    a = admins['A1'].value
    while a != None:
        user_model.insert(admins['A' + str(n)].value, admins['B' + str(n)].value, admins['C' + str(n)].value,
                          admins['D' + str(n)].value,
                          admins['E' + str(n)].value, admins['F' + str(n)].value, admins['G' + str(n)].value)
        n += 1
        a = admins['A' + str(n)].value


class ToCSVM(QWidget, Ui_ToCSV):
    def __init__(self, adm):
        super(ToCSVM, self).__init__()
        self.setupUi(self)
        self.adm = adm
        self.choose = []
        self.initUI()

    def initUI(self):
        self.btnto_csv.clicked.connect(self.to_csv)
        self.lodgers = LodgerModel(db.get_connection()).get_all(self.adm[7])
        self.lodger_session.setText(
            '\n'.join([x[1] for x in self.lodgers]))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = event.x(), event.y()
            y -= 50
            y //= 18
            print(y)
            self.choose.append(y)

    def to_csv(self):
        data = []
        lod = LodgerModel(db.get_connection())
        for i in self.choose:
            data.append(lod.get(self.lodgers[i][0]))
        print(data)
        with open("lodgers.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in data:
                writer.writerow(line)


class Add_hostelM(QWidget, Ui_Qadd_hostel):
    def __init__(self, name, type):
        super(Add_hostelM, self).__init__()
        self.setupUi(self)
        self.adm = name
        self.type = type
        self.initUI()

    def initUI(self):
        self.btnadd_hostel.clicked.connect(self.add_hotel)
        if self.type == -1:
            self.title.setText("Добавление отеля")
        else:
            lod = HotelModel(db.get_connection()).get(self.type)
            self.nlevel.setText(lod[1])
            self.nroom.setText(lod[2])
            self.country.setText(lod[3])
            self.city.setText(lod[4])
            self.street.setText(lod[5])
            self.house.setText(lod[6])
            self.title.setText("Редактирование отеля")

    def add_hotel(self):
        if self.type == -1:
            nlevel = self.nlevel.text()
            nroom = self.nroom.text()
            country = self.country.text()
            city = self.city.text()
            street = self.sreet.text()
            house = self.house.text()
            if nlevel == '':
                self.change_status("Вы не указали количество этажей")
            elif nroom == '':
                self.change_status("Вы не указали количество номеров")
            elif country == '':
                self.change_status("Вы не указали страну")
            elif city == '':
                self.change_status("Вы не указали город")
            elif street == '':
                self.change_status("Вы не указали улицу")
            elif house == '':
                self.change_status("Вы не указали номер дома")
            else:
                lodger = HotelModel(db.get_connection())
                lodger.insert(country, city, street, house, nlevel, nroom)
                self.close()
        else:
            nlevel = self.nlevel.text()
            nroom = self.nroom.text()
            country = self.country.text()
            city = self.city.text()
            street = self.sreet.text()
            house = self.house.text()
            lodger = HotelModel(db.get_connection())
            lodger.change(self.type, country, city, street, house, nlevel, nroom)
            self.close()

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)


class Add_adminM(QWidget, Ui_Qadd_admin):
    def __init__(self, name, type):
        super(Add_adminM, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btnadd_hostel.clicked.connect(self.add_admin)

    def add_admin(self):
        name = self.name.text()
        familyname = self.familyname.text()
        fathername = self.fathername.text()
        login = self.login.text()
        number = self.number.text()
        password = self.password.text()
        lodger = UserModel(db.get_connection())
        lodger.insert(login, password, familyname, name, fathername, number, 1)
        self.close()

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)


class ManagerM(QWidget, Ui_Qmanager):
    def __init__(self, obj):
        super(ManagerM, self).__init__()
        self.setupUi(self)
        self.o = obj
        self.choose_admin = -1
        self.choose_hotel = -1
        self.initUI()

    def initUI(self):
        self.btnin_admin.clicked.connect(self.in_admin)
        self.btnadd_admin.clicked.connect(self.add_admin)
        self.btnadd_hostel.clicked.connect(self.add_hotel)
        self.btnaapply.clicked.connect(self.apply)
        self.btnblock.clicked.connect(self.block)
        self.change()

    def apply(self):
        if self.adress_sort.isChecked():
            self.hotels = HotelModel(db.get_connection()).get_all()
            self.hotels.sort(key=lambda x: str(x[2]) + str(x[3]) + str(x[4]) + str(x[5]))
            self.hotel_session.setText('\n'.join(['[x] ' + str(x[3]) for x in self.hotels]))
        elif self.nroom_sort.isChecked():
            self.hotels = HotelModel(db.get_connection()).get_all()
            self.hotels.sort(key=lambda x: x[7])
            self.hotel_session.setText('\n'.join(['[x] ' + str(x[3]) for x in self.hotels]))
        elif self.time.isChecked():
            self.hotels = HotelModel(db.get_connection()).get_all()
            self.hotels.sort(key=lambda x: x[0])
            self.hotel_session.setText('\n'.join(['[x] ' + str(x[3]) for x in self.hotels]))

    def block(self):
        UserModel(db.get_connection()).block(self.choose_admin)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = event.x(), event.y()

            x -= 200
            y -= 70

            print(x, y)
            if y < 170:
                y //= 18

                self.hotels = HotelModel(db.get_connection()).get_all()
                if x <= 20:
                    self.delete_hotel(self.hotels[y-1][0])
                else:
                    self.choose_hotel = self.hotels[y-1][0]
            else:
                y //= 18
                y -= 9
                self.admins = UserModel(db.get_connection()).get_all()
                if x <= 20:
                    print(y)
                    self.delete_admin(self.admins[y-1][0])
                else:
                    self.choose_admin = self.admins[y-1][0]

    def mouseDoubleClickEvent(self, event):
        x, y = event.x(), event.y()
        try:
            x -= 10
            y -= 60
            x //= 6
            y //= 18
            if x <= 290:
                self.admins = UserModel(db.get_connection()).get_all()
                self.edit_lodger(self.admins[y][0])
            else:
                self.hotels = HotelModel(db.get_connection()).get_all()
                self.edit_hotel(self.hotels[y][0])
        except Exception as e:
            self.change_status(e)

    def add_admin(self):
        self.w1 = Add_adminM(self.o, -1)
        self.w1.show()
        self.change()

    def delete_admin(self, id):
        self.admins = UserModel(db.get_connection())
        self.admins.delete(id)

    def in_admin(self):
        self.admin = UserModel(db.get_connection())
        lod = self.admin.get(self.choose_lodger)
        if lod[8] != -1:
            self.change_status("Этот администратор уже назначен")
        else:
            self.admin.check_in(self.choose_admin, self.choose_hotel)
            self.change()

    def out_admin(self):
        self.lodgers = UserModel(db.get_connection())
        self.lodgers.check_out(self.choose_lodger)
        self.change()

    def edit_hotel(self, y):
        self.w1 = Add_hostelM(self.o, y)
        self.w1.show()
        self.change()

    def add_hotel(self):
        self.w1 = Add_hostelM(self.o, -1)
        self.w1.show()

    def delete_hotel(self, id):
        self.hotel = HotelModel(db.get_connection())
        room = self.hotel.get(id)
        if room[4] != 0:
            self.change_status("В этом отеле живут")
        else:
            self.hotel.delete(id)
            self.change()

    def edit_admin(self, id):
        self.w1 = Add_adminM(self.o, self.choose_admin)
        self.w1.show()
        self.change()

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)

    def change(self):
        self.hotels = HotelModel(db.get_connection()).get_all()
        self.hotel_session.setText('\n'.join(['[x] ' + str(x[3]) for x in self.hotels]))
        self.admins = UserModel(db.get_connection()).get_all()
        #print(self.hotels)
        self.admin_session.setText(
            '\n'.join(['[x] ' + x[1] + ' ' + str(x[7]) if x[7] else '[x] ' + x[1] for x in self.admins]))


class AddLodgerM(QWidget, Ui_Qadd_lodger):
    def __init__(self, Admin, type):
        super(AddLodgerM, self).__init__()
        self.setupUi(self)
        self.adm = Admin
        self.type = type
        self.initUI()

    def initUI(self):
        self.btnadd_hostel.clicked.connect(self.add_lodger)
        if self.type == -1:
            self.title.setText("Добавление постояльца")
        else:
            lod = LodgerModel(db.get_connection()).get(self.type)
            self.name.setText(lod[1])
            self.familyname.setText(lod[2])
            self.fathername.setText(lod[3])
            self.birt.setText(lod[4])
            self.sex.setText(lod[5])
            self.number.setText(lod[6])
            self.passport.setText(lod[7])
            self.title.setText("Редактирование постояльца")

    def add_lodger(self):
        if self.type == -1:
            name = self.name.text()
            familyname = self.familyname.text()
            fathername = self.fathername.text()
            birth = self.birt.text()
            sex = self.sex.text()
            number = self.number.text()
            passport = self.passport.text()
            if name == '':
                self.change_status("Вы не указали имя")
            elif familyname == '':
                self.change_status("Вы не указали фамилию")
            elif fathername == '':
                self.change_status("Вы не указали отчество")
            elif birth == '':
                self.change_status("Вы не указали дату рождения")
            elif sex == '':
                self.change_status("Вы не указали пол")
            elif number == '':
                self.change_status("Вы не указали номер телефона")
            elif passport == '':
                self.change_status("Вы не указали пасспортные данные")
            else:
                lodger = LodgerModel(db.get_connection())
                lodger.insert(name, familyname, fathername, number, sex, birth, passport, self.adm[7])
                self.close()
        else:
            lod = LodgerModel(db.get_connection()).get(self.type)
            name = self.name.text()
            familyname = self.familyname.text()
            fathername = self.fathername.text()
            birth = self.birt.text()
            sex = self.sex.text()
            number = self.number.text()
            passport = self.passport.text()
            lodger = LodgerModel(db.get_connection())
            lodger.change(self.type, name, familyname, fathername, number, sex, birth, passport, self.adm[7], lod[10])
            self.close()

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)


class Add_roomM(QWidget, Ui_Qadd_room):
    def __init__(self, Admin, type):
        super(Add_roomM, self).__init__()
        self.setupUi(self)
        self.adm = Admin
        self.type = type
        self.initUI()

    def initUI(self):
        self.btnadd_hostel.clicked.connect(self.add_room)
        if self.type == -1:
            self.title.setText("Добавление постояльца")
        else:
            lod = RoomModel(db.get_connection()).get(self.type)
            self.nlevel.setText(str(lod[1]))
            self.nlevel.setReadOnly(True)
            self.nroom.setText(str(lod[3]))
            self.country.setText(str(lod[2]))
            self.title.setText("Редактирование постояльца")

    def add_room(self):
        if self.type == -1:
            nlevel = self.nlevel.text()
            nroom = self.nroom.text()
            square = self.country.text()
            lodger = RoomModel(db.get_connection())
            if nlevel in lodger.get_ids(self.adm[7]) or int(nlevel) == 0:
                self.change_status("Комната с таким номером существует или номер не является натуральным числом")
            elif nroom == '':
                self.change_status("Вы не указали колличество комнат")
            elif square == '':
                self.change_status("Вы не указали площадь")
            else:
                lodger.insert(nlevel, nroom, square, self.adm[7])
                self.close()
        else:
            nroom = self.nroom.text()
            square = self.country.text()
            lodger = RoomModel(db.get_connection())
            lodger.change(self.type, nroom, square)
            self.close()

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)


class AdminM(QWidget, Ui_Qadmin):
    def __init__(self, obj):
        super(AdminM, self).__init__()
        self.setupUi(self)
        self.o = obj
        self.choose_lodger = -1
        self.choose_room = -1
        self.initUI()

    def initUI(self):
        self.btnin_lodger.clicked.connect(self.in_lodger)
        self.btnout_lodger.clicked.connect(self.out_lodger)
        self.btnadd_lodger.clicked.connect(self.add_lodger)
        self.btnadd_room.clicked.connect(self.add_room)
        self.btnto_csv.clicked.connect(self.to_csv)
        self.change()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = event.x(), event.y()
            x -= 10
            y -= 60
            y //= 18

            self.lodgers = LodgerModel(db.get_connection()).get_all(self.o[7])
            if x <= 20:
                lod = LodgerModel(db.get_connection()).get(self.lodgers[y][0])
                if lod[9] == None or lod[9] == 0:
                    self.delete_lodger(self.lodgers[y][0])
                else:
                    self.change_status("Нельзя удалить постояльца, который проживает в номере.")
            else:
                self.choose_lodger = self.lodgers[y][0]

            if x >= 290:
                x -= 290
                self.rooms = RoomModel(db.get_connection()).get_all(self.o[7])
                if x <= 20:
                    lod = RoomModel(db.get_connection()).get(self.rooms[y][0])
                    if lod[4] == 0:
                        self.delete_room(self.rooms[y][0])
                    else:
                        self.change_status("Нельзя удалить комнату, в которой проживает постоялец")
                else:
                    self.choose_room = self.rooms[y][0]

    def mouseDoubleClickEvent(self, event):
        x, y = event.x(), event.y()
        try:
            if 10 <= x <= 201 and 60 <= y <= 191:
                x -= 10
                y -= 60
                x //= 6
                y //= 18
                self.lodgers = LodgerModel(db.get_connection()).get_all(self.o[7])
                self.edit_lodger(self.lodgers[y][0])

            if 300 <= x <= 491 and 60 <= y <= 191:
                x -= 300
                y -= 60
                x //= 6
                y //= 18
                self.rooms = RoomModel(db.get_connection()).get_all(self.o[7])
                self.edit_room(self.rooms[y][0])
        except Exception as e:
            print(e)

    def add_lodger(self):
        self.w1 = AddLodgerM(self.o, -1)
        self.w1.show()
        self.change()

    def delete_lodger(self, id):
        self.lodgers = LodgerModel(db.get_connection())
        lod = self.lodgers.get(id)
        if lod[9] != None:
            self.change_status("Этот постоялец заселен. Его нельзя удалить.")
        else:
            self.lodgers.delete(id)
            self.change()

    def in_lodger(self):
        self.lodger = LodgerModel(db.get_connection())
        lod = self.lodger.get(self.choose_lodger)
        if lod[9] != None and lod[9] != 0:
            self.change_status("Этот постоялец заселен. Его нельзя заселить заново.")
        else:
            self.room = RoomModel(db.get_connection())
            room = self.room.get(self.choose_room)
            if room[4] != 0:
                self.change_status("Эта комната занята.")
                #print(room)
            else:
                self.lodger.check_in(self.choose_lodger, self.choose_room, self.o[7])
                self.room.check_in(self.choose_lodger, self.choose_room)
                HotelModel(db.get_connection()).in_lodger(self.o[7])
                self.change()

    def out_lodger(self):
        self.lodgers = LodgerModel(db.get_connection())
        self.lodgers.check_out(self.choose_lodger)
        self.room = RoomModel(db.get_connection())
        self.room.check_out(self.choose_lodger)
        HotelModel(db.get_connection()).out_lodger(self.o[7])
        self.change()

    def add_room(self):
        self.w1 = Add_roomM(self.o, -1)
        self.w1.show()
        self.change()

    def delete_room(self, id):
        self.rooms = RoomModel(db.get_connection())
        room = self.rooms.get(id)
        if room[4] != 0:
            self.change_status("Эта камната заселена. Вы не можете её удалить.")
        else:
            self.rooms.delete(id)
            self.change()

    def edit_lodger(self, id):
        self.w1 = AddLodgerM(self.o, id)
        self.w1.show()

    def edit_room(self, id):
        self.w1 = Add_roomM(self.o, id)
        self.w1.show()

    def to_csv(self):
        self.w1 = ToCSVM(self.o)
        self.w1.show()

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)

    def change(self):
        self.rooms = RoomModel(db.get_connection()).get_all(self.o[7])
        self.room_session.setText('\n'.join(['[x] ' + str(x[3]) for x in self.rooms]))
        self.lodgers = LodgerModel(db.get_connection()).get_all(self.o[7])
        self.lodger_session.setText(
            '\n'.join(['[x] ' + x[1] + ' ' + str(x[9]) if x[9] else '[x] ' + x[1] for x in self.lodgers]))


class LoginM(QMainWindow, Ui_Qlogin):
    def __init__(self):
        super(LoginM, self).__init__()
        self.setupUi(self)
        self.k = 0
        self.initUI()

    def initUI(self):
        self.btnlogin.clicked.connect(self.auth)
        self.btnexit.clicked.connect(self.exit)
        if self.k == 3:
            self.change_status("Система заблокированна. Осталось {} сек".format(
                60 - (time.time() - int(ErrModel(db.get_connection()).last()))))

    def auth(self):
        name = self.login.text()
        password = self.password.text()
        user_model = UserModel(db.get_connection())
        err = ErrModel(db.get_connection())
        exists = user_model.exists(name, password)
        now = time.time()
        if now - err.last() >= 60:
            self.k = 0
        if self.k < 3:
            if exists[0]:
                if exists[1][7] == 1:
                    self.w1 = AdminM(exists[1])
                    self.w1.show()
                    self.close()
                elif exists[1][7] == 0:
                    self.w1 = ManagerM(exists[1])
                    self.w1.show()
                    self.close()
                else:
                    self.k += 1
                    err.insert(time.time(), "Blocked User with id {} try to log in".format(exists[1][0]))
                    self.change_status("Вы заблокированны")
            else:
                self.k += 1
                err.insert(time.time(), "Unregistered User try to log in")
                self.change_status("Вы не зарегистрированны")
        else:
            self.change_status("Система заблокирована")
        if now - err.last() >= 60:
            self.k = 0

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)

    def exit(self):
        self.close()
        sys.exit(app.exec_())

    def time(self):
        self.upTime.setTime(self.upTime.time().addSecs(1))


app = QApplication(sys.argv)
ex = LoginM()
ex.show()
sys.exit(app.exec_())
