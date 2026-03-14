import os
import csv

import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.normpath(
    os.path.join(
        script_dir,
        '../../../homework/eugene_okulik/Lesson_16/hw_data/data.csv'
    )
)

missing_records = []

with open(file_path, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',')
    reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]
    print("Заголовки после нормализации:", reader.fieldnames)

    for row in reader:
        row = {k: (v.strip() if v else v) for k, v in row.items()}
        print("Обрабатывается строка:", row)

        query = """
            SELECT *
            FROM marks m
            JOIN students s ON m.student_id = s.id
            JOIN `groups` g ON s.group_id = g.id
            JOIN books b ON b.taken_by_student_id = s.id
            JOIN lessons l ON m.lesson_id = l.id
            JOIN subjects sub ON l.subject_id = sub.id
            WHERE s.name = %s
              AND s.second_name = %s
              AND g.title = %s
              AND b.title = %s
              AND sub.title = %s
              AND l.title = %s
              AND m.value = %s
        """
        cursor.execute(query, (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title'],
            row['mark_value']
        ))
        if cursor.fetchone() is None:
            missing_records.append(row)

db.close()

if missing_records:
    print("Следующие данные из CSV отсутствуют в базе данных:")
    for rec in missing_records:
        print(rec)
else:
    print("Все данные из CSV присутствуют в базе.")
