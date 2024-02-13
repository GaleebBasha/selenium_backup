from libs.connections import BasicActions
import pytest
from commons.myinfo import MyInfo
"""
1. Pytest
2. Behave
3. Unittest
4. Robot Frame
# pip3 install pytest
# 
"""
# user_data = (['Admin', 'admin123'], ['xsdf', 'fddsasd'])
# @pytest.mark.parametrize("username,password", user_data)
# def test_login(username, password):
def test_login():
    obj = MyInfo()
    obj.navigate_url()
    obj.login("Admin", "admin123")
    obj.navigate_myinfo()
    obj.fill_personal_data()
    # obj = BasicActions()
    # obj.navigate_url()
    # status = obj.login(username,password)
    # print("Hello")
    # assert status==True



# @pytest.mark.fail
# def test_invalid_login():
#     obj = BasicActions()
#     obj.navigate_url()
#     status = obj.login('asfgf', 'dfdsd')
#     assert status!=True
    
# @pytest.mark.parametrize("user,passwd", (["Admin", "admin123"], ["asasa", 'sadsa']))
# pip install pytest-html-reporter --- for more beutified log report use  --html-report=report.html
# pip install pytest-html -- for basic log report   --html=report.html