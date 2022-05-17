from operator import index
from read_user_info import *


number = 0
personal_code = 0
car_years = 0
for data in auto_user_info["auto_user"]:
    if data == "number":
       number = auto_user_info["auto_user"][data]
    if data == "personal_code":
       personal_code = auto_user_info["auto_user"][data]
    if data == "car_years":
       car_years = auto_user_info["auto_user"][data]

print(number, personal_code, car_years)