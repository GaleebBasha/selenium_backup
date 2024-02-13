from Basic_Act import Basic_Actions
from My_Info import My_Information
from admin_act import Admin_Act
from input import input_data

def test_login_invalid_creds():
    obj = Basic_Actions("/usr/local/bin/chromedriver")
    obj.get_url(input_data['url'])
    ret_status = obj.get_title("OrangeHRM")
    assert ret_status == True
    ret_status = obj.success_login(input_data['user'], input_data['passwd'])
    assert ret_status == False

def test_login_valid_creds():
    obj = Basic_Actions("/usr/local/bin/chromedriver")
    obj.get_url(input_data['url'])
    ret_status = obj.get_title("OrangeHRM")
    assert ret_status == True
    ret_status = obj.success_login(input_data['user'], input_data['passwd'])
    assert ret_status == True

def test_empty_filed():
    obj = Basic_Actions("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    ret_status = obj.get_title("OrangeHRM")
    assert ret_status == True
    ret_status = obj.success_login('', 'admin123')
    assert ret_status == False

def test_FPWD():
    obj = Basic_Actions("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    ret_status = obj.get_title("OrangeHRM")
    assert ret_status == True
    ret_status = obj.check_FPWD()
    assert ret_status == True

def test_edit_my_personal_details():
    obj = My_Information("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    ret_status = obj.get_title("OrangeHRM")
    assert ret_status == True
    ret_status = obj.success_login('admin', 'admin123')
    assert ret_status == True
    status = obj.navigate_my_info()
    assert status==True
    obj.edit_personals()

def test_delete_rec():
    obj = Admin_Act("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/")
    ret_status = obj.get_title("OrangeHRM")
    assert ret_status == True
    ret_status = obj.success_login('admin', 'admin123')
    assert ret_status == True
    status= obj.navigate_admin_page()
    assert status == True
    obj.delete_record("//table[@class='table hover']/tbody/tr[2]/td/input")
