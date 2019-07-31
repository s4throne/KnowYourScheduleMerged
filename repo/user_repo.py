from django.db import connection
import traceback

from model.teacher import Teacher
from model.user import User


class UserRepo(object):


    def signin(self, email):
        query = "SELECT teacher_id, first_name, email, password FROM teacher WHERE email = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [email])
                row = cursor.fetchone()
                if row is None:
                    return None
                else:
                    teacher = Teacher()
                    teacher.teacher_id = row[0]
                    teacher.first_name = row[1]
                    teacher.email = row[2]
                    return {"teacher": teacher, "password": row[3]}
        except Exception:
            traceback.print_exc()
            return None

    # def save(self, user, password):
    #     query = "INSERT INTO user(user_id, full_name, email, password, created_at) VALUES(%s,%s,%s,%s,%s)"
    #     try:
    #         with connection.cursor() as cursor:
    #             cursor.execute(query, [user.user_id, user.full_name, user.email, password, user.created_at])
    #             return True
    #     except Exception:
    #         traceback.print_exc()
    #         return False