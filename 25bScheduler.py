class Scheduler:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, date, description):
        self.appointments.append({"date": date, "description": description})

    def remove_appointment(self, index):
        self.appointments.pop(index)

    def get_appointment(self, index):
        return self.appointments[index]

    def list_appointments(self):
        return self.appointments


import unittest

class SchedulerTest(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_add_appointment(self):
        self.scheduler.add_appointment('2023-08-16', 'Meeting')
        self.assertEqual(self.scheduler.get_appointment(0), {'date': '2023-08-16', 'description': 'Meeting'})

    def test_remove_appointment(self):
        self.scheduler.add_appointment('2023-08-16', 'Meeting')
        self.scheduler.remove_appointment(0)
        self.assertEqual(self.scheduler.list_appointments(), [])

    def test_list_appointments(self):
        self.scheduler.add_appointment('2023-08-16', 'Meeting')
        self.scheduler.add_appointment('2023-08-17', 'Conference')
        self.assertEqual(self.scheduler.list_appointments(), [
            {'date': '2023-08-16', 'description': 'Meeting'},
            {'date': '2023-08-17', 'description': 'Conference'}
        ])

    def test_get_appointment(self):
        self.scheduler.add_appointment('2023-08-16', 'Meeting')
        self.assertEqual(self.scheduler.get_appointment(0), {'date': '2023-08-16', 'description': 'Meeting'})

if __name__ == '__main__':
    unittest.main()
