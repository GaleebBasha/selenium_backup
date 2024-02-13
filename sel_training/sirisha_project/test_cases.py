from Basic_Act import Basic_Action
from My_Info import My_Information
from dashboard import DashBoard

def test_login_valid_creds():
    obj = Basic_Action()
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    status = obj.check_title("OrangeHRM")
    assert status == True
    status = obj.success_login('admin', 'admin123')
    assert status == True

def test_login_invalid_creds():
    obj = Basic_Action()
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    status = obj.check_title("OrangeHRM")
    assert status == True
    status = obj.success_login('admin', 'admin3')
    assert status == False

def test_validate_FPWD():
    obj = Basic_Action()
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    status = obj.check_title("OrangeHRM")
    assert status == True
    status = obj.validate_FPW_link()
    assert status == True

def test_edit_myinfo_data():
    obj = My_Information()
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    status = obj.check_title("OrangeHRM")
    assert status == True
    status = obj.success_login('admin', 'admin123')
    assert status == True
    status = obj.navigate_to_myinfo()
    assert status==True
    obj.edit_info()

def test_apply_leave():