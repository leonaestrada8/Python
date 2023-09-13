from datetime import datetime, timedelta

class DateManipulation:

    def __init__(self, date_str):
        self.date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    def add_days(self, days):
        self.date += timedelta(days=days)
        return self.date.strftime('%Y-%m-%d %H:%M:%S')

    def subtract_days(self, days):
        self.date -= timedelta(days=days)
        return self.date.strftime('%Y-%m-%d %H:%M:%S')

    def get_day_of_week(self):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days_of_week[self.date.weekday()]

import unittest


class TestDateManipulation(unittest.TestCase):

    def test_add_days(self):
        date_manipulation = DateManipulation('2023-08-16 00:00:00')
        self.assertEqual(date_manipulation.add_days(5), '2023-08-21 00:00:00')

    def test_subtract_days(self):
        date_manipulation = DateManipulation('2023-08-16 00:00:00')
        self.assertEqual(date_manipulation.subtract_days(3), '2023-08-13 00:00:00')

    def test_get_day_of_week(self):
        date_manipulation = DateManipulation('2023-08-16 00:00:00')
        self.assertEqual(date_manipulation.get_day_of_week(), 'Wednesday')

if __name__ == '__main__':
    unittest.main()
