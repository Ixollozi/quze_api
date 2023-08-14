from database.model import User
from database import db

# функция регистрации пользователя


def register_user_db(name, phone_number):
    # проверка пользоветля на наличие в базе
    chekcer = User.query.filter_by(phone_number=phone_number).first()
    # если есть пользователь
    if chekcer:
        return chekcer.id
    # добавление данных в базу
    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()
    return new_user.id
