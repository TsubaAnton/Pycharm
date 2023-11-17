# Добавляем библиотеку random
import random

# Добавляем вопросы
json_data = [{
    "q": "How many days do we have in a week?",
    "d": "1",
    "a": "7"
}, {
    "q": "How many letters are there in the English alphabet?",
    "d": "3",
    "a": "26"
}, {
    "q": "How many sides are there in a triangle?",
    "d": "2",
    "a": "3"
}, {
    "q": "How many years are there in one Millennium?",
    "d": "2",
    "a": "1000"
}, {
    "q": "How many sides does hexagon have?",
    "d": "4",
    "a": "6"
}]


# Создаем класс Question
class Question():

    def __init__(self, question_text, difficulty, correct_answer):
        """Создает поля класса"""
        self.question_text = question_text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.asked = False
        self.user_answer = None
        self.get_points()

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        if self.difficulty == 1:
            self.points_question = 10
        elif self.difficulty == 2:
            self.points_question = 20
        elif self.difficulty == 3:
            self.points_question = 30
        elif self.difficulty == 4:
            self.points_question = 40
        elif self.difficulty == 5:
            self.points_question = 50

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if self.user_answer == self.correct_answer:
            return True
        return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question_text}\nСложность {self.difficulty}/5"

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f"Ответ верный, получено {self.points_question} баллов"

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f"Ответ неверный, верный ответ {self.correct_answer}"


def questions_json(json_data):
    """Создает список экземпляров класса"""
    random.shuffle(json_data)
    questions = []
    for data in json_data:
        question = Question(data["q"], int(data["d"]), data["a"])
        questions.append(question)
    return questions


def test(questions):
    """По очереди задает вопросы"""
    good_answer = 0
    points = 0
    for question in questions:
        print(f"Вопрос: {question.build_question()}")
        user_answer = input()
        question.user_answer = user_answer
        if question.is_correct():
            good_answer += 1
            points += question.points_question
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())
    final = (good_answer, points)
    return final


def statistics(questions):
    """Выводит статистику игры"""
    results = test(questions)
    good_answer, points = results
    print(f'''Вот и все!
Отвечено {good_answer} вопроса из {len(questions)}
Набрано баллов: {points}''')

# Запускает игру
input("Игра начинается")
# Создает список экземпляров класса
questions = questions_json(json_data)
# Выводит статистику игры
statistics(questions)


