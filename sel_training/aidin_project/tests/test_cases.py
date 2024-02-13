import sys
sys.path.append("/home/basha/PycharmProjects/sel_training/aidin_project")
from libs.Basic_Web_Actions import Basic_Act
from libs.My_Info import MyInfo
from configs.inputs import data

def test_with_valid_creds():
    obj = Basic_Act()
    obj.get_url(data["url"])
    obj.get_title()
    obj.login_with_valid_credentials(data['username'], data['password'])

def test_with_invalid_creds():
    obj = Basic_Act()
    obj.get_url(data["url"])
    obj.get_title()
    obj.login_with_invalid_credentials()

def test_modify_myinfo_page():
    obj = MyInfo()
    obj.get_url(data["url"])
    obj.get_title()
    obj.login_with_valid_credentials(username="Admin", password="admin123")
    obj.navigate_to_my_info_page()
    obj.fill_up_personal_details()
