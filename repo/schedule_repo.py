import traceback
from datetime import datetime

from django.db import connection

class ScheduleRepo(object):

    def save(self, schedule, created_at):
        query = "INSERT INTO schedule(subject_id, day_no, start_time, end_time, class_no, added_at) VALUES(%s,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [schedule.subject_id, schedule.day_no, schedule.start_time, schedule.end_time,schedule.class_no, created_at])
                return True
        except Exception as e:
            traceback.print_exc()
            return False
