# 导包
import config
from api.login import LoginAPI
import pytest
import json


# # 初始化
# 将数据与代码分离 数据放在data/login_json下
# test_data= [
#     ("admin", "HM_2023_test", 200 , "成功", 200),
#     ("", "HM_2023_test", 200 , "错误", 500),
#     ("liuliu666", "HM_2023_test",  200 , "错误", 500)
# ]

# 读取json数据
def build_data(json_file):

    # 定义空列表
    test_data = []

    # 打开json文件
    with open( json_file, 'r') as  f:

        # 加载json文件数据
        json_data = json.load(f)

        # 循环遍历json_data
        for case_data in json_data:

            # 转换数据格式[{}]  ===>>> [()]
            username  = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            message = case_data.get("message")
            code = case_data.get("code")
            
            test_data.append((username, password, status, message, code))
    return test_data



# 创建测试类
class TestLoginAPI:
    # 初始化
    uuid=None
    # 前置处理
    def setup(self):
        # 实例化
        self.login_api = LoginAPI()

        # 获取验码
        respond = self.login_api.get_verify_code()
        print(respond.json())

        # 获取uuid
        TestLoginAPI.uuid = respond.json().get("uuid")
    # 后置处理
    def teardown(self):
        pass


    # 登陆成功
    # @pytest.mark.parametrize( "username,password, status,message, code", test_data)
    @pytest.mark.parametrize("username,password, status,message, code", build_data(json_file = config.BASE_PATH+'/data/login.json'))
    def test01_success(self,username,password, status,message, code):
        test_data = {
            "username" : username,
            "password" : password,
            "code" : "2",
            "uuid" : TestLoginAPI.uuid
        }
        respond = self.login_api.login(test_data=test_data)

        # 断言响应状态码
        assert status == respond.status_code
        # 断言响应数据包含  成功
        assert message in respond.text
        # 断言 json 数据中的code值
        assert code == respond.json().get("code")


