# 导包
from api.login import LoginAPI

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
    def test01_success(self):
        test_data = {
            "username" : "admin",
            "password" : "HM_2023_test",
            "code" : "2",
            "uuid" : TestLoginAPI.uuid
        }
        respond = self.login_api.login(test_data=test_data)

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据包含  成功
        assert "成功" in respond.text
        # 断言 json 数据中的code值
        assert 200 == respond.json().get("code")


    # 登陆失败（用户名为空）
    def test02_without_username(self):
        test_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        respond = self.login_api.login(test_data=test_data)

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据包含  成功
        assert "错误" in respond.text
        # 断言 json 数据中的code值
        assert 500 == respond.json().get("code")



    # 登陆失败（未注册用户名）
    def test03_username_not_exist(self):
        test_data = {
            "username": "liuliu666",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        respond = self.login_api.login(test_data=test_data)

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据包含  成功
        assert "错误" in respond.text
        # 断言 json 数据中的code值
        assert 500 == respond.json().get("code")