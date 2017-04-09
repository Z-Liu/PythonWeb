'''
Created on 2017Äê4ÔÂ5ÈÕ

@author: Administrator
'''
import unittest
from flask import current_app
from app import create_app,db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app=