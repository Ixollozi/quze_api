from database.model import Question
from database import db


# Функция добавления вопроса -7 параметров
def add_question(main_text, var1, var2, var3, var4, correct_answer, level):
    new_question = Question(main_text=main_text, var1=var1, var2=var2,
                            var3=var3, var4=var4, correct_answer=correct_answer, level=level)
    db.session.add(new_question)
    db.session.commit()
# Вывести 20 вопросов - 1 параметр


def get_questions_db(level):
    show = Question.query.filter_by(level=level).all()
    return show[0:21]
# Проверка ответа пользователя


def check_answer(question_id, user_answer):
    question_id = Question.query.filter_by(question_id=question_id).first()
    if question_id.correct_answer == user_answer:
        return True
    else:
        return False
