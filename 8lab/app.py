import psycopg2
import sys

import datetime

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox, QLabel,
                             QTableWidgetItem, QPushButton, QMessageBox)

# class AnotherWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.choose = QWidget()

#         self.monday_gbox = QGroupBox("Понедельник")
        
#         self.svbox = QVBoxLayout()
#         self.setWindowTitle("Выбрать день")

#         self.shbox1 = QHBoxLayout()
#         self.shbox2 = QHBoxLayout()
#         self.shbox3 = QHBoxLayout()

#         self.svbox.addLayout(self.shbox1)
#         self.svbox.addLayout(self.shbox2)
#         self.svbox.addLayout(self.shbox3)

#         self.new_row = QPushButton("Добавить")
#         self.shbox1.addWidget(self.new_row)
#         self.new_row.clicked.connect(self._update_shedule)

#         self.mon = QPushButton("Понедельник")
#         self.shbox1.addWidget(self.mon)
#         self.tue = QPushButton("Вторник")
#         self.shbox1.addWidget(self.tue)
#         self.wed = QPushButton("Среда")
#         self.shbox2.addWidget(self.wed)
#         self.thu = QPushButton("Четверг")
#         self.shbox2.addWidget(self.thu)
#         self.fri = QPushButton("Пятница")
#         self.shbox3.addWidget(self.fri)
#         self.sat = QPushButton("Суббота")
#         self.shbox3.addWidget(self.sat)

#         # self.mon.clicked.connect(self._update_shedule)

