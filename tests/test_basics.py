'''
Created on 2017��4��5��

@author: Administrator
'''
import unittest
from flask import current_app
from app import create_app,db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app=