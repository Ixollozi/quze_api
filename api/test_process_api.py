from api import api_bp
from database import get_questions_db, check_answer, user_end_test_db
# url для получения запросов


@api_bp.route('/get-questions/<int:level>', methods=['GET'])
def get_questions(level: int):
    result = get_questions_db(level)
    return {'status': 1, 'questions': result}


@api_bp.route('/check-answer/<int:question_id>/<int:user_answer>', methods=['POST'])
def check_user_answer(question_id: int, user_answer: int):
    result = check_answer(question_id, user_answer)
    if result:
        return {'status': 1}
    else:
        return {'status': 0}


# url для завершения и получения результата теста


@api_bp.route('/done/<int:user_id>/<int:correct_answer>/<int:level>', methods=['POST'])
def commit_user_answers(user_id: int, correct_answer: int, level: int):
    result = user_end_test_db(user_id, correct_answer, level)
    return {'status': 1, 'correct_answer': correct_answer, 'top': result}
