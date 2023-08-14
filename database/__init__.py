from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# импорт все функции из файлов для бд
from database.leaderservice import *
from database.questionservice import *
from database.model import *
from database.registrationservice import *
