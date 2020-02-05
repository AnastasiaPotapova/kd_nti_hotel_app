class Admin:
    def __init__(self, cinema, name, x, y, films=None): #имя фамилия отчество отельк которму привязан
        self.cinema = cinema
        self.name = name
        self.films = films[:] if films else []
        self.x = x
        self.y = y

    def append(self, film_name, film_time): #отправка на сервер заселение + документ
        self.films.append(
            Film(film_name, film_time, self.name, self.cinema, self.x, self.y))

    def show_name(self): #отправка на сервер выселение + документ
        return self.name

    def spisok(self): #создание постояльца
        return [x.show_name() for x in self.films]

    def time_spisok(self): #удаление постояльца
        return [x.show_time() for x in self.films]

    def __getitem__(self, item): #создание цсв документа
        return self.films[item]
    # редактирование постояльца
    # Добавлять изменять и редактировать номера гостиницы


class Manager:
    def __init__(self, name='-', a=None): #
        self.name = name
        self.rooms = a[:] if a else []

    def append(self, room_name, x=5, y=5): #создавать, редактировать, удалять отели
        self.rooms.append(Room(self.name, room_name, x, y))

    def show_name(self): #создавать, редактировать, удалять админов
        return self.name

    def spisok(self):
        return [x.show_name() for x in self.rooms]

    def __getitem__(self, item):
        return self.rooms[item]