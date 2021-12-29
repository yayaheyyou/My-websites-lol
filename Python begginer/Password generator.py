
import math
import random
import string
import pip
import functools 
import sys


Numbers1 = str(random.randint(0, 100))
Numbers2 = str(random.randint(0, 100))
Numbers3 = str(random.randint(0, 100))
Numbers4 = str(random.randint(0, 100))

Characters = string.ascii_letters

Letters =  ''.join(random.choice(Characters) for i in range(10)) 

Password = Numbers2 + Letters + Numbers1

print(Password)
