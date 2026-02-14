from django.test import TestCase
from django.contrib.auth.hashers import make_password
from .grading import *

class TestHashedFlags(TestCase):
    
    def test_correct(self):
    
        flag = r"flag{Th1s_1s_th3_f1rs7_FlA6}"
        
        hashed = make_password(flag)

        cross_fingers = check_flag(flag, hashed)

        self.assertTrue(cross_fingers)

    def test_wrong(self):
    
        flag = r"flag{Th1s_1s_th3_f1rs7_FlA6}"
        
        hashed = make_password(flag)

        cross_fingers = check_flag("wrong", hashed)

        self.assertFalse(cross_fingers)

        
# Create your tests here.
