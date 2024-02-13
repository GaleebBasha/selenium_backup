from libraries.webrdriver_actions import WebActions
from commons.myinfo import MyInfo
from configs.variables import vars
import pytest

@pytest.mark.basic
def test_valid_login():
    obj = WebActions()
    obj.launch_website(vars['url'])
    res=obj.verify_user_creds(vars['username'], vars['password'])
    assert res==1

def test_invalid_login():
    obj = WebActions()
    obj.launch_website("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    res=obj.verify_user_creds("Amin", "admin123")
    assert res==-1

@pytest.mark.edit
def test_edit_my_info():
    obj = MyInfo()
    obj.login()
    obj.navigate_to_myinfo_page()
    obj.edit_myinfo_details()
    