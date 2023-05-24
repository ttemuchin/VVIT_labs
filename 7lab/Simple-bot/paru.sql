INSERT INTO subjects (name) VALUES ('Высшая математика');
INSERT INTO subjects (name) VALUES ('История');
INSERT INTO subjects (name) VALUES ('Физика');
INSERT INTO subjects (name) VALUES ('Математические основы баз данных');
INSERT INTO subjects (name) VALUES ('Игровые виды спорта');
INSERT INTO subjects (name) VALUES ('Иностранный язык');
INSERT INTO subjects (name) VALUES ('Основы Devops');
INSERT INTO subjects (name) VALUES ('Введение в информационные технологии');
INSERT INTO subjects (name) VALUES ('Проектный практикум');
\! chcp 1251
INSERT INTO teachers (full_name, subject) VALUES ('Шаймарданова Л. К.', 1);
INSERT INTO teachers (full_name, subject) VALUES ('Скляр Л. Н.', 2);
INSERT INTO teachers (full_name, subject) VALUES ('Вальковский С. Н.', 3);
INSERT INTO teachers (full_name, subject) VALUES ('Полищук Ю. В.', 4);
INSERT INTO teachers (full_name, subject) VALUES ('Волохова С. В.', 5);
INSERT INTO teachers (full_name, subject) VALUES ('Воронова Е. В.', 6);
INSERT INTO teachers (full_name, subject) VALUES ('Липатов В. Н.', 7);
INSERT INTO teachers (full_name, subject) VALUES ('Фурлетов Ю. М.', 8);
INSERT INTO teachers (full_name, subject) VALUES ('Потапченко Т. Д.', 9);
..
INSERT INTO teachers (full_name, subject) VALUES ('Файзулаев', 3);
INSERT INTO teachers (full_name, subject) VALUES ('Тренин А. Е.', 3);
еще изотова

..
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Понедельник', 2, 1, 'Н-514', '11:20');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Понедельник', 2, 2, 'Н-316', '13:10');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Понедельник', 2, 3, 'Н-340', '15:25');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Понедельник', 2, 4, 'Н-519', '17:15');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Среда', 2, 9, 'А-Л-208', '9:30');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Среда', 2, 7, 'А-ВЦ-302', '11:20');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Среда', 2, 7, 'А-414', '13:10');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Четверг', 2, 8, 'А-Л-205', '9:30');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Четверг', 2, 8, 'А-Л-205', '11:20');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Пятница', 2, 1, 'Н-330а', '11:20');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Пятница', 2, 5, 'Н-С-Зал', '13:10');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Понедельник', 1, 5, 'Н-С-Зал', '9:30');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Понедельник', 1, 6, 'Н-322', '11:20');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Вторник', 1, 6, 'Н-405', '11:20');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Вторник', 1, 3, 'Н-322а', '13:10');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Вторник', 1, 2, 'Н-404', '15:25');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Среда', 1, 1, 'Н-324', '11:20');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Среда', 1, 1, 'Н-514', '13:10');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Среда', 1, 3, 'Н-226', '15:25');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Четверг', 1, 8, 'А-Л-203', '9:30');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Четверг', 1, 7, 'А-ВЦ-206', '11:20');

INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Пятница', 1, 2, 'Н-227', '9:30');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Пятница', 1, 4, 'Н-535', '11:20');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Пятница', 1, 5, 'Н-С-Зал', '13:10');
INSERT INTO timetable (day, parity, subject, room_numb, start_time) VALUES ('Пятница', 1, 4, 'Н-410', '15:25');

INSERT INTO timetable (day, parity, room_numb, start_time) VALUES ('Суббота', 1, '-', '00:00');
INSERT INTO timetable (day, parity, room_numb, start_time) VALUES ('Суббота', 2, '-', '00:00');

ЗАПРОСЫ

день 
предмет кабинет время препод
SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Пятница' AND timetable.parity = 1 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Пятница' AND timetable.parity = 2 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Четверг' AND timetable.parity = 1 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Четверг' AND timetable.parity = 2 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Среда' AND timetable.parity = 1 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Среда' AND timetable.parity = 2 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Вторник' AND timetable.parity = 1 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Вторник' AND timetable.parity = 2 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Понедельник' AND timetable.parity = 1 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Понедельник' AND timetable.parity = 2 ORDER BY start_time;

SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject)
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.parity = 2 GROUP BY day ORDER BY start_time;



SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) 
JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Понедельник' AND timetable.parity = 1 ;


ORDER BY start_time
, timetable.id



Чтобы получить текущую дату и время используется функция NOW ().
Пример:
SELECT NOW ().
Результат: 2015-09-25 14:42:53.
Для получения только текущей даты есть функция CURDATE ().
Пример:
SELECT CURDATE ()
Результат: 2015-09-25.
И функция CURTIME (), которая возвращает только текущее время:
Пример:
SELECT CURTIME ()
Результат: 14:42:53.