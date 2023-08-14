from database import db
from database.model import Leadres
from database.model import User_anwers

# ЗАПИСЬ РЕЗУЛЬТАТА ТЕСТА


def user_end_test_db(user_id, correct_answer, level):
    exact_users_score = Leadres.query.filter_by(user_id, level=level).first()

    # проверить если что то внутри базы
    if exact_users_score:
        # к старым очкам добавить текущие
        exact_users_score.score += correct_answer
        db.session.commit()
    # если не было пользователя
    else:
        # создаем запись в базе данных
        new_leader_data = Leadres(user_id=user_id, level=level,
                                  score=correct_answer).order_by(Leadres.score.desc()).all()
        db.session.add(new_leader_data)
        db.session.commit()

    return True

# вывод лидеров из конретных уровней


def get_top_5_leaders(level):
    exact_level_leaders = Leadres.query.filter_by(level=level)
    return exact_level_leaders[:6]


def add_user_answer_db(user_id, question_id, user_answer, correctness):
    new_answer = User_anwers(user_id=user_id,
                             question_id=question_id,
                             user_answer=user_answer,
                             correctness=correctness)

    db.session.add(new_answer)
    db.session.commit()
