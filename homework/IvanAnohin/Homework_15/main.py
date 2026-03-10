import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ('Ivan', 'Ivanich')
)
student_id = cursor.lastrowid
print(f"Добавлен студент с ID: {student_id}")

cursor.execute(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s), (%s, %s)",
    ('Евгений Онегин', student_id, 'Война и мир', student_id)
)
print("Книги добавлены и выданы студенту.")

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ('Группа №1', '2006-09-01', '2007-05-01')
)
group_id = cursor.lastrowid
print(f"Добавлена группа с ID: {group_id}")

cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)
print(f"Студент {student_id} назначен в группу {group_id}.")

cursor.execute(
    "INSERT INTO subjects (title) VALUES (%s), (%s)",
    ('Математика', 'Физика')
)
cursor.execute("SELECT id, title FROM subjects WHERE title IN ('Математика', 'Физика')")
subjects = cursor.fetchall()
subject_ids = {row['title']: row['id'] for row in subjects}
print(
    f"Добавлены предметы: Математика (ID {subject_ids['Математика']}), "
    f"Физика (ID {subject_ids['Физика']})"
)

lessons_data = [
    (subject_ids['Математика'], 'Пределы функций'),
    (subject_ids['Математика'], 'Производные'),
    (subject_ids['Физика'], 'Кинематика'),
    (subject_ids['Физика'], 'Динамика')
]
lesson_ids = {}
for subject_id, title in lessons_data:
    cursor.execute(
        "INSERT INTO lessons (subject_id, title) VALUES (%s, %s)",
        (subject_id, title)
    )
    lesson_ids[title] = cursor.lastrowid
print("Уроки добавлены.")

marks_data = [
    (student_id, lesson_ids['Пределы функций'], 4),
    (student_id, lesson_ids['Производные'], 5),
    (student_id, lesson_ids['Кинематика'], 3),
    (student_id, lesson_ids['Динамика'], 4)
]
for student_id, lesson_id, value in marks_data:
    cursor.execute(
        "INSERT INTO marks (student_id, lesson_id, value) VALUES (%s, %s, %s)",
        (student_id, lesson_id, value)
    )
print("Оценки добавлены.")

db.commit()

print("\nОценки студента")
cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
for mark in cursor.fetchall():
    print(f"Урок ID {mark['lesson_id']}, оценка {mark['value']}")

print("\nКниги студента")
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
for book in cursor.fetchall():
    print(f"Книга: {book['title']}")

print("\nИтоговый отчёт")
query_report = """
    SELECT
        s.name AS student_name,
        s.second_name AS student_second_name,
        g.title AS group_name,
        b.title AS book_title,
        m.value AS mark,
        sub.title AS subject_name,
        l.title AS lesson_title
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON s.id = b.taken_by_student_id
    LEFT JOIN marks m ON s.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects sub ON l.subject_id = sub.id
    WHERE s.id = %s
    ORDER BY subject_name, lesson_title
"""
cursor.execute(query_report, (student_id,))
for row in cursor.fetchall():
    print(
        f"{row['student_name']} {row['student_second_name']}, "
        f"группа {row['group_name']}, "
        f"книга '{row['book_title']}', "
        f"предмет {row['subject_name']}, урок {row['lesson_title']}, оценка {row['mark']}"
    )

db.close()
