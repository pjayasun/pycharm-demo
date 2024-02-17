# Abdul Bari

import os
import time

print(os.path.exists("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions"))
print(os.path.isfile("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/calc.py"))

print(os.path.split("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/calc.py"))
print(os.path.join("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions", "calc.py"))

print(os.path.basename("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/calc.py"))
print(os.path.dirname("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/calc.py"))

print(time.ctime(os.path.getmtime("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/Factorial.py")))
print(time.ctime(os.path.getatime("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/Factorial.py")))

print(os.path.relpath("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/Factorial.py"))
print(os.path.abspath("/Users/praneshjayasundar/PycharmProjects/LearnPython/src/Functions/Factorial.py"))