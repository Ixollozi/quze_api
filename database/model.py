from database import db
# пользователи


class User(db.Model):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.String, unique=True)

# таблица лидеров


class Leadres(db.Model):
    __tablename__ = 'leaders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    level = db.Column(db.Integer, nulable=False)
    score = db.Column(db.Integer, nulable=False)

    user_fk = db.relationship(User)

# таблица вопрсов


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    main_text = db.Column(db.String, nulable=False)
    var1 = db.Column(db.String, nulable=False)
    var2 = db.Column(db.String, nulable=False)
    var3 = db.Column(db.String)
    var4 = db.Column(db.String)
    correct_answer = db.Column(db.Integer, nulable=False)
    level = db.Column(db.Intger, nulable=False)

# таблица ответов пользователей на вопросы


class User_anwers(db.Model):
    __tablename__ = 'user_answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Intger, db.ForeignKey('users.id'), nulable=False)
    question_id = db.Column(db.Intger, db.ForeignKey('question.id'), nulable=False)
    user_answer = db.Column(db.Intger, nulable=False)
    correctness = db.Column(db.Boolean, default=False)

    user_fk = db.relationship(User)
    question_fk = db.relationship(Question)
