import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtCore import Qt

from db import UserModel, DB, LodgerModel, HotelModel, RoomModel

from add_hostelvisual import Ui_Qadd_hostel
from add_lodgervisual import Ui_Qadd_lodger
from add_adminvisual import Ui_Qadd_admin
from adminvisual import Ui_Qadmin
from delete_lodgervisual import Ui_Qdelete_lodger
from edit_hostelvisual import Ui_Qedit_hostel
from loginvisual import Ui_Qlogin
from managervisual import Ui_Qmanager

db = DB()
user_model = UserModel(db.get_connection())
if user_model.exists('Admin', 'Admin')[0]:
    d = {'login': 'Admin', 'password': 'Admin', 'is_admin': '1'}
    a = {'login': 'Manager', 'password': 'Manager', 'is_admin': '0'}
    user_model.insert(d['login'], d['password'], '0', '0', '0', '0', d['is_admin'])
    user_model.insert(a["login"], a["password"], '0', '0', '0', '0', a["is_admin"])


class Add_hostelM(QWidget, Ui_Qadd_hostel):
    def __init__(self, name):
        super(Add_hostelM, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btnadd_hostel.clicked.connect(self.add_hotel)

    def add_hotel(self):
        nlevel = self.nlevel.text()
        nroom = self.nroom.text()
        country = self.country.text()
        city = self.city.text()
        street = self.sreet.text()
        house = self.house.text()
        lodger = HotelModel(db.get_connection())
        lodger.insert(country, city, street, house, nlevel, nroom)
        self.close()


class Add_adminM(QWidget, Ui_Qadd_admin):
    def __init__(self, name):
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


class ManagerM(QWidget, Ui_Qmanager):
    def __init__(self, name):
        super(ManagerM, self).__init__()
        self.setupUi(self)
        self.name = name
        self.initUI()

    def initUI(self):
        self.btnadd_admin.clicked.connect(self.add_admin)
        self.btnadd_hostel.clicked.connect(self.add_hostel)

    def add_admin(self):
        self.w1 = Add_adminM(self.name)
        self.w1.show()

    def add_hostel(self):
        self.w1 = Add_hostelM(self.name)
        self.w1.show()

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)


class CheckoutLodgerM(QWidget, Ui_Qadd_lodger):
    def __init__(self, name):
        super(CheckoutLodgerM, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btnadd_admin.clicked.connect(self.add_admin)
        self.boxfilm.addItems(self.room.spisok())
        self.btnadd_hostel.clicked.connect(self.add_hostel)


class CheckinLodgerM(QWidget, Ui_Qadd_lodger):
    def __init__(self, name):
        super(CheckinLodgerM, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btnadd_admin.clicked.connect(self.add_admin)
        self.boxfilm.addItems(self.room.spisok())
        self.btnadd_hostel.clicked.connect(self.add_hostel)


class DeleteLodgerM(QWidget, Ui_Qdelete_lodger):
    def __init__(self, name):
        super(DeleteLodgerM, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btnadd_admin.clicked.connect(self.add_admin)
        self.boxfilm.addItems(self.room.spisok())
        self.btnadd_hostel.clicked.connect(self.add_hostel)


class AddLodgerM(QWidget, Ui_Qadd_lodger):
    def __init__(self, Admin):
        super(AddLodgerM, self).__init__()
        self.setupUi(self)
        self.adm = Admin
        self.initUI()

    def initUI(self):
        self.btnadd_hostel.clicked.connect(self.add_lodger)

    def add_lodger(self):
        name = self.name.text()
        familyname = self.familyname.text()
        fathername = self.fathername.text()
        birth = self.birt.text()
        sex = self.sex.text()
        number = self.number.text()
        passport = self.passport.text()
        lodger = LodgerModel(db.get_connection())
        lodger.insert(name, familyname, fathername, number, sex, birth, passport)
        self.close()


class AdminM(QWidget, Ui_Qadmin):
    def __init__(self, obj):
        super(AdminM, self).__init__()
        self.setupUi(self)
        self.o = obj
        self.initUI()

    def initUI(self):
        self.btnin_lodger.clicked.connect(self.in_lodger)
        self.btnout_lodger.clicked.connect(self.out_lodger)
        self.btnadd_lodger.clicked.connect(self.add_lodger)
        self.btndelete_lodger.clicked.connect(self.delete_lodger)
        self.lodgers = LodgerModel(db.get_connection()).get_all()
        self.hotel_session.setText('\n'.join(['[x] ' + x[1] for x in self.lodgers]))
        self.rooms = RoomModel(db.get_connection()).get_all()
        self.hotel_session.setText('\n'.join(['[x] ' + x[1] for x in self.rooms]))

    def add_lodger(self):
        self.w1 = AddLodgerM(self.o)
        self.w1.show()
        self.lodgers = LodgerModel(db.get_connection()).get_all()
        self.hotel_session.setText('\n'.join(['[x] ' + x[1] for x in self.lodgers]))

    def delete_lodger(self):
        self.w1 = AddLodgerM()
        self.w1.show()

    def in_lodger(self):
        self.w1 = AddLodgerM()
        self.w1.show()

    def out_lodger(self):
        self.w1 = AddLodgerM()
        self.w1.show()


class LoginM(QMainWindow, Ui_Qlogin):
    def __init__(self):
        super(LoginM, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btnlogin.clicked.connect(self.auth)
        # self.settings_button.clicked.connect(self.show_settings)

    def auth(self):
        try:
            name = self.login.text()
            password = self.password.text()
            user_model = UserModel(db.get_connection())
            exists = user_model.exists(name, password)
            print(exists)
            if exists[0]:
                if exists[1][7] == 1:
                    self.w1 = AdminM(exists[1])
                    self.w1.show()
                    self.close()
                else:
                    self.w1 = ManagerM(exists[1])
                    self.w1.show()
                    self.close()
            else:
                self.change_status("Вы не зарегистрированны")

        except Exception as e:
            self.change_status(e)

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)


app = QApplication(sys.argv)
ex = LoginM()
ex.show()
sys.exit(app.exec_())
