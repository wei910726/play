from django.test import TestCase
import unittest
from datetime import datetime
import requests
# Create your tests here.


class Tlogin(unittest.TestCase):
    def setUp(self):
        print("Start test")

    def Test_right(self):
        payload = {
            'username': 'aaa',
            'password': 'cdcd1234',
            'is_superuser': False,
            'is_active': True,
            'is_staff': True,
            'date_joined': datetime.now()
        }
        r = requests.post(url="http://localhost:8000/signin/", data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "add user success")

    def Test_d_exists(self):
        payload = {
            'username': 'gab',
            'password': 'pypy1234',
            'is_superuser': False,
            'is_active': True,
            'is_staff': True,
            'date_joined': datetime.now()
        }
        r = requests.post(url="http://localhost:8000/signin/", data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10005)
        self.assertEqual(result['message', "user has already exists"])

    def Test_getc(self):
        payload = {
            'cust_id': 2,
        }
        r = requests.post(url="http://localhost:8000/get_credit/", data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['data']['credit_value'], 600)

    def Test_addc(self):
        payload = {
            'cust_id': 2,
            'credit_value': 400
        }
        r = requests.post(url="http://localhost:8000/add_credit/", data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "add credit success")

    def Test_delc(self):
        payload = {
            'cust_id': 2,
        }
        r = requests.post(url="http://localhost:8000/delete_credit/", data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "delete credit success")

    def Test_alter(self):
        payload = {
            'cust_id': 2,
            'credit_value': 600
        }
        r = requests.post(url="http://localhost:8000/alter_credit/", data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "alter credit success")
