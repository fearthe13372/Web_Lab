groupmates = [
    {
        "name": "Алексей",
        "surname": "Сазонов",
        "exams": ["Высшмат","web","ИН"],
        "marks": [4, 2, 5]
    },
    {
        "name": "Дарья",
        "surname": "Гердт",
        "exams": ["ЭИЭС", "АиГ", "wEB"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Иванов",
        "exams": ["Философия", "Рус", "ИКГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Виктор",
        "surname": "Прокопьев",
        "exams": ["WEB", "ЭИЭ", "ИКГ"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Елена",
        "surname": "Соколова",
        "exams": ["АиГ", "История", "ИНО"],
        "marks": [2, 3, 3]
    },
    {
		"name": "Вася",
		"surname": "Гурунов",
		"exams": ["Философия","КТП","ИС"],
		"marks": [4,4,3]
	},
	{
		"name": "Даниил",
		"surname": "Праченко",
		"exams": ["КТП","ИС","Философия"],
		"marks": [3,3,3]
	}
]

def filter_students(students, middle):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(20), u"Средний балл".ljust(15))
    for student in students:
        sum = 0
        for mark in student["marks"]:
            sum += mark
        average = sum / len(student["marks"])
        if (round(average, 2) > middle):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35), str(student["marks"]).ljust(20), str(round(average, 2)).ljust(15))

mid = float(input("средний балл: "))

filter_students(groupmates, mid)
