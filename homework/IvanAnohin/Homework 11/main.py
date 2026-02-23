class Book:
    material = 'Бумага'
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


book1 = Book('Идиот', 'Достоевский', 500, '000-0-00-123456-1')
book2 = Book('Преступление и наказание', 'Достоевский', 600, '000-0-00-123456-2')
book3 = Book('Война и мир', 'Толстой', 1200, '000-0-00-123456-3')
book4 = Book('Анна Каренина', 'Толстой', 800, '000-0-00-123456-4')
book5 = Book('Мастер и Маргарита', 'Булгаков', 400, '000-0-00-123456-5')

book4.reserved = True

print('Книги:')
for book in [book1, book2, book3, book4, book5]:
    if book.reserved:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.pages}, материал: {book.material}, зарезервирована')
    else:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.pages}, материал: {book.material}')


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject, grade, has_tasks, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

sb1 = SchoolBook('Алгебра', 'Иванов', 200, '000-0-00-123456-9', 'Математика', 9, True)
sb2 = SchoolBook('История', 'Петров', 250, '000-0-00-123456-8', 'История', 5, True)
sb3 = SchoolBook('География', 'Сидоров', 180, '000-0-00-123456-7', 'География', 7, False)
sb4 = SchoolBook('Физика', 'Васильев', 300, '000-0-00-123456-6', 'Физика', 10, True)

sb4.reserved = True

print('Учебники:')
for sb in [sb1, sb2, sb3, sb4]:
    if sb.reserved:
        print(f'Название: {sb.title}, Автор: {sb.author}, страниц: {sb.pages}, предмет: {sb.subject}, класс: {sb.grade}, зарезервирована')
    else:
        print(f'Название: {sb.title}, Автор: {sb.author}, страниц: {sb.pages}, предмет: {sb.subject}, класс: {sb.grade}')
