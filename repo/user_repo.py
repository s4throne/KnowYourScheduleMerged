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
                    return {"user": teacher, "password": row[3]}
        except Exception:
            traceback.print_exc()
            return None

    def save(self, user, confirmation, time):
        query = "INSERT INTO teacher (first_name, last_name, email, confirm_code, confirmed, added_at) VALUES(%s,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [user.first_name, user.last_name, user.email, confirmation, False, time])
                return True
        except Exception:
            traceback.print_exc()
            return False

    def register(self, email, confirmation, password):
        query = "SELECT COUNT(*) FROM teacher WHERE email= %s AND confirm_code = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [email, confirmation])
                row = cursor.fetchone()

                if row is None:
                    return False
                else:
                    if row[0] == 1:
                        query = "UPDATE teacher SET password = %s, confirm_code = %s, confirmed=%s WHERE email=%s"
                        cursor.execute(query, [password,"",True,email])
                        return True
                    else:
                        return False
        except Exception:
            traceback.print_exc()
            return False

