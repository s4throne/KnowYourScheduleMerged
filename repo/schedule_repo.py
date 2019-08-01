import traceback
from datetime import datetime

from django.db import connection

from model.tabRow import TabRow


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

    def getTeacher(self, id):
        query = "SELECT first_name FROM teacher WHERE teacher_id=%i"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [id])
                row = cursor.fetchone()
                return row[0]
        except Exception as e:
            traceback.print_exc()
            return None

    def fetchScheduleAll(self, day):
        query = "SELECT teacher_id FROM teacher"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    table = list()
                    for row in rows:
                        tabRow = TabRow()
                        tabRow.teacher_name = self.getTeacher(row[0])
                        query = "SELECT subject_name, class_no, start_time FROM subject s INNER JOIN schedule sc ON s.subject_id=sc.subject_id WHERE teacher_id=%i"
                        cursor.execute(query, [row[0]])
                        lis = cursor.fetchall()
                        if lis is None:
                            return None
                        else:
                            for li in lis:
                                if li[2] == "11:00":
                                    tabRow.time1 = (li[0], li[1])
                                elif li[2] == "12:00":
                                    tabRow.time2 = (li[0], li[1])
                                elif li[2] == "01:00":
                                    tabRow.time3 = (li[0], li[1])
                                elif li[2] == "02:30":
                                    tabRow.time4 = (li[0], li[1])
                                elif li[2] == "3:30":
                                    tabRow.time5 = (li[0], li[1])
                        table.append(tabRow)
                    return table
        except Exception as e:
            traceback.print_exc()
            return False
