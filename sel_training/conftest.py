import pytest
# import argparse

# @pytest.fixture
# def input_value():
#    input = 39
#    return input

# @pytest.fixture
# def input_string():
#    input = "Demo"
#    return input

# def pytest_addoption(parser):
#     print('conftest method')
#     parser.addoption("--hostip", action = "store", default = "127.0.0.1", help ="host ip address")
#     parser.addoption("--port", action="store", default="5000", help="port")

# @pytest.fixture
# def get_param(request):
#     config_param = {}
#     config_param["host"] = request.config.getoption("--hostip")
#     config_param["port"] = request.config.getoption("--port")
#     return config_param


# test_mock_argparse.py
# import argparse
# try:
#     from unittest import mock  # python 3.3+
# except ImportError:
#     import mock  # python 2.6-3.2


# def main():
#     parser = argparse.ArgumentParser(description='Process some integers.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                         help='an integer for the accumulator')
#     parser.add_argument('--sum', dest='accumulate', action='store_const',
#                         const=sum, default=max,
#                         help='sum the integers (default: find the max)')

#     args = parser.parse_args()
#     print(args)  # NOTE: this is how you would check what the kwargs are if you're unsure
#     return args.accumulate(args.integers)









