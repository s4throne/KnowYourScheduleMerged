import traceback

from django.db import connection


class SubjectRepo(object):

    def fetch_subjects(self):
        query = "SELECT subject_id, subject_name FROM subject ORDER BY subject_id"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    subjects = list()
                    for row in rows:
                        subject = {"name": row[1], "id": row[0]}
                        subjects.append(subject)
                return subjects
        except Exception as e:
            traceback.print_exc()
            return None

