from django.test import TestCase
import time


class App2Tests(TestCase):

    def test_app2_one(self):
        self.assertEqual(2, 2)

    def test_app2_long(self):
        time.sleep(10)
        self.assertEqual(True, True)
