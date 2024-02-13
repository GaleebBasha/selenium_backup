from libs.admin_act import Admin_Actions
from libs.base_act import Basic_Actions
from locators.elems_locs import LOCATORS
import time

def test_valid_login():
    obj = Basic_Actions()
    obj.get_to_url(LOCATORS['url'])
    obj.valid_login(LOCATORS['user'], LOCATORS['pwd'])
    status = obj.verify_login()
    assert status == True

def test_invalid_login():
    obj = Basic_Actions()
    obj.get_to_url("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
    obj.valid_login("Admin123", "admin123")
    status = obj.verify_login()
    assert status == False

def test_admin_act():
    obj = Admin_Actions()
    obj.get_to_url("https://opensource-demo.orangehrmlive.com/")
    obj.valid_login('Admin', 'admin123')
    status = obj.verify_login()
    assert status == True
    status = obj.navigate_to_admin_page()
    assert status == True

def test_search_admin():
    obj = Admin_Actions()
    obj.get_to_url("https://opensource-demo.orangehrmlive.com/")
    obj.valid_login('Admin', 'admin123')
    status = obj.verify_login()
    assert status == True
    status = obj.navigate_to_admin_page()
    assert status == True
    obj.search_user()
    time.sleep(10)

def test_delete_user():
    obj = Admin_Actions()
    obj.get_to_url("https://opensource-demo.orangehrmlive.com/")
    obj.valid_login('Admin', 'admin123')
    status = obj.verify_login()
    assert status == True
    status = obj.navigate_to_admin_page()
    assert status == True
    9w