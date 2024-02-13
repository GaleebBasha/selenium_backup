from libs.Basic_Act import Basic_Actions
from libs.My_Info import My_Information
from libs.Directory import My_Directory

def test_valid_login():
    obj = Basic_Actions("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    res = obj.check_title('OrangeHRM')
    assert res==True
    status = obj.success_login('admin', 'admin123')
    assert status==True

def test_invalid_login():
    obj = Basic_Actions("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    res = obj.check_title('OrangeHRM')
    assert res==True
    status = obj.success_login('admin', 'admin3')
    assert status == False

def test_FPWD_validate():
    obj = Basic_Actions("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    res = obj.check_title('OrangeHRM')
    assert res == True
    status = obj.validate_FPW_link()
    assert status == True

def test_edit_myinfo():
    obj = My_Information("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    res = obj.check_title('OrangeHRM')
    assert res == True
    status = obj.success_login('admin', 'admin123')
    assert status == True
    status = obj.navigate_myinfo_page()
    assert status == True
    obj.edit_my_info()


def test_edit_directory():
    obj = My_Directory("/usr/local/bin/chromedriver")
    obj.get_url("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    res = obj.check_title('OrangeHRM')
    assert res == True
    status = obj.success_login('admin', 'admin123')
    assert status == True
    status = obj.navigate_to_directory_page()
    assert status == True