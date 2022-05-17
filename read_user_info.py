import json

#####read json data
def get_data():

    file = open("C:/Users/glera/Desktop/insurance_test/user_info.json", "r")
    file_info = file.read()
    data = json.loads(file_info)

    return data

auto_user_info = get_data()

#print(auto_user_info)