#         self.choose.setLayout(self.svbox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Редактор расписания")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)#создает структуру, которую можно заполнять вкладками
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()
        self._create_teachers_tab()
        self._create_subjects_tab() 

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="timetable",
                                     user="postgres",
                                     password="manta2",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_teachers_tab(self):
            self.teachers_tab = QWidget()
            self.tabs.addTab(self.teachers_tab, "Teachers")

            self.teachers_gbox = QGroupBox("Список преподавателей")

            self.svbox = QVBoxLayout()
            self.shbox1 = QHBoxLayout()
            self.shbox2 = QHBoxLayout()
            self.shbox3 = QHBoxLayout()

            self.svbox.addLayout(self.shbox1)
            self.svbox.addLayout(self.shbox2)
            self.svbox.addLayout(self.shbox3)

            self.new_row = QPushButton("Добавить")
            self.shbox1.addWidget(self.new_row)
            self.new_row.clicked.connect(self._add_teachers)#_add_subject

            self.shbox2.addWidget(self.teachers_gbox)
            self._create_teachers_table()

            self.update_teachers_button = QPushButton("Update")
            self.shbox3.addWidget(self.update_teachers_button)
            self.update_teachers_button.clicked.connect(self._update_teachers_table)

            self.teachers_tab.setLayout(self.svbox)

    def _create_subjects_tab(self):
            self.subjects_tab = QWidget()
            self.tabs.addTab(self.subjects_tab, "Subjects")

            self.subjects_gbox = QGroupBox("Список предметов")

            self.svbox = QVBoxLayout()
            self.shbox1 = QHBoxLayout()
            self.shbox2 = QHBoxLayout()
            self.shbox3 = QHBoxLayout()

            self.svbox.addLayout(self.shbox1)
            self.svbox.addLayout(self.shbox2)
            self.svbox.addLayout(self.shbox3)

            self.new_row = QPushButton("Добавить")
            self.shbox1.addWidget(self.new_row)
            self.new_row.clicked.connect(self._add_subjects)#_add_subject

            self.shbox2.addWidget(self.subjects_gbox)
            self._create_subjects_table()

            self.update_subjects_button = QPushButton("Update")
            self.shbox3.addWidget(self.update_subjects_button)
            self.update_subjects_button.clicked.connect(self._update_subjects_table)

            self.subjects_tab.setLayout(self.svbox)

    def _create_shedule_tab(self):
            self.shedule_tab = QWidget()
            self.tabs.addTab(self.shedule_tab, "Shedule")

            self.monday_gbox = QGroupBox("Понедельник")
            self.tuesday_gbox = QGroupBox("Вторник")
            self.wednesday_gbox = QGroupBox("Среда")
            self.thursday_gbox = QGroupBox("Четверг")
            self.friday_gbox = QGroupBox("Пятница")
            self.saturday_gbox = QGroupBox("Суббота")
            self.null_gbox = QGroupBox("")


            self.svbox = QVBoxLayout()
            self.shbox1 = QHBoxLayout()
            self.shbox11 = QHBoxLayout()
            self.shbox2 = QHBoxLayout()
            self.shbox22 = QHBoxLayout()
            self.shbox3 = QHBoxLayout()
            self.shbox33 = QHBoxLayout()
            self.shbox4 = QHBoxLayout()
            self.shbox5 = QHBoxLayout()

            self.svbox.addLayout(self.shbox1)
            self.svbox.addLayout(self.shbox11)
            self.svbox.addLayout(self.shbox2)
            self.svbox.addLayout(self.shbox22)
            self.svbox.addLayout(self.shbox3)
            self.svbox.addLayout(self.shbox33)
            self.svbox.addLayout(self.shbox4)
            self.svbox.addLayout(self.shbox5)
            

            self.choose_week1_button = QPushButton("Нечётная неделя")
            self.shbox1.addWidget(self.choose_week1_button)
            self.choose_week2_button = QPushButton("Чётная неделя")
            self.shbox1.addWidget(self.choose_week2_button)

            self.new_row1 = QPushButton("Добавить MON")
            self.shbox2.addWidget(self.new_row1)
            self.new_row1.clicked.connect(lambda ch, day = 1: self._add_shedule(day))
            self.new_row2 = QPushButton("Добавить THU")
            self.shbox2.addWidget(self.new_row2)
            self.new_row2.clicked.connect(lambda ch, day = 4: self._add_shedule(day))
            self.new_row3 = QPushButton("Добавить TUE")
            self.shbox3.addWidget(self.new_row3)
            self.new_row3.clicked.connect(lambda ch, day = 2: self._add_shedule(day))
            self.new_row4 = QPushButton("Добавить FRI")
            self.shbox3.addWidget(self.new_row4)
            self.new_row4.clicked.connect(lambda ch, day = 5: self._add_shedule(day))
            self.new_row5 = QPushButton("Добавить WED")
            self.shbox4.addWidget(self.new_row5)
            self.new_row5.clicked.connect(lambda ch, day = 3: self._add_shedule(day))
            self.new_row6 = QPushButton("Добавить SAT")
            self.shbox4.addWidget(self.new_row6)
            self.new_row6.clicked.connect(lambda ch, day = 6: self._add_shedule(day))
                # joinButton.clicked.connect(lambda ch, num=[i, r[2], r[3]]: self._change_teacher_from_table(num[0], num[1], num[2]))

            self.shbox11.addWidget(self.null_gbox)

            self.shbox22.addWidget(self.monday_gbox)
            self.shbox33.addWidget(self.tuesday_gbox)
            self.shbox5.addWidget(self.wednesday_gbox)
            self.shbox22.addWidget(self.thursday_gbox)
            self.shbox33.addWidget(self.friday_gbox)
            self.shbox5.addWidget(self.saturday_gbox)

            parity = 1
            if parity == 1:
                self._create_monday_table()
                self._create_tuesday_table()
                self._create_wednesday_table()
                self._create_thursday_table()
                self._create_friday_table()
                self._create_saturday_table()
            else:
                self._create_monday_table()
                self._create_tuesday_table()
                self._create_wednesday_table()
                self._create_thursday_table()
                self._create_friday_table()
                self._create_saturday_table()

            self.update_shedule_button = QPushButton("Update")
            self.shbox1.addWidget(self.update_shedule_button)
            self.update_shedule_button.clicked.connect(self._update_shedule)

            self.shedule_tab.setLayout(self.svbox)


    def _create_teachers_table(self):
            self.teachers_table = QTableWidget()
            self.teachers_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.teachers_table.setColumnCount(4)
            self.teachers_table.setHorizontalHeaderLabels(["Имя", "Предмет", "Обновить", "Удалить"])


            self._update_teachers_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.teachers_table)
            self.teachers_gbox.setLayout(self.mvbox)

    def _create_subjects_table(self):
            self.subjects_table = QTableWidget()
            self.subjects_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.subjects_table.setColumnCount(4)
            self.subjects_table.setHorizontalHeaderLabels(["№", "Предмет", "Обновить", "Удалить"])


            self._update_subjects_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.subjects_table)
            self.subjects_gbox.setLayout(self.mvbox)


    def _create_monday_table(self):
            self.monday_table = QTableWidget()
            self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.monday_table.setColumnCount(6)
            self.monday_table.setHorizontalHeaderLabels(["Предмет", "Аудитория", "Время", "Преподаватель", "Обновить", "Удалить"])

            self._update_monday_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.monday_table)
            self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
            self.tuesday_table = QTableWidget()
            self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.tuesday_table.setColumnCount(6)
            self.tuesday_table.setHorizontalHeaderLabels(["Предмет", "Аудитория", "Время", "Преподаватель", "Обновить", "Удалить"])

            self._update_tuesday_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.tuesday_table)
            self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
            self.wednesday_table = QTableWidget()
            self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.wednesday_table.setColumnCount(6)
            self.wednesday_table.setHorizontalHeaderLabels(["Предмет", "Аудитория", "Время", "Преподаватель", "Обновить", "Удалить"])

            self._update_wednesday_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.wednesday_table)
            self.wednesday_gbox.setLayout(self.mvbox)

    def _create_thursday_table(self):
            self.thursday_table = QTableWidget()
            self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.thursday_table.setColumnCount(6)
            self.thursday_table.setHorizontalHeaderLabels(["Предмет", "Аудитория", "Время", "Преподаватель", "Обновить", "Удалить"])

            self._update_thursday_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.thursday_table)
            self.thursday_gbox.setLayout(self.mvbox)

    def _create_friday_table(self):
            self.friday_table = QTableWidget()
            self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.friday_table.setColumnCount(6)
            self.friday_table.setHorizontalHeaderLabels(["Предмет", "Аудитория", "Время", "Преподаватель", "Обновить", "Удалить"])

            self._update_friday_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.friday_table)
            self.friday_gbox.setLayout(self.mvbox)

    def _create_saturday_table(self):
            self.saturday_table = QTableWidget()
            self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.saturday_table.setColumnCount(6)
            self.saturday_table.setHorizontalHeaderLabels(["Предмет", "Аудитория", "Время", "Преподаватель", "Обновить", "Удалить"])

            self._update_saturday_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.saturday_table)
            self.saturday_gbox.setLayout(self.mvbox)

    def _update_teachers_table(self):
            self.cursor.execute("SELECT teachers.full_name, subjects.name, teachers.id, subjects.id FROM teachers JOIN subjects ON subjects.id = teachers.subject;")
            records = list(self.cursor.fetchall())

            self.teachers_table.setRowCount(len(records) + 1) #можно отбросить + 1 если добавить кнопку с добавлением ряда

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.teachers_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.teachers_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.teachers_table.setCellWidget(i, 2, joinButton)
                self.teachers_table.setCellWidget(i, 3, deleteButton)
                # print(r[0], r[1], r[2], r[3])
                joinButton.clicked.connect(lambda ch, num=[i, r[2], r[3]]: self._change_teacher_from_table(num[0], num[1], num[2]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[2]]: self._delete_teacher_from_table(num[0], num[1]))

            self.teachers_table.resizeRowsToContents()
    
    def _update_subjects_table(self):
            self.cursor.execute("SELECT * FROM subjects;")
            records = list(self.cursor.fetchall())
# SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
# JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Пятница' AND timetable.parity = 1 ORDER BY start_time;

            a = list()
            for i in range (0, (len(records) + 1)):
                a.append("|")
                i = i + 1

            self.subjects_table.setRowCount(len(records) + 1) #можно отбросить + 1 если добавить кнопку с добавлением ряда
            self.subjects_table.setVerticalHeaderLabels(a)
            

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.subjects_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.subjects_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.subjects_table.setCellWidget(i, 2, joinButton)
                self.subjects_table.setCellWidget(i, 3, deleteButton)

                joinButton.clicked.connect(lambda ch, num=[i, r[0]]: self._change_subject_from_table(num[0], num[1]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[0]]: self._delete_subject_from_table(num[0], num[1]))

            self.subjects_table.resizeRowsToContents()

    def _add_teachers(self):
            self.cursor.execute("INSERT INTO teachers (full_name, subject) VALUES ('...', 13);")
            self.conn.commit()

            self._update_teachers_table()

    def _add_subjects(self):
            self.cursor.execute("INSERT INTO subjects (name) VALUES ('...');")
            self.conn.commit()

            self._update_subjects_table()

    def _add_shedule(self, day):
            if day == 1:
                self.cursor.execute("INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Понедельник', 1, 1, '-', '00:00');")
                self.conn.commit()

                self._update_monday_table()

            if day == 2:
                self.cursor.execute("INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Вторник', 1, 1, '-', '00:00');")
                self.conn.commit()

                self._update_tuesday_table()

            if day == 3:
                self.cursor.execute("INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Среда', 1, 1, '-', '00:00');")
                self.conn.commit()

                self._update_wednesday_table()

            if day == 4:
                # self.cursor.execute("INSERT INTO subjects (name) VALUES ('empty');")
                self.cursor.execute("INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Четверг', 1, 1, '-', '00:00');")
                self.conn.commit()

                self._update_thursday_table()

            if day == 5:
                self.cursor.execute("INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Пятница', 1, 1, '-', '00:00');")
                self.conn.commit()

                self._update_friday_table()

            if day == 6:
                self.cursor.execute("INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Суббота', 1, 1, '-', '00:00');")
                self.conn.commit()

                self._update_saturday_table()


    def _update_monday_table(self):
            self.cursor.execute("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name, timetable.id FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Понедельник' AND timetable.parity = 1 ORDER BY start_time;")
            records = list(self.cursor.fetchall())

            self.monday_table.setRowCount(len(records) + 1) #можно отбросить + 1 если добавить кнопку с добавлением ряда

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.monday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.monday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.monday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
                self.monday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
                self.monday_table.setCellWidget(i, 4, joinButton)
                self.monday_table.setCellWidget(i, 5, deleteButton)

                joinButton.clicked.connect(lambda ch, num=[i, r[4], r[2], 1]: self._change_day_from_table(num[0], num[1], num[2], num[3]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[4], 1]: self._delete_day_from_table(num[0], num[1], num[2]))

            self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
            self.cursor.execute("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name, timetable.id FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Вторник' AND timetable.parity = 1 ORDER BY start_time;")
            records = list(self.cursor.fetchall())

            self.tuesday_table.setRowCount(len(records) + 1)

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.tuesday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.tuesday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.tuesday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
                self.tuesday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
                self.tuesday_table.setCellWidget(i, 4, joinButton)
                self.tuesday_table.setCellWidget(i, 5, deleteButton)

                joinButton.clicked.connect(lambda ch, num=[i, r[4], r[2], 2]: self._change_day_from_table(num[0], num[1], num[2], num[3]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[4], 2]: self._delete_day_from_table(num[0], num[1], num[2]))

            self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
            self.cursor.execute("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name, timetable.id FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Среда' AND timetable.parity = 1 ORDER BY start_time;")
            records = list(self.cursor.fetchall())

            self.wednesday_table.setRowCount(len(records) + 1)

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.wednesday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.wednesday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.wednesday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
                self.wednesday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
                self.wednesday_table.setCellWidget(i, 4, joinButton)
                self.wednesday_table.setCellWidget(i, 5, deleteButton)

                joinButton.clicked.connect(lambda ch, num=[i, r[4], r[2], 3]: self._change_day_from_table(num[0], num[1], num[2], num[3]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[4], 3]: self._delete_day_from_table(num[0], num[1], num[2]))

            self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
            self.cursor.execute("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name, timetable.id FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Четверг' AND timetable.parity = 1 ORDER BY start_time;")
            records = list(self.cursor.fetchall())

        #     print(records)

            self.thursday_table.setRowCount(len(records) + 1)

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.thursday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.thursday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.thursday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
                self.thursday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
                self.thursday_table.setCellWidget(i, 4, joinButton)
                self.thursday_table.setCellWidget(i, 5, deleteButton)

                joinButton.clicked.connect(lambda ch, num=[i, r[4], r[2], 4]: self._change_day_from_table(num[0], num[1], num[2], num[3]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[4], 4]: self._delete_day_from_table(num[0], num[1], num[2]))

        #     self.thursday_table.setCellWidget(len(records) + 1, 4, joinButton)

            self.thursday_table.resizeRowsToContents()

    def _update_friday_table(self):
            self.cursor.execute("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name, timetable.id FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Пятница' AND timetable.parity = 1 ORDER BY start_time;")
            records = list(self.cursor.fetchall())

            self.friday_table.setRowCount(len(records) + 1)

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.friday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.friday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.friday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
                self.friday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
                self.friday_table.setCellWidget(i, 4, joinButton)
                self.friday_table.setCellWidget(i, 5, deleteButton)

                joinButton.clicked.connect(lambda ch, num=[i, r[4], r[2], 5]: self._change_day_from_table(num[0], num[1], num[2], num[3]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[4], 5]: self._delete_day_from_table(num[0], num[1], num[2]))

            self.friday_table.resizeRowsToContents()

    def _update_saturday_table(self):
            self.cursor.execute("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name, timetable.id FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Суббота' AND timetable.parity = 1 ORDER BY start_time;")
            records = list(self.cursor.fetchall())

            self.saturday_table.setRowCount(len(records) + 1)

            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Join")
                deleteButton = QPushButton("Delete")
                self.saturday_table.setItem(i, 0,
                                        QTableWidgetItem(str(r[0])))
                self.saturday_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[1])))
                self.saturday_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
                self.saturday_table.setItem(i, 3,
                                        QTableWidgetItem(str(r[3])))
                self.saturday_table.setCellWidget(i, 4, joinButton)
                self.saturday_table.setCellWidget(i, 5, deleteButton)

                self.saturday_table.setCellWidget(len(records) + 1, 4, joinButton)

                joinButton.clicked.connect(lambda ch, num=[i, r[4], r[2], 6]: self._change_day_from_table(num[0], num[1], num[2], num[3]))
                deleteButton.clicked.connect(lambda ch, num=[i, r[4], 6]: self._delete_day_from_table(num[0], num[1], num[2]))

            self.saturday_table.resizeRowsToContents()
    

