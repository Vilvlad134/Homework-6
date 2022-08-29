# Homework 6

# Task#1
class Student:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

# Task 2
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Task 3
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение невозможно: один из студентов не значится в списках')
            return
        return self.average_rating < other.average_rating

# Task 3
    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя студента: {self.name}\n' \
              f'Фамилия студента: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating}\n' \
              f'Курсы обучения текущие: {courses_in_progress_string}\n' \
              f'Курсы обучения завершённые: {finished_courses_string}'
        return res

# Task 1
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Task 1
class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

# Task 3
    def __str__(self):
        grades_count = 0
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя лектора: {self.name}\nФамилия лектора: {self.surname}\nСредняя оценка лектора за занятия: {self.average_rating}'
        return res

# Task 3
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение невозможно: один из лекторов не значится в списках')
            return
        return self.average_rating < other.average_rating

# Task 1
class Reviewer(Mentor):

# Task 2    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Task 3
    def __str__(self):
        res = f'Имя проверяющего: {self.name}\nФамилия проверяющего: {self.surname}'
        return res

# Task 4
# Создание лекторов
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Пётр', 'Васильев')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Иван', 'Родионов')
lecturer_3.courses_attached += ['Python']

# Создание проверяющих
reviewer_1 = Reviewer('Олег', 'Савельев')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Владилен', 'Иванов')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

# Создание студентов
student_1 = Student('Денис', 'Судаков')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Роман', 'Миронов')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Владимир', 'Петров')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Выставление оценок лекторам
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_1.rate_hw(lecturer_2, 'Python', 5)
student_1.rate_hw(lecturer_2, 'Python', 7)
student_1.rate_hw(lecturer_2, 'Python', 8)

student_1.rate_hw(lecturer_1, 'Python', 7)
student_1.rate_hw(lecturer_1, 'Python', 8)
student_1.rate_hw(lecturer_1, 'Python', 9)

student_2.rate_hw(lecturer_2, 'Java', 10)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 9)

student_3.rate_hw(lecturer_3, 'Python', 5)
student_3.rate_hw(lecturer_3, 'Python', 6)
student_3.rate_hw(lecturer_3, 'Python', 7)

# Выставление оценок студентам
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 9)

reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 7)
reviewer_2.rate_hw(student_3, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 7)
reviewer_2.rate_hw(student_3, 'Python', 9)

# Вывод перечня студентов
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Вывод перечня лекторов
print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()
print()

# Сравнение студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
    f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2}')
print()

# Сравнение лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
    f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 < lecturer_2}')
print()

# Создаём списки студентов и лекторов
student_list = [student_1, student_2, student_3]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

# Task 4
def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list:
        if student.courses_in_progress == [course_name]:
            sum_all += student.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Task 4
def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course_name]:
            sum_all += lecturer.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекторам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()