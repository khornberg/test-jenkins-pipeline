from django.test import TestCase
import time


class App1Tests(TestCase):

    def test_app1_one(self):
        self.assertEqual(1, 1)

    def test_app1_long(self):
        time.sleep(60)
        self.assertEqual(True, True)