#     def _add_shedule(self):
#         #     self.saturday_table.setCellWidget(i, 4, joinButton)

    def _change_day_from_table(self, rowNum, timetable_id, time_now, the_day):
            row = list()
            if the_day == 1:
                for i in range(self.monday_table.columnCount()):
                        try:
                                row.append(self.monday_table.item(rowNum, i).text())
                        except:
                                row.append(None)
            if the_day == 2:
                for i in range(self.tuesday_table.columnCount()):
                        try:
                                row.append(self.tuesday_table.item(rowNum, i).text())
                        except:
                                row.append(None)   
            if the_day == 3:
                for i in range(self.wednesday_table.columnCount()):
                        try:
                                row.append(self.wednesday_table.item(rowNum, i).text())
                        except:
                                row.append(None)
            if the_day == 4:
                for i in range(self.thursday_table.columnCount()):
                        try:
                                row.append(self.thursday_table.item(rowNum, i).text())
                        except:
                                row.append(None) 
            if the_day == 5:
                for i in range(self.friday_table.columnCount()):
                        try:
                                row.append(self.friday_table.item(rowNum, i).text())
                        except:
                                row.append(None)
            if the_day == 6:
                for i in range(self.saturday_table.columnCount()):
                        try:
                                row.append(self.saturday_table.item(rowNum, i).text())
                        except:
                                row.append(None)    


            self.cursor.execute("SELECT * FROM subjects WHERE subjects.name = '%s';" % (row[0]))
            records1 = list(self.cursor.fetchall())
            if not records1:
                  QMessageBox.about(self, "Error", "subject")
            else:  
                sub_id = records1[0][0]
                self.cursor.execute("UPDATE timetable SET subject ='%d', room_numb = '%s' WHERE id = '%d';" % (sub_id, row[1], timetable_id))
                self.cursor.execute("UPDATE teachers SET full_name = '%s' WHERE subject = '%d';" % (row[3], sub_id))#, start_time = '%s' row[2], 
                if row[2] != time_now:
                        time = datetime.datetime.strptime(row[2], '%H:%M:%S')
                        # QMessageBox.about(self, "Not Error", "time \n%s\n%s " % (time, timetable_id))
                        self.cursor.execute("UPDATE timetable SET start_time = '%s' WHERE id = '%d';" % (time, timetable_id))#!!!!!, start_time = '%s' row[2], 
                else: 
                        QMessageBox.about(self, "Error", "time \n%s" % (time_now))
                self.conn.commit()

    def _delete_day_from_table(self, rowNum, timetable_id, the_day):
            if the_day == 1:
                self.monday_table.removeRow(rowNum)
            if the_day == 2:
                self.tuesday_table.removeRow(rowNum)
            if the_day == 3:
                self.wednesday_table.removeRow(rowNum)
            if the_day == 4:
                self.thursday_table.removeRow(rowNum)
            if the_day == 5:
                self.friday_table.removeRow(rowNum)
            if the_day == 6:
                self.saturday_table.removeRow(rowNum)

            self.cursor.execute("DELETE FROM timetable WHERE id = %d;" % (timetable_id))
            self.conn.commit()

    def _change_subject_from_table(self, rowNum, sub_id):
            row = list()
            for i in range(self.subjects_table.columnCount()):
                try:
                        row.append(self.subjects_table.item(rowNum, i).text())
                except:
                        row.append(None)    
        #     self.cursor.execute("SELECT * FROM subjects WHERE subjects.name = '%s';" % (row[1]))
        #     records1 = list(self.cursor.fetchall())
        #     if not records1:
        #           QMessageBox.about(self, "Error", "subject")
        #     else:  
            self.cursor.execute("UPDATE subjects SET name ='%s' WHERE id = '%d';" % (row[1], sub_id))

            self.conn.commit()

    def _delete_subject_from_table(self, rowNum, sub_id):
            self.subjects_table.removeRow(rowNum)
            self.cursor.execute("DELETE FROM subjects WHERE id = %d;" % (sub_id))
            self.conn.commit()         
                
    def _change_teacher_from_table(self, rowNum, teacher_id, sub_id):
            row = list()
            for i in range(self.teachers_table.columnCount()):
                try:
                        row.append(self.teachers_table.item(rowNum, i).text())
                except:
                        row.append(None)    
            self.cursor.execute("SELECT * FROM subjects WHERE subjects.name = '%s';" % (row[1]))
            records1 = list(self.cursor.fetchall())
            if not records1:
                  QMessageBox.about(self, "Error", "subject")
            else:  
                # self.cursor.execute("UPDATE subjects SET full_name = '%s', subject ='%s' WHERE id = '%d';" % (row[1], sub_id))
                # print(row[0], sub_id, teacher_id)
                self.cursor.execute("UPDATE teachers SET full_name = '%s', subject ='%d' WHERE id = '%d';" % (row[0], sub_id, teacher_id))

                self.conn.commit()

    def _delete_teacher_from_table(self, rowNum, teacher_id):
            self.teachers_table.removeRow(rowNum)
            self.cursor.execute("DELETE FROM teachers WHERE id = %d;" % (teacher_id))

            self.conn.commit()          


    def _update_shedule(self):
            self._update_monday_table()
            self._update_tuesday_table()
            self._update_wednesday_table()
            self._update_thursday_table()
            self._update_friday_table()
            self._update_saturday_table()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
# четность недели
# сокращение кода!! каскадное удаление посредством триггера внутри бд
# дизаен
# 