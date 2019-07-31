import traceback
from datetime import datetime

from django.db import connection

class ScheduleRepo(object):

    def save(self, schedule, added_at):
        query = "INSERT INTO schedule VALUES(%i,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                print(query, [schedule.subject_id, schedule.day_no,schedule.start_time, schedule.end_time, schedule.class_no, added_at])
                cursor.execute(query, [schedule.subject_id, schedule.day_no, schedule.start_time, schedule.end_time, schedule.class_no, added_at])
                return True
        except Exception as e:
            traceback.print_exc()
            return False
